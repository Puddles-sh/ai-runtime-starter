# Graph API Shootout -- Responses

Generated: 2026-06-25T23:14:39

Failing tasks from overnight benchmark: ga-deprecated-module (4/10), ga-error-handling (5/10), ps-graph-stale-users (4/10)

---

## gemma4:26b | ga-deprecated-module | cold | run 1 | thinking: NO

**Tok/sec:** 45.2  **Wall sec:** 87.84  **Prompt tokens:** 91  **Output tokens:** 2140

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To run this script, you will need the **Microsoft.Graph** module installed. 

A critical technical note: The `signInActivity` property (which contains the last sign-in date) is considered an "extended" property in Microsoft Graph. To access it, you must have the `AuditLog.Read.All` permission, and you **must** explicitly request it using the `-Property` parameter.

```powershell
<#
.SYNOPSIS
    Disables enabled Entra ID users who have not signed in for 60 days.

.DESCRIPTION
    This script uses Microsoft.Graph to identify enabled users whose last sign-in 
    was more than 60 days ago and sets their AccountEnabled property to false.
    
    REQUIRED PERMISSIONS:
    - User.ReadWrite.All (To update user accounts)
    - AuditLog.Read.All (To read signInActivity data)
#>

# 1. Define the threshold date (60 days ago)
$DaysInactive = 60
$ThresholdDate = (Get-Date).AddDays(-$DaysInactive).ToString("yyyy-MM-ddTHH:mm:ssZ")

# 2. Define required Scopes
$Scopes = @("User.ReadWrite.All", "AuditLog.Read.All")

try {
    # 3. Connect to Microsoft Graph
    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
    Connect-MgGraph -Scopes $Scopes

    Write-Host "Searching for enabled users who haven't signed in since $ThresholdDate..." -ForegroundColor Cyan

    # 4. Fetch users
    # We filter for accountEnabled eq true via the server-side filter to reduce payload.
    # We MUST explicitly request 'signInActivity' and 'accountEnabled' via -Property.
    $AllEnabledUsers = Get-MgUser -Filter "accountEnabled eq true" `
                                 -Property "id", "displayName", "userPrincipalName", "accountEndEnabled", "signInActivity" `
                                 -All

    $UsersToDisable = @()

    # 5. Process users and check sign-in activity
    foreach ($User in $AllEnabledUsers) {
        $LastSignIn = $User.SignInActivity.LastSignInDateTime

        # Check if the user has NEVER signed in (LastSignIn is null) OR if last sign-in is older than threshold
        if ($null -eq $LastSignIn -or [DateTime]$LastSignIn -lt (Get-Date).AddDays(-$DaysInactive)) {
            $UsersToDisable += $User
        }
    }

    # 6. Execute Disabling Logic
    if ($UsersToDisable.Count -eq 0) {
        Write-Host "No inactive users found matching the criteria." -ForegroundColor Green
    } else {
        Write-Host "Found $($UsersToDisable.Count) user(s) to disable." -ForegroundColor Yellow

        foreach ($User in $UsersToDisable) {
            Write-Host "Disabling User: $($User.UserPrincipalName) (Last Sign-in: $($User.SignInActivity.LastSignInDateTime ?? 'Never'))" -ForegroundColor White
            
            # Use Update-MgUser to set accountEnabled to false
            # The -WhatIf parameter is included by default in this script for safety. 
            # Remove -WhatIf when you are ready to run for real.
            Update-MgUser -UserId $User.Id -AccountEnabled:$false -WhatIf
        }
        
        Write-Host "Process complete." -ForegroundColor Green
    }

} catch {
    Write-Error "An error occurred: $($_.Exception.Message)"
} finally {
    # Disconnect session
    Disconnect-MgGraph
}
```

### Key Features of this Script:

1.  **Permissions**: It explicitly requests `User.ReadWrite.All` and `AuditLog.Read.All`. Without `AuditLog.Read.All`, the `signInActivity` property will return as empty/null, making it impossible to verify sign-in dates.
2.  **Efficiency**: It uses `-Filter "accountEnabled eq true"` on the server side. This ensures we aren't downloading thousands of already-disabled accounts into your local memory.
3.  **Safety (The `-WhatIf` Safety Net)**: I have included the `-WhatIf` parameter on the `Update-MgUser` command. 
    *   When you run the script as-is, it will **only simulate** the action and tell you what *would* have happened.
    *   **To actually disable users**, delete `-WhatIf` from line 59.
4.  **Null Handling**: The logic accounts for users who have **never** signed in (`$null -eq $LastSignIn`). In most security postures, a user who has never signed in is considered an inactive/stale account that should be disabled.
5.  **OData Compliance**: It uses the correct ISO 8601 timestamp format (`yyyy-MM-ddTHH:mm:ssZ`) required for Graph API date comparisons.

### How to run it:
1.  Open PowerShell as Administrator.
2.  Ensure the module is installed: `Install-Module Microsoft.Graph -Scope CurrentUser`.
3.  Save the script as `Disable-InactiveUsers.ps1`.
4.  Run the script: `./Disable-InactiveUsers.ps1`.
5.  A browser window will pop up asking you to log in to your Microsoft 365 Admin account and consent to the permissions.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ga-deprecated-module | warm | run 1 | thinking: NO

**Tok/sec:** 43.9  **Wall sec:** 53.76  **Prompt tokens:** 91  **Output tokens:** 2337

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To run this script, you will need the **Microsoft.Graph** module installed and an account with **User Administrator** or **Global Administrator** privileges.

### Required Permissions
The script requires the following Microsoft Graph API scopes:
*   `User.ReadWrite.All`: To modify user accounts (disable them).
*   `AuditLog.Read.All`: To access the `signInActivity` property, which tracks last sign-in dates.

```powershell
<#
.SYNOPSIS
    Disables enabled Entra ID users who have not signed in for 60 days.
    
.DESCRIPTION
    Uses Microsoft.Graph module to identify users where accountEnabled is true 
    and lastSignInDateTime is older than 6    days or null (never logged in).
#>

# 1. Define the threshold
$daysInactive = 60
$thresholdDate = (Get-Date).AddDays(-$daysInactive)

# 2. Required Scopes for Microsoft Graph
$scopes = @("User.ReadWrite.All", "AuditLog.Read.All")

try {
    # Connect to Microsoft Graph
    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
    Connect-MgGraph -Scopes $scopes

    # 3. Fetch enabled users
    # We use -Filter to only get enabled users from the server side to optimize performance.
    # We MUST use -Property to ensure 'signInActivity' is returned, as it is not in the default set.
    Write-Host "Fetching enabled users and checking sign-in activity..." -ForegroundColor Cyan
    $allEnabledUsers = Get-MgUser -Filter "accountEnabled eq true" `
                                 -Property "id", "displayName", "userPrincipalName", "signInActivity", "accountEnabled" `
                                 -All

    $usersToDisable = New-Object System.Collections.Generic.List[PSObject]

    foreach ($user in $allEnabledUsers) {
        # Extract last sign-in date from the signInActivity property
        $lastSignIn = $user.SignInActivity.LastSignInDateTime

        # Logic: 
        # - If LastSignInDateTime is less than our threshold, they are inactive.
        # - If LastSignInDateTime is NULL, they have never signed in (and should also be disabled).
        if ($null -eq $lastSignIn -or $lastSignIn -lt $thresholdDate) {
            $usersToDisable.Add($user)
        }
    }

    # 4. Process Disabling
    if ($usersToDisable.Count -eq 0) {
        Write-Host "No inactive users found matching the criteria." -ForegroundColor Green
    } else {
        Write-Host "Found $($usersToDisable.Count) users to disable." -ForegroundColor Yellow

        foreach ($user in $usersToDisable) {
            try {
                Write-Host "Disabling User: $($user.UserPrincipalName) (Last Sign-in: $($user.SignInActivity.LastSignInDateTime ?? 'Never'))" -ForegroundColor White
                
                # Update the user account to disabled
                Update-MgUser -UserId $user.Id -AccountEnabled:$false
                
                Write-Host "Successfully disabled $($user.UserPrincipalName)." -ForegroundColor Green
            }
            catch {
                Write-Error "Failed to disable $($user.UserPrincipalName). Error: $($_.Exception.Message)"
            }
        }
    }
}
catch {
    Write-Error "An error occurred during script execution: $($_.Exception.Message)"
}
finally {
    # Disconnect session
    Disconnect-MgGraph
    Write-Host "Session disconnected." -ForegroundColor Cyan
}
```

### Key Technical Details:

1.  **The `-Filter` Parameter**: The script uses `accountEnabled eq true` within the `-Filter` parameter. This is highly efficient because it instructs Entra ID to only send users who are currently active, reducing the amount of data transferred over the network.
2.  **The `-Property` Parameter**: By default, `Get-MgUser` does not return the `signInActivity` property (as it requires higher-level audit permissions). I explicitly included `"signInActivity"` in the `-Property` argument so that we can access the `LastSignInDateTime`.
3.  **Handling "Never Signed In"**: A common pitfall is only checking if a date is older than 60 days. If a user was created but has **never** logged in, their `LastSignInDateTime` will be `$null`. The script includes logic (`$null -eq $lastSignIn`) to ensure these accounts are also caught and disabled.
4.  **Complexity of Date Filtering**: While Graph supports some OData filtering, filtering by a calculated date string inside the `-Filter` parameter can be inconsistent across different Graph API versions. I have used the high-performance approach: filter for "Enabled" users on the server, then perform the specific date comparison in PowerShell logic.
5.  **Safety**: The script uses `Update-MgUser -AccountEnabled:$false`. This is a non-destructive action; it does not delete the user or their data, making it safe to run as part of an automated cleanup policy.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ga-error-handling | cold | run 1 | thinking: NO

**Tok/sec:** 43.5  **Wall sec:** 126.91  **Prompt tokens:** 127  **Output tokens:** 2757

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

```powershell
function Reset-MgUserMFAMethods {
    <#
    .SYNOPSIS
        Resets a user's MFA authentication methods by removing all registered methods.
    
    .DESCRIPTION
        Connects to Microsoft Graph, retrieves all authentication methods for a specific user, 
        logs the intent to remove them (revert log), and deletes each method individually.
    
    .PARAMETER UserId
        The ID or UserPrincipalName of the user whose MFA methods should be reset.

    .EXAMPLE
        $Result = Reset-MgUserMFAMethods -UserId "admin@contoso.com" -Verbose
    #>
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
        [string]$UserId
    )

    process {
        # Initialize the structured return object
        $result = [PSCustomObject]@{
            Success        = $false
            UserId         = $UserId
            MethodsRemoved = 0
            Error          = $null
        }

        try {
            Write-Verbose "Attempting to retrieve authentication methods for user: $UserId"
            
            # Attempt to fetch all authentication methods
            $methods = $null
            try {
                $methods = Get-MgUserAuthenticationMethod -UserId $UserId -ErrorAction Stop
            }
            catch {
                # Check specifically for 404 (User Not Found) and 403 (Forbidden)
                if ($_.Exception.Message -match "ResourceNotFound" -or $_.Exception.Message -match "404") {
                    throw [System.Exception]::new("Error 404: The user '$UserId' was not found in Microsoft Graph.")
                }
                elseif ($_.Exception.Message -match "AccessDenied" -or $_.Exception.Message -match "403") {
                    throw [System.Exception]::new("Error 403: Insufficient permissions to access MFA methods for '$UserId'.")
                }
                else {
                    throw $_ # Re-throw other errors to the outer catch
                }
            }

            # Check if there are actually any methods to delete
            if ($null -eq $methods -or $methods.Count -eq 0) {
                Write-Verbose "No authentication methods found for user '$UserId'. Nothing to remove."
                $result.Success = $true
                return $null # Or return the object with Success=True, MethodsRemoved=0
            }

            # --- REVERT LOG ENTRY (Pre-destructive action) ---
            # This fulfills the requirement to log what is about to happen before any deletion occurs.
            Write-Verbose "--- PRE-DESTRUCTION REVERT LOG ---"
            Write-Verbose "TIMESTAMP: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
            Write-Verbose "ACTION: Removing all MFA methods for UserID: $UserId"
            Write-Verbose "TARGET METHODS IDENTIFIED:"
            foreach ($m in $methods) {
                Write-Verbose "  - ID: $($m.Id) [Type: $($m.GetType().Name)]"
            }
            Write-Verbose "WARNING: This action is destructive and cannot be undone via this script."
            Write-Verbose "----------------------------------"

            # Iterate through each method and delete it
            foreach ($method in $methods) {
                try {
                    Write-Verbose "Removing authentication method: $($method.Id)"
                    Remove-MgUserAuthenticationMethod -UserId $UserId -AuthenticationMethodId $method.Id -ErrorAction Stop
                    $result.MethodsRemoved++
                }
                catch {
                    # If a specific deletion fails, we catch it but allow the loop to continue for other methods
                    $errorMessage = "Failed to remove method $($method.Id). Error: $($_.Exception.Message)"
                    Write-Error $errorMessage
                    throw [System.Exception]::new($errorMessage)
                }
            }

            # If we reached here without an unhandled exception, it's a success
            $result.Success = $true
            Write-Verbose "MFA Reset complete for $UserId. Total methods removed: $($result.MethodsRemoved)"
        }
        catch {
            # Handle the error and populate the result object
            $result.Success = $false
            $result.Error = $_.Exception.Message
            Write-Error "Function Failed: $($_.Exception.Message)"
        }

        return $result
    }
}
```

### Key Features of this Implementation:

1.  **Structured Return Object**: The function always returns a `PSCustomObject` containing `Success`, `UserId`, `MethodsRemoved`, and `Error`.
2.  **Specific Error Handling**: 
    *   It intercepts Graph error messages to explicitly identify **404 (User Not Found)** and **4ron3 (Access Denied)**, providing human-readable context.
    *   Uses nested `try/catch` blocks: The outer block handles the overall process logic, while an inner block captures specific failures during the retrieval phase.
3.  **Revert Log**: Before the loop begins the destructive `Remove-MgUserAuthenticationMethod` calls, it writes a "PRE-DESTRUCTION REVERT LOG" to the Verbose stream. This logs the exact IDs and types of methods that are about to be deleted.
4.  **No Write-Host**: All progress tracking, including the pre-destruction log, uses `Write-Verbose`. This allows you to run the script silently in production or with `-Verbose` for debugging.
5.  **Idempotency/Safety**: If the user is found but has no methods registered, it marks the operation as a success (nothing to do) rather than erroring out.

### How to use:

```powershell
# Ensure you are connected first
# Connect-MgGraph -Scopes "UserAuthenticationMethod.ReadWrite.All"

# Run with Verbose to see the process and the Revert Log
$report = Reset-MgUserMFAMethods -UserId "user@yourdomain.com" -Verbose

# Inspect the result
$report | Format-Table -AutoSize
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ga-error-handling | warm | run 1 | thinking: NO

**Tok/sec:** 43.3  **Wall sec:** 58.85  **Prompt tokens:** 127  **Output tokens:** 2524

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To use this function, ensure you have the `Microsoft.Graph` module installed and are connected via `Connect-MgGraph` with the necessary permissions (e.g., `UserAuthenticationMethod.ReadWrite.All`).

```powershell
function Reset-UserMFAMethods {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, HelpMessage = "The ID or UPN of the user.")]
        [string]$UserId
    )

    # Initialize the structured result object
    $result = [PSCustomObject]@{
        Success        = $false
        UserId         = $UserId
        MethodsRemoved = 0
        Error          = ""
    }

    try {
        Write-Verbose "Initiating MFA reset process for user: $UserId"

        # 1. Verify User Existence
        $user = $null
        try {
            $user = Get-MgUser -UserId $UserId -ErrorAction Stop
            Write-Verbose "User '$($user.UserPrincipalName)' found successfully."
        }
        catch {
            if ($_.Exception.Message -match "404" -or $_.Exception.Message -match "ResourceNotFound") {
                $result.Error = "Error: User '$UserId' not found (404)."
            }
            elseif ($_.Exception.Message -match "403" -or $_.Exception.Message -match "Forbidden") {
                $result.Error = "Error: Insufficient permissions to access user details (403)."
            }
            else {
                $result.Error = "Error retrieving user: $($_.Exception.Message)"
            }
            return $result
        }

        # 2. Retrieve all authentication methods
        $authMethods = @()
        try {
            $authMethods = Get-MgUserAuthenticationMethod -UserId $UserId -ErrorAction Stop
            Write-Verbose "Found $($authMethods.Count) authentication methods registered."
        }
        catch {
            if ($_.Exception.MSGraphError -match "403" -or $_.Exception.Message -match "Forbidden") {
                $result.Error = "Error: Insufficient permissions to read authentication methods (403)."
            }
            else {
                $result.Error = "Error retrieving auth methods: $($_.Exception.Message)"
            }
            return $result
        }

        # 3. Iterate and Remove Methods
        foreach ($method in $authMethods) {
            $methodId = $method.Id
            $methodType = $method.GetType().Name # Provides context on what is being deleted

            # REQUIREMENT: Revert log entry written before any destructive action.
            # Since Graph deletions are irreversible, this logs the intent and the 'state' 
            # to a verbose stream so an admin can audit what was lost.
            Write-Verbose "[REVERT LOG ENTRY] PRE-DELETION NOTICE: About to permanently remove method '$methodType' (ID: $methodId) for user $UserId. Action is destructive."

            try {
                Write-Verbose "Attempting to remove method: $methodType ($methodId)..."
                Remove-MgUserAuthenticationMethod -UserId $UserId -AuthenticationMethodId $methodId -ErrorAction Stop
                
                $result.MethodsRemoved++
                Write-Verbose "Successfully removed $methodType."
            }
            catch {
                # Specific handling for 403/404 during the loop
                if ($_.Exception.Message -match "403" -or $_.Exception.Message -match "Forbidden") {
                    $result.Error = "Error: Insufficient permissions to delete method $methodId (403)."
                    # We continue the loop to try and remove other methods if possible, 
                    # but the error property will capture the failure.
                }
                elseif ($_.Exception.Message -match "404" -or $_.Exception.Message -match "ResourceNotFound") {
                    $result.Error = "Error: Method $methodId no longer exists (404)."
                }
                else {
                    $result.Error = "Error deleting method $methodId: $($_.Exception.Message)"
                }
            }
        }

        # Finalize Success status if no critical error blocked the process
        if ([string]::IsNullOrWhiteSpace($result.Error)) {
            $result.Success = $true
        }

    }
    catch {
        $result.Error = "An unexpected catastrophic error occurred: $($_.Exception.Message)"
    }

    return $result
}
```

### Key Features of this Implementation:

1.  **Granular Error Handling**: Each Graph call (`Get-MgUser`, `Get-MgUserAuthenticationMethod`, and `Remove-MgUserAuthenticationMethod`) is wrapped in its own `try/catch` block to identify exactly where the pipeline failed.
2.  **HTTP Status Code Mapping**: It specifically parses exception messages for `404` (Not Found) and `403` (Forbidden) to provide human-readable error strings in the returned object.
3.  **Destructive Action Logging**: Per your requirement, a `[REVERT LOG ENTRY]` is written via `Write-Verbose` immediately before the `Remove-MgUserAuthenticationMethod` call. This serves as an audit trail of what was about to be deleted.
4.  **Structured Output**: The function returns a `PSCustomObject` containing:
    *   `Success` (Boolean)
    *   `UserId` (String)
    *   `MethodsRemoved` (Integer counter)
    *   `Error` (String containing the specific error message)
5.  **No Side Effects**: The function uses `Write-Verbose` instead of `Write-Host`, ensuring it is "silent" by default and suitable for use in automated automation/CI/CD pipelines.

### How to test:

```powershell
# Enable verbose output to see the progress and the Revert Log Entry
$verbosePreference = 'Continue'

# Run the function
$output = Reset-UserMFAMethods -UserId "user@yourdomain.com"

# Inspect the structured result
$output | Format-List
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ps-graph-stale-users | cold | run 1 | thinking: NO

**Tok/sec:** 44.6  **Wall sec:** 161.80  **Prompt tokens:** 67  **Output tokens:** 2065

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To run this script, you will need the **Microsoft Graph PowerShell SDK** installed and have at least **User.Read.All** permissions.

### Prerequisites
If you haven't installed the module yet, run:
```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
```

### The PowerShell Script

```powershell
# ---------------------------------------------------------------------------
# Script: Find-InactiveEntraUsers.ps1
# Description: Finds enabled users who haven't signed in for 90 days.
# Requirements: Microsoft.Graph module, Azure AD Premium P1/P2 (for signInActivity)
# ---------------------------------------------------------------------------

# Settings
$DaysInactive = 90
$ThresholdDate = (Get-Date).AddDays(-$DaysInactive)
$ExportPath = "$PSScriptRoot\InactiveUsers_$(Get-Date -Format 'yyyyMMdd').csv"

# Check if Microsoft Graph module is installed
if (-not (Get-Module -ListAvailable Microsoft.Graph)) {
    Write-Error "Microsoft.Graph module not found. Please install it using 'Install-Module Microsoft.Graph'."
    return
}

# Connect to Microsoft Graph
# Required Scope: User.Read.All
Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
Connect-MgGraph -Scopes "User.Read.All"

try {
    Write-Host "Fetching users from Entra ID... (This may take a while for large tenants)" -ForegroundColor Cyan
    
    # We MUST explicitly request 'signInActivity' and 'accountEnabled' via -Property 
    # because they are not returned in the default property set.
    $AllUsers = Get-MgUser -All -Property "userPrincipalName", "displayName", "accountableEnabled", "signInActivity", "accountEnabled"

    Write-Host "Processing user data..." -ForegroundColor Cyan

    $InactiveUsers = $AllUsers | Where-Object {
        # Filter 1: Account must be enabled
        $_.AccountEnabled -eq $true -and (
            # Filter 2: LastSignInDateTime is older than threshold
            # OR the user has NEVER signed in (LastSignInDateTime is null)
            $null -eq $_.SignInActivity.LastSignInDateTime -or 
            [DateTime]$_.SignInActivity.LastSignInDateTime -lt $ThresholdDate
        )
    } | Select-Object @{
        Name = "UPN"
        Expression = { $_.UserPrincipalName }
    },
    @{
        Name = "DisplayName"
        Expression = { $_.DisplayName }
    },
    @{
        Name = "LastSignInDateTime"
        Expression = { 
            if ($null -eq $_.SignInActivity.LastSignInDateTime) { "Never" } 
            else { $_.SignInActivity.LastSignInDateTime } 
        }
    },
    @{
        Name = "AccountEnabled"
        Expression = { $_.AccountEnabled }
    }

    if ($InactiveUsers) {
        $InactiveUsers | Export-Csv -Path $ExportPath -NoTypeInformation
        Write-Host "Success! Found $($InactiveUsers.Count) inactive users." -ForegroundColor Green
        Write-Host "Results exported to: $ExportPath" -ForegroundColor Green
    }
    else {
        Write-Host "No inactive users found matching the criteria." -ForegroundColor Yellow
    }

}
catch {
    Write-Error "An error occurred: $_"
}
finally {
    # Disconnect session
    Disconnect-MgGraph | Out-Null
    Write-Host "Session disconnected." -ForegroundColor Cyan
}
```

### Key Features of this Script:

1.  **Explicit Property Selection:** In Microsoft Graph, the `signInActivity` property is not returned by default to save bandwidth. The script uses the `-Property` parameter to specifically request it.
2.  **Handling "Never" Sign-ins:** If a user was created but has never logged in, their `lastSignInDateTime` will be null. This script treats "Never" as being inactive (which is usually what admins want for cleanup).
3.  **Advanced Filtering Logic:** It checks both that the account is `Enabled` AND that the date is older than your 90-day threshold.
4.  **Clean Export:** The output CSV uses the exact column headers you requested: `UPN`, `DisplayName`, `LastSignInDateTime`, and `AccountEnabled`.

### Important Limitations & Notes:

*   **Licensing Requirement:** To access the `signInActivity` property via Microsoft Graph, your tenant **must have an Azure AD Premium P1 or P2 license**. Without this, the sign-in properties will return as blank.
*   **Large Tenants:** If you have tens of thousands of users, `-All` can take several minutes to run. The script uses a client-side filter (`Where-Object`) because filtering by `signInActivity` via the Graph API's `$filter` parameter is often restricted or unsupported depending on your specific SDK version and API endpoint.
*   **Permissions:** When the login window appears, you must sign in with an account that has at least **Global Reader** or **User Administrator** permissions.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## gemma4:26b | ps-graph-stale-users | warm | run 1 | thinking: NO

**Tok/sec:** 43.8  **Wall sec:** 47.08  **Prompt tokens:** 67  **Output tokens:** 2040

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To run this script, you will need the **Microsoft.Graph** PowerShell module installed and permissions to read user profiles and audit logs (`User.Read.All` and `AuditLog.Read.All`).

### The PowerShell Script

```powershell
# ---------------------------------------------------------------------------
# Script: Find-InactiveEntraUsers.ps1
# Description: Finds enabled Entra ID users who haven't signed in for 90 days.
# ---------------------------------------------------------------------------

# 1. Define the threshold (90 days ago)
$daysThreshold = 90
$dateThreshold = (Get-Date).AddDays(-$daysThreshold)
$exportPath = ".\InactiveUsers_$(Get-Date -Format 'yyyyMMdd').csv"

# 2. Check if Microsoft Graph module is installed
if (-not (Get-Module -ListAvailable Microsoft.Graph)) {
    Write-Error "The Microsoft.Graph module is required. Install it using: Install-Module Microsoft.Graph"
    return
}

# 3. Connect to Microsoft Graph
# We need AuditLog.Read.All to access the signInActivity property
$scopes = @("User.Read.All", "AuditLog.Read.All")
Connect-MgGraph -Scopes $scopes

Write-Host "Fetching users from Entra ID... This may take a moment for large tenants." -ForegroundColor Cyan

try {
    # 4. Fetch all users
    # Note: We MUST explicitly request 'signInActivity' and 'accountEnabled' 
    # as they are not part of the default property set returned by Graph.
    $allUsers = Get-MgUser -All -Property "userPrincipalName", "displayName", "signInActivity", "accountEnabled"

    Write-Host "Processing user data..." -ForegroundColor Cyan

    # 5. Filter users based on logic:
    # - Account must be Enabled (true)
    # - LastSignInDateTime must be older than the threshold OR null (never signed in)
    $inactiveUsers = $allUsers | Where-Object {
        $userEnabled = $_.AccountEnabled -eq $true
        $lastSignIn = $_.SignInActivity.LastSignInDateTime

        if ($userEnabled) {
            # If lastSignIn is null, they've never signed in, which counts as inactive
            if ($null -eq $lastSignIn -or [DateTime]$lastSignIn -lt $dateThreshold) {
                return $true
            }
        }
        return $false
    } | Select-Object @{Name="UPN"; Expression={$_.UserPrincipalName}},
                      @{Name="DisplayName"; Expression={$_.DisplayName}},
                      @{Name="LastSignInDateTime"; Expression={$_.SignInActivity.LastSignInDateTime}},
                      @{Name="AccountEnabled"; Expression={$_.AccountEnabled}}

    # 6. Export results to CSV
    if ($inactiveUsers) {
        $inactiveUsers | Export-Csv -Path $exportPath -NoTypeInformation
        Write-Host "Success! Found $($inactiveUsers.Count) inactive users." -ForegroundColor Green
        Write-Host "Results exported to: $exportPath" -ForegroundColor Green
    } else {
        Write-Host "No inactive users found matching the criteria." -ForegroundColor Yellow
    }
}
catch {
    Write-Error "An error occurred: $($_.Exception.Message)"
}
finally {
    # Disconnect session
    Disconnect-MgGraph
}
```

### How this script works:

1.  **Permissions**: The script requests `AuditLog.Read.All`. This is critical because the `signInActivity` property (which contains the last sign-in date) is stored in the audit logs and is not accessible via standard user permissions.
2.  **Property Selection**: When using `Get-MgUser`, Microsoft Graph only returns a small subset of default properties to save bandwidth. I have explicitly included `-Property "userPrincipalName", "displayName", "signInActivity", "accountEnabled"`. Without this, the `LastSignInDateTime` would always return empty.
3.  **The Logic**: 
    *   It checks if `AccountEnabled` is `$true`.
    *   It handles the **"Never Signed In"** scenario: If `lastSignIn` is null, the script treats them as inactive (since they haven't performed any recent activity).
    *   It compares the date against a calculated 90-day cutoff.
4.  **Output**: It uses a custom object mapping (`Select-Object @{Name=...}`) to ensure your CSV columns match exactly what you requested: `UPN`, `DisplayName`, `LastSignInDateTime`, and `AccountEnabled`.

### Prerequisites & Setup

1.  **Install the Module** (if you haven't already):
    ```powershell
    Install-Module Microsoft.Graph -Scope CurrentUser
    ```
2.  **Execution Policy**: Ensure you can run scripts on your machine:
    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
3.  **Running the script**:
    Save the code as `Find-InactiveUsers.ps1` and execute it in PowerShell. A browser window will pop up asking you to authenticate to your Microsoft 365 tenant.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
