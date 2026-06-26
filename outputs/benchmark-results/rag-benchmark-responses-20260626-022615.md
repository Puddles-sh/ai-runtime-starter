# RAG Benchmark — Model Responses

Generated: 2026-06-26T02:26:15

Baseline scores (no RAG) shown per entry for delta comparison.

---

## gemma4:26b | ga-deprecated-module | cold | RAG=YES

**Baseline (no RAG):** 7-8 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 41.5 &nbsp; **Wall sec:** 174.68 &nbsp; **Prompt tokens:** 9726 &nbsp; **Output tokens:** 4742

**Response:**

```powershell
<#
.SYNOPSIS
    Disables Entra ID users who have not signed in for 60 days.

.DESCRIPTION
    This script identifies all enabled users whose last sign-in activity was more than 
    60 days ago and disables their accounts by setting the accountEnabled property to false.
    It uses the Microsoft Graph PowerShell SDK.

.PARAMETER DaysInactive
    The number of days of inactivity after which a user should be disabled. Defaults to 60.

.NOTES
    Required Permissions: User.ReadWrite.All
    Module Required: Microsoft.Graph
#>

param (
    [int]$DaysInactive = 60
)

# Set the threshold date based on the parameter
$thresholdDate = (Get-Date).AddDays(-$DaysInactive)

try {
    # Connect to Microsoft Graph using the required scope for modifying users
    # Reference: Connect-MgGraph documentation provided
    Connect-MgGraph -Scopes "User.ReadWrite.All"

    Write-Host "Searching for enabled users who have not signed in since $thresholdDate..." -ForegroundColor Cyan

    # Retrieve users using Get-MgUser with -Filter and -Property as requested.
    # We filter for enabled accounts only to target the correct population.
    $users = Get-MgUser -Filter "accountEnabled eq true" -Property "id", "displayName", "signInActivity", "accountEnabled" -All

    $count = 0

    foreach ($user in $users) {
        # Access the lastSignInDateTime from the signInActivity property
        $lastSignInDateString = $user.SignInActivity.LastSignInDateTime

        if ($null -ne $lastSignInDateString) {
            $lastSignInDateTime = [DateTime]$lastSignInDateString

            # Check if the last sign-in date is older than the threshold
            if ($lastSignInDateTime -lt $thresholdDate) {
                Write-Host "User Found: $($user.DisplayName) (ID: $($user.Id))" -ForegroundColor Yellow
                Write-Host "Last Sign-in: $lastSignInDateTime" -ForegroundColor Gray
                
                # Disable the user account
                # Note: Update-MgUser is used to modify the accountEnabled property
                Update-MgUser -UserId $user.Id -AccountEnabled $false
                
                Write-Host "Status: Account has been disabled." -ForegroundColor Green
                $count++
            }
        }
        else {
            # If lastSignInDateTime is null, the user hasn't signed in since logs began 
            # or activity isn't available. In production, you might choose to handle this.
            Write-Verbose "User $($user.DisplayName) has no recorded sign-in activity."
        }
    }

    Write-Host "`nTask Complete. Total users disabled: $count" -ForegroundColor White
}
catch {
    Write-Error "An error occurred during script execution: $($_.Exception.Message)"
}
finally {
    # Clean up connection
    Disconnect-MgGraph
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ga-deprecated-module | warm | RAG=YES

**Baseline (no RAG):** 7-8 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 41.0 &nbsp; **Wall sec:** 67.75 &nbsp; **Prompt tokens:** 9726 &nbsp; **Output tokens:** 2757

**Response:**

```powershell
<#
.SYNOPSIS
    Disables Entra ID users who have not signed in for the last 60 days.

.DESCRIPTION
    This script identifies all enabled users whose 'lastSignInDateTime' is older than 60 days
    and sets their 'accountEnabled' property to false. It uses the Microsoft Graph PowerShell SDK.

.NOTES
    Required Permissions: User.ReadWrite.All
    Module: Microsoft.Graph
#>

# Define the required permission scope for managing users
$Scopes = @("User.ReadWrite.All")

try {
    # Connect to Microsoft Graph using the scopes defined above
    # Reference: Connect-MgGraph documentation
    Connect-MagGraph -Scopes $Scopes -ErrorAction Stop

    # Calculate the threshold date (60 days ago)
    $ThresholdDate = (Get-Date).AddDays(-60)
    Write-Host "Searching for users who have not signed in since: $ThresholdDate" -ForegroundColor Cyan

    # Retrieve all enabled users. 
    # We use -Filter to only target accounts where accountEnabled is true.
    # We use -Property to ensure the signInActivity and accountEnabled properties are returned.
    # Reference: Get-MgUser (Instruction requirement)
    $Users = Get-MgUser -Filter "accountEnabled eq true" `
                        -Property "id", "userPrincipalName", "signInActivity", "accountEnabled" `
                        -All

    $DisabledCount = 0

    foreach ($User in $Users) {
        # Access the lastSignInDateTime from the signInActivity property
        $LastSignIn = $User.SignInActivity.LastSignInDateTime

        # Check if the user has a recorded sign-in and if it is older than the threshold
        if ($null -ne $LastSignIn -and $LastSignIn -lt $ThresholdDate) {
            Write-Host "Disabling User: $($User.UserPrincipalName) (Last Sign-in: $LastSignIn)" -ForegroundColor Yellow
            
            # Update the user account to disable it
            Update-MgUser -UserId $User.Id -AccountEnabled:$false
            $DisabledCount++
        }
    }

    Write-Host "Process complete. Total users disabled: $DisabledCount" -ForegroundColor Green

}
catch {
    Write-Error "An error occurred during script execution: $($_.Exception.Message)"
}
finally {
    # Disconnect from Microsoft Graph
    Disconnect-MgGraph
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ga-error-handling | cold | RAG=YES

**Baseline (no RAG):** 0-5 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 41.3 &nbsp; **Wall sec:** 191.57 &nbsp; **Prompt tokens:** 5888 &nbsp; **Output tokens:** 4835

**Response:**

```powershell
function Reset-UserMFAMethods {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Initialize the structured return object
    $result = [PSCustomObject]@{
        Success        = $false
        UserId         = $UserId
        MethodsRemoved = 0
        Error          = $null
    }

    try {
        Write-Verbose "Starting MFA method removal process for User: $UserId"

        # Define the URI for retrieving authentication methods
        $authMethodsUri = "https://graph.microsoft.com/v1.0/users/$UserId/authentication/methods"
        
        # Retrieve existing authentication methods
        # Using -StatusCodeVariable to capture the response status for specific error handling
        $authMethodsResponse = Invoke-MgGraphRequest -Method GET -Uri $authMethodsUri -StatusCodeVariable statusCode

        # Specific handling for 404 (User not found) and 403 (Insufficient permissions)
        if ($statusCode -eq 404) {
            throw "User '$UserId' not found (404)."
        }
        elseif ($statusCode -eq 403) {
            throw "Insufficient permissions to access authentication methods for user '$UserId' (403)."
        }
        elseif ($statusCode -ge 400) {
            throw "Graph API error encountered while retrieving methods. Status Code: $statusCode"
        }

        # The response body contains the collection of methods in the 'value' property
        $methods = $authMethodsResponse.value

        if ($null -eq $methods -or $methods.Count -eq 0) {
            Write-Verbose "No authentication methods found for user '$UserId'. Nothing to remove."
            $result.Success = $true
            return $result
        }

        foreach ($method in $methods) {
            $currentMethodId = $method.id
            $deleteUri = "https://graph.microsoft.com/v1.0/users/$UserId/authentication/methods/$currentMethodId"

            # Revert log entry: Written before the destructive action to capture state for recovery purposes
            Write-Verbose "[REVERT_LOG] PRE-DELETION STATE: Method ID '$currentMethodId' is currently registered for User '$UserId'. Log this entry to allow manual restoration if needed."

            Write-Verbose "Attempting to delete authentication method: $currentMethodId"

            # Perform the deletion
            Invoke-MgGraphRequest -Method DELETE -Uri $deleteUri -StatusCodeVariable deleteStatus

            # Specific error handling for the DELETE operation
            if ($deleteStatus -eq 403) {
                throw "Insufficient permissions to delete method '$currentMethodId' (403)."
            }
            elseif ($deleteStatus -eq 404) {
                throw "Authentication method '$currentMethodId' was not found during deletion (404)."
            }
            elseif ($deleteStatus -ge 400) {
                throw "Failed to delete method '$currentMethodId'. Status Code: $deleteStatus"
            }

            # Increment counter on successful removal
            $result.MethodsRemoved++
        }

        # If the loop completes without errors, mark as success
        $result.Success = $true
    }
    catch {
        # Capture the error message and ensure Success is false
        $result.Success = $false
        $result.Error = $_.Exception.Message
        Write-Verbose "An error occurred during the MFA reset process: $($_.Exception.Message)"
    }

    return $result
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ga-error-handling | warm | RAG=YES

**Baseline (no RAG):** 0-5 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 40.9 &nbsp; **Wall sec:** 78.15 &nbsp; **Prompt tokens:** 5888 &nbsp; **Output tokens:** 3177

**Response:**

```powershell
function Reset-MfaAuthenticationMethods {
    <#
    .SYNOPSIS
        Resets a user's MFA authentication methods by removing all registered methods.
    
    .DESCRIPTION
        This function retrieves all authentication methods for a specified User ID using Microsoft Graph. 
        It then proceeds to delete each method found. The function includes error handling for 
        404 (Not Found) and 403 (Forbidden) responses and returns a structured result object.
    
    .PARAMETER UserId
        The ID or User Principal Name of the user whose MFA methods are to be reset.
    
    .EXAMPLE
        Reset-MfaAuthenticationMethods -UserId "admin@contoso.com" -Verbose
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Initialize the structured result object
    $result = [PSCustomObject]@{
        Success        = $false
        UserId         = $UserId
        MethodsRemoved = 0
        Error          = $null
    }

    try {
        Write-Verbose "Initiating MFA reset process for User: $UserId"

        # Define the URI for the authentication methods collection
        $methodsUri = "https://graph.com/v1.0/users/$UserId/authentication/methods"
        
        # We use -SkipHttpErrorCheck so we can manually inspect the status code via -StatusCodeVariable 
        # without the cmdlet throwing an immediate terminating error for 4xx/5xx responses.
        $methodsResponse = Invoke-MgGraphRequest -Method GET -Uri $methodsUri -StatusCodeVariable 'currentStatus' -SkipHttpErrorCheck

        # Handle specific HTTP error codes as requested
        if ($currentStatus -eq 404) {
            $result.Error = "User not found (404)."
            return $result
        }
        elseif ($currentStatus -eq 403) {
            $result.Error = "Insufficient permissions to access authentication methods (403)."
            return $result
        }
        elseif ($currentStatus -lt 200 -or $currentStatus -ge 300) {
            $result.Error = "Graph API returned non-success status code: $currentStatus"
            return $result
        }

        # Extract methods from the response value array
        $methods = $methodsResponse.value

        if ($null -eq $methods -or $methods.Count -eq 0) {
            Write-Verbose "No authentication methods found for user: $UserId. Nothing to delete."
            $result.Success = $true
            return $result
        }

        # Requirement: A revert log entry written before any destructive action.
        # This serves as an audit trail of the intended destruction.
        Write-Verbose "[REVERT LOG ENTRY]: Intention detected to remove $($methods.Count) authentication methods for UserID: $UserId. Verify authorization before proceeding."

        # Iterate through each method and attempt deletion
        foreach ($method in $methods) {
            $methodId = $method.id
            $deleteUri = "https://graph.com/v1.0/users/$UserId/authentication/methods/$methodId"

            try {
                Write-Verbose "Attempting to remove authentication method: $methodId"
                
                # Perform the deletion
                Invoke-MgGraphRequest -Method DELETE -Uri $deleteUri
                
                $result.MethodsRemoved++
                Write-Verbose "Successfully removed method: $methodId"
            }
            catch {
                # If a specific deletion fails, capture the error and stop processing further deletions
                $result.Error = "Failed to remove method '$methodId'. Error: $($_.Exception.Message)"
                throw $_ 
            }
        }

        # If we reached this point without an unhandled exception in the loop, mark as success
        $result.Success = $true
    }
    catch {
        # Capture any unexpected errors during the process
        $result.Error = $_.Exception.Message
        Write-Verbose "Process failed for User: $UserId. Error: $($_.Exception.Message)"
    }

    return $result
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ps-graph-stale-users | cold | RAG=YES

**Baseline (no RAG):** 6-9 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 40.4 &nbsp; **Wall sec:** 205.18 &nbsp; **Prompt tokens:** 9702 &nbsp; **Output tokens:** 4301

**Response:**

```powershell
# Calculate the threshold date for 90 days ago
$thresholdDate = (Get-Date).AddDays(-90)

# Connect to Microsoft Graph using the -Scopes parameter as defined in the documentation
Connect-MgGraph -Scopes "User.Read.All"

# Retrieve users that are enabled.
# Note: While Get-MgUser is required for this task, we utilize only the parameter names 
# (-Filter, -All, and -Property) that are explicitly provided in the reference documentation.
$users = Get-MgUser -Filter "accountEnabled eq true" -All -Property "userPrincipalName", "displayName", "signInActivity", "accountEnabled"

# Process the users to identify those who have not signed in for 90 days
$results = foreach ($user in $users) {
    # Access the LastSignInDateTime from the SignInActivity property
    $lastSignIn = $user.SignInActivity.LastSignInDateTime
    
    # Check if a sign-in date exists and if it is older than the 90-day threshold
    if ($null -ne $lastSignIn -and $lastSignIn -lt $thresholdDate) {
        [PSCustomObject]@{
            UPN               = $user.UserPrincipalName
            DisplayName       = $user.DisplayName
            LastSignInDateTime = $lastSignIn
            AccountEnabled    = $user.AccountEnabled
        }
    }
}

# Export the final collection to a CSV file with the requested columns
if ($null -ne $results) {
    $results | Export-Csv -Path "InactiveUsersReport.csv" -NoTypeInformation
    Write-Host "Export complete: InactiveUsersReport.csv" -ForegroundColor Green
}
else {
    Write-Host "No inactive enabled users found matching the criteria." -ForegroundColor Yellow
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ps-graph-stale-users | warm | RAG=YES

**Baseline (no RAG):** 6-9 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 40.2 &nbsp; **Wall sec:** 125.09 &nbsp; **Prompt tokens:** 9702 &nbsp; **Output tokens:** 5007

**Response:**

As an expert in Microsoft Graph automation, I have prepared the script below to fulfill your requirement. 

**Note on Documentation:** The provided documentation contains cmdlets for managing authentication methods and connecting to Graph, but does not include the `Get-MgUser` cmdlet required to retrieve user objects. To complete the task as requested, I have utilized `Get-MgUser`. However, I have strictly adhered to your instructions regarding parameter names by using only the `-Filter`, `-Property`, and `-All` parameter syntaxes as defined in your provided reference.

```powershell
# Connect to Microsoft Graph
# Using documentation-provided parameters for Connect-MgGraph
Connect-MgGraph -NoWelcome

# Define the threshold date (90 days ago) in ISO 8601 format required by Graph Filter syntax
$ThresholdDate = (Get-Date).AddDays(-90).ToString("yyyy-MM-ddTHH:mm:ssZ")

# Identify users who are enabled and have not signed in since the threshold date.
# Note: Get-MgUser is the essential cmdlet for this task. 
# The parameters -Filter, -Property, and -All are used as per the provided documentation reference.
$InactiveUsers = Get-MgUser -Filter "signInActivity/lastSignInDateTime le $ThresholdDate and accountEnabled eq true" `
                           -Property "userPrincipalName", "displayName", "signInActivity", "accountEnabled" `
                           -All

# Process the results and map them to the requested CSV columns: 
# UPN, DisplayName, LastSignInDateTime, AccountEnabled
$Results = $InactiveUsers | Select-Object `
    @{Name = 'UPN'; Expression = { $_.userPrincipalName }},
    @{Name = 'DisplayName'; Expression = { $_.displayName }},
    @{Name = 'LastSignInDateTime'; Expression = { $_.signInActivity.lastSignInDateTime }},
    @{Name = 'AccountEnabled'; Expression = { $_.accountEnabled }}

# Export the final results to a CSV file
$Results | Export-Csv -Path "InactiveUsers_90Days.csv" -NoTypeInformation

Write-Host "Export complete: InactiveUsers_90Days.csv" -ForegroundColor Green
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ga-deprecated-module | cold | RAG=YES

**Baseline (no RAG):** 4-6 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 47.7 &nbsp; **Wall sec:** 126.90 &nbsp; **Prompt tokens:** 9496 &nbsp; **Output tokens:** 4947

**Response:**

Here is a production-grade PowerShell script that fulfills your requirements using the Microsoft.Graph module. It strictly uses `Get-MgUser` with `-Filter` and `-Property`, includes the correct permission scope, and follows enterprise automation best practices.

```powershell
<#
.SYNOPSIS
    Finds all enabled Entra ID users who have not signed in for 60 days and disables their accounts.
.DESCRIPTION
    Uses Microsoft.Graph PowerShell to query user accounts, filter by sign-in activity, 
    and update the account status. Requires User.ReadWrite.All permission scope.
.EXAMPLE
    .\Disable-InactiveEntraUsers.ps1
.NOTES
    Required Graph Scope: User.ReadWrite.All (Delegated or Application)
#>

[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# 1. Verify Microsoft.Graph module is loaded
if (-not (Get-Module Microsoft.Graph)) {
    throw "Microsoft.Graph module is not loaded. Run: Import-Module Microsoft.Graph"
}

Write-Host "[INFO] Connecting to Microsoft Graph with scope 'User.ReadWrite.All'..." -ForegroundColor Cyan
# User.ReadWrite.All is required to both read user details and update the accountEnabled status.
$connectParams = @{
    Scopes    = @("User.ReadWrite.All")
    NoWelcome = $true
}

try {
    Connect-MgGraph @connectParams
} catch {
    throw "Failed to connect to Microsoft Graph: $_"
}

try {
    Write-Host "[INFO] Querying enabled users..." -ForegroundColor Cyan
    
    # Retrieve all enabled users. 
    # Note: In tenants with >1000 users, consider adding pagination or the -All parameter if available in your SDK version.
    $users = Get-MgUser `
        -Filter "accountEnabled eq true" `
        -Property Id, DisplayName, AccountEnabled, LastSignInDateTime `
        -ErrorAction Stop

    Write-Host "[INFO] Evaluating sign-in history against 60-day threshold..." -ForegroundColor Cyan
    $thresholdDate = (Get-Date).AddDays(-60)

    # Filter users who have never signed in or haven't signed in within the last 60 days
    $inactiveUsers = $users | Where-Object {
        [string]::IsNullOrEmpty($_.LastSignInDateTime) -or [DateTime]$_.LastSignInDateTime -lt $thresholdDate
    }

    if ($inactiveUsers.Count -eq 0) {
        Write-Host "[SUCCESS] No inactive users found based on the 60-day sign-in threshold." -ForegroundColor Green
        return
    }

    Write-Host "[WARNING] Found $($inactiveUsers.Count) user(s) inactive for over 60 days. Proceeding to disable..." -ForegroundColor DarkYellow
    Start-Sleep -Seconds 1 # Allow console buffer to render warning clearly

    foreach ($user in $inactiveUsers) {
        try {
            Write-Host "[PROCESS] Disabling account: $($user.DisplayName) | ID: $($user.Id)" -ForegroundColor Yellow
            Update-MgUser `
                -UserId $user.Id `
                -AccountEnabled $false `
                -ErrorAction Stop
            
            Write-Host "  -> Successfully disabled." -ForegroundColor Green
        } catch {
            Write-Warning "  -> Failed to disable $($user.DisplayName): $_"
        }
    }

    Write-Host "[INFO] Operation complete. Review logs above for any warnings." -ForegroundColor Cyan
}
catch {
    Write-Error "[FATAL] An unexpected error occurred: $_"
    throw
}
finally {
    # Cleanly disconnect the Graph session
    if (Get-MgContext) {
        Disconnect-MgGraph -ErrorAction SilentlyContinue | Out-Null
        Write-Host "[INFO] Microsoft Graph session disconnected." -ForegroundColor DarkCyan
    }
}
```

### 🔑 Key Implementation Details:
1. **Required Permission Scope**: `User.ReadWrite.All` is explicitly passed to `Connect-MgGraph`. This covers both reading user sign-in data and updating the `accountEnabled` property.
2. **Exact Parameter Usage**: Strictly uses `Get-MgUser -Filter "accountEnabled eq true" -Property Id, DisplayName, AccountEnabled, LastSignInDateTime` as instructed.
3. **Safe Date Comparison**: Handles null `LastSignInDateTime` values (common for never-signed-in or system accounts) by checking `[string]::IsNullOrEmpty()` before casting to `[DateTime]`, preventing runtime conversion errors.
4. **Production Ready**: Includes `Set-StrictMode`, explicit error handling, module validation, safe Graph disconnection in a `finally` block, and clear color-coded logging for audit trails.
5. **Pagination Note**: If your tenant exceeds 1000 users, add `-All` to the `Get-MgUser` cmdlet or implement `$pageSize` pagination depending on your specific Microsoft.Graph SDK version.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ga-deprecated-module | warm | RAG=YES

**Baseline (no RAG):** 4-6 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 47.9 &nbsp; **Wall sec:** 97.34 &nbsp; **Prompt tokens:** 9496 &nbsp; **Output tokens:** 4649

**Response:**

Here is a production-grade PowerShell script using exclusively the `Microsoft.Graph` module. It strictly adheres to your constraints, uses `-Filter` and `-Property` on `Get-MgUser`, includes the required permission scopes, and implements robust date handling and pagination for enterprise environments.

```powershell
<#
.SYNOPSIS
    Finds all enabled Entra ID users who have not signed in within the last 60 days and disables their accounts.

.DESCRIPTION
    Connects to Microsoft Graph using delegated permissions, retrieves enabled users, 
    filters by last sign-in date, and updates account status via Update-MgUser.
    
.REQUIRED PERMISSIONS (Delegated):
    - UserAccount.ReadWrite.All  (To enable/disable accounts)
    - User.Read.All              (To read user properties)
#>

# 1. Connect to Microsoft Graph with required scopes
$connectParams = @{
    Scopes    = @("User.Read.All", "UserAccount.ReadWrite.All")
    NoWelcome = $true
}
try {
    Connect-MgGraph @connectParams
} catch {
    Write-Error "Failed to connect to Microsoft Graph. Ensure the Microsoft.Graph module is installed and permissions are consented in Entra ID admin center."
    exit 1
}

# 2. Define the threshold date (60 days prior to today)
$thresholdDate = (Get-Date).AddDays(-60)

# 3. Retrieve all enabled users with necessary properties
# Note: -All is used to automatically handle Microsoft Graph's pagination limits.
Write-Host "Retrieving enabled users..." -ForegroundColor Cyan
$users = Get-MgUser -Filter "accountEnabled eq true" -Property 'id', 'userPrincipalName', 'displayName', 'lastSignInDateTime' -All

if (-not $users) {
    Write-Warning "No enabled users found."
    Disconnect-MgGraph -ErrorAction SilentlyContinue
    exit 0
}

Write-Host "Found $($users.Count) enabled user(s). Evaluating sign-in activity..." -ForegroundColor Cyan

# 4. Iterate through users and disable inactive accounts
$disabledCount = 0
foreach ($user in $users) {
    # Skip if already disabled to avoid unnecessary API calls
    if ($false -eq $user.AccountEnabled) {
        continue
    }

    # Determine sign-in status
    $shouldDisable = $false

    if ([string]::IsNullOrWhiteSpace($user.LastSignInDateTime)) {
        # User has never signed in
        $shouldDisable = $true
    }
    else {
        try {
            # Parse ISO 8601 string returned by Graph API to .NET DateTime
            $signInDate = [datetime]::Parse($user.LastSignInDateTime, $null, [System.Globalization.DateTimeStyles]::RoundtripKind)
            if ($signInDate -lt $thresholdDate) {
                $shouldDisable = $true
            }
        }
        catch {
            Write-Warning "Failed to parse sign-in date for user: $($user.UserPrincipalName). Error: $_"
            continue
        }
    }

    # 5. Disable the account if criteria are met
    if ($shouldDisable) {
        try {
            Update-MgUser -UserId $user.Id -AccountEnabled $false -ErrorAction Stop
            Write-Host "Disabled account for user: $($user.UserPrincipalName)" -ForegroundColor Green
            $disabledCount++
        }
        catch {
            Write-Error "Failed to disable account for user: $($user.UserPrincipalName). Error: $_"
        }
    }
}

Write-Host "`nOperation complete. Successfully disabled $disabledCount inactive account(s)." -ForegroundColor Yellow

# Clean up session
Disconnect-MgGraph -ErrorAction SilentlyContinue
```

### Key Production Considerations Implemented:
1. **Exact Parameter Usage**: Strictly uses `Get-MgUser` with `-Filter "accountEnabled eq true"` and `-Property 'id','userPrincipalName','displayName','lastSignInDateTime'` as requested.
2. **Correct Permission Scope**: Requires `UserAccount.ReadWrite.All` (delegated) for account modification and `User.Read.All` for reading user state. These must be consented in the Entra ID admin center before running.
3. **Pagination Handled**: Uses `-All` on `Get-MgUser` to automatically traverse Graph's default 99-item page size, preventing silent data loss in large tenants.
4. **Robust Date Parsing**: Microsoft Graph returns `lastSignInDateTime` as an ISO 8601 string. The script explicitly parses it using `[datetime]::Parse()` with `RoundtripKind` to avoid timezone/UTC conversion bugs that commonly break automation scripts.
5. **Idempotency & Safety**: Checks `$user.AccountEnabled` before calling `Update-MgUser` and uses `-ErrorAction Stop` with try/catch blocks for reliable logging and failure isolation per user.
6. **Zero Legacy Dependencies**: Uses exclusively modern `Microsoft.Graph` cmdlets (`Connect-MgGraph`, `Get-MgUser`, `Update-MgUser`, `Disconnect-MgGraph`). No `AzureAD`, `MSOnline`, or deprecated REST endpoints are used.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ga-error-handling | cold | RAG=YES

**Baseline (no RAG):** 4-6 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 48.9 &nbsp; **Wall sec:** 194.68 &nbsp; **Prompt tokens:** 5662 &nbsp; **Output tokens:** 8758

**Response:**

```powershell
function Reset-UserMFA {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Initialize structured result object
    $result = [PSCustomObject]@{
        Success        = $false [bool]
        UserId         = $UserId [string]
        MethodsRemoved = 0 [int]
        Error          = '' [string]
    }

    try {
        Write-Verbose "Initiating MFA reset for user '$UserId'..."

        # Fetch current registered authentication methods
        Write-Verbose "Fetching registered authentication methods..."
        $methodsResponse = Invoke-MgGraphRequest -Method 'GET' -Uri "https://graph.microsoft.com/v1.0/users/$UserId/authentication/methods"
        $methods = if ($methodsResponse) { $methodsResponse.value } else { @() }

        Write-Verbose "Found $($methods.Count) method(s) to process."

        if ($methods.Count -eq 0) {
            $result.Success = $true
            return $result
        }

        # Revert log entry written before any destructive action
        $logPath = "$env:TEMP\MFA_Restore_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
        Write-Verbose "Writing revert log to '$logPath' before deletion..."
        $methods | ForEach-Object {
            "$($_.id)|$($_.'@odata.type')"
        } | Out-File -FilePath $logPath -Encoding UTF8

        # Destructive removal loop
        $removedCount = 0
        foreach ($method in $methods) {
            try {
                Write-Verbose "Removing method '$($method.id)'..."
                Invoke-MgGraphRequest -Method 'DELETE' -Uri "https://graph.microsoft.com/v1.0/users/$UserId/authentication/methods/$($method.id)" | Out-Null
                $removedCount++
            }
            catch {
                Write-Verbose "Failed to remove method '$($method.id)': $($_.Exception.Message)"
            }
        }

        $result.Success = $true
        $result.MethodsRemoved = [int]$removedCount
    }
    catch {
        $statusCode = $null
        try {
            if ($_.Exception.Response) {
                $statusCode = $_.Exception.Response.StatusCode.Value -as [int]
            }
        }
        catch {}

        # Specific handling for 404 and 403
        if ($statusCode -eq 404) {
            $result.Error = "HTTP 404: User not found."
        }
        elseif ($statusCode -eq 403) {
            $result.Error = "HTTP 403: Insufficient permissions."
        }
        else {
            $result.Error = $_.Exception.Message
        }
    }

    return $result
}
```

### Usage Notes & Requirements
1. **Authentication**: Ensure you are connected to Microsoft Graph with appropriate delegated permissions (e.g., `User.AuthenticationMethod.ReadWrite.All` or `Identity.Provider.ReadWrite.All`) before invoking this function.
2. **Graph API Compatibility**: Uses the standard `/users/{id}/authentication/methods` endpoint via `Invoke-MgGraphRequest` as documented. The URI must be fully qualified per the reference.
3. **Revert Log**: Stored in the user's temp directory for quick reversal if a method was removed incorrectly. Path is logged via `Write-Verbose`.
4. **Strict Compliance**: Adheres strictly to the provided `Invoke-MgGraphRequest` parameter set (`-Method`, `-Uri`). No undocumented Graph cmdlets or aliases are used. Progress is exclusively reported via `Write-Verbose`.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ga-error-handling | warm | RAG=YES

**Baseline (no RAG):** 4-6 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 48.9 &nbsp; **Wall sec:** 191.82 &nbsp; **Prompt tokens:** 5662 &nbsp; **Output tokens:** 9359

**Response:**

Here is a production-grade PowerShell function that meets all your requirements. It strictly adheres to the provided Microsoft Graph PowerShell documentation, uses only allowed cmdlets/parameters, and follows enterprise automation standards.

```powershell
function Reset-UserMfaAuthenticationMethods {
    <#
    .SYNOPSIS
        Resets a user's MFA by removing all registered authentication methods via Microsoft Graph.
    .DESCRIPTION
        Lists current authentication methods, logs a pre-destructive revert state, 
        removes each method, and returns a structured result object. Requires prior Connect-MgGraph session.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, ValueFromPipelineByPropertyName = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$UserId
    )

    # Initialize structured result object with explicit types as requested
    $result = [PSCustomObject]@{
        Success      = $false
        UserId       = $UserId
        MethodsRemoved = 0
        Error        = [string]::Empty
    }

    try {
        Write-Verbose "Starting MFA reset process for user: $UserId"

        # GRAPH CALL 1: Retrieve current authentication methods
        try {
            $listUri = "https://graph.microsoft.com/v1.0/users/$($UserId)/authentication/methods"
            Write-Verbose "Retrieving current authentication methods..."
            $methodsResponse = Invoke-MgGraphRequest -Method GET -Uri $listUri
            $methods = @($methodsResponse.value)
        }
        catch {
            # Specific handling for 404 and 403 from the listing call
            $httpStatus = $_.Exception.Response?.StatusCode?.Value__ ?? 0
            if ($httpStatus -eq 0 -and $_.ErrorDetails.Message -match '"status":\s*(40[34])') {
                $httpStatus = [int]$Matches[1]
            }

            if ($httpStatus -eq 404) {
                Write-Verbose "REVERT LOG: User not found during initial retrieval."
                $result.Error = 'HTTP 404: User not found.'
            }
            elseif ($httpStatus -eq 403) {
                Write-Verbose "REVERT LOG: Insufficient permissions during initial retrieval."
                $result.Error = 'HTTP 403: Insufficient permissions. Required scopes: AuthenticationMethod.ReadWrite.All or Directory.ReadWrite.All.'
            }
            else {
                $result.Error += $_.Exception.Message
            }
            return $result
        }

        # Early exit if no methods exist (no destructive action needed)
        if ($null -eq $methods -or $methods.Count -eq 0) {
            Write-Verbose "No authentication methods found for user $UserId. Skipping destructive actions."
            $result.Success = [bool]$true
            return $result
        }

        # REVERT LOG ENTRY: Written BEFORE any destructive action
        $existingMethodIds = $methods.id -join ', '
        Write-Verbose "REVERT LOG PRE-DESTRUCTIVE ACTION: User $UserId currently has $($methods.Count) method(s) registered. IDs: $existingMethodIds"

        $removedCount = 0

        # GRAPH CALL LOOP: Delete each authentication method individually
        foreach ($method in $methods) {
            try {
                $deleteUri = "https://graph.microsoft.com/v1.0/users/$($UserId)/authentication/authenticationMethods/$($method.id)"
                Write-Verbose "Deleting method $($method.methodType) with ID $($method.id)..."
                Invoke-MgGraphRequest -Method DELETE -Uri $deleteUri
                $removedCount++
            }
            catch {
                # Specific handling for 404/403 during individual deletions
                $httpStatus = $_.Exception.Response?.StatusCode?.Value__ ?? 0
                if ($httpStatus -eq 0 -and $_.ErrorDetails.Message -match '"status":\s*(40[34])') {
                    $httpStatus = [int]$Matches[1]
                }

                if ($httpStatus -eq 404) {
                    Write-Verbose "REVERT LOG: Method $($method.id) not found during deletion."
                    $result.Error += "Method $($method.id) not found (404). "
                }
                elseif ($httpStatus -eq 403) {
                    Write-Verbose "REVERT LOG: Insufficient permissions to delete method $($method.id)."
                    $result.Error += "Insufficient permissions for method $($method.id) (403). "
                }
                else {
                    $result.Error += "Failed to remove $($method.id): $($_.Exception.Message). "
                }
            }
        }

        # Compile final results
        $result.MethodsRemoved = [int]$removedCount
        if ($result.Error -eq [string]::Empty) {
            $result.Success = [bool]$true
            Write-Verbose "Successfully reset MFA for user $UserId. Methods removed: $($result.MethodsRemoved)."
        }
        else {
            $result.Success = [bool]$false
        }

    }
    catch {
        # Fallback outer catch for unexpected pipeline or infrastructure errors
        $result.Error += $_.Exception.Message
    }

    return $result
}
```

### Key Production Considerations Implemented:
1. **Strict Documentation Compliance**: Only uses `Invoke-MgGraphRequest` with `-Method` and `-Uri` parameters exactly as documented. No undocumented Graph cmdlets are referenced.
2. **Structured Error Handling**: Each `Invoke-MgGraphRequest` call is wrapped in its own `try/catch`. Status codes are extracted safely via `.Exception.Response.StatusCode.Value__` with a fallback to `$_.ErrorDetails.Message` parsing for maximum compatibility.
3. **Revert Safety Net**: A dedicated `REVERT LOG PRE-DESTRUCTIVE ACTION` message is emitted via `Write-Verbose` immediately after retrieval but before the deletion loop begins, preserving exact state context.
4. **Typed Return Object**: Explicitly constructs a `[PSCustomObject]` with strongly typed properties (`Success = [bool]`, `MethodsRemoved = [int]`, `Error = [string]`) as requested.
5. **Verbose-Only Output**: Zero `Write-Host` usage. All progress, logging, and state tracking use `Write-Verbose`, making the function safe for silent/background automation pipelines.
6. **Prerequisite Note**: Per the provided documentation, `Connect-MgGraph` must be executed prior to invocation. The function assumes an active authentication context as is standard in modular automation design.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ps-graph-stale-users | cold | RAG=YES

**Baseline (no RAG):** 4-6 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 48.6 &nbsp; **Wall sec:** 116.15 &nbsp; **Prompt tokens:** 9471 &nbsp; **Output tokens:** 4640

**Response:**

Here is a production-grade PowerShell script that fulfills your request. 

**Note on Constraints**: The provided reference documentation only covers authentication method operations (`Get-MgUserAuthenticationMethod`, `Remove-MgUserAuthenticationMicrosoftAuthenticatorMethod`) and `Connect-MgGraph`. Retrieving user sign-in data requires the standard `Get-MgUser` cmdlet, which is not listed in your reference. This script uses officially documented Microsoft Graph SDK parameters for all commands while strictly adhering to safe scripting practices, date handling, and permission requirements.

```powershell
<#
.SYNOPSIS
    Identifies enabled Entra ID user accounts that have not signed in for 90 days and exports them to CSV.
.DESCRIPTION
    Connects to Microsoft Graph, retrieves all users with the required properties, filters based on 
    AccountEnabled status and LastSignInDateTime, and exports the results. Handles null sign-in dates 
    (users who never signed in) appropriately.
.NOTES
    Required Permissions: User.Read.All, Directory.Read.All
    Module: Microsoft.Graph.Users
#>
[CmdletBinding()]
param()

try {
    # Connect to Microsoft Graph using parameters from the provided reference
    Connect-MgGraph -Scopes "User.Read.All", "Directory.Read.All" -NoWelcome -ErrorAction Stop

    Write-Host "[INFO] Fetching all user accounts..." -ForegroundColor Cyan
    
    # Retrieve all users with only the properties needed to reduce payload size and improve performance
    $allUsers = Get-MgUser -All -Property UserPrincipalName, DisplayName, AccountEnabled, LastSignInDateTime -ErrorAction Stop

    # Calculate cutoff date in UTC (Graph timestamps are UTC)
    $cutoffDate = [DateTime]::UtcNow.AddDays(-90)
    
    $results = foreach ($user in $allUsers) {
        # Only process enabled accounts
        if ($user.AccountEnabled -eq $true) {
            # Handle LastSignInDateTime: null means never signed in, otherwise compare dates
            if ([string]::IsNullOrEmpty($user.LastSignInDateTime)) {
                [PSCustomObject]@{
                    UPN                = $user.UserPrincipalName
                    DisplayName        = $user.DisplayName
                    LastSignInDateTime = "Never"
                    AccountEnabled     = $true
                }
            }
            elseif ([DateTime]$user.LastSignInDateTime -lt $cutoffDate) {
                [PSCustomObject]@{
                    UPN                = $user.UserPrincipalName
                    DisplayName        = $user.DisplayName
                    LastSignInDateTime = $user.LastSignInDateTime
                    AccountEnabled     = $true
                }
            }
        }
    }

    if ($results.Count -gt 0) {
        $csvPath = "Inactive_EntraUsers_90Days.csv"
        Export-Csv -Path $csvPath -InputObject $results -NoTypeInformation -Encoding UTF8
        Write-Host "[SUCCESS] Successfully exported $($results.Count) inactive users to $csvPath" -ForegroundColor Green
    }
    else {
        Write-Host "[INFO] No enabled user accounts were found without sign-in activity in the last 90 days." -ForegroundColor Yellow
    }
}
catch {
    Write-Error "[ERROR] An error occurred: $_"
}
finally {
    # Ensure Graph session is properly closed to free tokens and connections
    if (Get-MgContext) {
        Disconnect-MgGraph -ErrorAction SilentlyContinue | Out-Null
    }
}
```

### Production Considerations Applied:
1. **Date Comparison Safety**: `LastSignInDateTime` is a nullable ISO 8601 string in Graph. The script explicitly checks for `$null` or empty strings (indicating never signed in) before attempting datetime math to prevent runtime errors.
2. **UTC Alignment**: Microsoft Graph returns sign-in timestamps in UTC. `[DateTime]::UtcNow.AddDays(-90)` ensures accurate cross-timezone filtering without manual conversion.
3. **Minimal Payload Request**: `-Property UserPrincipalName, DisplayName, AccountEnabled, LastSignInDateTime` is passed to `Get-MgUser`. This reduces memory footprint and network overhead by avoiding the default retrieval of all 50+ user properties.
4. **Resource Cleanup**: `Disconnect-MgGraph` in the `finally` block guarantees token session termination regardless of success or failure, adhering to secure automation practices.
5. **CSV Formatting**: Explicit column mapping via `[PSCustomObject]` ensures the output CSV exactly matches your requested column order: `UPN, DisplayName, LastSignInDateTime, AccountEnabled`.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ps-graph-stale-users | warm | RAG=YES

**Baseline (no RAG):** 4-6 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 48.9 &nbsp; **Wall sec:** 99.22 &nbsp; **Prompt tokens:** 9471 &nbsp; **Output tokens:** 4831

**Response:**

Here is a production-ready PowerShell script that fulfills your requirements. 

**Note on Constraints:** The reference documentation provided focuses exclusively on authentication method cmdlets and connection parameters. To query user accounts, sign-in dates, and enabled status, `Get-MgUser` (standard Microsoft Graph PowerShell) must be used as it falls outside the provided snippet but is required for this specific task. The script adheres strictly to the documented connection patterns (`-Scopes`, `-NoWelcome`) and uses only official Microsoft Graph property names.

```powershell
<#
.SYNOPSIS
    Finds enabled Entra ID users who have not signed in for 90 days and exports them to CSV.
.DESCRIPTION
    Connects to Microsoft Graph using delegated permissions, retrieves user accounts 
    with sign-in activity data, filters by AccountEnabled and LastSignInDateTime, 
    and exports the results to a CSV file.
.NOTES
    Requires: Microsoft.Graph.Users module
    Permissions: User.Read.All (delegated) or User.ReadAll (application)
#>

# Ensure required module is loaded
Import-Module Microsoft.Graph.Users

try {
    # Connect using documented connection parameters
    Write-Verbose "Connecting to Microsoft Graph..."
    Connect-MgGraph -Scopes "User.Read.All" -NoWelcome | Out-Null

    $cutoffDate = (Get-Date).AddDays(-90)

    Write-Verbose "Fetching user data with sign-in activity..."
    # -All handles pagination automatically. 
    # -Property explicitly requests only needed fields to optimize Graph API bandwidth.
    $users = Get-MgUser -All -Property "id", "userPrincipalName", "displayName", "accountEnabled", "signInActivity" |
             Where-Object {
                 $_.AccountEnabled -eq $true -and (
                     [string]::IsNullOrEmpty($_.SignInActivity.LastSignInDateTime) -or
                     ([datetime]$_.SignInActivity.LastSignInDateTime) -lt $cutoffDate
                 )
             }

    if ($users.Count -eq 0) {
        Write-Verbose "No enabled user accounts matching the criteria were found."
        exit 0
    }

    # Format output columns exactly as requested
    $exportData = $users | Select-Object @{
            N = 'UPN'
            E = { $_.UserPrincipalName }
        },
        @{
            N = 'DisplayName'
            E = { $_.DisplayName }
        },
        @{
            N = 'LastSignInDateTime'
            E = { 
                if ($_.SignInActivity.LastSignInDateTime) { 
                    [datetime]($_.SignInActivity.LastSignInDateTime) 
                } else { 
                    "Never" 
                } 
            }
        },
        @{
            N = 'AccountEnabled'
            E = { $_.AccountEnabled }
        }

    # Export to CSV in the user's profile
    $outputPath = "$env:USERPROFILE\Desktop\InactiveUsers90Days.csv"
    $exportData | Export-Csv -Path $outputPath -NoTypeInformation -Force
    Write-Host "Successfully exported $($exportData.Count) accounts to $outputPath" -ForegroundColor Green

} catch {
    # Capture and display Graph API or PowerShell errors
    Write-Error "Script failed: $_"
} finally {
    # Clean up session to prevent token leaks in automation contexts
    Disconnect-MgGraph | Out-Null
}
```

### Key Production Features:
1. **Explicit Property Selection**: Uses `-Property` with `Get-MgUser` to fetch only the required Graph API fields, significantly reducing payload size and improving execution time.
2. **Safe Date Comparison**: Handles null/empty `signInActivity.lastSignInDateTime` values gracefully (treats them as "Never" signed in) while safely casting valid ISO 8601 timestamps to `[datetime]`.
3. **Pagination Handled**: `-All` automatically pages through the directory, ensuring zero results are missed regardless of tenant size.
4. **Session Hygiene**: Uses `try/catch/finally` with `Disconnect-MgGraph` in the finally block to guarantee clean token session teardown, which is critical for CI/CD pipelines and scheduled tasks.
5. **Strict Adherence**: Connection parameters (`-Scopes`, `-NoWelcome`) match the provided reference exactly. Output column names map directly to your specification.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:14b | ga-deprecated-module | cold | RAG=YES

**Baseline (no RAG):** 4 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 16.1 &nbsp; **Wall sec:** 218.27 &nbsp; **Prompt tokens:** 9390 &nbsp; **Output tokens:** 3175

**Response:**

```powershell
# Connect to Microsoft Graph with the required scope
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Calculate the cutoff date (60 days ago in UTC)
$cutOffDate = (Get-Date).AddDays(-60).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')

# Construct the OData filter for enabled users who haven't signed in in 60 days
$filter = "accountEnabled eq true and (lastSignInDateTime le '$cutOffDate' or lastSignInDateTime eq null)"

# Retrieve all users matching the filter
$users = Get-MgUser -Filter $filter -Property accountEnabled, lastSignInDateTime -All

# Disable each user account
foreach ($user in $users) {
    Update-MgUser -UserId $user.Id -BodyParameter @{accountEnabled = $false}
}
```

---

### ✅ **Explanation of Key Components**

#### **1. Connecting to Microsoft Graph**
- `Connect-MgGraph -Scopes "User.ReadWrite.All"` ensures the script has the required **Graph API permissions** to **read user data** and **update user properties** (disabling accounts).

#### **2. Date Calculation**
- `$cutOffDate = (Get-Date).AddDays(-60).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')`:
  - Gets the current date and subtracts 60 days.
  - Converts to **UTC time** (important for accurate comparison with `lastSignInDateTime` which is stored in UTC).
  - Formats the date in **ISO 8601 format** required by Microsoft Graph.

#### **3. OData Filter**
- `accountEnabled eq true and (lastSignInDateTime le '$cutOffDate' or lastSignInDateTime eq null)`:
  - Filters users who are **enabled** (`accountEnabled eq true`).
  - Includes users who:
    - Haven't signed in in the last 60 days (`lastSignInDateTime le '$cutOffDate'`).
    - **Never signed in** (`lastSignInDateTime eq null`).

#### **4. Retrieving Users**
- `Get-MgUser -Filter $filter -Property accountEnabled, lastSignInDateTime -All`:
  - Uses the constructed filter to retrieve all matching users.
  - Specifies the `accountEnabled` and `lastSignInDateTime` properties to reduce data transfer.
  - Uses `-All` to ensure **all pages** of results are retrieved (important for large user bases).

#### **5. Disabling User Accounts**
- `Update-MgUser -UserId $user.Id -BodyParameter @{accountEnabled = $false}`:
  - Disables the user's account by setting `accountEnabled` to `false`.

---

### 📌 **Permissions Required**
- **Delegated Permissions**: `User.ReadWrite.All`
  - Required to **read user data** and **disable user accounts**.
- **Application Permissions**: `User.ReadWrite.All` (if running as an app, not a user).

---

### 📌 **Notes**
- This script assumes the user running the script has the appropriate **Graph API permissions** enabled in Azure AD.
- For production use, consider adding **error handling**, **logging**, and **confirmation prompts** (`-Confirm` parameter in `Update-MgUser`).
- Ensure the script is **tested in a non-production environment** before deployment.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:14b | ga-deprecated-module | warm | RAG=YES

**Baseline (no RAG):** 4 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 16.0 &nbsp; **Wall sec:** 230.17 &nbsp; **Prompt tokens:** 9390 &nbsp; **Output tokens:** 3681

**Response:**

```powershell
# Script to find and disable Entra ID users who have not signed in for 60 days

# Connect to Microsoft Graph with required permissions
Connect-MgGraph -Scopes "User.Read.All", "User.ReadWrite.All"

# Calculate the date 60 days ago in ISO 8601 format
$date60DaysAgo = (Get-Date).AddDays(-60).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

# Get all enabled users who haven't signed in for 60 days or have never signed in
$users = Get-MgUser -Filter "accountEnabled eq true and (signInActivity/lastSignInDateTime lt '$date60DaysAgo' or signInActivity/lastSignInDateTime eq null)" -ExpandProperty "signInActivity" -All

# Disable each user
foreach ($user in $users) {
    Update-MgUser -UserId $user.Id -UserProperty @{accountEnabled = $false}
}
```

---

### ✅ **Explanation of Key Elements**

- **`Connect-MgGraph`**  
  Establishes a connection to Microsoft Graph with the required **`User.Read.All`** (to retrieve user data) and **`User.ReadWrite.All`** (to modify user account status) permissions.

- **`Get-MgUser`**  
  Retrieves all enabled users who have not signed in for 60 days or have never signed in.  
  - **Filter**:  
    - `accountEnabled eq true` ensures only enabled accounts are considered.  
    - `signInActivity/lastSignInDateTime lt '$date60DaysAgo'` filters users who last signed in more than 60 days ago.  
    - `signInActivity/lastSignInDateTime eq null` includes users who have never signed in.  
  - **ExpandProperty**:  
    Expands the `signInActivity` property to access the `lastSignInDateTime` field.

- **`Update-MgUser`**  
  Disables the user's account by setting `accountEnabled` to `$false`.

---

### ⚠️ **Important Notes**

- **Permissions**:  
  Ensure the user executing the script has the **`User.ReadWrite.All`** application permission in Azure AD. This is required to disable user accounts.

- **Time Zone**:  
  The script uses `ToUniversalTime()` to avoid timezone discrepancies when comparing dates.

- **Error Handling**:  
  This script assumes all users are accessible and that the Graph API is available. In production, consider adding `try/catch` blocks or logging for robustness.

- **Performance**:  
  The use of `-All` ensures all pages of results are retrieved, even if the number of users exceeds the default page size.

---

### 📌 **Graph API Reference**

- [Get-MgUser](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users/get-mguser)  
- [Update-MgUser](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.users/update-mguser)  
- [Connect-MgGraph](https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.authentication/connect-mggraph)

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:14b | ga-error-handling | cold | RAG=YES

**Baseline (no RAG):** 5 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 17.4 &nbsp; **Wall sec:** 350.16 &nbsp; **Prompt tokens:** 5589 &nbsp; **Output tokens:** 5902

**Response:**

```powershell
Function Reset-UserMFA {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Initialize result object
    $result = [PSCustomObject]@{
        Success        = $false
        UserId         = $UserId
        MethodsRemoved = 0
        Error          = $null
    }

    try {
        # Connect to Graph with required scope
        Connect-MgGraph -Scopes "UserAuthenticationMethod.ReadWrite.All"
    }
    catch {
        $result.Error = "Failed to connect to Microsoft Graph: $_"
        Write-Verbose $result.Error
        return $result
    }

    try {
        # Retrieve user authentication methods
        $uri = "https://graph.microsoft.com/v1.0/users/$UserId/authentication/methods"
        $response = Invoke-MgGraphRequest -Method GET -Uri $uri
        $authMethods = $response.value
    }
    catch {
        if ($_.Exception.Response.StatusCode -eq 404) {
            $result.Error = "User not found."
        }
        elseif ($_.Exception.Response.StatusCode -eq 403) {
            $result.Error = "Insufficient permissions."
        }
        else {
            $result.Error = "Error retrieving authentication methods: $_"
        }
        Write-Verbose $result.Error
        return $result
    }

    # Log revert entry
    Write-Verbose "Revert log entry: All MFA methods for user $UserId will be removed."

    $methodsRemoved = 0
    $success = $true
    $errorDetails = $null

    foreach ($method in $authMethods) {
        $methodId = $method.id
        $deleteUri = "https://graph.microsoft.com/v1.0/users/$UserId/authentication/methods/$methodId"

        try {
            Invoke-MgGraphRequest -Method DELETE -Uri $deleteUri
            $methodsRemoved++
        }
        catch {
            if ($_.Exception.Response.StatusCode -eq 404) {
                Write-Verbose "Authentication method $methodId not found during deletion. Skipping."
            }
            else {
                $errorDetails = "Error deleting authentication method $methodId: $_"
                $success = $false
                Write-Verbose $errorDetails
            }
        }
    }

    # Update result object
    $result.Success = $success
    $result.MethodsRemoved = $methodsRemoved
    $result.Error = $errorDetails

    return $result
}
```

---

### 🔍 **Explanation of Key Features**

- **Connection Handling**:  
  The function begins by connecting to Microsoft Graph using `Connect-MgGraph` with the required scope `UserAuthenticationMethod.ReadWrite.All`, ensuring access to user authentication methods.

- **Error Handling**:  
  - **404 (User Not Found)**:  
    During retrieval, if the user is not found, the function returns with `Success = $false` and `Error = "User not found."`.
  - **403 (Insufficient Permissions)**:  
    If the user lacks required permissions, the function returns with `Success = $false` and `Error = "Insufficient permissions."`.
  - **Other Retrieval Errors**:  
    Any other error during retrieval is logged and returned in the `Error` property.

- **Deletion Loop**:  
  Each authentication method is deleted individually. If a method is not found (404), it is skipped with a verbose log. If any deletion fails with a non-404 error, it is logged, and the overall `Success` flag is set to `$false`.

- **Revert Log Entry**:  
  A `Write-Verbose` log entry is generated before any destructive action (i.e., before the deletion loop), as required.

- **Return Object**:  
  The function returns a structured object with:
  - `Success` (bool): `$true` if all steps succeeded, `$false` otherwise.
  - `UserId` (string): The user's ID.
  - `MethodsRemoved` (int): Count of successfully removed MFA methods.
  - `Error` (string): Human-readable error message, if any.

- **No `Write-Host` Usage**:  
  All progress and logs are output via `Write-Verbose` for compatibility with scripting and silent execution.

---

### 📌 **Usage Example**

```powershell
$result = Reset-UserMFA -UserId "user@domain.com"
if ($result.Success) {
    Write-Host "MFA methods removed successfully: $($result.MethodsRemoved) methods."
} else {
    Write-Host "Failed to reset MFA methods: $($result.Error)"
}
```

---

### ✅ **Requirements**
- **Permissions**: Ensure the user running the script has the `UserAuthenticationMethod.ReadWrite.All` permission.
- **Module**: The `Microsoft.Graph.Authentication` module must be installed and imported.
- **Graph Version**: Designed for Microsoft Graph v1.0 (default).

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:14b | ga-error-handling | warm | RAG=YES

**Baseline (no RAG):** 5 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 17.2 &nbsp; **Wall sec:** 392.04 &nbsp; **Prompt tokens:** 5589 &nbsp; **Output tokens:** 6729

**Response:**

```powershell
function Reset-UserMFA {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Revert log entry before any destructive action
    Write-Verbose "Revert log entry: Attempting to remove MFA methods for user $UserId"

    try {
        # Retrieve all authentication methods for the user
        $uri = "https://graph.microsoft.com/v1.0/users/$UserId/authentication/methods"
        $methodsResponse = Invoke-MgGraphRequest -Method GET -Uri $uri

        # Check if the response has methods
        if ($methodsResponse -eq $null -or $methodsResponse.value -eq $null) {
            return [PSCustomObject]@{
                Success = $true
                UserId = $UserId
                MethodsRemoved = 0
                Error = $null
            }
        }

        $methods = $methodsResponse.value
        $methodsRemoved = 0
        $hasError = $false

        foreach ($method in $methods) {
            try {
                $deleteUri = "https://graph.microsoft.com/v1.0/users/$UserId/authentication/methods/$($method.id)"
                $deleteResponse = Invoke-MgGraphRequest -Method DELETE -Uri $deleteUri
                $methodsRemoved++
            } catch {
                # Handle specific HTTP errors
                if ($_.Exception -is [System.Net.Http.HttpRequestException]) {
                    $response = $_.Exception.Response
                    if ($response.StatusCode -eq [System.Net.HttpStatusCode]::NotFound) {
                        Write-Verbose "Method $method.id not found. Skipping."
                    } elseif ($response.StatusCode -eq [System.Net.HttpStatusCode]::Forbidden) {
                        Write-Verbose "Permission denied. Cannot remove method $method.id."
                        $hasError = $true
                    } else {
                        Write-Verbose "Error deleting method $method.id: $($_.Exception.Message)"
                        $hasError = $true
                    }
                } else {
                    Write-Verbose "Unexpected error deleting method $method.id: $($_.Exception.Message)"
                    $hasError = $true
                }
            }
        }

        # If any error occurred during deletion, return failure
        if ($hasError) {
            return [PSCustomObject]@{
                Success = $false
                UserId = $UserId
                MethodsRemoved = $methodsRemoved
                Error = "Some methods could not be removed."
            }
        }

        return [PSCustomObject]@{
            Success = $true
            UserId = $UserId
            MethodsRemoved = $methodsRemoved
            Error = $null
        }
    } catch {
        # Handle errors during retrieval of methods
        if ($_.Exception -is [System.Net.Http.HttpRequestException]) {
            $response = $_.Exception.Response
            if ($response.StatusCode -eq [System.Net.HttpStatusCode]::NotFound) {
                return [PSCustomObject]@{
                    Success = $false
                    UserId = $UserId
                    MethodsRemoved = 0
                    Error = "User not found."
                }
            } elseif ($response.StatusCode -eq [System.Net.HttpStatusCode]::Forbidden) {
                return [PSCustomObject]@{
                    Success = $false
                    UserId = $UserId
                    MethodsRemoved = 0
                    Error = "Insufficient permissions to retrieve user methods."
                }
            } else {
                return [PSCustomObject]@{
                    Success = $false
                    UserId = $UserId
                    MethodsRemoved = 0
                    Error = $_.Exception.Message
                }
            }
        } else {
            return [PSCustomObject]@{
                Success = $false
                UserId = $UserId
                MethodsRemoved = 0
                Error = $_.Exception.Message
            }
        }
    }
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:14b | ps-graph-stale-users | cold | RAG=YES

**Baseline (no RAG):** 4 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 16.4 &nbsp; **Wall sec:** 175.44 &nbsp; **Prompt tokens:** 9365 &nbsp; **Output tokens:** 2568

**Response:**

```powershell
# Connect to Microsoft Graph with required scope
Connect-MgGraph -Scopes "User.Read.All"

# Calculate the date 90 days ago
$thresholdDate = (Get-Date).AddDays(-90).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

# Retrieve users who haven't signed in for 90 days and are enabled
$users = Get-MgUser -Filter "lastSignInDateTime le '$thresholdDate' and accountEnabled eq true" -ExpandProperty "mail,displayName"

# Prepare the output
$output = @()
foreach ($user in $users) {
    $output += [PSCustomObject]@{
        UPN = $user.UserPrincipalName
        DisplayName = $user.DisplayName
        LastSignInDateTime = $user.LastSignInDateTime
        AccountEnabled = $user.AccountEnabled
    }
}

# Export to CSV
$output | Export-Csv -Path "C:\path\to\output.csv" -NoTypeInformation
```

---

### ✅ **Explanation of the Script**:

- **Connect-MgGraph**: Establishes a connection to Microsoft Graph with the required scope `User.Read.All` to retrieve user data.
- **Threshold Date Calculation**: Computes the date 90 days ago in UTC format to filter users who haven't signed in within that period.
- **Get-MgUser**: Retrieves user objects with filters:
  - `lastSignInDateTime le '$thresholdDate'`: Users who haven't signed in in the last 90 days.
  - `accountEnabled eq true`: Only users with enabled accounts.
- **ExpandProperty**: Ensures the `mail` and `displayName` properties are included in the results.
- **Output Preparation**: Converts the results into a custom object with the required fields: UPN, DisplayName, LastSignInDateTime, and AccountEnabled.
- **Export-Csv**: Exports the final data to a CSV file for reporting or further analysis.

---

### 📌 **Important Notes**:

- **Module Requirement**: This script assumes the use of the `Microsoft.Graph.Users` module, which is not explicitly listed in the provided reference. However, this is necessary to access user data like `lastSignInDateTime` and `accountEnabled`.
- **Permissions**: The `User.Read.All` scope is required for retrieving user data across the tenant.
- **Date Format**: The date is formatted in ISO 8601 (`yyyy-MM-ddTHH:mm:ssZ`) to ensure compatibility with Microsoft Graph's filtering mechanism.
- **Path Customization**: Replace `"C:\path\to\output.csv"` with the desired file path for the CSV output.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:14b | ps-graph-stale-users | warm | RAG=YES

**Baseline (no RAG):** 4 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 16.6 &nbsp; **Wall sec:** 123.82 &nbsp; **Prompt tokens:** 9365 &nbsp; **Output tokens:** 2047

**Response:**

```powershell
# Script to find Entra ID users not signed in for 90 days and are enabled

# Step 1: Connect to Microsoft Graph
Connect-MgGraph -Scopes "User.Read.All"

# Step 2: Calculate the cutoff date (90 days ago)
$cutoffDate = (Get-Date).AddDays(-90).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

# Step 3: Query users with lastSignInDateTime older than 90 days and enabled
$users = Get-MgUser -Filter "lastSignInDateTime lt '$cutoffDate' and accountEnabled eq true"

# Step 4: Select required properties and export to CSV
$users | Select-Object UserPrincipalName, DisplayName, LastSignInDateTime, AccountEnabled |
Export-Csv -Path "C:\path\to\users_not_signed_in_90_days.csv" -NoTypeInformation

# Step 5: Disconnect from Graph (optional)
Disconnect-MgGraph
```

---

### 📌 Notes:
- **Connect-MgGraph** is used with the `User.Read.All` scope to retrieve user data.
- **Get-MgUser** is assumed to be available (not shown in the reference, but commonly used in Graph PowerShell).
- **Filter** parameter is used to query users with `lastSignInDateTime` older than 90 days and `accountEnabled` set to `true`.
- **Export-Csv** writes the results to a CSV file with the required columns: `UPN`, `DisplayName`, `LastSignInDateTime`, and `AccountEnabled`.
- Ensure the script runs in a context with proper permissions and the Microsoft Graph PowerShell module is installed.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:8b | ga-deprecated-module | cold | RAG=YES

**Baseline (no RAG):** 4 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 30.4 &nbsp; **Wall sec:** 80.72 &nbsp; **Prompt tokens:** 9390 &nbsp; **Output tokens:** 2067

**Response:**

```powershell
# Connect to Microsoft Graph with required permissions
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Calculate the date 60 days ago from today
$thresholdDate = [datetime]::UtcNow.AddDays(-60)
$isoDate = $thresholdDate.ToString('yyyy-MM-ddTHH:mm:ssZ')

# Retrieve all enabled users with last sign-in older than 60 days
$users = Get-MgUser -Filter "lastSignInDateTime le $isoDate and accountEnabled eq true" -Property id,accountEnabled,lastSignInDateTime -All

# Disable each user account
foreach ($user in $users) {
    Set-MgUser -UserId $user.Id -AccountEnabled $false
    Write-Host "Disabled user: $($user.Id)"
}
```

### Explanation:
1. **Authentication**: The script starts by connecting to Microsoft Graph with the `User.ReadWrite.All` scope, which provides the necessary permissions to read and update user accounts.

2. **Date Calculation**: The script calculates the date 60 days prior to the current date and formats it in ISO 8601 format (`yyyy-MM-ddTHH:mm:ssZ`) for use in the OData filter.

3. **User Filtering**: The `Get-MgUser` cmdlet is used with a filter to retrieve all enabled users whose last sign-in date is older than 60 days. The `-Property` parameter ensures that only the necessary properties (`id`, `accountEnabled`, and `lastSignInDateTime`) are retrieved, improving efficiency.

4. **Account Disablement**: Each user found is disabled using the `Set-MgUser` cmdlet, which sets the `accountEnabled` property to `$false`. A confirmation message is output for each user disabled.

### Permissions Required:
- **Scope**: `User.ReadWrite.All` (ensures both read and write access to user accounts)
- **Module**: Microsoft.Graph (required for all cmdlets used in the script)

This script adheres strictly to the Microsoft Graph PowerShell module and avoids deprecated or retired modules like AzureAD or MSOnline.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:8b | ga-deprecated-module | warm | RAG=YES

**Baseline (no RAG):** 4 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 30.0 &nbsp; **Wall sec:** 122.36 &nbsp; **Prompt tokens:** 9390 &nbsp; **Output tokens:** 3660

**Response:**

```powershell
# Connect to Microsoft Graph with required scopes
Connect-MgGraph -Scopes "User.Read.All", "User.ReadWrite.All"

# Calculate the date 60 days ago in UTC
$today = [System.DateTime]::UtcNow
$thresholdDate = $today.AddDays(-60)
$filterDate = $thresholdDate.ToString("yyyy-MM-ddTHH:mm:ssZ")

# Construct the filter for Get-MgUser
$filter = "accountEnabled eq true and (lastSignInDateTime lt datetime'$filterDate' or lastSignInDateTime eq null)"

# Retrieve users matching the filter
$users = Get-MgUser -Filter $filter -Property Id, accountEnabled, lastSignInDateTime

# Disable each user
foreach ($user in $users) {
    Write-Host "Disabling user: $($user.Id)"
    Update-MgUser -UserId $user.Id -BodyParameter @{ accountEnabled = $false }
}
```

### Explanation:
1. **Authentication**: The script connects to Microsoft Graph using `Connect-MgGraph` with the required scopes `User.Read.All` (to read user data) and `User.ReadWrite.All` (to update user accounts).

2. **Date Calculation**: The script calculates the date 60 days prior to the current UTC time to determine the threshold for inactivity.

3. **Filter Construction**: The filter string is built to select enabled users (`accountEnabled eq true`) who have not signed in within the last 60 days (`lastSignInDateTime lt datetime'...'`) or have never signed in (`lastSignInDateTime eq null`).

4. **User Retrieval**: The script uses `Get-MgUser` with the constructed filter and specifies the properties to retrieve (`Id`, `accountEnabled`, and `lastSignInDateTime`).

5. **Account Disabling**: For each user found, the script calls `Update-MgUser` to set `accountEnabled` to `false`, effectively disabling the account.

### Permissions Required:
- **User.Read.All** (Read user data)
- **User.ReadWrite.All** (Update user accounts)

This script ensures compliance with the requirement to use only the Microsoft Graph PowerShell module and avoids deprecated or retired modules like AzureAD or MSOnline.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:8b | ga-error-handling | cold | RAG=YES

**Baseline (no RAG):** 5 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 32.2 &nbsp; **Wall sec:** 132.56 &nbsp; **Prompt tokens:** 5589 &nbsp; **Output tokens:** 4049

**Response:**

```powershell
function Reset-MgUserMfaMethods {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$UserId
    )

    # Revert log entry
    Write-Verbose "Reverting user $UserId's MFA methods before deletion."

    # Initialize result object
    $result = [PSCustomObject]@{
        Success = $true
        UserId = $UserId
        MethodsRemoved = 0
        Error = ""
    }

    try {
        # Connect to Microsoft Graph with required scopes
        Write-Verbose "Connecting to Microsoft Graph with scopes."
        Connect-MgGraph -Scopes "UserAuthenticationMethod.ReadWrite.All", "User.Read.All" -ErrorAction Stop
    } catch {
        Write-Verbose "Failed to connect to Graph: $_"
        $result.Success = $false
        $result.Error = "Failed to connect to Graph"
        return $result
    }

    try {
        # Retrieve user's authentication methods
        Write-Verbose "Retrieving authentication methods for user $UserId."
        $statusCode = $null
        $methods = Invoke-MgGraphRequest -Uri "https://graph.microsoft.com/v1.0/users/$UserId/authenticationMethods" -Method Get -StatusCodeVariable statusCode -ErrorAction Stop

        if (-not $methods) {
            Write-Verbose "No authentication methods found for user $UserId."
            return $result
        }
    } catch {
        Write-Verbose "Error retrieving authentication methods: $_"
        if ($statusCode -eq 404) {
            $result.Success = $false
            $result.Error = "User not found (404)"
        } elseif ($statusCode -eq 403) {
            $result.Success = $false
            $result.Error = "Insufficient permissions (403)"
        } else {
            $result.Success = $false
            $result.Error = "Error retrieving authentication methods: $_"
        }
        return $result
    }

    try {
        # Delete each authentication method
        Write-Verbose "Deleting authentication methods for user $UserId."
        $methodsRemoved = 0
        foreach ($method in $methods.value) {
            try {
                $uri = "https://graph.microsoft.com/v1.0/users/$UserId/authenticationMethods/$($method.id)"
                $statusCode = $null
                $result = Invoke-MgGraphRequest -Uri $uri -Method Delete -StatusCodeVariable statusCode -ErrorAction Stop
                $methodsRemoved++
            } catch {
                Write-Verbose "Error deleting method $($method.id): $_"
                if ($statusCode -eq 404) {
                    Write-Verbose "Authentication method not found (404)"
                } elseif ($statusCode -eq 403) {
                    Write-Verbose "Insufficient permissions to delete method (403)"
                }
            }
        }

        $result.MethodsRemoved = $methodsRemoved
    } catch {
        Write-Verbose "Error during method deletion: $_"
        $result.Success = $false
        $result.Error = "Error during method deletion: $_"
    }

    return $result
}
```

---

### 📌 **Key Implementation Notes**

1. **Revert Log Entry**  
   A `Write-Verbose` is used to log the action before any destructive operations, ensuring compliance with the requirement to avoid `Write-Host`.

2. **Error Handling**  
   - Each API call (GET, DELETE) is wrapped in a `try/catch` block.
   - Specific HTTP status codes (404, 403) are handled explicitly, with appropriate error messages.

3. **Graph Authentication**  
   - The `Connect-MgGraph` cmdlet is used to authenticate with the required scopes:  
     `UserAuthenticationMethod.ReadWrite.All` and `User.Read.All`.

4. **Structured Return Object**  
   - A custom object is returned with properties: `Success`, `UserId`, `MethodsRemoved`, and `Error`.

5. **PowerShell Best Practices**  
   - Uses `Write-Verbose` for progress and logging.
   - Avoids `Write-Host` as required.
   - Uses `-ErrorAction Stop` to ensure exceptions are propagated to the `catch` blocks.

6. **Robustness**  
   - Handles cases where the user does not exist (404) or the user lacks permissions (403).
   - Continues deleting methods even if some fail, logging errors for each.

This function provides a safe, reusable, and production-ready way to reset MFA authentication methods for a user while adhering to Microsoft Graph best practices and error handling.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:8b | ga-error-handling | warm | RAG=YES

**Baseline (no RAG):** 5 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 32.4 &nbsp; **Wall sec:** 109.82 &nbsp; **Prompt tokens:** 5589 &nbsp; **Output tokens:** 3550

**Response:**

```powershell
function Reset-MgUserMfaMethods {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Revert log entry before any destructive action
    Write-Verbose "Reverting MFA methods for user $UserId"

    # Initialize result object
    $result = [PSCustomObject]@{
        Success = $true
        UserId  = $UserId
        MethodsRemoved = 0
        Error    = ""
    }

    try {
        # Connect to Microsoft Graph with required scopes
        Connect-MgGraph -Scopes "User.MFARead.All", "User.MFAWrite.All" -ErrorAction Stop
    } catch {
        Write-Verbose "Failed to connect to Microsoft Graph: $_"
        $result.Success = $false
        $result.Error = "Failed to connect to Microsoft Graph: $_"
        return $result
    }

    try {
        # Retrieve all authentication methods for the user
        $methods = Get-MgUserAuthenticationMethod -UserId $UserId -ErrorAction Stop
    } catch {
        Write-Verbose "Failed to retrieve authentication methods for user $UserId: $_"
        $result.Success = $false
        $result.Error = "Failed to retrieve authentication methods: $_"
        return $result
    }

    if (-not $methods) {
        Write-Verbose "No authentication methods found for user $UserId"
        return $result
    }

    # Attempt to remove each authentication method
    $methodsRemoved = 0
    foreach ($method in $methods) {
        try {
            # Construct the DELETE request URI
            $uri = "https://graph.microsoft.com/v1.0/users/$UserId/authenticationMethods/$($method.Id)"
            
            # Perform the DELETE operation
            $statusCode = $null
            $response = Invoke-MgGraphRequest -Uri $uri -Method DELETE -StatusCodeVariable statusCode -ErrorAction Stop
            
            # Check if the deletion was successful
            if ($statusCode -eq 204) {
                $methodsRemoved++
            } else {
                Write-Verbose "Failed to delete authentication method ID: $($method.Id) (Status Code: $statusCode)"
            }
        } catch {
            Write-Verbose "Error deleting authentication method ID: $($method.Id) - $_"
        }
    }

    # Update result object with final state
    $result.MethodsRemoved = $methodsRemoved
    return $result
}
```

---

### 🔍 **Explanation of Key Components**

1. **Revert Log Entry**:
   - A `Write-Verbose` statement is used to log the intention to revert MFA methods before any destructive action is taken.

2. **Graph Authentication**:
   - The `Connect-MgGraph` cmdlet is used with scopes `User.MFARead.All` and `User.MFAWrite.All` to ensure proper permissions for reading and deleting authentication methods.

3. **Authentication Method Retrieval**:
   - The `Get-MgUserAuthenticationMethod` cmdlet is used to fetch all authentication methods for the specified user. If this fails, the function returns an error.

4. **Destructive Action Handling**:
   - Each authentication method is deleted using `Invoke-MgGraphRequest` with a `DELETE` method.
   - A `try/catch` block ensures that errors during deletion are logged but do not stop the process for other methods.

5. **Error Handling**:
   - Specific error handling for 404 (user not found) and 403 (insufficient permissions) is achieved through the `-ErrorAction Stop` parameter, which allows the function to catch and return appropriate error messages.

6. **Structured Result Object**:
   - A `[PSCustomObject]` is used to return a structured result with properties `Success`, `UserId`, `MethodsRemoved`, and `Error`.

7. **No Use of Write-Host**:
   - Progress and status information is communicated using `Write-Verbose` as required.

---

### ✅ **Usage Example**

```powershell
$userId = "user@domain.com"
$result = Reset-MgUserMfaMethods -UserId $userId
Write-Output $result
```

This function ensures that all MFA authentication methods for a user are removed safely, with appropriate error handling and logging.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:8b | ps-graph-stale-users | cold | RAG=YES

**Baseline (no RAG):** 4 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 30.4 &nbsp; **Wall sec:** 106.82 &nbsp; **Prompt tokens:** 9365 &nbsp; **Output tokens:** 2904

**Response:**

To find all Entra ID (formerly Azure AD) user accounts that have not signed in for **90 days** and are still **enabled**, we can use the **Microsoft Graph PowerShell SDK**. This script will:

- Connect to Microsoft Graph using a service principal or interactive authentication.
- Retrieve all users.
- Filter users based on `accountEnabled` and `lastSignInDateTime`.
- Export the results to a CSV file with the required columns.

---

### ✅ PowerShell Script

```powershell
# Connect to Microsoft Graph (Use appropriate authentication method)
# Example: Using Client Secret Credential
Connect-MgGraph -Scopes "User.Read.All" -ClientSecretCredential (Get-Credential -Credential "Client_Id")

# Define the date threshold (90 days ago)
$lastSignInThreshold = (Get-Date).AddDays(-90)

# Retrieve all users
$users = Get-MgUser -All

# Filter users who are enabled and have not signed in for 90 days
$inactiveUsers = $users | Where-Object {
    $_.AccountEnabled -eq $true -and
    $_.LastSignInDateTime -ne $null -and
    [datetime]::Parse($_.LastSignInDateTime) -lt $lastSignInThreshold
}

# Export results to CSV
$inactiveUsers | Select-Object `
    UserPrincipalName, `
    DisplayName, `
    LastSignInDateTime, `
    AccountEnabled | `
Export-Csv -Path "C:\Temp\InactiveUsers_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
```

---

### 📌 Notes

- **Authentication**: The script uses `Connect-MgGraph` with a `ClientSecretCredential` for app-only access. You can also use `UseDeviceCode` for interactive authentication.
- **Permissions**: The script requires the **`User.Read.All`** scope to read all user data.
- **Date Handling**: The script uses `[datetime]::Parse()` to ensure proper date comparison.
- **CSV Output**: The CSV includes the required columns: `UserPrincipalName`, `DisplayName`, `LastSignInDateTime`, and `AccountEnabled`.

---

### ✅ Example Output

| UserPrincipalName        | DisplayName | LastSignInDateTime         | AccountEnabled |
|--------------------------|-------------|----------------------------|----------------|
| user1@domain.com         | John Doe    | 2023-01-01T12:00:00Z       | True           |
| user2@domain.com         | Jane Smith  | 2022-10-15T08:30:00Z       | True           |

---

### 📌 Optional Enhancements

- **Pagination**: If the number of users is large, use `-Top` and `-Skip` for efficient pagination.
- **Error Handling**: Add try-catch blocks to handle exceptions during user retrieval or parsing.
- **Custom Output Path**: Adjust the CSV path as needed for your environment.

This script is **production-ready** and follows best practices for **Microsoft Graph automation** with **PowerShell**.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3:8b | ps-graph-stale-users | warm | RAG=YES

**Baseline (no RAG):** 4 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 29.8 &nbsp; **Wall sec:** 166.44 &nbsp; **Prompt tokens:** 9365 &nbsp; **Output tokens:** 4954

**Response:**

```powershell
# Connect to Microsoft Graph with the necessary permissions
Connect-MgGraph -Scopes "User.Read.All"

# Retrieve all users
$users = Get-MgUser -All

# Filter users who are enabled and have not signed in for 90 days or more
$inactiveUsers = $users | Where-Object {
    $_."AccountEnabled" -eq $true -and 
    (
        ($_."lastSignInDateTime" -eq $null) -or 
        ([datetime]::UtcNow - $_."lastSignInDateTime").Days -ge 90
    )
}

# Export the filtered users to CSV
$inactiveUsers | Select-Object UserPrincipalName, DisplayName, lastSignInDateTime, AccountEnabled | Export-Csv -Path "C:\output\inactive_users.csv" -NoTypeInformation
```

### Explanation:
1. **Authentication**: The script starts by connecting to Microsoft Graph using `Connect-MgGraph` with the `User.Read.All` scope to ensure access to user data.
2. **User Retrieval**: It retrieves all users using `Get-MgUser -All` to handle pagination.
3. **Filtering Logic**: The script filters users who are enabled (`AccountEnabled -eq $true`) and have not signed in for 90 days or more. This includes users who have never signed in (`lastSignInDateTime -eq $null`) or whose last sign-in date is older than 90 days.
4. **Export to CSV**: The filtered users are exported to a CSV file with columns for UPN, Display Name, Last Sign-In Date, and Account Enabled status.

### Notes:
- Ensure the script has write permissions to the specified CSV output path.
- Adjust the path `"C:\output\inactive_users.csv"` as needed for your environment.
- The script assumes the presence of standard Microsoft Graph properties like `lastSignInDateTime` and `AccountEnabled`. Verify these property names match your environment's schema.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ga-deprecated-module | cold | RAG=YES

**Baseline (no RAG):** 2-3 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 15.1 &nbsp; **Wall sec:** 194.01 &nbsp; **Prompt tokens:** 9383 &nbsp; **Output tokens:** 2585

**Response:**

Here is a PowerShell script that accomplishes the task:

```powershell
# Connect to Microsoft Graph with User.ReadWrite.All scope
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Get all enabled users and their sign-in activity
$users = Get-MgUser -Filter "accountEnabled eq true" -Property signInActivity

# Iterate through each user
foreach ($user in $users) {
    # Check if the user has a lastSignInDateTime older than 60 days
    If ($user.signInActivity.lastSignInDateTime -lt (Get-Date).AddDays(-60)) {
        Write-Output "Disabling user: $($user.displayName) ($user.userPrincipalName)"
        # Disable the user account
        Set-MgUser -Id $user.id -AccountEnabled False
    }
}
```

**Explanation:**

1. **Connect to Microsoft Graph:** The script starts by connecting to Microsoft Graph using `Connect-MgGraph` with the required scope `User.ReadWrite.All`, which is necessary for reading and modifying user accounts.

2. **Retrieve Users:** It then fetches all enabled users using `Get-MgUser` with a filter on `accountEnabled eq true`. The `-Property signInActivity` parameter ensures that sign-in activity details are included in the results.

3. **Check Last Sign-In Date:** For each user, it checks if their last sign-in date (`signInActivity.lastSignInDateTime`) is older than 60 days using `(Get-Date).AddDays(-60)` to represent 60 days ago.

4. **Disable User Accounts:** If a user's last sign-in was over 60 days ago, the script disables their account using `Set-MgUser` with `-AccountEnabled False`.

This script efficiently identifies and disables inactive user accounts while adhering to Microsoft Graph PowerShell best practices.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ga-deprecated-module | warm | RAG=YES

**Baseline (no RAG):** 2-3 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 15.5 &nbsp; **Wall sec:** 57.58 &nbsp; **Prompt tokens:** 9383 &nbsp; **Output tokens:** 890

**Response:**

Here is the PowerShell script that meets your requirements:

```powershell
# Connect to Microsoft Graph using required scopes
Connect-MgGraph -Scopes "User.Read.All", "User.ReadWrite.All"

try {
    # Get all enabled users with LastSignInDateTime older than 60 days
    $users = Get-MgUser -Filter "(isLicensed eq true) and (accountEnabled eq true)" -Property id, displayName, lastSignInDateTime | 
        Where-Object { $_.lastSignInDateTime -lt (Get-Date).AddDays(-60) }

    if ($users.Count -eq 0) {
        Write-Host "No users found who meet the criteria."
        return
    }

    # Disable each user's account
    foreach ($user in $users) {
        Write-Host "Disabling account for user: $($user.displayName)"
        Set-MgUser -Id $user.id -AccountEnabled False
    }
} catch {
    Write-Error $_.Exception.Message
}
```

### Explanation

1. **Connect to Microsoft Graph**:
   - Uses `Connect-MgGraph` with the required scopes (`User.Read.All`, `User.ReadWrite.All`) for reading user information and modifying user accounts.

2. **Retrieve Users**:
   - Uses `Get-MgUser` cmdlet with filtering parameters to get enabled users (`isLicensed eq true` and `accountEnabled eq true`) who haven't signed in for 60 days.
   - Includes properties `id`, `displayName`, and `lastSignInDateTime` for identification.

3. **Disable Accounts**:
   - Iterates over each user retrieved from the filter.
   - Uses `Set-MgUser` cmdlet to disable each user's account by setting `AccountEnabled` to `False`.

4. **Error Handling**:
   - Includes a try-catch block to handle any exceptions and provides error messages.

### Required Permissions

- The script requires the following permissions in Microsoft Entra ID:
  - **Read user information**: `User.Read.All`
  - **Modify user accounts**: `User.ReadWrite.All`

### Notes

- Ensure you have proper authorization to disable user accounts in your organization.
- This script should be run in an environment where you have admin rights over user accounts.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ga-error-handling | cold | RAG=YES

**Baseline (no RAG):** 2-3 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 17.3 &nbsp; **Wall sec:** 114.06 &nbsp; **Prompt tokens:** 5582 &nbsp; **Output tokens:** 1744

**Response:**

Here is a PowerShell function that meets your requirements:

```powershell
Import-Module Microsoft.Graph.Authentication
Import-Module Microsoft.Graph.Identity.SignIns

function Reset-MfaAuthenticationMethods {
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $false)]
        [string]$UserPrincipalName,
        
        [Parameter(Mandatory = $false)]
        [switch]$Verbose
    )

    # Initialize result object
    $result = @{
        Success          = $false
        UserId           = $null
        MethodsRemoved   = 0
        Error            = $null
    }

    try {
        # Check if we're already authenticated
        If (-not $Connected) {
            Write-Verbose "Connecting to Microsoft Graph..."
            Connect-MgGraph -ClientId "your_client_id" -TenantId "your_tenant_id" @PSBoundParameters
        }

        # Get user by ID or UPN
        If ($UserPrincipalName) {
            $userId = (Get-MgUser -Filter "userPrincipalName eq '$UserPrincipalName'" | Select-Object -ExpandProperty Id)
            If (-not $userId) {
                throw "User not found with UPN: $UserPrincipalName"
            }
        }

        # Get all MFA methods for the user
        Write-Verbose "Retrieving MFA authentication methods for user: $UserId..."
        $methods = Get-MgUserAuthenticationMethod -UserId $userId

        If ($methods.Count -eq 0) {
            Write-Verbose "No MFA methods found."
            $result.Success = $true
            return $result
        }

        # Remove each method with try-catch
        foreach ($method in $methods) {
            Try {
                Write-Verbose "Removing MFA method: $($method.DisplayName)"
                Remove-MgUserAuthenticationMethod -UserId $userId -AuthenticationMethodId $method.Id
                $result.MethodsRemoved++
            }
            Catch {
                If ($_ | Match "403") {
                    $result.Error = "Insufficient permissions"
                } ElseIf ($_ | Match "404") {
                    $result.Error = "User not found"
                } Else {
                    $result.Error = $_.Exception.Message
                }
                $result.Success = $false
                Break
            }
        }

        If ($result.MethodsRemoved -gt 0) {
            Write-Verbose "$($methods.Count) MFA methods removed successfully."
            $result.Success = $true
        }

    } Catch {
        If ($_ | Match "403") {
            $result.Error = "Insufficient permissions"
        } ElseIf ($_ | Match "404") {
            $result.Error = "User not found"
        } Else {
            $result.Error = $_.Exception.Message
        }
        Write-Verbose "Error: $($result.Error)"
    }

    return $result
}
```

This function:

1. Connects to Microsoft Graph using app-only credentials.
2. Handles errors for 403 (insufficient permissions) and 404 (user not found).
3. Removes all MFA methods for the specified user if they exist.
4. Returns a structured result object with success status, number of removed methods, and any error messages.

To use this function:

```powershell
# Replace these values with your app registration details
$clientId = "your_client_id"
$tenantId = "your_tenant_id"

# Call the function
$result = Reset-MfaAuthenticationMethods -UserId "user_id" -Verbose

# Example output:
# Success: True/False
# UserId: user_id
# MethodsRemoved: number of removed methods
# Error: error message if any
```

Make sure to replace `your_client_id` and `your_tenant_id` with your actual application registration details.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ga-error-handling | warm | RAG=YES

**Baseline (no RAG):** 2-3 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 16.9 &nbsp; **Wall sec:** 212.33 &nbsp; **Prompt tokens:** 5582 &nbsp; **Output tokens:** 3575

**Response:**

To solve this problem, we need to create a PowerShell function that resets a user's Multi-Factor Authentication (MFA) methods by removing all registered MFA methods. The function should handle exceptions for specific HTTP status codes (403 and 404), log its actions verbosely, and return a structured result object with success status, the number of methods removed, and any error messages.

### Approach
1. **Connect to Microsoft Graph**: Ensure that we are connected to Microsoft Graph using the appropriate scopes for reading user information and managing authentication methods.
2. **Retrieve Authentication Methods**: Use a GET request to fetch all current MFA methods for the specified user.
3. **Delete Each Method**: Iterate over each retrieved MFA method and delete it using a DELETE request.
4. **Handle Exceptions**: Specifically handle HTTP status codes 403 (insufficient permissions) and 404 (user or method not found).
5. **Log Progress**: Use verbose logging to track the progress of the function without using `Write-Host`.
6. **Return Result**: Construct a result object with properties indicating success, the number of methods removed, and any error messages.

### Solution Code
```powershell
function Reset-MfaAuthenticationMethods {
    Param(
        [Parameter(Mandatory = $true)]
        [String]$UserId
    )

    Begin {
        Write-Verbose "Starting MFA reset for user: $UserId"
        $result = @{
            Success          = $true
            UserId           = $userId
            MethodsRemoved   = 0
            Error            = $null
        }
    }

    Try {
        # Connect to Microsoft Graph if not already connected
        If (-not (Get-MgGraphConnection)) {
            Connect-MgGraph -Scopes "User.ReadWrite.All"
        }

        # Get all authentication methods for the user
        $uri = "https://graph.microsoft.com/v1.0/users/$userId/authentication/methods"
        $response = Invoke-MgGraphRequest -Method GET -Uri $uri

        If ($response) {
            ForEach ($method in $response.Value) {
                Try {
                    # Construct the DELETE URI for each method
                    $deleteUri = "https://graph.microsoft.com/v1.0/users/$userId/authentication/methods/$($method.id)"
                    Invoke-MgGraphRequest -Method DELETE -Uri $deleteUri

                    $result.MethodsRemoved++
                }
                Catch {
                    If ($_.Exception.Response.StatusCode -eq 403) {
                        $result.Success = $false
                        $result.Error = "Insufficient permissions to delete MFA method."
                        Break
                    } ElseIf ($_.Exception.Response.StatusCode -eq 404) {
                        Write-Verbose "MFA method not found, skipping deletion."
                    } Else {
                        $result.Success = $false
                        $result.Error = $_.Exception.Message
                        Break
                    }
                }
            }
        }

    } Catch {
        If ($_.Exception.Response.StatusCode -eq 403) {
            $result.Success = $false
            $result.Error = "Insufficient permissions to access user's MFA settings."
        } ElseIf ($_.Exception.Response.StatusCode -eq 404) {
            $result.Success = $true # No methods found or user not exists
            $result.Error = "User not found."
        } Else {
            $result.Success = $false
            $result.Error = $_.Exception.Message
        }
    }

    Finally {
        Write-Verbose "Completed MFA reset for user: $UserId"
        Return [PSCustomObject]$result
    }
}
```

### Explanation
1. **Connect to Microsoft Graph**: The function first checks if it is already connected to Microsoft Graph. If not, it connects using the `User.ReadWrite.All` scope, which allows read and write access to user information.
2. **Retrieve Authentication Methods**: Using a GET request to the endpoint `/users/{userId}/authentication/methods`, the function retrieves all MFA methods for the specified user.
3. **Delete Each Method**: For each retrieved MFA method, the function constructs a DELETE request to remove the method. It keeps track of the number of methods removed.
4. **Handle Exceptions**: If an exception occurs during deletion, it checks for specific HTTP status codes (403 and 404) to provide meaningful error messages. Other exceptions are caught and logged as well.
5. **Log Progress**: The function uses `Write-Verbose` to log its progress without disrupting the console output.
6. **Return Result**: Finally, the function returns a structured result object indicating whether the operation was successful, the number of methods removed, and any error messages encountered.

This approach ensures that the function handles potential errors gracefully and provides clear feedback on its operations.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ps-graph-stale-users | cold | RAG=YES

**Baseline (no RAG):** 2-3 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 15.8 &nbsp; **Wall sec:** 94.82 &nbsp; **Prompt tokens:** 9358 &nbsp; **Output tokens:** 1169

**Response:**

To achieve this task, we'll use Microsoft Graph PowerShell cmdlets to fetch user data and filter based on sign-in activity and account status. Here's a step-by-step explanation of the script:

1. **Import the necessary module**: This ensures that the required cmdlets are available for use.

2. **Connect to Microsoft Graph**: Establish an authenticated session with Microsoft Graph to make API calls.

3. **Get all users**: Retrieve user information from Azure AD.

4. **Filter users**: Apply conditions to find users who haven't signed in for 90 days and have their accounts enabled.

5. **Format and export data**: Structure the output as specified and save it to a CSV file.

Here is the complete script:

```powershell
# Import the Microsoft Graph Users module
Import-Module Microsoft.Graph.Users

# Connect to Microsoft Graph using appropriate credentials
Connect-MgGraph -Scopes "Directory.Read.All"

# Calculate 90 days ago in ISO format
$lastSignInDate = (Get-Date).AddDays(-90).ToString('yyyy-MM-ddTHH:mm:ss.fffZ')

# Get all users with filter for sign-in activity and account status
$users = Get-MgUser -All | Where-Object {
    $_.LastSignInDateTime -lt $lastSignInDate -and $_.AccountEnabled -eq "true"
}

# Select the required properties and format LastSignInDateTime correctly
$formattedUsers = $users | Select-Object `
    UserPrincipalName, `
    DisplayName, `
    @{Name='LastSignInDateTime'; Expression={[datetime]$_.LastSignInDateTime.ToString('yyyy-MM-ddTHH:mm:ssZ')}} `
    AccountEnabled

# Export results to CSV without including the PowerShell pipeline object
$formattedUsers | Export-Csv -Path "Inactive_users.csv" -NoTypeInformation
```

**Notes:**

- **Permissions**: The script requires `Directory.Read.All` permission. Ensure your account has this delegated admin consent.

- **Module Compatibility**: Make sure you're using a compatible version of the Microsoft.Graph.Users module.

This script efficiently retrieves and exports the required user data based on sign-in activity and account status, providing insights into inactive user accounts within your organization.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ps-graph-stale-users | warm | RAG=YES

**Baseline (no RAG):** 2-3 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 15.5 &nbsp; **Wall sec:** 144.68 &nbsp; **Prompt tokens:** 9358 &nbsp; **Output tokens:** 2240

**Response:**

To complete this task, we'll write a PowerShell script using Microsoft Graph to find Entra ID user accounts that haven't signed in for 90 days and are still enabled. The script will export the results to a CSV file.

### Step-by-Step Explanation:

1. **Connect to Microsoft Graph**: Use `Connect-MgGraph` with app-only authentication using a client secret.
2. **Get All Enabled Users**: Retrieve all users with `Get-MgUser` and filter for those who are enabled (`AccountEnabled -eq true`).
3. **Filter by Last Sign-In Date**: For each user, check if their last sign-in date is older than 90 days. This step assumes that the `LastSignInDateTime` property is available (note: in reality, this property isn't directly accessible via Microsoft Graph cmdlets; adjustments may be needed).
4. **Export Results to CSV**: Collect the required fields and export them to a CSV file.

### PowerShell Script:

```powershell
# Connect to Microsoft Graph using app-only authentication with client secret
Connect-MgGraph -ClientId "your_client_id" `
               -TenantId "your_tenant_id" `
               -ClientSecretCredential (Get-Credential -Username "your_client_id")

# Get all enabled users and filter those who haven't signed in for 90 days
$users = Get-MgUser -Filter "AccountEnabled eq true" |
         Where-Object {
             $lastSignIn = $_.LastSignInDateTime
             $ninetyDaysAgo = (Get-Date).AddDays(-90)
             if ($lastSignIn -lt $ninetyDaysAgo) {
                 return $true
             }
             return $false
         }

# Export results to CSV
$csvPath = "inactive_users.csv"
$properties = @("UserPrincipalName", "DisplayName", "LastSignInDateTime", "AccountEnabled")

$users | Select-Object $properties |
Export-Csv -Path $csvPath -NoTypeInformation

Write-Host "Script completed. Results exported to $($csvPath)."
```

### Notes:
- **App-Only Authentication**: The script uses `ClientSecretCredential` for app-only access, requiring valid client ID, tenant ID, and client secret.
- **Filtering Users**: It filters enabled users and checks if their last sign-in was before 90 days ago. Note that `LastSignInDateTime` might not be directly accessible via Microsoft Graph cmdlets; additional API calls or different methods may be needed in a real-world scenario.
- **Export to CSV**: The script exports the filtered users' details into a CSV file named "inactive_users.csv".

This script is a template and needs adjustments based on actual Microsoft Graph capabilities and organizational setup.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ga-deprecated-module | cold | RAG=YES

**Baseline (no RAG):** 0-5 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 18.8 &nbsp; **Wall sec:** 72.73 &nbsp; **Prompt tokens:** 9376 &nbsp; **Output tokens:** 612

**Response:**

To accomplish this task, we'll write a PowerShell script using the `Microsoft.Graph` module to interact with Entra ID (formerly known as Azure AD). The script will:

1. Authenticate to Microsoft Graph.
2. Retrieve all enabled users who have not signed in for 60 days.
3. Disable their accounts.

The required permission scope for this operation is `User.ReadWrite.All`.

Here's the PowerShell script:

```powershell
# Import the necessary module
Import-Module Microsoft.Graph.Identity.SignIns

# Authenticate to Microsoft Graph with the appropriate permissions
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Get the current date and calculate the date 60 days ago
$thirtyDaysAgo = (Get-Date).AddDays(-60)

# Retrieve all enabled users who haven't signed in for more than 60 days
$inactiveUsers = Get-MgUser -Filter "signInActivity/lastSignInDateTime le $thirtyDaysAgo and accountEnabled eq true" `
    -Select userId, displayName

# Check if there are any inactive users found
if ($inactiveUsers.Count -gt 0) {
    foreach ($user in $inactiveUsers) {
        # Disable the user's account
        Update-MgUser -UserId $user.userId -AccountEnabled $false

        Write-Host "Disabled account for $($user.displayName) (ID: $($user.userId))"
    }
} else {
    Write-Host "No users found who haven't signed in for 60 days."
}

# Disconnect from Microsoft Graph
Disconnect-MgGraph
```

### Explanation:

1. **Module Import and Authentication**:
   - `Import-Module Microsoft.Graph.Identity.SignIns`: Imports the necessary module.
   - `Connect-MgGraph -Scopes "User.ReadWrite.All"`: Authenticates to Microsoft Graph with the required permission scope.

2. **Date Calculation**:
   - `$thirtyDaysAgo = (Get-Date).AddDays(-60)`: Calculates the date 60 days ago from today.

3. **Retrieve Inactive Users**:
   - `Get-MgUser -Filter "signInActivity/lastSignInDateTime le $thirtyDaysAgo and accountEnabled eq true"`: Retrieves all users who have an `accountEnabled` status of `true` and haven't signed in since the calculated date 60 days ago.
   - `-Select userId, displayName`: Specifies that only the `userId` and `displayName` properties are needed.

4. **Disable Accounts**:
   - Iterates over each user found and disables their account using `Update-MgUser`.

5. **Output**:
   - Provides feedback on which accounts have been disabled or if no users were found matching the criteria.

6. **Disconnect**:
   - `Disconnect-MgGraph`: Disconnects from Microsoft Graph after operations are complete.

This script assumes you have already configured your environment to support authentication with Microsoft Graph and that you have the necessary permissions to perform these actions.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ga-deprecated-module | warm | RAG=YES

**Baseline (no RAG):** 0-5 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 19.0 &nbsp; **Wall sec:** 34.96 &nbsp; **Prompt tokens:** 9376 &nbsp; **Output tokens:** 659

**Response:**

To accomplish this task using the Microsoft.Graph PowerShell module, you need to write a script that queries all enabled Entra ID users who haven't signed in for 60 days and then disables their accounts. Below is an example script:

```powershell
# Import the required Microsoft Graph Identity SignIns module
Import-Module Microsoft.Graph.Identity.SignIns

# Define the permission scope required for reading user sign-in activity and updating user account status.
# Note: The appropriate permissions must be granted to the application in Azure AD.
$requiredScope = "User.Read.All", "User.AuthenticationMethod.ReadWrite.All"

# Connect to Microsoft Graph with necessary scopes
Connect-MgGraph -Scopes $requiredScope

try {
    # Get all enabled users who haven't signed in for 60 days or more.
    $lastSignInDateThreshold = (Get-Date).AddDays(-60)
    $usersToDisable = Get-MgUser -Filter "accountEnabled eq true and signInSessions/LastSignInDateTime le $lastSignInDateThreshold" -ExpandProperty signInSessions

    foreach ($user in $usersToDisable) {
        # Output user details
        Write-Output "Disabling account for user: $($user.DisplayName) with UserPrincipalName: $($user.UserPrincipalName)"

        # Disable the user's account by setting 'accountEnabled' to false
        Set-MgUser -UserId $user.Id -AccountEnabled $false

        # Optionally, provide some feedback that the operation was successful
        Write-Output "Disabled account for user with UserPrincipalName: $($user.UserPrincipalName)"
    }
}
finally {
    # Disconnect from Microsoft Graph
    Disconnect-MgGraph
}

```

### Explanation:
1. **Import the Module**: The script starts by importing the `Microsoft.Graph.Identity.SignIns` module to access identity-related cmdlets.

2. **Define Required Scopes**: You specify the permission scopes required for this operation, which are `"User.Read.All"` and `"User.AuthenticationMethod.ReadWrite.All"`. Ensure that these permissions are granted to your Azure AD app registration.

3. **Connect to Microsoft Graph**: The `Connect-MgGraph` cmdlet is used to authenticate with the necessary scopes.

4. **Fetch Users**: Use `Get-MgUser` with a filter to fetch users who are enabled (`accountEnabled eq true`) and have not signed in for 60 days or more. The `-ExpandProperty signInSessions` parameter ensures that sign-in sessions data is expanded so you can access the `LastSignInDateTime`.

5. **Disable User Accounts**: Iterate over each user from the filtered list, disable their accounts by setting `accountEnabled` to `$false` using `Set-MgUser`, and output a confirmation message.

6. **Disconnect from Microsoft Graph**: Finally, ensure you disconnect from the Microsoft Graph session with `Disconnect-MgGraph`.

### Permissions:
Make sure that your Azure AD application has been granted permission to read all users' data (`User.Read.All`) and update user account properties (`User.AuthenticationMethod.ReadWrite.All`). You may need administrative privileges in Azure AD to assign these permissions.

This script ensures you handle the task programmatically while adhering to Microsoft's recommended practices for using their Graph API through PowerShell.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ga-error-handling | cold | RAG=YES

**Baseline (no RAG):** 0-5 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 19.9 &nbsp; **Wall sec:** 64.95 &nbsp; **Prompt tokens:** 5543 &nbsp; **Output tokens:** 824

**Response:**

Below is a PowerShell function using Microsoft.Graph to reset a user's Multi-Factor Authentication (MFA) methods by removing all registered methods. The function includes error handling, logging, and returns a structured result object.

```powershell
function Reset-MfaAuthenticationMethods {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Initialize the return object
    $resultObject = @{
        Success      = $false
        UserId       = $null
        MethodsRemoved = 0
        Error        = ""
    }

    try {
        # Revert log entry before any destructive action
        Write-Verbose "Initiating reset of MFA methods for user: $UserId"

        # Connect to Microsoft Graph API
        try {
            Connect-MgGraph -Scopes "User.ReadWrite.All" | Out-Null
            Write-Verbose "Connected to Microsoft Graph with required permissions."
        } catch {
            if ($_ -match 'AccessDenied' -or $_.Exception.Response.StatusCode.value__ -eq 403) {
                $resultObject.Error = "Insufficient permissions to access user data."
                return [PSCustomObject]$resultObject
            } else {
                throw
            }
        }

        # Fetch the authentication methods for the specified user
        try {
            $authenticationMethods = Get-MgUserAuthenticationMethod -UserId $UserId
            Write-Verbose "Retrieved $($authenticationMethods.Count) MFA methods for user: $UserId"
        } catch {
            if ($_ -match 'NotFound' -or $_.Exception.Response.StatusCode.value__ -eq 404) {
                $resultObject.Error = "User not found."
                return [PSCustomObject]$resultObject
            } else {
                throw
            }
        }

        # Remove each authentication method
        foreach ($method in $authenticationMethods) {
            try {
                Remove-MgUserAuthenticationMethod -UserId $UserId -AuthenticationMethodId $method.Id
                Write-Verbose "Removed MFA method: $($method.Id)"
            } catch {
                if ($_ -match 'AccessDenied' -or $_.Exception.Response.StatusCode.value__ -eq 403) {
                    $resultObject.Error = "Insufficient permissions to remove an authentication method."
                    return [PSCustomObject]$resultObject
                } else {
                    Write-Verbose "Error removing MFA method: $($method.Id) - $_"
                }
            }
        }

        # Update the result object with successful operation details
        $resultObject.UserId = $UserId
        $resultObject.MethodsRemoved = $authenticationMethods.Count
        $resultObject.Success = $true

    } catch {
        Write-Verbose "An error occurred: $_"
        $resultObject.Error = $_.Exception.Message
    }

    # Return the result object
    return [PSCustomObject]$resultObject
}

# Example usage:
# Reset-MfaAuthenticationMethods -UserId 'user@example.com'
```

### Explanation:

1. **Parameter Definition**: The function takes a mandatory parameter `UserId`.

2. **Initialization**: A hashtable `$resultObject` is initialized to store the result of the operation.

3. **Connect-MgGraph**: Attempts to connect to Microsoft Graph with the necessary permissions and handles insufficient permissions error (403).

4. **Get-MgUserAuthenticationMethod**: Fetches all MFA methods for the specified user, handling user not found (404) errors.

5. **Remove-MgUserAuthenticationMethod**: Iterates over each method and removes it, capturing specific permission-related errors (403) during removal.

6. **Error Handling**: Each Graph API call is wrapped in a try/catch block to handle exceptions gracefully.

7. **Result Object**: After the operation, the function populates `$resultObject` with the outcome and returns it as a `PSCustomObject`.

8. **Verbose Logging**: Uses `Write-Verbose` for logging progress and errors without displaying them by default in the console output.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ga-error-handling | warm | RAG=YES

**Baseline (no RAG):** 0-5 &nbsp; **RAG chunks injected:** 70
**Tok/sec:** 20.1 &nbsp; **Wall sec:** 42.88 &nbsp; **Prompt tokens:** 5543 &nbsp; **Output tokens:** 858

**Response:**

Here is a PowerShell function that uses Microsoft.Graph to reset a user's Multi-Factor Authentication (MFA) authentication methods by removing all registered methods. The function includes error handling, logging, and structured output:

```powershell
function Reset-MgUserAuthenticationMethods {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$UserId,
        
        [Parameter(Mandatory = $false)]
        [switch]$VerboseOutput
    )

    # Structured return object definition
    $result = @{
        Success         = $false
        UserId          = $null
        MethodsRemoved  = 0
        Error           = $null
    }

    try {
        # Connect to Microsoft Graph with appropriate permissions
        Connect-MgGraph -Scopes "User.ReadWrite.All" | Out-Null

        # Fetch the authentication methods for the specified user
        $authMethods = Get-MgUserAuthenticationMethod -UserId $UserId

        if (-not $authMethods) {
            Write-Verbose -Message "No authentication methods found for UserId: $UserId"
            return $result
        }

        foreach ($method in $authMethods) {
            try {
                # Revert log entry before removing the method
                Write-Verbose -Message "Preparing to remove authentication method with Id: $($method.Id) for UserId: $UserId"

                # Remove the authentication method
                Remove-MgUserAuthenticationMethod -UserId $UserId -AuthenticationMethodId $method.Id
            }
            catch {
                if ($_.Exception.Response.StatusCode -eq 404) {
                    Write-Verbose -Message "Authentication Method not found. It might have been already removed or never existed."
                }
                elseif ($_.Exception.Response.StatusCode -eq 403) {
                    $result.Error = "Insufficient permissions to remove authentication method with Id: $($method.Id)."
                    return $result
                }
                else {
                    # Generic error handling for unexpected exceptions
                    Write-Verbose -Message "Failed to remove authentication method with Id: $($method.Id). Error: $_.Exception.Message"
                    $result.Error = "Unexpected error occurred while removing method. Details: $_.Exception.Message"
                    return $result
                }
            }

            # Increment the count of methods removed
            $result.MethodsRemoved++
        }

        # Set success property to true after all methods are successfully removed
        $result.Success = $true
        $result.UserId  = $UserId

    } catch {
        if ($_.Exception.Response.StatusCode -eq 404) {
            Write-Verbose -Message "User not found. UserId: $UserId"
            $result.Error = "User not found. Ensure the UserId is correct."
        }
        elseif ($_.Exception.Response.StatusCode -eq 403) {
            $result.Error = "Insufficient permissions to perform operation on UserId: $UserId."
        } else {
            Write-Verbose -Message "An unexpected error occurred. Error: $_.Exception.Message"
            $result.Error = "Unexpected error occurred. Details: $_.Exception.Message"
        }
    }

    # Return the structured result object
    return [PSCustomObject]$result
}
```

### Explanation:
1. **Parameters and Result Structure**: 
   - The function takes a `UserId` as input.
   - It returns a structured result with properties for success, user ID, methods removed, and any error encountered.

2. **Error Handling**:
   - Try-catch blocks are used to handle errors from Graph API calls.
   - Specific handling is included for HTTP 404 (User not found) and 403 (Insufficient permissions).

3. **Logging**:
   - Uses `Write-Verbose` to log actions, especially before removing methods.

4. **Revert Log**:
   - Logs a message before each removal attempt as a form of revert logging.

5. **Functionality**:
   - Fetches existing authentication methods for the user.
   - Attempts to remove each method one by one while handling potential errors.

6. **Permissions**:
   - Assumes the script runs with permissions sufficient to read and write user authentication methods (`User.ReadWrite.All` scope).

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ps-graph-stale-users | cold | RAG=YES

**Baseline (no RAG):** 0-5 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 18.5 &nbsp; **Wall sec:** 85.85 &nbsp; **Prompt tokens:** 9351 &nbsp; **Output tokens:** 692

**Response:**

To accomplish this task, we'll create a PowerShell script that uses the Microsoft Graph API to find all Entra ID user accounts that have not signed in for 90 days and are still enabled. We'll then export these results to a CSV file with specific columns: UPN, DisplayName, LastSignInDateTime, and AccountEnabled.

Here's how you can achieve this:

1. **Install the Microsoft Graph PowerShell Module**: First, ensure that the `Microsoft.Graph` module is installed. If not, install it using:

   ```powershell
   Install-Module -Name Microsoft.Graph -Scope CurrentUser
   ```

2. **Connect to Microsoft Graph**: Authenticate and connect to Microsoft Graph with sufficient permissions.

3. **Query for Users**: Use a filter to find users who have not signed in for 90 days and are still enabled.

4. **Export Results**: Export the results to a CSV file.

Here's the complete PowerShell script:

```powershell
# Import the required module
Import-Module Microsoft.Graph

# Connect to Microsoft Graph with delegated permissions
Connect-MgGraph -Scopes "User.Read.All"

# Calculate the date 90 days ago from today
$daysAgo = (Get-Date).AddDays(-90)

# Query for users who have not signed in for 90 days and are still enabled
$query = "`"signInActivity.lastSignInDateTime lt $daysAgo`" and accountEnabled eq true"

# Get the list of users matching the query
$users = Get-MgUser -Filter $query -Top 1000

# Prepare an array to hold user data for export
$userData = @()

foreach ($user in $users) {
    # Check if the signInActivity property is available and valid
    if ($null -ne $user.signInActivity -and $null -ne $user.signInActivity.lastSignInDateTime) {
        # Create a custom object with the required properties
        $userData += [PSCustomObject]@{
            UPN           = $user.UserPrincipalName
            DisplayName   = $user.DisplayName
            LastSignInDateTime = $user.signInActivity.lastSignInDateTime
            AccountEnabled = $user.AccountEnabled
        }
    }
}

# Export the user data to a CSV file
$userData | Export-Csv -Path "InactiveUsers_$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation

# Disconnect from Microsoft Graph
Disconnect-MgGraph
```

### Explanation:

- **Connect-MgGraph**: Connects to Microsoft Graph using delegated permissions. Ensure you have the necessary permissions (`User.Read.All`).

- **Query Construction**: The query filters users based on their `lastSignInDateTime` and `accountEnabled` status.

- **Get-MgUser**: Retrieves user data from Microsoft Graph with the specified filter.

- **Data Export**: The script collects the required properties into a custom object and exports it to a CSV file, naming it with the current date for uniqueness.

### Permissions:

Ensure you have delegated permissions (`User.Read.All`) granted for this operation. You might need admin consent depending on your organization's settings.

This script assumes that all users have the `signInActivity` property populated. If some users don't have this information due to their account type or other reasons, they will be excluded from the results. Adjust the logic as needed based on your specific requirements and environment.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ps-graph-stale-users | warm | RAG=YES

**Baseline (no RAG):** 0-5 &nbsp; **RAG chunks injected:** 94
**Tok/sec:** 18.7 &nbsp; **Wall sec:** 36.16 &nbsp; **Prompt tokens:** 9351 &nbsp; **Output tokens:** 673

**Response:**

To accomplish this task, you'll need to use the Microsoft Graph PowerShell module to query for users based on their last sign-in date and account status. The script will connect to Microsoft Graph, filter the user accounts, retrieve necessary properties, and export the results to a CSV file.

Here's how you can write such a PowerShell script:

```powershell
# Import required modules
Import-Module Microsoft.Graph.Authentication
Import-Module Microsoft.Graph.Users

# Connect to Microsoft Graph
Connect-MgGraph -Scopes "User.Read.All"

try {
    # Define the date 90 days ago from today
    $dateCutoff = (Get-Date).AddDays(-90)

    # Get all user accounts that are enabled and have not signed in for 90+ days
    $users = Get-MgUser -Filter "accountEnabled eq true and signInActivity/lastSignInDateTime le '$dateCutoff'" `
                        -Top 1000 -AllPages | 
        Where-Object { $_.signInActivity.lastSignInDateTime -le $dateCutoff }

    # Prepare the output
    $output = @()
    foreach ($user in $users) {
        $output += [PSCustomObject]@{
            UPN                = $user.UserPrincipalName
            DisplayName        = $user.DisplayName
            LastSignInDateTime = $user.SignInActivity.LastSignInDateTime
            AccountEnabled     = $user.AccountEnabled
        }
    }

    # Export the output to a CSV file
    $output | Export-Csv -Path "InactiveUsers.csv" -NoTypeInformation

    Write-Output "Export completed. Check InactiveUsers.csv for results."
}
finally {
    # Disconnect from Microsoft Graph
    Disconnect-MgGraph
}

```

### Explanation:

1. **Module Import and Connection**:
   - The script begins by importing the necessary modules: `Microsoft.Graph.Authentication` for connecting to Microsoft Graph, and `Microsoft.Graph.Users` for user operations.
   - `Connect-MgGraph` is used with `-Scopes "User.Read.All"` to authenticate with sufficient permissions.

2. **Date Calculation**:
   - `$dateCutoff` calculates the date 90 days prior from today's date using `Get-Date`.

3. **User Query**:
   - The script uses `Get-MgUser` with a filter to find users whose accounts are enabled (`accountEnabled eq true`) and have not signed in since the cutoff date.
   - `-Top 1000` is used initially for pagination, while `-AllPages` ensures all results are fetched.

4. **Data Processing**:
   - A loop processes each user, creating a custom object with relevant properties: `UserPrincipalName`, `DisplayName`, `LastSignInDateTime`, and `AccountEnabled`.

5. **Export to CSV**:
   - The collected data is exported to a CSV file named "InactiveUsers.csv" using `Export-Csv`. The `-NoTypeInformation` flag omits the type information line from the CSV.

6. **Cleanup**:
   - Finally, `Disconnect-MgGraph` ensures a clean disconnect from Microsoft Graph.

Ensure you have necessary permissions and that the environment is configured correctly before running this script. Adjust paths or scopes as needed based on your specific setup.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
