# Graph API Shootout -- Responses

Generated: 2026-06-25T22:36:34

Failing tasks from overnight benchmark: ga-deprecated-module (4/10), ga-error-handling (5/10), ps-graph-stale-users (4/10)

---

## deepseek-r1:14b | ga-deprecated-module | cold | run 1 | thinking: NO

**Tok/sec:** 22.1  **Wall sec:** 46.65  **Prompt tokens:** 78  **Output tokens:** 932

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here's a PowerShell script that accomplishes this task using only the Microsoft.Graph PowerShell module:

```powershell
# Connect to Microsoft Graph
Connect-MgGraph -Scopes " openid profile Directory.AccessAsUser.All"

# Get all enabled users with lastSignInDateTime and isEnabled properties, and filter those who haven't signed in for 60 days
$usersToDisable = Get-MgUser -All `
    -Property userPrincipalName, displayName, isEnabled, lastSignInDateTime `
    -Filter "isEnabled eq true and lastSignInDateTime lt [datetime]((Get-Date).AddDays(-60))" `
    -PageSize 500

# Disable each user account
foreach ($user in $usersToDisable) {
    try {
        Set-MgUser -Id $user.id -IsEnabled $false
        Write-Output "Disabled user: $($user.displayName) ($user.userPrincipalName)"
    }
    catch {
        Write-Error "Failed to disable user: $($user.displayName) ($user.userPrincipalName). Error: $_"
    }
}
```

### Explanation:
1. **Connect to Microsoft Graph**: The script starts by connecting to Microsoft Graph using the `Connect-MgGraph` cmdlet with the necessary scopes. The required scopes are:
   - `openid`: For sign-in as user
   - `profile`: For profile access
   - `Directory.AccessAsUser.All`: To manage directory objects

2. **Get Users**: The script retrieves all enabled users who have not signed in for 60 days using the `Get-MgUser` cmdlet with filtering and pagination:
   - `isEnabled eq true`: Ensures we only get enabled user accounts
   - `lastSignInDateTime lt [datetime]((Get-Date).AddDays(-60))`: Filters users who haven't signed in for 60 days
   - `-All`: Enables pagination to retrieve all results
   - `-PageSize 500`: Sets the page size to 500 to optimize performance

3. **Disable Users**: The script iterates over each user and disables their account using `Set-MgUser`. Each operation is wrapped in a try-catch block to handle any potential errors.

### Important Notes:
- **Permissions**: Ensure that the Microsoft Entra ID application has the required permissions:
  - **Delegated Permissions**:
    - openid
    - profile
    - Directory.AccessAsUser.All
  - These permissions must be granted in Azure Active Directory (Azure AD) for the app to access user data and manage accounts.
  
- **Error Handling**: The script includes basic error handling to catch any exceptions that occur during the account disabling process.

This script should be run with appropriate permissions, ideally as a service principal or application identity with the necessary Graph API permissions.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ga-deprecated-module | warm | run 1 | thinking: NO

**Tok/sec:** 22.0  **Wall sec:** 34.96  **Prompt tokens:** 78  **Output tokens:** 766

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here's a PowerShell script that accomplishes the task using only the Microsoft.Graph module:

```powershell
# Connect to Microsoft Graph with required permissions
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Pilot run to test filtering without making changes
Get-MgUser -Filter "isEnabled eq true" `
           -Property id, displayName, mail, signInActivity `
| Where-Object { 
    $_.signInActivity.lastSignInDateTime -eq $null -or `
    (New-TimeSpan -Start $_.signInActivity.lastSignInDateTime).Days -ge 60 
} |
Format-Table id, displayName, mail, signInActivity

# If the pilot run looks correct, uncomment and modify the following to disable users
#Get-MgUser -Filter "isEnabled eq true" `
#           -Property id, displayName, mail, signInActivity `
#| Where-Object { 
#    $_.signInActivity.lastSignInDateTime -eq $null -or `
#    (New-TimeSpan -Start $_.signInActivity.lastSignInDateTime).Days -ge 60 
#} |
#ForEach-Object {
#    Write-Host "Disabling user: $($PSItem.displayName) ($($PSItem.mail))"
#    Disable-MgUser -Id $PSItem.id -Confirm:$false
#}

# Optional: Log disabled users to a file or notify administrators
```

**Note:** 
- Replace `-Scopes` with the appropriate Microsoft Graph API permissions required (e.g., `Directory.ReadWrite.All`). 
- The script first runs in pilot mode to test filtering without making changes. Uncomment and modify the second section to actually disable accounts.
- Always test thoroughly before running in production.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ga-error-handling | cold | run 1 | thinking: NO

**Tok/sec:** 20.1  **Wall sec:** 283.50  **Prompt tokens:** 113  **Output tokens:** 5657

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here's a PowerShell function that meets your requirements:

```powershell
Function Reset-MfaAuthenticationMethods ($userId) {
    $result = [PSCustomObject]@{
        Success      = $true
        UserId       = $userId
        MethodsRemoved = 0
        Error        = ""
    }

    # Attempt to retrieve the user. Handle 404 and other exceptions.
    Try {
        Write-Verbose "Checking if user '$userId' exists..."
        $user = Get-MgUser -Id $userId
        If ($user -eq $null) {
            $result.Success = $false
            $result.Error = "User not found."
            return $result
        }
    } catch [Microsoft.Graph.ServiceException] {
        If ($_.Exception.Response.StatusCode.ValueToString -eq "404") {
            $result.Success = $false
            $result.Error = "User not found."
            Write-Verbose "Revert action: User does not exist."
            return $result
        }
    } catch {
        $result.Success = $false
        $result.Error = $_.Exception.Message
        Write-Verbose "Revert action: An unexpected error occurred during user retrieval."
        return $result
    }

    # Attempt to get authentication methods. Handle 403 and other exceptions.
    Try {
        Write-Verbose "Retrieving authentication methods for user '$userId'..."
        $methods = Get-MgUserAuthenticationMethod -UserId $userId
    } catch [Microsoft.Graph.ServiceException] {
        If ($_.Exception.Response.StatusCode.ValueToString -eq "403") {
            $result.Success = $false
            $result.Error = "Insufficient permissions to access authentication methods."
            Write-Verbose "Revert action: Insufficient permissions."
            return $result
        }
        $result.Success = $false
        $result.Error = $_.Exception.Message
        Write-Verbose "Revert action: An unexpected error occurred while retrieving authentication methods."
        return $result
    }

    # If no methods exist, return with success.
    If ($methods.Count -eq 0) {
        $result.MethodsRemoved = 0
        Write-Verbose "No authentication methods found. Nothing to remove."
        return $result
    }

    Write-Verbose "Found $($methods.Count) authentication methods. Proceeding to remove them."

    # Attempt to remove each method, handle exceptions for each.
    Try {
        ForEach ($method in $methods) {
            Try {
                Write-Verbose "Attempting to remove authentication method '$($method.DisplayName)'..."
                Remove-MgUserAuthenticationMethod -InstanceId $method.InstanceId -UserId $userId
                $result.MethodsRemoved++
                Write-Verbose "Successfully removed '$($method.DisplayName)'"
            } catch [Microsoft.Graph.ServiceException] {
                If ($_.Exception.Response.StatusCode.ValueToString -eq "403") {
                    $result.Success = $false
                    $result.Error += "Insufficient permissions to remove method '$($method.DisplayName)'. "
                } Else {
                    $result.Success = $false
                    $result.Error += $_.Exception.Message + "; "
                }
            } catch {
                $result.Success = $false
                $result.Error += $_.Exception.Message + "; "
            }
        }
    } catch {
        $result.Success = $false
        $result.Error = $_.Exception.Message
    }

    return $result
}
```

**Explanation:**

1. **Error Handling and Verbose Logging**: The function uses `Write-Verbose` for progress logging, avoiding `Write-Host` as requested.

2. **Try/Catch Blocks**: Each major operation (retrieving the user, methods, removing each method) is wrapped in try/catch blocks to handle exceptions gracefully.

3. **404 Handling**: If the user isn't found, it returns an error with "User not found."

4. **403 Handling**: If permissions are insufficient during any step (like retrieving methods or removing them), it returns an appropriate error message.

5. **Partial Success**: The function continues attempting to remove each method even if some fail, but marks the overall operation as unsuccessful if any errors occur.

6. **Result Object**: Returns a structured result object with properties indicating success/failure, user ID, count of removed methods, and any error messages.

**Example Usage:**

```powershell
# Replace 'user@domain.com' with the actual user ID.
$result = Reset-MfaAuthenticationMethods -userId "user@domain.com"
If ($result.Success) {
    Write-Output "Successfully reset MFA for user '$($result.UserId)': $($result.MethodsRemoved) methods removed."
} Else {
    Write-Warning "Failed to reset MFA: $($result.Error)"
}
```

**Notes:**

- Ensure you're authenticated with Microsoft Graph before running the function using `Connect-MgGraph`.
- The function attempts to remove all types of MFA methods (e.g., Email, SMS, Authenticator App).
- If no MFA methods are found, it returns with zero methods removed.
- Handles partial failures during method removals but considers the overall operation a failure if any errors occur.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ga-error-handling | warm | run 1 | thinking: NO

**Tok/sec:** 21.8  **Wall sec:** 77.83  **Prompt tokens:** 113  **Output tokens:** 1690

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here's a PowerShell function that meets your requirements:

```powershell
function Reset-MfaAuthenticationMethods {
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,
        
        [switch]$Verbose
    )

    $result = @{
        Success            = $false
        UserId             = $null
        MethodsRemoved     = 0
        Error              = ""
    }

    try {
        # Connect to Microsoft Graph with existing authentication context
        Write-Verbose "Connecting to Microsoft Graph..."
        if (-not (Connect-MgGraph -ErrorAction Stop)) {
            throw "Failed to connect to Microsoft Graph."
        }

        $result.UserId = $UserId

        # Check if user exists before attempting any destructive actions
        try {
            $user = Get-MgUser -Id $UserId -ErrorAction Stop
        }
        catch [Microsoft.Graph_exceptions_Microsoft_Graph_ServiceException] {
            if ($_.Exception.StatusCode -eq 404) {
                $result.Error = "User not found."
                return $result
            } else {
                throw $_.Exception.Message
            }
        }

        # Retrieve all MFA methods for the user
        Write-Verbose "Getting MFA authentication methods..."
        $mfaMethods = Get-MgUserAuthenticationMethod -UserId $UserId

        if ($mfaMethods.Count -eq 0) {
            $result.Success = $true
            $result.MethodsRemoved = 0
            return $result
        }

        Write-Verbose "Found $($mfaMethods.Count) MFA methods. Preparing to remove..."
        
        # Log a revert entry before any destructive action
        Write-Verbose "Log: Reverting MFA authentication methods for user $($UserId)."

        foreach ($method in $mfaMethods) {
            try {
                if ($method.Supports撤消 -eq $true) {
                    Remove-MgUserAuthenticationMethod -UserId $UserId -Id $method.Id -ErrorAction Stop
                    $result.MethodsRemoved++
                } else {
                    Write-Warning "Skipping method with no support for removal."
                }
            }
            catch [Microsoft.Graph_exceptions_Microsoft_Graph_ServiceException] {
                if ($_.Exception.StatusCode -eq 403) {
                    $result.Error = "Insufficient permissions to remove MFA methods."
                    break
                } else {
                    Write-Error $_.Exception.Message
                    throw
                }
            }
        }

        if ($result.MethodsRemoved -gt 0) {
            $result.Success = $true
        } else {
            $result.Error = "No MFA methods were removed."
        }

        return $result

    }
    catch [Microsoft.Graph_exceptions_Microsoft_Graph_ServiceException] {
        if ($_.Exception.StatusCode -eq 403) {
            $result.Error = "Insufficient permissions to access user or remove MFA methods."
            $result.Success = $false
        } elseif ($_.Exception.StatusCode -eq 404) {
            $result.Error = "User not found."
            $result.UserId = $null
            $result.Success = $false
        } else {
            $result.Error = $_.Exception.Message
            Write-Error $_.Exception.Message
        }
        return $result
    }
    catch {
        $result.Error = $_.Exception.Message
        $result.Success = $false
        Write-Error $_.Exception.Message
        return $result
    }
}
```

### Explanation:
1. **Function Definition**: Takes a mandatory `UserId` parameter and an optional Verbose switch for logging.

2. **Graph Authentication**:
   - Attempts to connect to Microsoft Graph.
   - If it fails, returns with Success set to `$false`.

3. **User Existence Check**:
   - Tries to get the user by ID.
   - Handles 404 (user not found) and other errors.

4. **MFA Methods Retrieval**:
   - Fetches all MFA methods for the specified user.
   - If none are found, returns immediately with `MethodsRemoved` set to 0.

5. **Revert Log Entry**:
   - Writes a Verbose message before any destructive actions.

6. **Removing MFA Methods**:
   - Loops through each method and attempts removal using `Remove-MgUserAuthenticationMethod`.
   - Counts the number of successfully removed methods.
   - Handles specific errors like 403 (insufficient permissions) and other exceptions.

7. **Error Handling**:
   - Catches common exceptions and returns an error message in the structured result object.

8. **Return Value**:
   - Returns a structured object with Success, UserId, MethodsRemoved, and Error properties.
   - Uses Verbose logging for progress instead of Write-Host.

This function provides comprehensive error handling and logging while ensuring destructive actions are preceded by proper user validation and logging.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ps-graph-stale-users | cold | run 1 | thinking: NO

**Tok/sec:** 22.2  **Wall sec:** 47.14  **Prompt tokens:** 53  **Output tokens:** 997

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here's a PowerShell script that uses Microsoft Graph to find Entra ID (Azure AD) user accounts that have not signed in for 90 days but are still enabled:

```powershell
# Import the Microsoft Graph PowerShell module
Import-Module Microsoft.Graph.Beta.Identity.Governance

# Connect to Microsoft Graph with an account that has admin privileges
Connect-MgGraph -ClientId "your_client_id" -TenantId "your_tenant_id" -Secret "your_client_secret"

# Get all users that have not signed in for 90 days and are enabled
$users = Get-MgUser -All `
    -Filter "lastSignInDateTime le (now-90d)" `
    -Properties accountEnabled, displayName, upn, lastSignInDateTime

# Format the output to include only the required columns and export to CSV
$users | Select-Object UserPrincipalName, DisplayName, LastSignInDateTime, AccountEnabled | Export-Csv -Path "InactiveUsers.csv" -NoTypeInformation
```

### Prerequisites:
1. **Register an Azure AD Application**:
   - Register an application in Azure Portal with the required permissions: `User.Read.All`, `Group.Read.All`, and `Directory.ReadAll`.
   - Ensure the app has admin consent.

2. **Install Microsoft Graph PowerShell Module**:
   ```powershell
   Install-Module Microsoft.Graph.Beta.Identity.Governance
   ```

3. **Set up Authentication**:
   - Replace `"your_client_id"`, `"your_tenant_id"`, and `"your_client_secret"` with your actual Azure AD application credentials.

### Notes:
- The script connects to Microsoft Graph using the `Connect-MgGraph` cmdlet.
- It uses the `Get-MgUser` cmdlet with a filter to get users who haven't signed in for 90 days (`lastSignInDateTime le (now-90d)`).
- The results are formatted and exported to a CSV file named "InactiveUsers.csv" with the specified columns.

### Explanation:
- **LastSignInDateTime**: This property shows the date and time of the user's last sign-in. If a user hasn't signed in for 90 days, this value will be null or earlier than `now-90d`.
- **AccountEnabled**: Indicates whether the user account is enabled.
- The script assumes you have an Azure AD application with the necessary permissions and that you're connecting using an account with admin privileges.

This script should be run periodically (e.g., daily) to monitor inactive users in your organization.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## deepseek-r1:14b | ps-graph-stale-users | warm | run 1 | thinking: NO

**Tok/sec:** 21.8  **Wall sec:** 77.53  **Prompt tokens:** 53  **Output tokens:** 1688

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To find all Entra ID user accounts that have not signed in for 90 days and are still enabled using PowerShell with Microsoft Graph, follow these steps:

### Prerequisites:
1. **Install Required Modules**:
   - Install the `MSAL.PS` module from the PowerShell Gallery to authenticate with Microsoft Graph.
     ```powershell
     Install-Module MSAL.PS -Scope CurrentUser
     ```
2. **Register an Application in Azure AD**:
   - Register your script as an application in Azure Active Directory and grant it the necessary permissions (e.g., "Directory.Read.All").

### PowerShell Script:

```powershell
# Import required modules
Import-Module MSAL.PS

# Authentication configuration
$tenantId = "your_tenant_id"  # Replace with your tenant ID
$client_id = "your_client_id"  # Replace with your application client ID
$client_secret = "your_client_secret"  # Replace with your client secret

# Set up the date for filtering (90 days ago)
$date90DaysAgo = (Get-Date).AddDays(-90).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ss.000Z')

# Path to save the output CSV
$csvOutputPath = "C:\Users\CurrentUser\Desktop\InactiveUsers.csv"

# Authenticate with Microsoft Graph using MSAL
try {
    $authResult = Connect-Msal -ClientId $client_id `
                             -ClientSecret $client_secret `
                             -Authority "https://login.microsoftonline.com/$tenantId"
} catch {
    Write-Error "Authentication failed: $_.Exception.Message"
    exit 1
}

# Initialize variables for pagination
$users = @()
$nextLinkUrl = $null

# Loop through all pages of users until no next link is returned
do {
    if ($nextLinkUrl -ne $null) {
        $uri = $nextLinkUrl
    } else {
        # First API call to get the initial page of users
        try {
            $response = Invoke-MgGraphRequest -Uri "https://graph.microsoft.com/v1.0/users?$select=UserPrincipalName,displayName,lastSignInDateTime,accountEnabled&$filter=AccountEnabled eq true and lastSignInDateTime le $date90DaysAgo" `
                                             -Method GET `
                                             -ErrorAction Stop
        } catch {
            Write-Error "API request failed: $_"
            exit 1
        }
    }

    # Parse the response
    try {
        $jsonResponse = ConvertFrom-Json $response.Content
        if ($jsonResponse.value) {
            foreach ($user in $jsonResponse.value) {
                $users += $user
            }
        }
        if ($jsonResponse.'@odata.nextLink') {
            $nextLinkUrl = $jsonResponse.'@odata.nextLink'
        } else {
            $nextLinkUrl = $null
        }
    } catch {
        Write-Error "Parsing response failed: $_"
        exit 1
    }

} while ($nextLinkUrl -ne $null)

# Filter out users with null or empty LastSignInDateTime (optional, depending on your needs)
$filteredUsers = $users | Where-Object { $_.lastSignInDateTime -ne $null } 

# Export to CSV
try {
    $columns = 'UserPrincipalName', 'displayName', 'lastSignInDateTime', 'accountEnabled'
    $filteredUsers | Select-Object $columns | Export-Csv -Path $csvOutputPath -NoTypeInformation -Encoding UTF8 -Delimiter ','
} catch {
    Write-Error "Export to CSV failed: $_"
    exit 1
}

# Optional: Remove the variable from memory after use
Remove-Variable users, csvOutputPath, nextLinkUrl

Write-Host "Script completed successfully. Results saved to $csvOutputPath"
```

### Explanation:
1. **Authentication**:
   - The script authenticates with Microsoft Graph using a service principal (application registration) for better reliability and non-interactive access.

2. **API Request**:
   - Fetches all users with enabled accounts (`AccountEnabled eq true`) who haven't signed in for 90 days.
   - Uses the `lastSignInDateTime` property to filter inactive users.

3. **Handling Large Datasets**:
   - Implements pagination to handle large datasets by looping through all pages of results returned by Microsoft Graph.

4. **Output**:
   -Exports the filtered results into a CSV file with the specified columns: UPN, DisplayName, LastSignInDateTime, and AccountEnabled.

### Notes:
- Ensure you have the correct permissions for your application in Azure AD.
- Replace placeholders (`your_tenant_id`, `your_client_id`, `your_client_secret`) with your actual values.
- The script assumes that the `lastSignInDateTime` is available. If this property isn't returned, ensure your API query includes it in the `$select` parameter.

This script will efficiently gather and report on inactive users, aiding in account management and cleanup processes.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ga-deprecated-module | cold | run 1 | thinking: NO

**Tok/sec:** 22.2  **Wall sec:** 38.99  **Prompt tokens:** 84  **Output tokens:** 607

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To accomplish this task using the `Microsoft.Graph` PowerShell module, you will need to ensure that you have the necessary permissions in Azure Active Directory (Azure AD) to access user sign-in details and modify account statuses.

### Required Permissions:
1. **User.Read.All**: To read all users' basic information.
2. **User.AuthenticationMethod.ReadWrite.All**: To read and write user authentication methods, including enabling/disabling accounts.

Ensure that your application registration in Azure AD has these permissions granted and consented by an administrator if necessary.

Here's a script to find Entra ID users who have not signed in for 60 days and disable their accounts:

```powershell
# Connect to Microsoft Graph with the required scopes
Connect-MgGraph -Scopes "User.Read.All", "User.AuthenticationMethod.ReadWrite.All"

# Calculate the date 60 days ago from today
$cutoffDate = (Get-Date).AddDays(-60)

# Get all enabled users who haven't signed in since the cutoff date
$users = Get-MgUser -Filter "signInActivity/lastSignInDateTime lt $cutoffDate and accountEnabled eq true" -Property signInActivity.lastSignInDateTime

foreach ($user in $users) {
    # Output user details (optional)
    Write-Output "Disabling account for User: $($user.DisplayName) with UPN: $($user.UserPrincipalName)"

    # Disable the user's account
    Set-MgUser -UserId $user.Id -AccountEnabled $false

    # Optionally, you can send an email to notify the user or log this action
}

# Disconnect from Microsoft Graph
Disconnect-MgGraph
```

### Explanation:

1. **Connect-MgGraph**: Connects to Microsoft Graph with the necessary scopes for reading users and modifying account statuses.

2. **cutoffDate Calculation**: Determines the date 60 days prior to today, which will be used to filter users based on their last sign-in activity.

3. **Get-MgUser**: Uses the `-Filter` parameter to retrieve users who are enabled (`accountEnabled eq true`) but haven't signed in since the cutoff date. The `signInActivity.lastSignInDateTime` property is specified to ensure it's retrieved.

4. **Loop Through Users**: Iterates over each user that meets the criteria, optionally outputs their details for logging or audit purposes, and then disables their account using `Set-MgUser`.

5. **Disconnect-MgGraph**: Disconnects from Microsoft Graph after operations are complete.

### Pre-requisites:
- Install the `Microsoft.Graph` module if not already installed: 
  ```powershell
  Install-Module -Name Microsoft.Graph
  ```
- Ensure you have admin consent for the required permissions in Azure AD.
- Run this script with appropriate privileges to modify user accounts.

This script should be executed by an administrator or a service principal with sufficient permissions. Always test scripts in a non-production environment first to ensure they work as expected and do not disrupt operations.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ga-deprecated-module | warm | run 1 | thinking: NO

**Tok/sec:** 22.4  **Wall sec:** 28.55  **Prompt tokens:** 84  **Output tokens:** 633

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To accomplish this task using the Microsoft.Graph PowerShell module, you'll need to ensure you have the appropriate permissions set up in your Azure AD tenant for accessing user sign-in activity data through Microsoft Graph API. The necessary permission is `User.Read.All`. You also need to use the `Microsoft.Graph.Identity.SignIns` scope if you want to access user sign-ins.

Here’s a PowerShell script that finds all enabled Entra ID users who haven't signed in for 60 days and disables their accounts:

```powershell
# Connect to Microsoft Graph with appropriate permissions
Connect-MgGraph -Scopes "User.Read.All", "Identity.SignIns.Read.All"

try {
    # Get the current date minus 60 days
    $cutoffDate = (Get-Date).AddDays(-60)

    # Query for enabled users who have not signed in within the last 60 days
    $inactiveUsers = Get-MgUser -Filter "signInActivity/lastSignInDateTime le '$($cutoffDate.ToString('yyyy-MM-ddTHH:mm:ssZ'))' and userState eq 'Enabled'" -Property "id, userPrincipalName"

    foreach ($user in $inactiveUsers) {
        # Check if the user has last sign-in date before cutoff date
        if (-not $user.SignInActivity.LastSignInDateTime -or 
            [datetime]::Parse($user.SignInActivity.LastSignInDateTime) -lt $cutoffDate) {

            Write-Output "Disabling account for: $($user.UserPrincipalName)"

            # Disable the user's account
            Set-MgUser -UserId $user.Id -AccountEnabled $false

            Write-Output "Account disabled for: $($user.UserPrincipalName)"
        }
    }

} catch {
    Write-Error "An error occurred: $_"
}

# Disconnect from Microsoft Graph session
Disconnect-MgGraph
```

### Key Points:

1. **Permissions**: Ensure the `User.Read.All` and `Identity.SignIns.Read.All` scopes are configured in your Azure AD app registration for accessing user profiles and sign-in data.

2. **Date Handling**: The script calculates a cutoff date 60 days prior to the current date and uses it in filtering users based on their last sign-in time.

3. **Filter Query**: The `-Filter` parameter includes conditions for both `lastSignInDateTime` and `userState`. Note that `signInActivity/lastSignInDateTime le ...` is used to find users with a last sign-in time less than or equal to the cutoff date, combined with checking if the user state is 'Enabled'.

4. **Loop Through Users**: For each user returned by the filter query, it checks their `LastSignInDateTime` and ensures they haven't signed in since before the cutoff date.

5. **Account Disabling**: The script then disables these accounts using `Set-MgUser`.

6. **Error Handling**: Basic error handling is included to catch any issues during execution.

Ensure you test this script in a controlled environment first, and have proper backups or confirmation steps if needed, as account disabling is irreversible without an administrator's intervention.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ga-error-handling | cold | run 1 | thinking: NO

**Tok/sec:** 21.9  **Wall sec:** 47.70  **Prompt tokens:** 116  **Output tokens:** 754

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Certainly! Below is a PowerShell function that meets your requirements:

```powershell
function Reset-MFAForUser {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Define the result object
    $result = @{
        Success      = $false
        UserId       = $null
        MethodsRemoved = 0
        Error        = ""
    }

    try {
        # Attempt to get user's MFA methods
        Write-Verbose "Retrieving MFA authentication methods for User ID: $UserId"
        $mfaMethods = Get-MgUserAuthenticationMethod -UserId $UserId

        if (-not $mfaMethods) {
            Write-Verbose "No MFA methods found for User ID: $UserId"
            return $result
        }

        # Log revert entry before removing methods
        Write-Verbose "Logging revert entry for User ID: $UserId with $($mfaMethods.Count) methods to remove"

        foreach ($method in $mfaMethods) {
            try {
                Write-Verbose "Removing MFA method ID: $($method.Id) for User ID: $UserId"
                Remove-MgUserAuthenticationMethod -AuthenticationMethodId $method.Id
                $result.MethodsRemoved++
            } catch {
                if ($_.__CLASS -eq 'Microsoft.Graph.PowerShell.AuthenticationException' -and $_.Exception.Response.StatusCode -eq 404) {
                    Write-Verbose "User ID: $UserId not found"
                    $result.Error = "User not found"
                    return $result
                }
                elseif ($_.__CLASS -eq 'Microsoft.Graph.PowerShell.AuthorizationException' -and $_.Exception.Response.StatusCode -eq 403) {
                    Write-Verbose "Insufficient permissions to remove MFA methods for User ID: $UserId"
                    $result.Error = "Insufficient permissions"
                    return $result
                }
                else {
                    Write-Verbose "Error removing MFA method ID: $($method.Id): $_"
                    $result.Error = $_.Exception.Message
                    return $result
                }
            }
        }

        # If all methods are removed successfully
        $result.Success = $true
        $result.UserId = $UserId

    } catch {
        Write-Verbose "Error retrieving MFA authentication methods for User ID: $UserId: $_"
        if ($_.__CLASS -eq 'Microsoft.Graph.PowerShell.AuthenticationException' -and $_.Exception.Response.StatusCode -eq 404) {
            Write-Verbose "User ID: $UserId not found"
            $result.Error = "User not found"
        }
        elseif ($_.__CLASS -eq 'Microsoft.Graph.PowerShell.AuthorizationException' -and $_.Exception.Response.StatusCode -eq 403) {
            Write-Verbose "Insufficient permissions to retrieve MFA methods for User ID: $UserId"
            $result.Error = "Insufficient permissions"
        } else {
            Write-Verbose "Unexpected error retrieving MFA authentication methods for User ID: $UserId: $_"
            $result.Error = $_.Exception.Message
        }
    }

    return [PSCustomObject]$result
}
```

### Key Points:
- **Error Handling**: Each Graph call is wrapped in a `try/catch` block to handle exceptions, including specific handling for 404 and 403 errors.
- **Verbose Logging**: Uses `Write-Verbose` to log progress and actions without using `Write-Host`.
- **Revert Log Entry**: Logs an entry before any destructive action (removing MFA methods).
- **Result Object**: Returns a structured object with properties indicating success, user ID, number of methods removed, and any error messages.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ga-error-handling | warm | run 1 | thinking: NO

**Tok/sec:** 22.1  **Wall sec:** 36.74  **Prompt tokens:** 116  **Output tokens:** 806

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Certainly! Below is a PowerShell function that accomplishes your requirements using the Microsoft Graph API to reset a user's Multi-Factor Authentication (MFA) methods:

```powershell
function Reset-MFAForUser {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Define the result object structure
    $result = @{
        Success   = $false
        UserId    = $null
        MethodsRemoved = 0
        Error     = $null
    }

    try {
        Write-Verbose "Attempting to retrieve MFA methods for user: $UserId"

        # Get all registered authentication methods for the user
        $authMethods = Get-MgUserAuthenticationMethod -UserId $UserId

        if (-not $authMethods) {
            $result.UserId = $UserId
            $result.Error = "No MFA methods found for user."
            Write-Verbose $result.Error
            return $result
        }

        # Log the current state before removing any methods
        Write-Verbose "Logging existing MFA methods for user: $UserId"
        
        foreach ($method in $authMethods) {
            Write-Verbose "Removing method ID: $($method.Id)"
            
            try {
                Remove-MgUserAuthenticationMethod -UserId $UserId -Id $method.Id
                Write-Verbose "Removed authentication method ID: $($method.Id)"
                $result.MethodsRemoved++
            } catch {
                # Handle potential errors during removal of each method
                if ($_.Exception.Response.StatusCode -eq [System.Net.HttpStatusCode]::NotFound) {
                    Write-Verbose "Method not found for removal: $($method.Id)"
                }
                elseif ($_.Exception.Response.StatusCode -eq [System.Net.HttpStatusCode]::Forbidden) {
                    $result.Error = "Insufficient permissions to remove MFA method ID: $($method.Id)"
                    Write-Verbose $result.Error
                    return $result
                } else {
                    # Log any unexpected errors for removal
                    $result.Error = $_.Exception.Message
                    Write-Verbose $result.Error
                    return $result
                }
            }
        }

        $result.UserId = $UserId
        $result.Success = $true

    } catch {
        if ($_.Exception.Response.StatusCode -eq [System.Net.HttpStatusCode]::NotFound) {
            $result.UserId = $UserId
            $result.Error = "User not found."
            Write-Verbose $result.Error
        }
        elseif ($_.Exception.Response.StatusCode -eq [System.Net.HttpStatusCode]::Forbidden) {
            $result.UserId = $UserId
            $result.Error = "Insufficient permissions to access user MFA methods."
            Write-Verbose $result.Error
        } else {
            # Log any unexpected errors during retrieval
            $result.Error = $_.Exception.Message
            Write-Verbose $result.Error
        }
    }

    return $result
}

# Example usage:
# Connect-MgGraph -Scopes "User.ReadWrite.All" before using the function

```

### Key Points:

1. **Error Handling**: 
   - The function uses try/catch blocks to handle errors around each Graph API call.
   - It specifically checks for `404 Not Found` (user not found) and `403 Forbidden` (insufficient permissions).

2. **Logging**:
   - Progress is logged using `Write-Verbose`.
   - A log entry is made before any destructive action (removal of MFA methods).

3. **Return Object**:
   - The function returns an object with properties: `Success`, `UserId`, `MethodsRemoved`, and `Error`.

4. **Permissions**:
   - Ensure you have the necessary permissions (`User.ReadWrite.All`) to perform these operations.

5. **Prerequisites**:
   - You need to connect to Microsoft Graph using `Connect-MgGraph` with appropriate scopes before running this function.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ps-graph-stale-users | cold | run 1 | thinking: NO

**Tok/sec:** 21.9  **Wall sec:** 52.95  **Prompt tokens:** 59  **Output tokens:** 807

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To accomplish this task, you will need to use the Microsoft Graph API to access Entra ID (formerly known as Azure Active Directory) user account data. The script below demonstrates how to authenticate to Microsoft Graph using a service principal or an application with appropriate permissions, retrieve users who haven't signed in for 90 days but are still enabled, and export this information into a CSV file.

Before running the script, ensure you have:

1. Created an Azure AD app registration with API permissions for `User.Read.All` under Microsoft Graph.
2. Assigned a role to your service principal or user account that allows reading all users' data (e.g., Global Reader).
3. Installed the `Microsoft.Graph.Authentication` and `Microsoft.Graph.Users` PowerShell modules.

Here's how you can write the script:

```powershell
# Install required modules if not already installed
Install-Module -Name Microsoft.Graph.Authentication -Force -Scope CurrentUser
Install-Module -Name Microsoft.Graph.Users -Force -Scope CurrentUser

# Import necessary modules
Import-Module Microsoft.Graph.Authentication
Import-Module Microsoft.Graph.Users

# Variables for authentication
$clientId = "YOUR_CLIENT_ID"
$clientSecret = "YOUR_CLIENT_SECRET"
$tenantId = "YOUR_TENANT_ID"

# Authenticate to Microsoft Graph using client credentials flow
Connect-MgGraph -ClientId $clientId -ClientSecret $clientSecret -TenantId $tenantId -Scopes "User.Read.All"

try {
    # Get the current date and calculate the threshold for 90 days ago
    $currentDate = Get-Date
    $thresholdDate = $currentDate.AddDays(-90)

    # Query users who haven't signed in within the last 90 days and are still enabled
    $users = Get-MgUser -Filter "accountEnabled eq true and signInActivity/lastSignInDateTime le '$($thresholdDate.ToString("yyyy-MM-ddTHH:mm:ssZ"))'"

    # Initialize an array to store results
    $results = @()

    foreach ($user in $users) {
        if ($null -eq $user.signInActivity.lastSignInDateTime) {
            # Handle users with no sign-in activity recorded
            continue
        }

        $lastSignInDate = $user.signInActivity.lastSignInDateTime

        if ($lastSignInDate -lt $thresholdDate) {
            # Collect the required data
            $result = [PSCustomObject]@{
                UPN          = $user.UserPrincipalName
                DisplayName  = $user.DisplayName
                LastSignInDateTime = $lastSignInDate
                AccountEnabled = $user.AccountEnabled
            }

            # Add result to results array
            $results += $result
        }
    }

    # Export the results to a CSV file
    $csvFilePath = "InactiveUsers_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv"
    $results | Export-Csv -Path $csvFilePath -NoTypeInformation

    Write-Host "Results exported successfully to: $csvFilePath"

} finally {
    # Disconnect from Microsoft Graph
    Disconnect-MgGraph
}
```

### Key Points:
- **Authentication:** The script uses a client secret for authentication. Ensure the app registration's credentials are correctly set up.
- **Permissions:** You need the `User.Read.All` permission to read all users' sign-in activities and other details.
- **Date Calculation:** Converts current date minus 90 days into a format suitable for comparison with user last sign-in dates.
- **Handling Users Without Sign-In Activity:** Users who have never signed in may not have a `lastSignInDateTime`. The script skips these to focus only on those who haven't logged in within the specified timeframe.

Replace placeholders like `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `YOUR_TENANT_ID` with actual values from your Azure AD app registration. Adjust permissions if necessary, and ensure your environment is set up for using Microsoft Graph PowerShell SDK modules.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## phi4:14b | ps-graph-stale-users | warm | run 1 | thinking: NO

**Tok/sec:** 22.0  **Wall sec:** 34.85  **Prompt tokens:** 59  **Output tokens:** 763

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

To accomplish this task, you'll need to use the Microsoft Graph PowerShell module to interact with Azure Active Directory (formerly known as Entra ID). This script will authenticate using OAuth2, query for users who have not signed in for 90 days but are still enabled, and then export the results to a CSV file. Ensure that you have the necessary permissions and that the Microsoft Graph PowerShell SDK is installed.

### Prerequisites:
1. **Install the Microsoft Graph PowerShell Module:**
   ```powershell
   Install-Module -Name Microsoft.Graph -Scope CurrentUser
   ```

2. **Register an application in Azure AD** with appropriate API permissions (e.g., `User.Read.All`, `AuditLog.Read.All`). Download and securely store the client ID, tenant ID, and client secret.

3. **Grant admin consent** for these permissions within your Azure AD.

4. **Install required modules:**
   ```powershell
   Install-Module -Name Microsoft.Graph.Authentication
   ```

### PowerShell Script:

```powershell
# Import the necessary module
Import-Module Microsoft.Graph.Authentication

# Define application registration details
$clientId = "YOUR_CLIENT_ID"
$clientSecret = "YOUR_CLIENT_SECRET"
$tenantId = "YOUR_TENANT_ID"

# Authenticate using OAuth2 client credentials flow
Connect-MgGraph -ClientId $clientId -ClientSecret $clientSecret -TenantId $tenantId -Scopes "User.Read.All", "AuditLog.Read.All"

# Calculate the date 90 days ago from today
$cutoffDate = (Get-Date).AddDays(-90)

# Query users who are enabled and have not signed in for 90 days
$users = Get-MgUser -Filter "accountEnabled eq true" | ForEach-Object {
    $userPrincipalName = $_.UserPrincipalName

    # Get the last sign-in date using audit logs
    $signInLogs = Get-MgAuditLogSignInByTargetId -UserId $_.Id | Sort-Object -Property CreatedDateTime -Descending | Select-Object -First 1

    if ($null -ne $signInLogs) {
        $lastSignInDate = $signInLogs.CreatedDateTime
    } else {
        # If no sign-in logs are found, set to a default past date
        $lastSignInDate = [datetime]::MinValue
    }

    # Check if the last sign-in was more than 90 days ago
    if ($lastSignInDate -lt $cutoffDate) {
        [PSCustomObject]@{
            UPN         = $userPrincipalName
            DisplayName = $_.DisplayName
            LastSignInDateTime = $lastSignInDate
            AccountEnabled   = $_.AccountEnabled
        }
    }
}

# Export the results to a CSV file
$users | Export-Csv -Path "InactiveUsers.csv" -NoTypeInformation

# Disconnect from Microsoft Graph session
Disconnect-MgGraph
```

### Explanation:
- **Authentication:** Uses OAuth2 client credentials flow for authentication.
- **User Filtering:** Filters users who are enabled (`accountEnabled eq true`) and checks their last sign-in date using the audit logs.
- **Audit Logs:** Queries the `SignInLogs` to find the most recent login attempt. If no log is found, it assumes they haven't signed in.
- **Date Comparison:** Compares the last sign-in date with a cutoff date (90 days ago).
- **Export:** Exports the filtered users to a CSV file named `InactiveUsers.csv`.

### Important Notes:
- Ensure you have the necessary permissions to read user and audit log data.
- Handle sensitive information like client secrets securely.
- Adjust the script as needed for your specific environment or requirements.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ga-deprecated-module | cold | run 1 | thinking: NO

**Tok/sec:** 51.6  **Wall sec:** 121.77  **Prompt tokens:** 84  **Output tokens:** 5789

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here is a production-ready PowerShell script that meets all your requirements. It uses exclusively the `Microsoft.Graph` module, leverages `Get-MgUser` with `-Filter` and `-Property`, applies safe date/timezone handling, and includes the exact Microsoft Graph permissions required.

```powershell
<#
.SYNOPSIS
    Finds enabled Entra ID users with no sign-in activity in the last 60 days and disables their accounts.
.DESCRIPTION
    Uses ONLY the Microsoft.Graph PowerShell module. Retrieves enabled users via Get-MgUser, 
    filters locally for 60-day inactivity, and disables them using Update-MgUser.
.NOTES
    Required Graph Scopes: User.Read.All, User.EnableDisable.All
    Required Entra ID Role: Global Administrator or Identity Administrator
#>

[CmdletBinding()]
param(
    [int]$DaysInactive = 60
)

# Ensure we are connected to Microsoft Graph with the required scopes
$graphContext = Get-MgContext -ErrorAction SilentlyContinue
if (-not $graphContext) {
    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
    Connect-MgGraph -Scopes "User.Read.All", "User.EnableDisable.All" -NoWelcome
}

# Calculate cutoff date in UTC for accurate comparison with Graph API timestamps
$cutoffOffset = [DateTimeOffset]::UtcNow.AddDays(-$DaysInactive)

Write-Host "Retrieving enabled users..." -ForegroundColor Cyan
# Retrieve all enabled users. The Graph API does not support server-side filtering by signInActivity,
# so we use -Filter for accountEnabled and apply the 60-day threshold locally in PowerShell.
$enabledUsers = Get-MgUser `
    -Filter "accountEnabled eq true" `
    -Property "id", "displayName", "userPrincipalName", "signInActivity" `
    -All

Write-Host "Evaluating sign-in activity for the last $($DaysInactive) days..." -ForegroundColor Cyan
$inactiveUsers = foreach ($user in $enabledUsers) {
    $lastSignInStr = $user.SignInActivity?.LastSignInDateTime
    
    # Users with no sign-in record are considered inactive (never signed in or account was disabled previously)
    if ([string]::IsNullOrWhiteSpace($lastSignInStr)) {
        $isInactive = $true
    } else {
        $signInOffset = [DateTimeOffset]::Parse($lastSignInStr)
        $isInactive = ($signInOffset -lt $cutoffOffset)
    }

    if ($isInactive) {
        Write-Host "Found inactive user: $($user.UserPrincipalName)" -ForegroundColor Yellow
        [PSCustomObject]@{
            Id              = $user.Id
            UserPrincipalName = $user.UserPrincipalName
            DisplayName     = $user.DisplayName
        }
    }
}

if ($inactiveUsers.Count -eq 0) {
    Write-Host "No enabled users found who have been inactive for the last $($DaysInactive) days." -ForegroundColor Green
    exit
}

Write-Host "Disabling $($inactiveUsers.Count) inactive user(s)..." -ForegroundColor Red
foreach ($user in $inactiveUsers) {
    try {
        # Set -WhatIf:$false to actually disable accounts. Use -WhatIf to preview changes first.
        Update-MgUser -UserId $user.Id -AccountEnabled $false -WhatIf:$false
        Write-Host "Successfully disabled: $($user.UserPrincipalName)" -ForegroundColor Green
    } catch {
        Write-Warning "Failed to disable user $($user.UserPrincipalName): $_"
    }
}

Write-Host "Operation complete. Disconnecting from Graph..." -ForegroundColor Gray
Disconnect-MgGraph -ErrorAction SilentlyContinue
```

### 🔑 Important Implementation Notes:
1. **Permissions Required:** The script requests `User.Read.All` (to read user properties) and `User.EnableDisable.All` (to toggle the `accountEnabled` flag). Run `Connect-MgGraph` interactively or use a service principal with these scopes consented in Entra ID.
2. **API Filter Limitation:** Microsoft Graph v1.0 `/users` endpoint **does not support server-side filtering by `signInActivity/lastSignInDateTime`** via OData. The script correctly uses `-Filter "accountEnabled eq true"` to narrow the initial dataset, then safely filters the 60-day threshold locally in PowerShell. This is the recommended and supported approach by Microsoft.
3. **Timezone Safety:** Graph API returns sign-in timestamps as UTC ISO 8601 strings. The script uses `[DateTimeOffset]::Parse()` for timezone-agnostic comparison to prevent false positives during DST transitions.
4. **Safety Recommendation:** Change `-WhatIf:$false` to `-WhatIf` in the `Update-MgUser` line before production use to preview which accounts will be modified without applying changes.

### 📦 Prerequisites:
```powershell
Install-Module Microsoft.Graph -Force
Import-Module Microsoft.Graph
# Then run the script as an account with Global Admin or Identity Admin rights.
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ga-deprecated-module | warm | run 1 | thinking: NO

**Tok/sec:** 51.8  **Wall sec:** 94.65  **Prompt tokens:** 84  **Output tokens:** 4882

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here is a complete, production-ready PowerShell script that meets all your requirements using **only** the `Microsoft.Graph` module.

### 🔐 Required Microsoft Graph Permissions
To run this script successfully, you must have an account with one of the following roles or delegated permissions:
- `User.Read.All` → To read user profiles and `signInActivity`
- `User.ManageIdentities.All` → To disable user accounts
*(Note: These scopes require admin consent in your Azure tenant.)*

### 📜 PowerShell Script
```powershell
#requires -Modules Microsoft.Graph.Users

# 1. Connect to Microsoft Graph with required scopes
$scopes = "User.Read.All", "User.ManageIdentities.All"
Connect-MgGraph -Scopes $scopes | Out-Null

Write-Host "Connected to Microsoft Graph." -ForegroundColor Green

# 2. Define the 60-day threshold
$cutoffDate = (Get-Date).AddDays(-60)

Write-Host "Searching for enabled users with no sign-in activity in the last 60 days..." -ForegroundColor Cyan

# 3. Retrieve enabled users and fetch signInActivity property
# ⚠️ IMPORTANT GRAPH API NOTE: Microsoft Graph does NOT support server-side OData filtering 
# on signInActivity. We use -Filter for accountEnabled, fetch signInActivity via -Property, 
# and filter client-side in PowerShell.
$usersToProcess = Get-MgUser -Filter "accountEnabled eq true" -Property signInActivity -All

$disabledCount = 0
$skippedCount = 0

foreach ($user in $usersToProcess) {
    # Skip users with zero recorded sign-in activity (never logged in or data unavailable)
    if (-not $user.SignInActivity -or $null -eq $user.SignInActivity.lastSignInDateTime) {
        Write-Host "$($user.DisplayName) | No sign-in history found. Skipping." -ForegroundColor Yellow
        $skippedCount++
        continue
    }

    # Parse the ISO 8601 timestamp returned by Graph
    $lastLogin = Get-Date $user.SignInActivity.lastSignInDateTime

    if ($lastLogin -lt $cutoffDate) {
        Write-Host "Disabling: $($user.UserPrincipalName) | Last login: $lastLogin" -ForegroundColor Red
        
        try {
            Update-MgUser -UserId $user.Id -AccountEnabled $false
            Write-Host "Successfully disabled account." -ForegroundColor Green
            $disabledCount++
        }
        catch {
            Write-Warning "Failed to disable $($user.UserPrincipalName): $_"
        }
    }
}

Write-Host "`n----------------------------------------`n" -ForegroundColor White
Write-Host "Operation Complete:" -ForegroundColor Cyan
Write-Host "- Accounts disabled: $disabledCount" -ForegroundColor Green
Write-Host "- Accounts skipped (no sign-in history): $skippedCount" -ForegroundColor Yellow

# 4. Clean up session
Disconnect-MgGraph | Out-Null
```

### 🛡️ Important Implementation Notes
1. **Server-Side Filtering Limitation**: Microsoft Graph API v1.0 **does not support** filtering users by `signInActivity` on the server. Attempting `-Filter "signInActivity/lastSignInDateTime lt ..." + returns `400 Bad Request`. The script correctly uses `-Filter` for `accountEnabled`, fetches sign-in data via `-Property signInActivity`, and applies the 60-day rule client-side. This is the officially supported approach.
2. **Safety Recommendation**: Before running in production, comment out the `Update-MgUser` line and uncomment a test block to verify which accounts would be affected:
   ```powershell
   # Write-Host "WOULD DISABLE: $($user.UserPrincipalName) (Last login: $lastLogin)" -ForegroundColor Cyan
   ```
3. **Tenant Admin Consent**: After assigning `User.Read.All` and `User.ManageIdentities.All`, ensure they are consented by a Global Administrator in the Azure Portal or via PowerShell (`Grant-MgOauth2PermissionGrant`).
4. **Module Version**: This script requires `Microsoft.Graph` v1.27+ (preferably v2.x). Install/Update with: `Install-Module Microsoft.Graph -Force -Scope CurrentUser`

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ga-error-handling | cold | run 1 | thinking: NO

**Tok/sec:** 51.6  **Wall sec:** 148.20  **Prompt tokens:** 120  **Output tokens:** 7189

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here is a production-ready PowerShell function that meets all your specifications. It uses the modern `Microsoft.Graph` SDK, strictly avoids `Write-Host`, implements granular try/catch blocks, handles HTTP 404/403 explicitly, generates an audit/revert log before deletions, and returns exactly the requested structured object.

```powershell
function Reset-UserMFA {
    [CmdletBinding()]
    [OutputType([PSCustomObject])]
    param(
        [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
        [string]$UserId
    )
    process {
        # Initialize structured result object
        $result = [PSCustomObject]@{
            Success        = $false
            UserId         = $UserId
            MethodsRemoved = 0
            Error          = ''
        }

        try {
            Write-Verbose "Initiating MFA reset process for user: $UserId"

            # Graph Call 1: Retrieve all registered authentication methods
            $methods = @()
            try {
                $methods = Get-MgUserAuthenticationMethod -UserId $UserId -All -ErrorAction Stop
            } catch {
                $result.Error = Format-GraphError $_ "Retrieval of authentication methods"
                return $result
            }

            # Early exit if no methods are registered
            if (-not $methods) {
                Write-Verbose "No MFA methods found for user. Skipping destructive phase."
                $result.Success = $true
                return $result
            }

            # Revert/Audit log entry generated BEFORE any destructive action
            $revertLogEntry = @"
[REVERT_LOG:MFA_RESET]
Action: Authentication Methods Removal (Reset)
Target UserId: $UserId
Timestamp: $(Get-Date -Format 'o')
Pre-Removal State: Method IDs = @($( ($methods.Id | ForEach-Object { "'$_'" }) -join ', '))
Recovery Note: All registered MFA methods have been purged. User will be prompted to re-register on next sign-in.
Manual Audit ID: $([Guid]::NewGuid().ToString())
==================================================
"@
            Write-Verbose $revertLogEntry

            # Graph Call 2: Iterate and remove each authentication method
            $removedCount = 0
            foreach ($method in $methods) {
                try {
                    Write-Verbose "Removing authentication method ID: $($method.Id)"
                    Remove-MgUserAuthenticationMethod -UserId $UserId -AuthenticationMethodId $method.Id -ErrorAction Stop
                    $removedCount++
                } catch {
                    # Capture per-method failure but continue processing remaining methods if not critical
                    $methodErr = Format-GraphError $_ "Removal of $($method.Id)"
                    Write-Warning "Failed to remove method $($method.Id): $methodErr"
                    $result.Error = $methodErr
                }
            }

            # Success path
            $result.Success = ($result.MethodsRemoved -gt 0) -or ($methods.Count -eq 0)
            $result.MethodsRemoved = $removedCount
            Write-Verbose "MFA reset completed. Successfully removed $removedCount method(s)."
        } catch {
            # Fallback for unexpected non-graph-specific errors
            if ([string]::IsNullOrEmpty($result.Error)) {
                $result.Error = Format-GraphError $_ "General execution"
            }
        }

        return $result
    }
}

function Format-GraphError {
    [CmdletBinding()]
    param(
        [System.Exception]$Exception,
        [string]$Context
    )
    
    # Extract HTTP status code from Microsoft.Graph SDK exceptions (v1 & v2 compatible)
    $statusCode = $null
    if ($Exception -is [Microsoft.Graph.PowerShell.Models.MicrosoftGraphHttpErrorInfo]) {
        $statusCode = $Exception.StatusCode
    } elseif ($Exception.InnerException.Response.StatusCode) {
        $statusCode = [int]$Exception.InnerException.Response.StatusCode
    }

    # Specific handling for 404 and 403 as requested
    if ($statusCode -eq 404 -or $Exception.Message -match '.*user not found.*|.*not found in directory.*' -i) {
        return "User not found (404). Verify the UserId and ensure the user exists in Azure AD."
    }
    if ($statusCode -eq 403 -or $Exception.Message -match '.*permission denied.*|.*insufficient privileges.*|.*authorization failed.*' -i) {
        return "Insufficient permissions (403). Ensure you have User.AuthenticationMethod.ReadWrite.All or equivalent directory permissions."
    }

    # Default fallback for other HTTP or runtime errors
    return "Error during $Context: $($Exception.Message)"
}
```

### Key Implementation Details:
1. **Strict Return Object**: Returns exactly `{ Success, UserId, MethodsRemoved, Error }` with typed properties as requested.
2. **Granular Try/Catch**: Each `Microsoft.Graph` cmdlet (`Get-MgUserAuthenticationMethod` and `Remove-MgUserAuthenticationMethod`) is wrapped in its own try/catch block to isolate failures and continue processing where appropriate.
3. **404/403 Handling**: The `Format-GraphError` helper explicitly checks the Graph SDK's `.StatusCode` property and falls back to regex message parsing for robustness across module versions. Maps directly to your requested strings.
4. **Pre-Destructive Revert Log**: Generated as a structured audit block with timestamps, pre-deletion IDs, and a manual recovery note before entering the removal loop. Output via `Write-Verbose` per constraints.
5. **No `Write-Host`**: All console output uses `Write-Verbose` (for progress) and `Write-Warning` (for non-fatal removal failures). The function returns only the structured object.
6. **Usage Note**: Requires an active `Connect-MgGraph` session with `User.AuthenticationMethod.ReadWrite.All` application permission. The `-All` parameter on retrieval ensures pagination handles users with multiple registered methods.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ga-error-handling | warm | run 1 | thinking: NO

**Tok/sec:** 51.2  **Wall sec:** 170.89  **Prompt tokens:** 120  **Output tokens:** 8725

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
function Reset-UserMFA {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$UserId,

        [Parameter(Mandatory = $false)]
        [string]$RevertLogPath
    )

    # Initialize structured result object with explicit types
    $result = [PSCustomObject]@{
        [bool]Success        = $false
        [string]UserId       = $UserId
        [int]MethodsRemoved  = 0
        [string]Error        = $null
    }

    Write-Verbose "Starting MFA reset process for user: $UserId"

    # Helper to safely extract HTTP status code from Microsoft.Graph exceptions
    function Get-GraphStatusCode {
        param($Exception)
        try { return [int]$Exception.Exception.Response.StatusCode } catch { }
        if ($Exception.ErrorDetails.Code -match "^\d{3}$") { return [int]$Exception.ErrorDetails.Code }
        return $null
    }

    # Helper to set error and return result
    function Set-ResultError {
        param($Res, $Msg)
        $Res.Error = $Msg
        return $Res
    }

    # 1. Verify Graph Context (Graph call)
    try {
        Get-MgContext | Out-Null
    } catch [System.Exception] {
        return Set-ResultError $result "Not connected to Microsoft Graph. Run Connect-MgGraph first."
    }

    # 2. Fetch current MFA methods (Graph call: non-destructive)
    Write-Verbose "Fetching registered authentication methods..."
    $currentMethods = $null
    try {
        $currentMethods = Get-MgUserAuthenticationMethod -UserId $UserId -All
    } catch [Microsoft.Graph.PowerShell.Runtime.RestException] {
        $code = Get-GraphStatusCode $_
        if ($code -eq 403) { return Set-ResultError $result "Insufficient permissions to read MFA methods (403)." }
        if ($code -eq 404) { return Set-ResultError $result "User not found. Cannot read MFA methods (404)." }
        return Set-ResultError $result "Failed to fetch MFA methods: $($_.Exception.Message)"
    } catch [System.Exception] {
        return Set-ResultError $result "Unexpected error fetching MFA methods: $($_.Exception.Message)"
    }

    # 3. Write revert log entry BEFORE any destructive action
    if ($currentMethods) {
        try {
            if (-not $RevertLogPath) {
                $RevertLogPath = Join-Path $env:TEMP "MFA_Reset_Revert_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv"
            }
            # Create a structured log entry containing backup data for potential restoration
            $revertData = foreach ($m in $currentMethods) {
                [PSCustomObject]@{
                    Action           = "MFA_METHOD_BACKUP"
                    UserId           = $UserId
                    Timestamp        = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
                    MethodId         = $m.Id
                    DisplayName      = $m.DisplayName
                    Type             = $m.AdditionalProperties.'@odata.type'
                    CreatedDateTime  = $m.CreatedDateTime
                }
            }
            $revertData | Export-Csv -Path $RevertLogPath -NoTypeInformation -Encoding UTF8
            Write-Verbose "Revert log entry written to: $RevertLogPath"
        } catch [System.Exception] {
            Write-Verbose "Warning: Failed to write revert log. Proceeding with removal. Error: $_.Exception.Message"
        }
    } else {
        Write-Verbose "No registered MFA methods found for this user."
        $result.Success = $true
        return $result
    }

    # 4. Remove each method (Destructive action: Graph call inside loop)
    if ($null -eq $currentMethods) { $currentMethods = @() }
    foreach ($method in $currentMethods) {
        try {
            Write-Verbose "Removing authentication method: $($method.Id)"
            Remove-MgUserAuthenticationMethod -UserId $UserId -AuthenticationMethodId $method.Id -Confirm:$false | Out-Null
            $result.MethodsRemoved++
        } catch [Microsoft.Graph.PowerShell.Runtime.RestException] {
            $code = Get-GraphStatusCode $_
            if ($code -eq 403) { $result.Error += "Insufficient permissions to remove method $($method.Id) (403). " }
            elseif ($code -eq 404) { $result.Error += "User or method not found during removal of $($method.Id) (404). " }
            else { $result.Error += "Graph API error removing $($method.Id): $($_.Exception.Message) " }
        } catch [System.Exception] {
            $result.Error += "Unexpected error removing $($method.Id): $($_.Exception.Message) "
        }
    }

    # 5. Finalize result state and return
    if ([string]::IsNullOrEmpty($result.Error)) {
        $result.Success = $true
    } else {
        $result.Error = $result.Error.TrimEnd(" ")
    }

    Write-Verbose "Reset process completed. Success: $($result.Success) | MethodsRemoved: $($result.MethodsRemoved)"
    return $result
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ps-graph-stale-users | cold | run 1 | thinking: NO

**Tok/sec:** 51.8  **Wall sec:** 136.83  **Prompt tokens:** 59  **Output tokens:** 6632

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here's a complete, production-ready PowerShell script using the **Microsoft.Graph** module. It handles pagination, null sign-in dates, UTC conversion, and exports exactly to your requested format.

### Prerequisites
```powershell
# Run once in an elevated/standard PowerShell session
Install-Module Microsoft.Graph.Users -Force -Scope CurrentUser
Import-Module Microsoft.Graph.Users
```

### PowerShell Script
```powershell
#requires -Modules Microsoft.Graph.Users

param(
    [string]$OutputFile = "InactiveUsers_90Days.csv"
)

Write-Host "[1/5] Connecting to Microsoft Graph..." -ForegroundColor Cyan
Connect-MgGraph -Scopes "User.Read.All"

$cutoffDate = (Get-Date).ToUniversalTime().AddDays(-90)
Write-Host "Cutoff date: $($cutoffDate.ToString('yyyy-MM-dd HH:mm:ss UTC'))" -ForegroundColor DarkGray

# Initialize Graph API URI with pagination support
$uri = "https://graph.microsoft.com/v1.0/users?`$filter=accountEnabled+eq+true&`$select=id,displayName,userPrincipalName,lastSignInDateTime,accountEnabled&`$top=999"
$allEnabledUsers = @()

Write-Host "[2/5] Fetching enabled user accounts (paginated)..." -ForegroundColor Yellow
do {
    $response = Invoke-MgGraphRequest -Method GET -Uri $uri
    $allEnabledUsers += $response.value
    
    if ($response.'@odata.nextLink') {
        $uri = $response.'@odata.nextLink'
    } else {
        break
    }
} while ($true)

Write-Host "[3/5] Evaluating sign-in history for $($allEnabledUsers.Count) accounts..." -ForegroundColor Yellow

$inactiveUsers = @()
foreach ($user in $allEnabledUsers) {
    $lastSignInUTC = $null
    if ($user.lastSignInDateTime) {
        try {
            # Parse ISO8601 string and force UTC comparison
            $lastSignInUTC = [datetime]::Parse($user.lastSignInDateTime).ToUniversalTime()
        } catch {
            Write-Warning "Failed to parse date for $($user.userPrincipalName): $($user.lastSignInDateTime)"
        }
    }

    # Mark as inactive if never signed in OR last sign-in is older than 90 days
    if ($null -eq $lastSignInUTC -or $lastSignInUTC -lt $cutoffDate) {
        $inactiveUsers += [PSCustomObject]@{
            UPN = $user.userPrincipalName
            DisplayName = $user.displayName
            LastSignInDateTime = if ($lastSignInUTC) { $lastSignInUTC.ToString("yyyy-MM-dd HH:mm:ss") } else { "Never" }
            AccountEnabled = $user.accountEnabled
        }
    }
}

if ($inactiveUsers.Count -gt 0) {
    $csvPath = Join-Path (Get-Location).Path $OutputFile
    Write-Host "[4/5] Exporting $($inactiveUsers.Count) inactive accounts to CSV..." -ForegroundColor Cyan
    
    $inactiveUsers | Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8
    Write-Host "[5/5] Success! Results saved to: $csvPath" -ForegroundColor Green
} else {
    Write-Host "No enabled users found that haven't signed in for 90 days." -ForegroundColor Yellow
}

Disconnect-MgGraph
```

### Key Features & Notes
| Feature | Implementation |
|---------|----------------|
| **Pagination** | Explicitly loops through `@odata.nextLink` to handle tenants with >1,000 enabled users |
| **Date Handling** | Parses Graph's ISO8601 strings, forces UTC conversion, and safely handles `"Never"` (null) sign-ins |
| **Filtering Logic** | Catches both users who **never signed in** and those whose last sign-in is **>90 days ago** |
| **Exact Output** | Matches requested columns: `UPN`, `DisplayName`, `LastSignInDateTime`, `AccountEnabled` |
| **Permissions** | Uses `User.Read.All` (sufficient for directory read). Run as a Global Admin or Directory Reader for best results |

### How to Run
1. Save as `Get-InactiveEntraUsers.ps1`
2. Open PowerShell 5.1 or 7+
3. Execute: `.\Get-InactiveEntraUsers.ps1 -OutputFile "Users_Inactive_90Days.csv"`
4. Review the CSV in your working directory

### ⚠️ Important Considerations
- **Large Tenants (>50k users):** Local filtering after fetch is accurate but may take 2-5 minutes. For enterprise scale, consider running this as a scheduled runbook via Azure Automation or using the Graph `/reports/getActiveUserDetails` endpoint for aggregated licensing/usage data instead of user object state.
- **Conditional Access:** These accounts are still enabled and could authenticate if not restricted by CA policies. Always verify with HR/provisioning systems before disabling or removing.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
## qwen3.6:35b | ps-graph-stale-users | warm | run 1 | thinking: NO

**Tok/sec:** 51.5  **Wall sec:** 111.16  **Prompt tokens:** 59  **Output tokens:** 5708

**Graph Accuracy Checklist:**
- AzureAD or MSOnline module used? -> automatic Hallucination: FAIL
- Correct sign-in property? (SignInActivity.LastSignInDateTime, NOT LastSignInDate)
- -Filter and -Property used correctly with Get-MgUser?
- MFA method cmdlets real? (Get-MgUserAuthenticationMethod / Remove-MgUserAuthenticationMethod)
- 404 vs 403 error handling distinguished in catch blocks?
- Write-Verbose not Write-Host for progress output?
- Return object properties match spec (Success, UserId, MethodsRemoved, Error)?

**Response:**

Here's a complete, production-ready PowerShell script using the modern `Microsoft.Graph` module. It handles pagination, null sign-in dates (accounts that have never signed in), date comparisons, and exports to your specified CSV format.

```powershell
<#
.SYNOPSIS
    Finds Entra ID users who are enabled but have not signed in for 90 days (configurable).
.DESCRIPTION
    Connects to Microsoft Graph, queries enabled users, filters by last sign-in date,
    and exports results to a CSV file with the requested columns.
.EXAMPLE
    .\Get-InactiveEntraIDUsers.ps1 -OutputCsvPath "C:\Reports\InactiveUsers_90Days.csv" -InactiveDays 90
#>

param(
    [string]$OutputCsvPath = ".\InactiveEntraIDUsers_90Days.csv",
    [int]$InactiveDays = 90
)

# Ensure the Microsoft.Graph module is loaded
try {
    Import-Module Microsoft.Graph -ErrorAction Stop
} catch {
    Write-Warning "Microsoft.Graph module not found. Installing..."
    Install-Module Microsoft.Graph -Force -Scope CurrentUser -AllowClobber -Confirm:$false
    Import-Module Microsoft.Graph
}

# Define required scopes for reading user sign-in data
$scopes = @("User.Read.All")

try {
    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
    Connect-MgGraph -Scopes $scopes
    
    # Calculate cutoff date in UTC (Graph API uses ISO 8601 UTC timestamps)
    $cutoffDate = [DateTime]::UtcNow.AddDays(-$InactiveDays)
    
    Write-Host "Fetching enabled user accounts..." -ForegroundColor Cyan
    # -All handles pagination automatically. -Property limits returned fields for performance.
    $enabledUsers = Get-MgUser -Filter "accountEnabled eq true" -All -Property "userPrincipalName,displayName,lastSignInDateTime,accountEnabled"
    
    if (-not $enabledUsers) {
        Write-Host "No enabled user accounts found." -ForegroundColor Yellow
        exit
    }
    
    Write-Host "Filtering users inactive for more than $InactiveDays days..." -ForegroundColor Cyan
    
    # Filter: Last sign-in is null (never signed in) OR older than cutoff date
    $inactiveUsers = $enabledUsers | Where-Object {
        $null -eq $_.LastSignInDateTime -or [DateTime]::Parse($_.LastSignInDateTime) -lt $cutoffDate
    }
    
    if ($inactiveUsers) {
        # Format output to ensure consistent CSV columns and handle null dates gracefully
        $report = $inactiveUsers | ForEach-Object {
            [PSCustomObject]@{
                UPN                = $_.UserPrincipalName
                DisplayName        = $_.DisplayName
                LastSignInDateTime = if ([string]::IsNullOrEmpty($_.LastSignInDateTime)) { "Never" } 
                                    else { [DateTime]::Parse($_.LastSignInDateTime).ToString("yyyy-MM-ddTHH:mm:ssZ") }
                AccountEnabled     = $_.AccountEnabled
            }
        }
        
        # Export to CSV with UTF-8 encoding and no type metadata
        $report | Export-Csv -Path $OutputCsvPath -NoTypeInformation -Encoding UTF8
        Write-Host "Successfully exported $($report.Count) inactive user(s) to '$OutputCsvPath'" -ForegroundColor Green
    } else {
        Write-Host "No users found matching the criteria." -ForegroundColor Yellow
    }
}
catch {
    Write-Error "An error occurred: $_"
}
finally {
    # Clean up Graph session
    Disconnect-MgGraph -ErrorAction SilentlyContinue | Out-Null
}
```

### 📋 How to Use
1. Save the script as `Get-InactiveEntraIDUsers.ps1`
2. Run it in PowerShell 5.1+ or PowerShell 7+:
   ```powershell
   .\Get-InactiveEntraIDUsers.ps1 -OutputCsvPath "C:\reports\inactive_users.csv" -InactiveDays 90
   ```

### 🔑 Important Notes
| Aspect | Details |
|--------|---------|
| **Permissions Required** | `User.Read.All` delegated or application role. Requires a user with at least `Directory Readers` or `User Administrator` directory role. |
| **Tenant Size Limit** | Client-side filtering (`Where-Object`) works well for most orgs (<10k enabled users). If your tenant exceeds ~8,000-10,000 enabled users, add server-side date filtering: `-Filter "accountEnabled eq true and lastSignInDateTime lt '$($cutoffDate.ToString("yyyy-MM-ddTHH:mm:ssZ"))'"` to bypass the Graph 10k object query limit. |
| **Never Signed-In Accounts** | The script correctly catches accounts where `lastSignInDateTime` is `$null` (e.g., newly created or unprovisioned accounts) and marks them as `"Never"` in the CSV. |
| **Date Format** | Outputs dates in ISO 8601 UTC format (`yyyy-MM-ddTHH:mm:ssZ`) for compatibility with reporting tools, Excel, and audit systems. |

Let me know if you need this adapted for conditional access remediation, auto-remediation workflows, or hybrid Azure AD join environments!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _

---
