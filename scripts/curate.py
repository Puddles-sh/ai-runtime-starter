#!/usr/bin/env python3
"""Curate — hand-authored corpus entries for known model failure modes.

Scout crawls what MS publishes. Curate fills in what models still get wrong
even when the docs are present — typically property access patterns and REST
URI paths that training weights override in retrieved context.

Each chunk targets a specific confirmed failure mode from benchmark scoring.
Add new entries here when Scorer/Auditor logs reveal recurring hallucinations.

Usage:
  python3 curate.py
  python3 curate.py --output-dir ~/rag-corpus

Index with the scraped corpus:
  python3 indexer.py ~/rag-corpus/curated-corpus-TIMESTAMP.jsonl
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Curated chunks
# Each dict matches the scout.py output schema exactly: id, cmdlet, module,
# chunk_type, tier, content, source_url.
# ---------------------------------------------------------------------------

CURATED: list[dict] = [

    # -----------------------------------------------------------------------
    # Failure: ga-deprecated-module, ps-graph-stale-users
    # Root cause: qwen3.6 (and others) use $user.LastSignInDateTime or
    # $user.lastSignInDateTime as a direct property — it does not exist.
    # The real property is $user.SignInActivity.LastSignInDateTime, and you
    # must explicitly request it with -Property "signInActivity".
    # Source: https://learn.microsoft.com/en-us/graph/api/resources/signinactivity
    # -----------------------------------------------------------------------
    {
        "id": "signinactivity-property-access-t1",
        "cmdlet": "Get-MgUser",
        "module": "microsoft.graph.users",
        "chunk_type": "summary",
        "tier": 1,
        "content": """\
# Get-MgUser — SignInActivity Property Access (CRITICAL)

## WRONG — these properties do NOT exist on the user object:
$user.LastSignInDateTime           # always $null
$user.lastSignInDateTime           # always $null
$user.LastSignInDate               # always $null

## CORRECT — SignInActivity is a NESTED OBJECT:
$user.SignInActivity.LastSignInDateTime
$user.SignInActivity.LastNonInteractiveSignInDateTime

## You MUST request it explicitly with -Property:
Get-MgUser -Property "id","userPrincipalName","displayName","accountEnabled","signInActivity" -All

Without '-Property signInActivity' the field is NOT returned — it will be $null even if the
user has signed in. This is a Graph API projection rule, not a PowerShell limitation.

## SignInActivity object structure:
- LastSignInDateTime                  (string, ISO 8601 UTC — interactive sign-ins)
- LastNonInteractiveSignInDateTime    (string, ISO 8601 UTC — non-interactive/service sign-ins)
- LastSignInRequestId                 (string)

## Required permissions:
- AuditLog.Read.All (required for signInActivity — User.Read.All alone is insufficient)
- User.Read.All

## Filter pattern for stale accounts (60/90-day cutoff):
```powershell
$cutoff = (Get-Date).AddDays(-60).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")
$users = Get-MgUser -Property "id","userPrincipalName","displayName","accountEnabled","signInActivity" -All |
    Where-Object {
        $_.AccountEnabled -eq $true -and
        ($_.SignInActivity -eq $null -or
         $_.SignInActivity.LastSignInDateTime -lt $cutoff)
    }
```
""",
        "source_url": "https://learn.microsoft.com/en-us/graph/api/resources/signinactivity",
    },

    {
        "id": "signinactivity-property-access-t2",
        "cmdlet": "Get-MgUser",
        "module": "microsoft.graph.users",
        "chunk_type": "reference",
        "tier": 2,
        "content": """\
# Get-MgUser — Full SignInActivity Reference

## Resource type: microsoft.graph.signInActivity
URL: https://learn.microsoft.com/en-us/graph/api/resources/signinactivity

The signInActivity property is a complex type returned as a child object on the
microsoft.graph.user resource. It is NOT a scalar property on the user object.

## Complete property table:
| Property                              | Type     | Description                                         |
|---------------------------------------|----------|-----------------------------------------------------|
| lastSignInDateTime                    | String   | Last interactive sign-in date/time (ISO 8601 UTC)  |
| lastNonInteractiveSignInDateTime      | String   | Last non-interactive sign-in (service tokens, etc.) |
| lastSignInRequestId                   | String   | Request ID of the last sign-in                      |
| lastSuccessfulSignInDateTime          | String   | Last successful sign-in (includes non-interactive)  |
| lastSuccessfulSignInRequestId         | String   | Request ID of last successful sign-in               |

## Why models get this wrong:
- Older MSOnline / AzureAD modules exposed LastSignInDate as a top-level scalar
- The Graph SDK wraps it in a SignInActivity sub-object — a breaking change from the deprecated modules
- Graph API projection means the property is omitted (not $null-typed) unless explicitly requested

## Full script example — find and disable stale users:
```powershell
Connect-MgGraph -Scopes "User.Read.All","AuditLog.Read.All","User.EnableDisableAccount.All"

$cutoff = (Get-Date).AddDays(-60).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

$stale = Get-MgUser `
    -Property "id","userPrincipalName","displayName","accountEnabled","signInActivity" `
    -All |
    Where-Object {
        $_.AccountEnabled -eq $true -and
        ($_.SignInActivity -eq $null -or
         $_.SignInActivity.LastSignInDateTime -lt $cutoff)
    }

foreach ($user in $stale) {
    Update-MgUser -UserId $user.Id -AccountEnabled:$false
    Write-Output "Disabled: $($user.UserPrincipalName)"
}
```
""",
        "source_url": "https://learn.microsoft.com/en-us/graph/api/resources/signinactivity",
    },

    # -----------------------------------------------------------------------
    # Failure: ga-error-handling
    # Root cause: models hallucinate REST URI paths for authentication methods.
    # Common wrong paths: /authentication/authenticationMethods/, /identity/authentication/
    # Correct path: /users/{id}/authentication/methods
    # Also: Remove-MgUserAuthenticationMethod does NOT exist — must use type-specific cmdlets.
    # -----------------------------------------------------------------------
    {
        "id": "mfa-auth-methods-uris-t1",
        "cmdlet": "Get-MgUserAuthenticationMethod",
        "module": "microsoft.graph.identity.signins",
        "chunk_type": "summary",
        "tier": 1,
        "content": """\
# MFA Authentication Methods — Correct URI Paths and Cmdlet Names

## WRONG REST URIs (do not use — these do not exist):
/authentication/authenticationMethods/
/users/{id}/authentication/authMethods/
/identity/authentication/methods/
/v1.0/authentication/

## CORRECT REST URIs (for use with Invoke-MgGraphRequest):
GET    /users/{userId}/authentication/methods
DELETE /users/{userId}/authentication/microsoftAuthenticatorMethods/{methodId}
DELETE /users/{userId}/authentication/softwareOathMethods/{methodId}
DELETE /users/{userId}/authentication/phoneAuthenticationMethods/{methodId}
DELETE /users/{userId}/authentication/fido2Methods/{methodId}

## WRONG PowerShell cmdlet (does NOT exist):
Remove-MgUserAuthenticationMethod   # hallucinated — will fail

## CORRECT PowerShell cmdlets (type-specific — use these):
Get-MgUserAuthenticationMethod -UserId $userId -All
Remove-MgUserAuthenticationMicrosoftAuthenticatorMethod -UserId $userId -AuthenticationMethodId $id
Remove-MgUserAuthenticationSoftwareOathMethod -UserId $userId -AuthenticationMethodId $id
Remove-MgUserAuthenticationPhoneMethod -UserId $userId -PhoneAuthenticationMethodId $id

## Identify method type from @odata.type in AdditionalProperties:
#microsoft.graph.microsoftAuthenticatorAuthenticationMethod
#microsoft.graph.softwareOathAuthenticationMethod
#microsoft.graph.phoneAuthenticationMethod
#microsoft.graph.fido2AuthenticationMethod

## Required permissions:
- UserAuthenticationMethod.Read.All (read)
- UserAuthenticationMethod.ReadWrite.All (delete)
""",
        "source_url": "https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethods-overview",
    },

    {
        "id": "mfa-auth-methods-uris-t2",
        "cmdlet": "Remove-MgUserAuthenticationMicrosoftAuthenticatorMethod",
        "module": "microsoft.graph.identity.signins",
        "chunk_type": "reference",
        "tier": 2,
        "content": """\
# MFA Reset Function — Full Reference with Error Handling Pattern

## Correct pattern for resetting all MFA methods for a user:
```powershell
function Reset-UserMfaMethods {
    param([string]$UserId)

    $result = [PSCustomObject]@{
        Success        = $false
        UserId         = $UserId
        MethodsRemoved = 0
        Error          = $null
    }

    try {
        $methods = Get-MgUserAuthenticationMethod -UserId $UserId -All -ErrorAction Stop
    }
    catch {
        if ($_.Exception.Message -match "404|Resource.*not found") {
            $result.Error = "User not found: $UserId"
        } elseif ($_.Exception.Message -match "403|Forbidden|Insufficient") {
            $result.Error = "Insufficient permissions — requires UserAuthenticationMethod.ReadWrite.All"
        } else {
            $result.Error = $_.Exception.Message
        }
        return $result
    }

    foreach ($method in $methods) {
        $type = $method.AdditionalProperties["@odata.type"]
        $id   = $method.Id

        Write-Verbose "Removing method type=$type id=$id"

        try {
            switch ($type) {
                "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod" {
                    Remove-MgUserAuthenticationMicrosoftAuthenticatorMethod `
                        -UserId $UserId -AuthenticationMethodId $id -ErrorAction Stop
                }
                "#microsoft.graph.softwareOathAuthenticationMethod" {
                    Remove-MgUserAuthenticationSoftwareOathMethod `
                        -UserId $UserId -AuthenticationMethodId $id -ErrorAction Stop
                }
                "#microsoft.graph.phoneAuthenticationMethod" {
                    Remove-MgUserAuthenticationPhoneMethod `
                        -UserId $UserId -PhoneAuthenticationMethodId $id -ErrorAction Stop
                }
                "#microsoft.graph.fido2AuthenticationMethod" {
                    Remove-MgUserAuthenticationFido2Method `
                        -UserId $UserId -Fido2AuthenticationMethodId $id -ErrorAction Stop
                }
                default {
                    Write-Verbose "Skipping unhandled method type: $type"
                    continue
                }
            }
            $result.MethodsRemoved++
        }
        catch {
            $result.Error = "Failed removing $type : $($_.Exception.Message)"
            return $result
        }
    }

    $result.Success = $true
    return $result
}
```

## Key correctness rules:
1. No generic Remove-MgUserAuthenticationMethod exists — always switch on @odata.type
2. The REST path is /users/{id}/authentication/methods — never /authentication/authenticationMethods/
3. 404 from Get-MgUserAuthenticationMethod means user not found; 403 means permission denied
4. $false is valid PowerShell boolean literal — [bool]$false is unnecessary but not harmful
5. Return the PSCustomObject (not Write-Output) so callers can inspect properties
""",
        "source_url": "https://learn.microsoft.com/en-us/graph/api/resources/authenticationmethods-overview",
    },
]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Curate — write hand-authored corpus chunks for known model failure modes.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 curate.py
  python3 curate.py --output-dir ~/rag-corpus

Index afterward:
  python3 indexer.py ~/rag-corpus/curated-corpus-TIMESTAMP.jsonl
""",
    )
    parser.add_argument("--output-dir", type=Path, default=Path.home() / "rag-corpus")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    output_path = args.output_dir / f"curated-corpus-{timestamp}.jsonl"

    print("Curate — hand-authored corpus entries")
    print(f"  Chunks : {len(CURATED)}")
    print(f"  Output : {output_path}\n")

    with output_path.open("w", encoding="utf-8") as fh:
        for chunk in CURATED:
            fh.write(json.dumps(chunk) + "\n")
            tier = chunk.get("tier", "?")
            print(f"  wrote  [{chunk['id']}]  tier={tier}")

    print(f"\nDone. {len(CURATED)} chunks written.")
    print(f"\nNext step:")
    print(f"  python3 indexer.py {output_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
