# Ollama Model Responses

Generated: 2026-06-25T14:37:48

Review each response below and score manually using the rubric:
| Dimension | Score 1-10 |
|---|---|
| Accuracy — facts, cmdlets, syntax correct? | |
| Completeness — fully answers the request? | |
| Format — clean and usable without editing? | |
| Hallucination risk — invented cmdlets or endpoints? | |
| Consistency — similar quality on repeat runs? | |

---

## qwen3:8b | chat-explain | cold | run 1 | thinking: NO

**Tok/sec:** 39.0 &nbsp; **Wall sec:** 10.70 &nbsp; **Prompt tokens:** 41 &nbsp; **Output tokens:** 353

**Response:**

A homelab is a personal setup where someone runs their own servers, networks, or IT gear at home—like testing tools, experimenting with tech, or hosting services. For IT ops pros, it’s a safe sandbox to practice skills, troubleshoot real-world issues, or test new tools without risking production systems. It’s great for learning without the pressure of real-world consequences. Plus, you can run your own email, DNS, or monitoring tools, giving you hands-on experience with the same tech you manage daily. It’s a way to stay sharp, experiment freely, and even support personal projects or small businesses. Essentially, it’s a playground for IT professionals to grow, learn, and innovate—right in their own home.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | chat-explain | warm | run 1 | thinking: NO

**Tok/sec:** 38.5 &nbsp; **Wall sec:** 9.81 &nbsp; **Prompt tokens:** 41 &nbsp; **Output tokens:** 371

**Response:**

A homelab is a personal tech setup at home where you experiment with servers, networks, or software. IT pros might build one to safely test configurations, troubleshoot issues, or learn new tools without risking real systems. It’s like a sandbox for hands-on practice. For IT ops, it’s perfect for experimenting with automation scripts, cloud setups, or troubleshooting scenarios. It helps you stay sharp, prepare for certifications, or explore cutting-edge tech without company resources. Plus, it’s cost-effective and lets you collaborate with others or share knowledge. Whether you’re debugging a tricky problem or trying out a new OS, a homelab gives you control and flexibility—no pressure, just learning. It’s a great way to keep your skills fresh and ahead of the curve.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | chat-troubleshoot | cold | run 1 | thinking: NO

**Tok/sec:** 38.5 &nbsp; **Wall sec:** 15.80 &nbsp; **Prompt tokens:** 46 &nbsp; **Output tokens:** 545

**Response:**

Sure! Let’s walk through a few simple checks together.  

**1. Check if the internet is working:**  
First, can you open a browser and visit a website like Google or YouTube? If you can’t access the internet at all, the update might have messed up your connection, and the VPN issue is just a side effect. If you *can* browse, then the problem is probably with the VPN itself.  

**2. Restart the VPN app or service:**  
Sometimes, updates can cause apps to glitch. Try closing the VPN app completely (right-click its icon in the taskbar and select "Exit") and then reopening it. If it’s a built-in Windows VPN, go to Settings > Network & Internet > VPN, and try reconnecting. If it’s a third-party app, make sure you’re using the correct login credentials (sometimes updates reset those).  

**3. Check for firewall or antivirus blocks:**  
Windows updates might have changed your firewall or antivirus settings. Temporarily disable your antivirus (if it’s a third-party app) or set it to “allow” the VPN connection. Also, check Windows Defender Firewall settings: go to Control Panel > Windows Defender Firewall > Allow an app through firewall, and make sure the VPN app is listed.  

Let me know what you find after these steps—happy to help further! 😊

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | chat-troubleshoot | warm | run 1 | thinking: NO

**Tok/sec:** 38.3 &nbsp; **Wall sec:** 17.54 &nbsp; **Prompt tokens:** 46 &nbsp; **Output tokens:** 665

**Response:**

Sure! Let’s walk through the first three steps together, like troubleshooting with a friend:  

1. **Check if the VPN is even set up correctly**  
   *“First, let me make sure the VPN is still in your settings. Did you notice if the connection option disappeared or if the login details changed after the update? Sometimes updates can reset settings, so maybe you’ll need to re-enter your password or check the server address.”*  

2. **Verify your internet connection**  
   *“Next, can you still access the internet normally? Try opening a browser and checking a website. If your laptop can’t connect to the web, the VPN won’t work either. Maybe the update messed up your network settings or Wi-Fi.”*  

3. **Check for firewall/antivirus interference**  
   *“Lastly, some updates or security software might block the VPN. Have you tried temporarily disabling your firewall or antivirus to see if that helps? (Don’t worry—just keep it off for a few minutes to test.) If that fixes it, you’ll know it’s a security setting issue.”*  

Let me know what happens at each step, and we’ll keep going from there! 😊

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | chat-summarize | cold | run 1 | thinking: NO

**Tok/sec:** 38.9 &nbsp; **Wall sec:** 7.85 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 240

**Response:**

The certificate for corp-vpn.contoso.com expired on June 1, 2026, causing a surge in authentication failures (from 2 to 340 per hour). We’re rolling back the certificate bundle to resolve the issue and restore normal access. This should fix the login problems soon.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | chat-summarize | warm | run 1 | thinking: NO

**Tok/sec:** 38.4 &nbsp; **Wall sec:** 9.46 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 357

**Response:**

The certificate for the corporate VPN expired on June 1, 2026, causing a spike in failed login attempts (from 2 to 340 per hour). We’re rolling back the certificate setup to fix the issue. This should resolve authentication problems and prevent further disruptions.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ps-graph-device-list | cold | run 1 | thinking: NO

**Tok/sec:** 37.4 &nbsp; **Wall sec:** 62.30 &nbsp; **Prompt tokens:** 65 &nbsp; **Output tokens:** 2269

**Response:**

Here's a PowerShell script that uses the **Microsoft Graph PowerShell module** to list all **Intune-managed Windows devices** where the **last sync is older than 7 days**, and outputs the required properties: `DeviceName`, `LastSyncDateTime`, and `ComplianceState`. The script uses **`-Select`** and **`-Filter`** to optimize the query.

---

### ✅ **PowerShell Script**

```powershell
# Load the Microsoft Graph module
Import-Module Microsoft.Graph

# Connect to Microsoft Graph (ensure you're authenticated)
Connect-MgGraph -Scopes "DeviceManagementServiceConfiguration.ReadWriteAll"

# Calculate the date 7 days ago (UTC)
$date = [datetime]::UtcNow.AddDays(-7)

# Format the date in ISO 8601 format for filtering
$filter = "lastSyncDateTime le '$($date.ToString('yyyy-MM-ddTHH:mm:ssZ'))'"

# Retrieve Intune-managed devices with last sync older than 7 days
$devices = Get-MgDeviceManagementManagedDevice `
    -Select deviceName, lastSyncDateTime, complianceState `
    -Filter $filter

# Output the results in the desired format
$devices | Select-Object DeviceName, LastSyncDateTime, ComplianceState
```

---

### 📌 **Explanation**

1. **Authentication**:
   - `Connect-MgGraph` authenticates the user and grants the required permissions (`DeviceManagementServiceConfiguration.ReadWriteAll`).

2. **Date Calculation**:
   - `DateTime.UtcNow.AddDays(-7)` calculates the date **7 days ago in UTC**, ensuring the filter aligns with the API's expectations.

3. **Filtering**:
   - The filter `lastSyncDateTime le <date>` selects devices whose last sync is **less than or equal to** the date 7 days ago.

4. **Selecting Properties**:
   - `-Select deviceName, lastSyncDateTime, complianceState` ensures only the required properties are retrieved, reducing payload size.

5. **Output**:
   - `Select-Object` renames the properties to match the specified output format (`DeviceName`, `LastSyncDateTime`, `ComplianceState`).

---

### 📌 **Requirements**
- **Microsoft Graph PowerShell module** installed:  
  ```powershell
  Install-Module -Name Microsoft.Graph -Force
  ```
- **Permissions**: The user must have **DeviceManagementServiceConfiguration.ReadWriteAll** scope to access Intune device data.

---

### 🚨 **Notes**
- **Time Zone**: The script uses **UTC** for consistency with Microsoft Graph API.
- **ComplianceState**: This is a boolean property indicating whether the device is compliant.
- **Error Handling**: You may want to add try/catch blocks for production use.

Let me know if you need to filter for **Windows 10/11 devices** or add additional properties like `DeviceModel` or `OperatingSystem`.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ps-graph-device-list | warm | run 1 | thinking: NO

**Tok/sec:** 36.5 &nbsp; **Wall sec:** 116.66 &nbsp; **Prompt tokens:** 65 &nbsp; **Output tokens:** 4246

**Response:**

Here's a PowerShell script that leverages the **Microsoft Graph PowerShell module** to list all **Intune-managed Windows devices** where the **last sync is older than 7 days**, and outputs the **DeviceName**, **LastSyncDateTime**, and **ComplianceState** in a clean, formatted table. It uses **`-Filter`** and **`-Select`** to optimize API calls and reduce data transfer.

---

### ✅ PowerShell Script

```powershell
# Connect to Microsoft Graph (ensure you have the correct permissions)
Connect-MgGraph -Scopes "DeviceManagementDevices.Read.All"

# Calculate the date 7 days ago (UTC)
$sevenDaysAgo = [datetime]::UtcNow.AddDays(-7)

# Construct the OData filter string
$filter = "platform eq 'windows' and lastSyncDateTime lt datetime'$($sevenDaysAgo.ToString('yyyy-MM-ddTHH:mm:ssZ'))'"

# Retrieve Intune-managed Windows devices with the specified filter and selected properties
$devices = Get-MgDeviceManagementDevice -Filter $filter -Select deviceName,lastSyncDateTime,complianceState

# Format and output the results with renamed columns
$devices | Select-Object -Property @{
    Name = "DeviceName"
    Expression = { $_.deviceName }
}, @{
    Name = "LastSyncDateTime"
    Expression = { $_.lastSyncDateTime }
}, @{
    Name = "ComplianceState"
    Expression = { $_.complianceState }
} | Format-Table -AutoSize
```

---

### 📌 Explanation

- **`Connect-MgGraph`**: Authenticates with Microsoft Graph using the appropriate scope (`DeviceManagementDevices.Read.All`) to access device management data.
- **`$sevenDaysAgo`**: Calculates the date 7 days before the current UTC time.
- **`$filter`**: Uses OData syntax to filter Windows devices whose `lastSyncDateTime` is older than 7 days.
- **`Get-MgDeviceManagementDevice`**: Fetches the filtered devices with only the required properties (`deviceName`, `lastSyncDateTime`, and `complianceState`).
- **`Select-Object`**: Renames the properties for better readability in the output table.
- **`Format-Table`**: Displays the results in a clean, tabular format.

---

### 📌 Notes

- **Authentication**: Ensure you are running the script in an environment where Microsoft Graph authentication is handled (e.g., via interactive login or service principal).
- **Permissions**: The script requires the `DeviceManagementDevices.Read.All` scope. If you're using a service principal, make sure it has the required permissions in Azure AD.
- **UTC Time**: The script uses UTC time for consistency with Microsoft Graph API, which typically returns UTC timestamps.

---

### 📌 Output Example

| DeviceName     | LastSyncDateTime         | ComplianceState |
|----------------|--------------------------|-----------------|
| Laptop01       | 2023-10-01T12:34:56Z     | nonCompliant    |
| Desktop02      | 2023-09-28T08:15:30Z     | compliant       |

---

This script is efficient, secure, and adheres to Microsoft Graph best practices for querying device management data.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ps-graph-stale-users | cold | run 1 | thinking: NO

**Tok/sec:** 36.9 &nbsp; **Wall sec:** 88.89 &nbsp; **Prompt tokens:** 60 &nbsp; **Output tokens:** 3219

**Response:**

Here's a PowerShell script that uses the **Microsoft Graph PowerShell module** to identify **Entra ID users who have not signed in for 90 days and are still enabled**, then exports the results to a **CSV file** with the specified columns:

---

### ✅ **PowerShell Script**

```powershell
# Connect to Microsoft Graph with necessary permissions
Connect-MgGraph -Scopes "User.Read.All"

# Calculate cutoff date (90 days ago in UTC)
$cutoffDate = (Get-Date).AddDays(-90).ToUniversalTime()

# Initialize an array to store inactive users
$inactiveUsers = @()

# Get all users from Entra ID
$users = Get-MgUser -All

# Filter users who are enabled and last signed in before the cutoff date
foreach ($user in $users) {
    if ($user.AccountEnabled -and $user.LastSignInDateTime -and $user.LastSignInDateTime -lt $cutoffDate) {
        $inactiveUsers += [PSCustomObject]@{
            UPN = $user.UserPrincipalName
            DisplayName = $user.DisplayName
            LastSignInDateTime = $user.LastSignInDateTime
            AccountEnabled = $user.AccountEnabled
        }
    }
}

# Export results to CSV
$inactiveUsers | Export-Csv -Path "C:\output\inactive_users.csv" -NoTypeInformation
Write-Host "Inactive users exported to C:\output\inactive_users.csv"
```

---

### 📌 **Key Notes**

1. **Permissions**:
   - The script requires the **`User.Read.All`** permission to retrieve all user data.
   - If this is the first run, the script will prompt for sign-in and consent to the required permissions.

2. **Date Handling**:
   - The script calculates the cutoff date in **UTC** to match the UTC-based `LastSignInDateTime` property.
   - This ensures accurate comparisons regardless of the user's local time zone.

3. **Output**:
   - The CSV file is saved to `C:\output\inactive_users.csv`.
   - You can modify the path as needed or prompt the user for a custom location.

4. **CSV Columns**:
   - The output includes the required columns: `UPN`, `DisplayName`, `LastSignInDateTime`, and `AccountEnabled`.

---

### 🧠 **Best Practices**
- **Ensure the directory `C:\output` exists**, or modify the path in the script.
- **Run the script with elevated privileges** if needed (e.g., for file system access).
- For production use, consider **logging errors** or **adding a progress bar** for large user directories.

---

### 🚀 **Optional Enhancements**
- **Filter by Organizational Unit (OU)**: Add a filter to retrieve users from specific OUs.
- **Use Azure AD PowerShell Module**: For more granular control over user properties.
- **Automate with Scheduled Task**: Run the script periodically to monitor inactive users.

Let me know if you'd like to add these features!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ps-graph-stale-users | warm | run 1 | thinking: NO

**Tok/sec:** 36.8 &nbsp; **Wall sec:** 95.27 &nbsp; **Prompt tokens:** 60 &nbsp; **Output tokens:** 3493

**Response:**

Here's a PowerShell script that uses the Microsoft Graph API to identify Entra ID (formerly Azure AD) users who have not signed in for 90 days and are still enabled. The results are exported to a CSV file with the specified columns.

---

### ✅ **PowerShell Script: Find Inactive Entra ID Users**

```powershell
# Import the Microsoft Graph PowerShell module
if (-not (Get-Module -ListAvailable -Name Microsoft.Graph)) {
    Write-Host "Installing Microsoft Graph PowerShell module..."
    Install-Module -Name Microsoft.Graph -Force
}

# Connect to Microsoft Graph API
Connect-MgGraph -Scopes User.Read.All

# Get all users
$users = Get-MgUser -All

# Define threshold date (90 days ago in UTC)
$threshold = [DateTime]::UtcNow.AddDays(-90)

# Collect results
$results = @()

foreach ($user in $users) {
    if ($user.AccountEnabled -eq $true -and $user.LastSignInDateTime -ne $null -and $user.LastSignInDateTime.UtcDateTime -lt $threshold) {
        $result = [PSCustomObject] @{
            UPN = $user.UserPrincipalName
            DisplayName = $user.DisplayName
            LastSignInDateTime = $user.LastSignInDateTime.UtcDateTime
            AccountEnabled = $user.AccountEnabled
        }
        $results += $result
    }
}

# Export results to CSV
$results | Export-Csv -Path "InactiveUsers.csv" -NoTypeInformation
Write-Host "Inactive users exported to 'InactiveUsers.csv'"
```

---

### 📌 **Key Notes**

1. **Authentication & Permissions**:
   - The script uses the `User.Read.All` scope to access user data.
   - You must have **admin privileges** to run this script. If you're using a service principal, ensure it has the necessary permissions.

2. **UTC Time Handling**:
   - The script compares the `LastSignInDateTime` in **UTC** to ensure accurate results regardless of the system's local time zone.

3. **Pagination**:
   - The `-All` parameter in `Get-MgUser` ensures all users are retrieved, even if the result set is large.

4. **CSV Output**:
   - The CSV includes the columns: **UPN**, **DisplayName**, **LastSignInDateTime**, and **AccountEnabled**.
   - The `LastSignInDateTime` is exported as a UTC datetime string.

---

### 📁 **Output File**
- The script generates a CSV file named **`InactiveUsers.csv`** in the current working directory.
- The file contains only users who:
  - Are **enabled**.
  - Have **not signed in** for **90 days or more**.
  - Have a valid `LastSignInDateTime`.

---

### 🔒 **Security & Best Practices**
- **Do not run this script in production environments** without proper safeguards.
- **Use a service principal** for automation instead of interactive authentication.
- Ensure the script is run in a secure environment to avoid exposing credentials or sensitive data.

Let me know if you'd like to add additional filters (e.g., by department, lifecycle state, etc.) or integrate with other tools!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ps-graph-app-assignment | cold | run 1 | thinking: NO

**Tok/sec:** 36.7 &nbsp; **Wall sec:** 105.95 &nbsp; **Prompt tokens:** 52 &nbsp; **Output tokens:** 3825

**Response:**

Here's a PowerShell function that uses the **Microsoft Graph PowerShell SDK** to retrieve an Intune app by its display name and then lists the groups it is assigned to, including the **assignment intent** (required vs. available). It includes **error handling** for cases where the app is not found.

---

### ✅ PowerShell Function: `Get-IntuneAppGroupAssignments`

```powershell
function Get-IntuneAppGroupAssignments {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$AppName
    )

    try {
        # Ensure the Microsoft Graph PowerShell module is installed and connected
        if (-not (Get-MgGraphConnection)) {
            Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
            Connect-MgGraph -Scopes "DeviceManagementApps.Read.All"
        }

        # Step 1: Find the app by display name
        $uri = "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps?\$filter=displayName eq '$AppName'"
        $appResponse = Invoke-MgGraphRequest -Url $uri -Method Get

        if (-not $appResponse) {
            throw "Failed to retrieve app information."
        }

        if ($appResponse.value.Count -eq 0) {
            throw "App with display name '$AppName' not found."
        }

        # Step 2: Get the app's ID
        $appId = $appResponse.value[0].id

        # Step 3: Retrieve assignments for the app
        $assignUri = "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps/$appId/assign"
        $assignResponse = Invoke-MgGraphRequest -Url $assignUri -Method Get

        if (-not $assignResponse) {
            throw "Failed to retrieve app assignments."
        }

        # Step 4: Process and format the assignments
        $assignments = @()
        foreach ($assignment in $assignResponse.value) {
            $group = $assignment.group
            $intent = $assignment.intent
            $assignments += [PSCustomObject]@{
                Group     = $group.displayName
                Intent    = $intent
                GroupId   = $group.id
                AssignmentType = "Assigned"
            }
        }

        return $assignments

    } catch {
        Write-Error "Error retrieving app assignments: $_"
        return @()
    }
}
```

---

### 📌 Function Usage Example

```powershell
# Example: Get assignments for an app named "MyApp"
$assignments = Get-IntuneAppGroupAssignments -AppName "MyApp"

if ($assignments.Count -gt 0) {
    Write-Host "App assignments:"
    $assignments | Format-Table -AutoSize
} else {
    Write-Host "No assignments found for the app."
}
```

---

### 🚀 Notes

- **Authentication**: The function uses `Connect-MgGraph` to authenticate with the Microsoft Graph API. Ensure that the user has the **Microsoft Graph PowerShell module** installed and has the necessary permissions (e.g., `DeviceManagementApps.Read.All`).
- **Error Handling**: If the app isn't found, the function throws an error and returns an empty array. All other exceptions are caught and logged.
- **Output**: The function returns a list of custom objects with the group name, assignment intent, and group ID.

---

### 📦 Prerequisites

- **Install Microsoft Graph PowerShell SDK**:
  ```powershell
  Install-Module -Name Microsoft.Graph
  ```
- **Connect to Microsoft Graph**:
  ```powershell
  Connect-MgGraph -Scopes "DeviceManagementApps.Read.All"
  ```

---

This function provides a clean, reusable way to retrieve group assignments for an Intune app, with proper handling of common errors.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ps-graph-app-assignment | warm | run 1 | thinking: NO

**Tok/sec:** 36.5 &nbsp; **Wall sec:** 117.28 &nbsp; **Prompt tokens:** 52 &nbsp; **Output tokens:** 4271

**Response:**

Here's a well-structured PowerShell function that uses the **Microsoft Graph PowerShell SDK** to retrieve the list of groups an Intune app is assigned to, including the **assignment intent** (required or available). It includes **error handling** for cases where the app is not found and provides a clear output in the form of custom objects.

---

### ✅ **Function: `Get-IntuneAppGroupAssignments`**

```powershell
function Get-IntuneAppGroupAssignments {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$DisplayName
    )

    try {
        # Connect to Microsoft Graph with the required scope
        Connect-MgGraph -Scopes "DeviceManagementApps.Read.All"
    } catch {
        Write-Error "Failed to connect to Microsoft Graph: $_"
        return
    }

    try {
        # URL encode the display name for the filter
        $encodedDisplayName = [System.Web.HttpUtility]::UrlEncode($DisplayName)
        $filter = "displayName eq '$encodedDisplayName'"

        # Get apps by display name
        $apps = Get-MgDeviceAppManagementMobileApp -Filter $filter
        if (-not $apps) {
            Write-Error "App with display name '$DisplayName' not found."
            return
        }
    } catch {
        Write-Error "Error retrieving apps: $_"
        return
    }

    # Select the first app (assuming unique display name)
    $app = $apps | Select-Object -First 1

    try {
        # Get assignments for the app
        $assignments = Get-MgDeviceAppManagementMobileAppAssignment -DeviceAppManagementMobileAppId $app.id
        if (-not $assignments) {
            Write-Warning "No assignments found for the app."
            return
        }

        # Process each assignment and return custom objects
        foreach ($assignment in $assignments) {
            $target = $assignment.target
            if ($target -and $target.group) {
                $groupId = $target.group.id
                $groupName = $target.group.displayName
                $intent = $assignment.intent
                [PSCustomObject]@{
                    DisplayName = $groupName
                    GroupId     = $groupId
                    Intent      = $intent
                }
            }
        }
    } catch {
        Write-Error "Error retrieving assignments: $_"
        return
    }
}
```

---

### 📌 **Key Features**

- ✅ **Authentication**: Uses `Connect-MgGraph` with the required scope `"DeviceManagementApps.Read.All"` to access Intune app data.
- ✅ **Filtering**: Properly URL-encodes the display name to handle special characters in filters.
- ✅ **Error Handling**: Catches and reports errors during connection, app retrieval, or assignment fetching.
- ✅ **Output**: Returns a list of custom objects with `DisplayName`, `GroupId`, and `Intent` for each group the app is assigned to.

---

### 🧪 **Usage Example**

```powershell
Get-IntuneAppGroupAssignments -DisplayName "My Intune App"
```

**Output:**
```powershell
DisplayName     GroupId                 Intent
------------     --------                -------
Marketing Team   group-12345             Required
IT Department    group-67890             Available
```

---

### ⚠️ **Requirements**

- **Prerequisites**: 
  - The [Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/graph/powershell/) must be installed.
  - The user must have **permissions** to read Intune apps and their assignments (e.g., `DeviceManagementApps.Read.All`).
- **Note**: This function assumes the display name is unique. If multiple apps exist with the same name, only the first one is processed.

---

### 📌 **Next Steps**

- Optionally, extend this function to handle multiple apps with the same display name.
- Add support for exporting the output to CSV or JSON for reporting purposes.

Let me know if you'd like to enhance this further!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | runbook-offboard | cold | run 1 | thinking: NO

**Tok/sec:** 37.5 &nbsp; **Wall sec:** 56.70 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 2062

**Response:**

1. **Disable the Microsoft 365 Account**  
   - Log in to the Microsoft 365 Admin Center or Azure AD portal.  
   - Navigate to **Users > All Users** and select the employee’s account.  
   - Disable the account by clicking **Disable account**.  
   - Confirm the action and note the date.  
   - **Done**: [ ]  

2. **Block Sign-In to Prevent Access**  
   - In Azure AD, go to **Users > All Users** and select the employee’s account.  
   - Under **Account settings**, click **Block sign-in**.  
   - Confirm the action and note the date.  
   - **Done**: [ ]  

3. **Revoke Active Sessions**  
   - In Azure AD, go to **Users > All Users** and select the employee’s account.  
   - Under **Account settings**, click **Revoke all sessions**.  
   - Confirm the action and note the date.  
   - **Done**: [ ]  

4. **Wipe or Retire the Device (if enrolled in Intune)**  
   - Log in to the Microsoft Intune admin center.  
   - Navigate to **Devices > All Devices** and locate the employee’s device.  
   - Select the device and click **Wipe** (if enrolled) or **Retire** (if not enrolled).  
   - Confirm the action and note the date.  
   - **Done**: [ ]  

5. **Archive the Mailbox (if applicable)**  
   - Log in to the Microsoft Exchange Admin Center.  
   - Navigate to **Recipients > Mailboxes** and select the employee’s mailbox.  
   - Archive the mailbox or delete it (per compliance policies).  
   - Confirm the action and note the date.  
   - **Done**: [ ]  

6. **Verify All Actions Are Completed**  
   - Cross-check the account status in Azure AD and Exchange Admin Center.  
   - Confirm the device is wiped or retired (if applicable).  
   - Ensure no active sessions or sign-in attempts are recorded.  
   - **Done**: [ ]  

7. **Update Records and Documentation**  
   - Update the employee’s offboarding status in HR or IT systems.  
   - Document all actions taken for audit or compliance purposes.  
   - **Done**: [ ]  

8. **Notify Relevant Teams (if applicable)**  
   - Inform the IT team, HR, or compliance department of the offboarding completion.  
   - Share the final status and any required follow-up.  
   - **Done**: [ ]  

**Note**: Always follow company-specific compliance policies and ensure all data is securely removed or archived.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | runbook-offboard | warm | run 1 | thinking: NO

**Tok/sec:** 37.9 &nbsp; **Wall sec:** 28.65 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 1079

**Response:**

1. **Disable the Microsoft 365 Account**  
   - Action: Navigate to the Microsoft 365 Admin Center, locate the employee's account, and disable it.  
   - Responsible Party: Microsoft 365 Admin  
   - Done: [ ]  

2. **Revoke Active Sessions**  
   - Action: Use the Microsoft 365 Admin Center to revoke all active sessions for the employee’s account.  
   - Responsible Party: Microsoft 365 Admin  
   - Done: [ ]  

3. **Block Sign-In for the Account**  
   - Action: In the Microsoft 365 Admin Center, block sign-in for the employee’s account to prevent future access.  
   - Responsible Party: Microsoft 365 Admin  
   - Done: [ ]  

4. **Archive the Employee’s Mailbox**  
   - Action: Use the Exchange Admin Center to archive the employee’s mailbox (e.g., move to a retention label or archive mailbox).  
   - Responsible Party: Exchange Admin  
   - Done: [ ]  

5. **Wipe or Retire Company-Owned Devices (Intune)**  
   - Action: If the employee used a company-owned device, use Intune to wipe the device or retire it. For personal devices, confirm ownership and follow applicable policies.  
   - Responsible Party: Intune Admin  
   - Done: [ ]  

6. **Remove Intune Device Enrollment**  
   - Action: In Intune, remove the employee’s device from enrollment to ensure it no longer receives policies or updates.  
   - Responsible Party: Intune Admin  
   - Done: [ ]  

7. **Verify Account and Device Status**  
   - Action: Confirm the employee’s account is disabled, sign-in is blocked, and the device (if applicable) is wiped/retired.  
   - Responsible Party: Microsoft 365 Admin / Intune Admin  
   - Done: [ ]  

8. **Update Access Controls and Permissions**  
   - Action: Remove the employee’s access to shared resources (e.g., SharePoint, Teams, OneDrive) and adjust permissions in relevant systems.  
   - Responsible Party: System Admins  
   - Done: [ ]  

9. **Document and Notify Stakeholders**  
   - Action: Record the offboarding steps in a log and notify the HR/IT team of the completion.  
   - Responsible Party: IT Manager  
   - Done: [ ]  

10. **Final Verification**  
    - Action: Perform a final check to ensure all systems, accounts, and devices are properly offboarded.  
    - Responsible Party: IT Manager  
    - Done: [ ]  

**Notes:**  
- Ensure compliance with data retention policies when archiving mailboxes.  
- For personal devices, follow company policy on data removal and ownership.  
- Use Microsoft 365’s "User Account Cleanup" tool if applicable.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | runbook-cert-rotation | cold | run 1 | thinking: NO

**Tok/sec:** 37.4 &nbsp; **Wall sec:** 58.17 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 2115

**Response:**

**Runbook: Rotating an Expired SCEP Certificate Profile in Intune**  
*Last Updated: [Date]*  
*Change-Control Required: Yes (see notes)*  

---

### **1. Identify Affected Devices**  
**Objective:** Locate devices with expired SCEP certificates.  

**Steps:**  
1. **Access Intune Admin Center:**  
   - Navigate to **Devices > Configuration profiles**.  
   - Filter by SCEP certificate profile name.  
2. **Check Compliance Status:**  
   - Go to **Devices > Compliance policies**.  
   - Filter by policy name (e.g., "SCEP Certificate Renewal") to identify non-compliant devices.  
3. **Query Microsoft Graph API (Optional):**  
   - Use Azure AD Graph or Microsoft Graph API to filter devices with expired certificates.  
     Example query:  
     ```  
     GET /deviceManagement/deviceCompliancePolicies?$filter=displayName eq 'SCEP Certificate Renewal'  
     ```  
4. **Document Affected Devices:**  
   - List device names, models, and user details in a spreadsheet for tracking.  

**Change-Control Note:**  
- **Requires approval** for accessing production device data.  

---

### **2. Prepare New Certificate**  
**Objective:** Generate and validate the new SCEP certificate.  

**Steps:**  
1. **Renew Certificate with CA:**  
   - Use your organization’s Certificate Authority (CA) to issue a new certificate.  
   - Ensure the new certificate includes the same subject name and SANs as the old one.  
2. **Validate Certificate:**  
   - Confirm the new certificate is valid and has a sufficient expiration date.  
   - Test the certificate in a staging environment (if applicable).  

**Change-Control Note:**  
- **Requires approval** for certificate renewal, especially if involving internal CA or third-party CA.  

---

### **3. Update SCEP Profile in Intune**  
**Objective:** Replace the expired certificate in the SCEP profile.  

**Steps:**  
1. **Create New SCEP Profile:**  
   - Go to **Devices > Configuration profiles > Create profile**.  
   - Select **SCEP Certificate** as the profile type.  
   - Enter the new certificate details (e.g., CA URL, subject name, renewal settings).  
   - Assign the profile to the affected device groups.  
2. **Deactivate Old Profile (Optional):**  
   - If the old profile is no longer needed, deactivate it to avoid conflicts.  

**Change-Control Note:**  
- **Requires approval** for modifying production profiles.  

---

### **4. Force Device Sync**  
**Objective:** Ensure devices apply the new certificate immediately.  

**Steps:**  
1. **Push Policy Update:**  
   - In Intune, go to **Devices > All devices** and select the affected devices.  
   - Use the **Force sync** option to trigger a certificate renewal.  
2. **iOS Devices:**  
   - Use the command:  
     ```  
     sudo profiles install /var/tmp/IntuneProfile.mobileconfig  
     ```  
   - Alternatively, guide users to manually refresh settings.  
3. **Android Devices:**  
   - Use the **Intune Management API** to send a sync command.  
   - Alternatively, push a policy update via MDM.  

**Change-Control Note:**  
- **Requires approval** for mass sync operations in production.  

---

### **5. Verify Certificate Installation**  
**Objective:** Confirm the new certificate is active and the old one is revoked.  

**Steps:**  
1. **Check Compliance Status:**  
   - In Intune, verify that affected devices are now compliant.  
2. **Inspect Device Certificates:**  
   - For iOS: Go to **Settings > General > About > Certificate Trust Settings**.  
   - For Android: Use device management tools or check via ADB.  
3. **Validate Certificate Revocation:**  
   - Ensure the old certificate is revoked (if applicable) via your CA’s CRL or OCSP.  

**Change, Control Note:**  
- **Requires approval** for certificate revocation in production environments.  

---

### **6. Post-Rotation Tasks**  
**Objective:** Finalize the rotation and document changes.  

**Steps:**  
1. **Archive Old Certificate:**  
   - Store the old certificate securely for audit purposes.  
2. **Update Documentation:**  
   - Update internal documentation with the new certificate details and rotation date.  
3. **Monitor for Issues:**  
   - Track device compliance reports for 7 days post-rotation.  

**Change-Control Note:**  
- **Requires approval** for final documentation and audit trails.  

---

### **7. Escalation Plan**  
- If devices fail to renew certificates:  
  - Recheck Intune profile settings.  
  - Contact the CA team for certificate issues.  
  - Escalate to IT security for audit/revocation concerns.  

---

**End of Runbook**  
*Note: Always test changes in a non-production environment before applying to production.*

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | runbook-cert-rotation | warm | run 1 | thinking: NO

**Tok/sec:** 37.3 &nbsp; **Wall sec:** 61.38 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 2283

**Response:**

**Runbook: Rotating an Expired SCEP Certificate Profile in Intune**  
**Objective:** Replace an expired SCEP certificate profile in Microsoft Intune, ensuring affected devices are updated, and verifying the new certificate is correctly applied.  

---

### **1. Preparation**  
**Steps:**  
- **Prerequisites:**  
  - Ensure the new SCEP certificate is issued and valid.  
  - Confirm access to the Certificate Authority (CA) for revoking the old certificate.  
  - Verify the new certificate meets organizational requirements (e.g., subject name, validity period).  
- **Change-Control Approval:**  
  - **Required:** Obtain approval for certificate rotation (e.g., via IT governance tools).  
  **Note:** This step is critical to ensure compliance with organizational policies and security protocols.  

---

### **2. Identify Affected Devices**  
**Steps:**  
1. **Access Intune Portal:**  
   - Navigate to **Devices > Device Compliance > Compliance Policies**.  
   - Locate the SCEP certificate profile and check compliance status.  
2. **Filter Non-Compliant Devices:**  
   - Use **Device Compliance** reports to identify devices with expired certificates.  
   - Filter by **Compliance Status** → **Non-Compliant** and **Certificate Expiry**.  
3. **Export Device List (Optional):**  
   - Use PowerShell or Intune API to export device identifiers (e.g., device IDs, device names).  

**Note:** If the certificate is not directly tied to compliance, manually check device logs or use third-party tools to identify devices with the old certificate.  

---

### **3. Update the SCEP Certificate Profile**  
**Steps:**  
1. **Create a New SCEP Certificate Profile:**  
   - In Intune, go to **Devices > Configuration Profiles > Profiles > SCEP Certificate Profile**.  
   - Configure the new profile with the updated certificate details (e.g., subject name, validity period).  
   - Ensure the **CA server** and **SCEP settings** match your infrastructure.  
2. **Disable/Archive the Old Profile:**  
   - Disable the old profile to prevent conflicts.  
   - Archive it for audit purposes.  
3. **Assign the New Profile:**  
   - Assign the new profile to the affected device groups.  
   - **Change-Control Approval:** Required for profile creation/update (e.g., via ticketing system).  

**Note:** If the old certificate was issued via a CA, ensure the new certificate is issued with the same CA to avoid enrollment failures.  

---

### **4. Force a Sync on Affected Devices**  
**Steps:**  
1. **Trigger Manual Sync (Device-Level):**  
   - For individual devices, use the **Intune MDM** command to force a sync:  
     - **Windows:** Use `PowerShell` to run `Invoke-IntuneDeviceSync`.  
     - **iOS/macOS:** Use the **MDM Push** command via Intune.  
2. **Bulk Sync via Intune:**  
   - Navigate to **Devices > All Devices** and select **Sync Now** for the affected devices.  
3. **Monitor Sync Status:**  
   - Check **Device Compliance** logs to confirm enrollment success.  

**Note:** Devices may take 5–15 minutes to sync after the profile update.  

---

### **5. Verify the New Certificate is Applied**  
**Steps:**  
1. **Check Device Compliance:**  
   - Confirm the devices are now **Compliant** in the **Compliance Policies** section.  
2. **Validate Certificate Installation:**  
   - **Windows:** Use `certmgr.msc` to verify the new certificate is installed.  
   - **iOS/macOS:** Check **Settings > General > About > Certificate Trust Settings**.  
3. **Check Certificate Expiry:**  
   - Ensure the new certificate’s validity period is correct.  
4. **Revoke Old Certificate (if applicable):**  
   - Use the CA’s **CRL (Certificate Revocation List)** or **Online Certificate Status Protocol (OCSP)** to revoke the old certificate.  
   - **Change-Control Approval:** Required for certificate revocation.  

---

### **6. Post-Rotation Steps**  
**Steps:**  
- **Monitor Logs:** Track any enrollment errors in Intune’s **Device Compliance** logs.  
- **Update Documentation:** Update internal records with the new certificate’s details and rotation date.  
- **Communicate:** Notify affected users or teams of the certificate update.  
- **Archive Old Profile:** Store the old profile securely for audit purposes.  

---

### **7. Rollback Plan (Optional)**  
- **If Issues Occur:**  
  - Re-enable the old SCEP profile and force a sync.  
  - Revoke the new certificate if necessary.  
  - **Note:** Rollback should be approved via change-control procedures.  

---

**Key Considerations:**  
- **Change-Control Approval:** Required for profile updates, certificate revocation, and any infrastructure changes.  
- **Communication:** Ensure stakeholders are informed of the rotation and potential disruptions.  
- **Testing:** Test the new certificate in a non-production environment before full rollout.  

**End of Runbook**

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | script-daily-health | cold | run 1 | thinking: NO

**Tok/sec:** 36.5 &nbsp; **Wall sec:** 112.52 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 4045

**Response:**

```bash
#!/bin/bash

# Service status check: Ollama
SERVICE_STATUS=$(systemctl is-active ollama 2>/dev/null)
if [ "$SERVICE_STATUS" == "active" ]; then
    echo "Service status: PASS"
else
    echo "Service status: FAIL"
fi

# Disk usage check
DISK_USAGE=$(df -h / | awk '{print $5}' | cut -d'%' -f1)
if [ "$DISK_USAGE" -gt 80 ]; then
    echo "Disk usage: WARN (Usage: $DISK_USAGE%)"
else
    echo "Disk usage: PASS (Usage: $DISK_USAGE%)"
fi

# Ollama API responsiveness
API_RESPONCE=$(curl --max-time 5 -s http://localhost:11434/api/version 2>/dev/null)
if echo "$API_RESPONCE" | grep -q '"model_name"'; then
    echo "Ollama API responsiveness: PASS"
else
    echo "Ollama API responsiveness: FAIL"
fi

# Docker container state check
DOCKER_CONTAINER=$(docker ps -f "name=open-webui" --format "{{.Status}}" 2>/dev/null)
if echo "$DOCKER_CONTAINER" | grep -q 'Up'; then
    echo "Docker container state: PASS"
else
    echo "Docker container state: FAIL"
fi
```

**Usage Instructions:**
1. Save the script as `health_check.sh`.
2. Make it executable: `chmod +x health_check.sh`.
3. Schedule it daily with cron:
   ```bash
   0 0 * * * /path/to/health_check.sh >> /path/to/health_check.log 2>&1
   ```
4. Adjust container names/services as needed for your environment.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | script-daily-health | warm | run 1 | thinking: NO

**Tok/sec:** 36.2 &nbsp; **Wall sec:** 129.48 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 4677

**Response:**

Here's a repeatable daily health-check script for your homelab running Ollama and Open WebUI on Ubuntu. Each check outputs a one-line `PASS/WARN/FAIL` summary:

```bash
#!/bin/bash

# Service status check (Ollama service)
if systemctl is-active --quiet ollama; then
    echo "PASS: Ollama service is active"
else
    echo "FAIL: Ollama service is not active"
fi

# Disk usage check (root filesystem)
disk_usage=$(df -h / | grep / | awk '{print $5}' | cut -d'%' -f1)
if [ "$disk_usage" -gt 90 ]; then
    echo "FAIL: Disk usage is $disk_usage%"
elif [ "$disk_usage" -gt 80 ]; then
    echo "WARN: Disk usage is $disk_usage%"
else
    echo "PASS: Disk usage is $disk_usage%"
fi

# Ollama API responsiveness check
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:11434/api/version)
if [ "$response" -eq 200 ]; then
    echo "PASS: Ollama API is responsive"
else
    echo "FAIL: Ollama API is not responsive"
fi

# Docker container state check (Open WebUI container)
if docker inspect --format='{{.State.Running}}' open-webui 2>/dev/null | grep -q 'true'; then
    echo "PASS: Open WebUI container is running"
else
    echo "FAIL: Open WebUI container is not running"
fi
```

---

### 🔍 **Explanation of Checks**
1. **Service Status (Ollama)**  
   - Checks if the `ollama` systemd service is active.  
   - `PASS` if running, `FAIL` if not.

2. **Disk Usage**  
   - Monitors root filesystem usage.  
   - `PASS` if <80%, `WARN` if 80–90%, `FAIL` if >90%.

3. **Ollama API Responsiveness**  
   - Sends a request to `http://localhost:11434/api/version`.  
   - `PASS` if HTTP 200, `FAIL` otherwise.

4. **Docker Container State (Open WebUI)**  
   - Verifies the `open-webui` container is running.  
   - `PASS` if active, `FAIL` if stopped or missing.

---

### 📌 **Usage**
1. Save the script to a file (e.g., `health_check.sh`).  
2. Make it executable:  
   ```bash
   chmod +x health_check.sh
   ```
3. Run manually or schedule with `cron` (e.g., daily at 2 AM):  
   ```bash
   0 2 * * * /path/to/health_check.sh >> /var/log/health_check.log 2>&1
   ```

This script ensures your homelab remains operational and provides actionable insights for troubleshooting.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | clf-intent | cold | run 1 | thinking: NO

**Tok/sec:** 38.9 &nbsp; **Wall sec:** 7.52 &nbsp; **Prompt tokens:** 101 &nbsp; **Output tokens:** 226

**Response:**

{"category": "group-membership", "confidence": 0.95, "reasoning": "The request explicitly asks to add a user to a specific named group."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | clf-intent | warm | run 1 | thinking: NO

**Tok/sec:** 38.5 &nbsp; **Wall sec:** 5.51 &nbsp; **Prompt tokens:** 101 &nbsp; **Output tokens:** 206

**Response:**

{"category": "group-membership", "confidence": 0.95, "reasoning": "The request involves adding a user to a specific group (SharePoint-Finance-RW), which directly relates to group membership management."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | clf-risk | cold | run 1 | thinking: NO

**Tok/sec:** 38.6 &nbsp; **Wall sec:** 10.23 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 330

**Response:**

{"risk": "HIGH", "revertable": true, "reasoning": "Disabling MFA temporarily compromises account security, increasing risk of unauthorized access during the period it's inactive."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | clf-risk | warm | run 1 | thinking: NO

**Tok/sec:** 38.4 &nbsp; **Wall sec:** 8.26 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 311

**Response:**

{"risk": "HIGH", "revertable": true, "reasoning": "Disabling MFA reduces account security and increases risk of unauthorized access during the testing period."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | clf-ambiguous | cold | run 1 | thinking: NO

**Tok/sec:** 38.9 &nbsp; **Wall sec:** 7.59 &nbsp; **Prompt tokens:** 100 &nbsp; **Output tokens:** 228

**Response:**

{"category": "needs-clarification", "confidence": 0.0, "reasoning": "The request lacks specific details about which user and group are involved.", "missing_info": ["user identifier", "group name"]}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | clf-ambiguous | warm | run 1 | thinking: NO

**Tok/sec:** 38.6 &nbsp; **Wall sec:** 5.12 &nbsp; **Prompt tokens:** 100 &nbsp; **Output tokens:** 191

**Response:**

{"category": "needs-clarification", "confidence": 0.0, "reasoning": "The request lacks specific details about which user and group are involved.", "missing_info": ["user name", "group name"]}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ga-deprecated-module | cold | run 1 | thinking: NO

**Tok/sec:** 36.3 &nbsp; **Wall sec:** 120.69 &nbsp; **Prompt tokens:** 85 &nbsp; **Output tokens:** 4325

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here's a PowerShell script that fulfills the requirements of finding and disabling Entra ID users who have not signed in for 60 days using only the **Microsoft.Graph** PowerShell module. It uses **OData filters** with the `Get-MgUser` cmdlet and properly sets the required **Graph API permissions**.

---

### ✅ **PowerShell Script**

```powershell
# Import the Microsoft Graph module
Import-Module Microsoft.Graph

# Connect to Microsoft Graph with required permissions
Connect-MgGraph -Scopes "User.Read.All", "User.ReadWrite.All"

# Calculate the date 60 days ago
$thresholdDate = [datetime]::Now.AddDays(-60)
$thresholdDateStr = $thresholdDate.ToString("yyyy-MM-ddTHH:mm:ssZ")

# Get enabled users who have not signed in for 60 days or have never signed in
$users = Get-MgUser -Filter "accountEnabled eq true and (lastSignInDateTime lt '$thresholdDateStr' or lastSignInDateTime eq null)" -Property id, accountEnabled, lastSignInDateTime

# Disable each user
foreach ($user in $users) {
    Write-Host "Disabling user: $($user.id)"
    Update-MgUser -UserId $user.id -BodyParameter @{ "accountEnabled" = $false }
}

Write-Host "Script completed."
```

---

### 📌 **Key Features**

- **Only Microsoft.Graph module** is used (no AzureAD or MSOnline).
- Uses **OData filtering** with `Get-MgUser` to efficiently find users.
- **Permissions** required:
  - `User.Read.All` – To read user properties.
  - `User.ReadWrite.All` – To update user properties (disable accounts).
- **Filters**:
  - `accountEnabled eq true` – Ensures only enabled users are considered.
  - `lastSignInDateTime lt '$thresholdDateStr'` – Users who haven't signed in in the last 60 days.
  - `lastSignInDateTime eq null` – Users who have never signed in.

---

### ⚠️ **Important Notes**

1. **Permissions**: Ensure the user or service principal has consented to the required permissions (`User.Read.All` and `User.ReadWrite.All`) in the Azure AD portal.
2. **Date Format**: The script uses the ISO 8601 format (`yyyy-MM-ddTHH:mm:ssZ`) for the date filter.
3. **Safety**: You may want to add a `-WhatIf` parameter to the `Update-MgUser` cmdlet for testing before disabling accounts.
4. **Error Handling**: Consider adding error handling or logging for production use.

---

### ✅ **Summary**

This script efficiently finds and disables Entra ID users who have not signed in for 60 days using the **Microsoft Graph API** and the **Microsoft.Graph PowerShell module**, adhering to the constraints of using only the Graph module and avoiding deprecated modules like AzureAD or MSOnline.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ga-deprecated-module | warm | run 1 | thinking: NO

**Tok/sec:** 36.5 &nbsp; **Wall sec:** 107.69 &nbsp; **Prompt tokens:** 85 &nbsp; **Output tokens:** 3922

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here's a PowerShell script that fulfills your requirements using the **Microsoft.Graph** module to find and disable Entra ID users who haven't signed in for 60 days. It adheres to the specified constraints and includes the required permissions and parameters.

---

### ✅ **PowerShell Script: Disable Inactive Entra ID Users**

```powershell
# Connect to Microsoft Graph with the required permissions
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Calculate the date 60 days ago in UTC
$date60DaysAgo = [System.DateTime]::UtcNow.AddDays(-60).ToString('yyyy-MM-ddTHH:mm:ssZ')

# Get all enabled users who have not signed in for 60 days
$users = Get-MgUser -Filter "accountEnabled eq true and lastSignInDate lt datetime'$date60DaysAgo'" -All -Property 'Id,DisplayName,LastSignInDate'

# Disable each user
foreach ($user in $users) {
    Write-Host "Disabling user: $($user.DisplayName) (ID: $($user.Id))" -ForegroundColor Yellow
    Update-MgUser -UserId $user.Id -AccountEnabled $false
}

Write-Host "Script completed. Disabled users who haven't signed in for 60 days." -ForegroundColor Green
```

---

### 🔐 **Permissions Required**

To make this script work, the following **Microsoft Graph permissions** must be granted:

- **`User.ReadWrite.All`**: Required for reading user properties (like `lastSignInDate`) and updating the `accountEnabled` status.

> ⚠️ **Note**: These permissions must be granted through an Azure AD application registration or by a user with admin privileges. The script will prompt for authentication and consent if not already granted.

---

### 🧠 **Key Points**

- **`-Filter`**: Uses OData syntax to filter enabled users with a `lastSignInDate` older than 60 days.
- **`-Property`**: Specifies the properties to retrieve (`Id`, `DisplayName`, and `LastSignInDate`) for efficiency.
- **UTC Time**: The script uses UTC for date calculations to match the Graph API's datetime format.
- **`-All`**: Ensures all users are retrieved, even across multiple pages.

---

### 📌 **Usage Instructions**

1. **Install the Microsoft Graph PowerShell module** (if not already installed):
   ```powershell
   Install-Module -Name Microsoft.Graph
   ```

2. **Run the script** in a PowerShell session with administrative privileges.

3. **Ensure** the user or service principal has the correct permissions (`User.ReadWrite.All`) in Azure AD.

---

### 📌 **Output Example**

```
Disabling user: John Doe (ID: 12345678-1234-1234-1234-123456789012)
Disabling user: Jane Smith (ID: 87654321-4321-4321-4321-012345678901)
Script completed. Disabled users who haven't signed in for 60 days.
```

---

### 🛡️ **Security & Compliance**

- This script is intended for **administrative use** and should be run in a secure environment.
- Ensure you **do not expose sensitive credentials** in scripts or logs.
- Always **test the script in a non-production environment** first.

Let me know if you'd like to add logging, pagination, or email notifications!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ga-param-names | cold | run 1 | thinking: NO

**Tok/sec:** 36.9 &nbsp; **Wall sec:** 87.12 &nbsp; **Prompt tokens:** 90 &nbsp; **Output tokens:** 3155

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
# Parameters for the script
param(
    [string]$GroupId,
    [string]$UserId
)

# Connect to Microsoft Graph
Connect-MgGraph -Scopes "GroupMember.ReadWrite.All", "User.ReadWrite.All"

# Attempt to add the user to the group
try {
    Write-Host "Adding user to group..."
    New-MgGroupMember -GroupId $GroupId -DirectoryObjectId $UserId
    Write-Host "User added to group successfully."
} catch {
    # Check if the error is due to the user already being a member
    if ($_.Exception.Response.StatusCode.Value__ -eq 400) {
        $errorContent = $_.Exception.Response.Content.ReadAsStringAsync().Result
        if ($errorContent -match "already a member") {
            Write-Host "User is already a member of the group."
        } else {
            Write-Error "An unexpected error occurred while adding the user: $_"
        }
    } else {
        Write-Error "An error occurred while adding the user: $_"
    }
    exit 1
}

# Verify the membership
Write-Host "Verifying membership..."
try {
    $members = Get-MgGroupMember -GroupId $GroupId
    $isMember = $members | Where-Object { $_.DirectoryObjectId -eq $UserId } | Select-Object -First 1

    if ($isMember) {
        Write-Host "Verification successful: User is a member of the group."
    } else {
        Write-Host "Verification failed: User is not a member of the group."
        exit 1
    }
} catch {
    Write-Error "Failed to verify membership: $_"
    exit 1
}

Write-Host "Script completed successfully."
```

---

### **Explanation:**

1. **Parameters:**
   - `$GroupId`: The unique ID of the group to which the user will be added.
   - `$UserId`: The `DirectoryObjectId` (same as `ObjectId`) of the user to add to the group.

2. **Authentication:**
   - Uses `Connect-MgGraph` to authenticate with Microsoft Graph, requesting the necessary scopes for group and user management.

3. **Adding the User:**
   - Uses `New-MgGroupMember` with `-GroupId` and `-DirectoryObjectId` to add the user to the group.
   - Catches a `400 Bad Request` error if the user is already a member and handles it gracefully.

4. **Verification:**
   - Retrieves the group's members using `Get-MgGroupMember` and checks if the user's `DirectoryObjectId` exists in the result.
   - If the user is not found, the script exits with an error code.

5. **Error Handling:**
   - Catches and logs specific Graph API errors, such as the user already being a member.
   - Ensures the script exits with appropriate status codes for automation or debugging.

This script ensures that the user is added to the group and verifies that the membership was successful, with robust error handling for common scenarios.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ga-param-names | warm | run 1 | thinking: NO

**Tok/sec:** 37.1 &nbsp; **Wall sec:** 76.42 &nbsp; **Prompt tokens:** 90 &nbsp; **Output tokens:** 2824

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
param(
    [string]$GroupId,
    [string]$DirectoryObjectId
)

# Connect to Microsoft Graph with required scopes
Connect-MgGraph -Scopes "Group.ReadWrite.All", "User.ReadWrite.All"

try {
    # Attempt to add the user to the group
    New-MgGroupMember -GroupId $GroupId -DirectoryObjectId $DirectoryObjectId
    Write-Host "User added to group. Verifying membership..."

    # Retrieve all members of the group to verify the user's membership
    $members = Get-MgGroupMember -GroupId $GroupId
    $memberExists = $members | Where-Object { $_.DirectoryObjectId -eq $DirectoryObjectId }

    if ($memberExists) {
        Write-Host "Verification successful. User is a member of the group."
    } else {
        Write-Host "Verification failed. User is not a member of the group."
    }
} catch {
    # Check for the specific error when the user is already a member
    if ($_.Exception.Response.StatusCode.Value__ -eq 400 -and 
        $_.Exception.Response.Content.ReadAsStringAsync().Result -match "already a member") {
        Write-Host "User is already a member of the group."
    } else {
        Write-Error "An error occurred: $_"
    }
}
```

---

### ✅ Key Features

- **Correct Parameter Usage**: Uses `-GroupId` and `-DirectoryObjectId` as required by `New-MgGroupMember`.
- **Error Handling**: Specifically catches the 400 error when the user is already a member of the group.
- **Verification**: Immediately checks if the user is a member of the group using `Get-MgGroupMember`.
- **Permissions**: Requires `Group.ReadWrite.All` and `User.ReadWrite.All` scopes for proper functionality.

---

### 📌 Notes

- The script assumes the user has already authenticated with Microsoft Graph and has the necessary permissions.
- If the user is already a member, the script will output a message and **not** attempt to add them again.
- The verification step ensures the operation was successful, even if there is a delay in the API response.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ga-pagination | cold | run 1 | thinking: NO

**Tok/sec:** 35.8 &nbsp; **Wall sec:** 157.20 &nbsp; **Prompt tokens:** 96 &nbsp; **Output tokens:** 5571

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
# Connect to Microsoft Graph
Connect-MgGraph -Scopes "DeviceManagementReadAll"

# Initialize variables
$allDevices = @()
$uri = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"

# Loop through pages
do {
    # Make the request
    $response = Invoke-MgGraphRequest -Uri $uri -Method Get
    # Add the devices from this page
    $allDevices += $response.value
    # Check if there's a nextLink
    $uri = $response.'@odata.nextLink'
} while ($uri)

# Output total device count
Write-Host "Total devices found: $($allDevices.Count)"

# Export to CSV
$allDevices | Export-Csv -Path "IntuneDevices.csv" -NoTypeInformation
```

### Explanation

1. **Authentication**:
   - The script starts by connecting to Microsoft Graph using `Connect-MgGraph` with the required scope `"DeviceManagementReadAll"`.

2. **Initialization**:
   - `$allDevices` is initialized as an empty array to collect all devices.
   - `$uri` is set to the Graph API endpoint for Intune-managed devices.

3. **Pagination Handling**:
   - A `do-while` loop is used to fetch all pages of results.
   - Each iteration makes a GET request to the current `$uri` using `Invoke-MgGraphRequest`.
   - The response includes a `value` array of devices and a `@odata.nextLink` for the next page.
   - Devices from the current page are added to `$allDevices`.
   - The loop continues until there is no more `@odata.nextLink`.

4. **Output and Export**:
   - The total number of devices is printed to the console.
   - All collected devices are exported to a CSV file named `IntuneDevices.csv`.

This script ensures that all Intune-managed devices are retrieved, handles pagination correctly, and provides a structured output for further analysis.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ga-pagination | warm | run 1 | thinking: NO

**Tok/sec:** 35.3 &nbsp; **Wall sec:** 195.99 &nbsp; **Prompt tokens:** 96 &nbsp; **Output tokens:** 6902

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here's a PowerShell script that retrieves **all Intune-managed devices** from a Microsoft 365 tenant using the **Microsoft Graph API**, while **correctly handling pagination** via the `@odata.nextLink` property. The script uses **manual pagination** via `Invoke-MgGraphRequest`, ensuring compatibility across different environments and versions of the Microsoft Graph PowerShell module.

---

### ✅ PowerShell Script: Intune Device Inventory with Pagination

```powershell
# Connect to Microsoft Graph
Connect-MgGraph -Scopes "DeviceManagementReadAll"

# Initialize variables
$allDevices = @()
$uri = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"

# Loop through pages until no more devices are returned
do {
    # Make a GET request to the Graph API
    $response = Invoke-MgGraphRequest -Uri $uri -Method GET

    # Extract the device list from the response
    $devices = $response.value

    # Add the current batch of devices to the collection
    $allDevices += $devices

    # Update the URI to the next page if available
    $uri = $response.'@odata.nextLink'
} while ($uri)

# Output the total number of devices
$totalDevices = $allDevices.Count
Write-Host "Total Intune Managed Devices: $totalDevices"

# Export devices to CSV
$allDevices | Export-Csv -Path "C:\IntuneDevices.csv" -NoTypeInformation -Encoding UTF8

Write-Host "Devices exported to C:\IntuneDevices.csv"
```

---

### 📌 Key Features

- **Authentication**: Uses `Connect-MgGraph` to authenticate with the Microsoft Graph API and request the `DeviceManagementReadAll` scope.
- **Pagination Handling**: Uses `@odata.nextLink` to fetch subsequent pages of results.
- **Export to CSV**: All devices are exported to a CSV file named `IntuneDevices.csv` in the `C:\` directory.
- **Robustness**: Handles large datasets by iterating through all pages of results.

---

### 📝 Notes

- **CSV Export**: The script exports all device properties. If you need to export only specific properties, you can filter the `$allDevices` array before exporting.
- **Permissions**: Ensure the user account has the appropriate **Azure AD permissions** (e.g., `DeviceManagementReadAll`) to access Intune-managed devices.
- **Location**: The CSV file is saved to `C:\`, but you can modify the path as needed.

---

### 🧠 Why Manual Pagination?

While `Get-MgDeviceManagementManagedDevice -All` can be used, it's **not guaranteed to be available** in all versions of the Microsoft Graph PowerShell module. Using `Invoke-MgGraphRequest` ensures **compatibility** and **explicit control** over the pagination process, which is especially important for environments with limited or outdated module versions.

---

### 🔁 Optional: Using `-All` Parameter (if supported)

If you're using a version of the module that supports the `-All` parameter, you can simplify the script as follows:

```powershell
Connect-MgGraph -Scopes "DeviceManagementReadAll"
$devices = Get-MgDeviceManagementManagedDevice -All
$total = $devices.Count
Write-Host "Total devices: $total"
$devices | Export-Csv -Path "C:\IntuneDevices.csv" -NoTypeInformation
```

This version is **more concise** but may **not work in all environments**. The manual approach is **more reliable and flexible**.

---

### ✅ Final Output

- **Total device count**: Printed to the console.
- **CSV file**: Contains all Intune-managed devices with their properties.

Let me know if you'd like to filter the exported CSV or add additional device properties!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ga-error-handling | cold | run 1 | thinking: NO

**Tok/sec:** 36.2 &nbsp; **Wall sec:** 131.30 &nbsp; **Prompt tokens:** 120 &nbsp; **Output tokens:** 4687

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
function Reset-MfaMethods {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory)]
        [string]$UserId
    )

    # Revert log entry
    Write-Verbose "Revert log entry: Attempting to remove MFA methods for user $UserId"

    try {
        # Attempt to retrieve user details
        $user = Get-MgUser -UserId $UserId
    } catch {
        $statusCode = $_.Exception.Response.StatusCode.Value__
        if ($statusCode -eq 404) {
            return [PSCustomObject]@{
                Success      = $false
                UserId       = $UserId
                MethodsRemoved = 0
                Error        = "User not found"
            }
        } elseif ($statusCode -eq 403) {
            return [PSCustomObject]@{
                Success      = $false
                UserId       = $UserId
                MethodsRemoved = 0
                Error        = "Insufficient permissions to access user"
            }
        } else {
            return [PSCustomObject]@{
                Success      = $false
                UserId       = $UserId
                MethodsRemoved = 0
                Error        = "Error retrieving user: $_"
            }
        }
    }

    try {
        # Retrieve all MFA methods for the user
        $methods = Get-MgUserAuthenticationMethod -UserId $UserId
    } catch {
        $statusCode = $_.Exception.Response.StatusCode.Value__
        if ($statusCode -eq 404) {
            return [PSCustomObject]@{
                Success      = $false
                UserId       = $UserId
                MethodsRemoved = 0
                Error        = "User not found"
            }
        } elseif ($statusCode -eq 403) {
            return [PSCustomObject]@{
                Success      = $false
                UserId       = $UserId
                MethodsRemoved = 0
                Error        = "Insufficient permissions to access authentication methods"
            }
        } else {
            return [PSCustomObject]@{
                Success      = $false
                UserId       = $UserId
                MethodsRemoved = 0
                Error        = "Error retrieving authentication methods: $_"
            }
        }
    }

    $methodsRemoved = 0
    $errorMessages = @()

    foreach ($method in $methods) {
        try {
            # Attempt to delete each MFA method
            Remove-MgUserAuthenticationMethod -UserId $UserId -AuthenticationMethodId $method.Id
            $methodsRemoved++
        } catch {
            $statusCode = $_.Exception.Response.StatusCode.Value__
            if ($statusCode -eq 403) {
                Write-Verbose "Insufficient permissions to delete authentication method $method.Id"
                $errorMessages += "Insufficient permissions to delete method: $method.Id"
            } elseif ($statusCode -eq 404) {
                Write-Verbose "Authentication method $method.Id not found"
                $errorMessages += "Method $method.Id not found"
            } else {
                Write-Verbose "Error deleting authentication method $method.Id: $_"
                $errorMessages += "Error deleting method $method.Id: $_"
            }
        }
    }

    # Return structured result object
    return [PSCustomObject]@{
        Success      = $true
        UserId       = $UserId
        MethodsRemoved = $methodsRemoved
        Error        = ($errorMessages -join "; ")
    }
}
```

---

### ✅ **Function Overview**

This PowerShell function, `Reset-MfaMethods`, safely removes all MFA authentication methods for a specified user using the Microsoft Graph API. It ensures:

- **Revert Log Entry**: A log entry is written before any destructive action.
- **Error Handling**: Specific handling for `404` (user not found) and `403` (insufficient permissions) at every API call.
- **Safe Deletion**: Each MFA method is deleted in a `try/catch` block, with errors logged but not terminating the process.
- **Return Object**: A structured object is returned with `Success`, `UserId`, `MethodsRemoved`, and `Error` properties.

---

### 📌 **Usage Example**

```powershell
Reset-MfaMethods -UserId "user@domain.com"
```

---

### 📌 **Return Object Structure**

| Property        | Description                                       |
|-----------------|---------------------------------------------------|
| **Success**     | `true` if all operations succeeded; `false` otherwise. |
| **UserId**      | The user ID for which MFA methods were removed.     |
| **MethodsRemoved** | Number of MFA methods successfully removed.        |
| **Error**       | A semicolon-separated list of errors encountered.   |

---

### 📌 **Notes**

- The function assumes the user has already authenticated and connected to Microsoft Graph.
- All output is directed through `Write-Verbose` for progress tracking.
- The function does **not** use `Write-Host` as requested.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ga-error-handling | warm | run 1 | thinking: NO

**Tok/sec:** 36.4 &nbsp; **Wall sec:** 114.23 &nbsp; **Prompt tokens:** 120 &nbsp; **Output tokens:** 4147

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
function Reset-MfaMethods {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    # Revert log entry written before any destructive action
    Write-Verbose "Reverting MFA methods for user $UserId"

    try {
        # Attempt to retrieve the user's authentication methods
        $authMethods = Get-MgUserAuthenticationMethod -UserId $UserId -ErrorAction Stop
    } catch {
        if ($_.Exception.Response.StatusCode -eq [System.Net.HttpStatusCode]::NotFound) {
            Write-Verbose "User $UserId not found."
            return [PSCustomObject]@{
                Success        = $false
                UserId         = $UserId
                MethodsRemoved = 0
                Error          = "User not found"
            }
        } elseif ($_.Exception.Response.StatusCode -eq [System.Net.HttpStatusCode]::Forbidden) {
            Write-Verbose "Insufficient permissions for user $UserId."
            return [PSCustomObject]@{
                Success        = $false
                UserId         = $UserId
                MethodsRemoved = 0
                Error          = "Insufficient permissions"
            }
        } else {
            Write-Verbose "An error occurred while retrieving authentication methods for user $UserId: $_"
            return [PSCustomObject]@{
                Success        = $false
                UserId         = $UserId
                MethodsRemoved = 0
                Error          = "Error retrieving authentication methods: $_"
            }
        }
    }

    $methodsRemoved = 0

    # Iterate through each authentication method and attempt deletion
    foreach ($method in $authMethods) {
        try {
            # Delete the authentication method
            Remove-MgUserAuthenticationMethod -UserId $UserId -AuthenticationMethodId $method.Id -ErrorAction Stop
            $methodsRemoved++
        } catch {
            if ($_.Exception.Response.StatusCode -eq [System.Net.HttpStatusCode]::Forbidden) {
                Write-Verbose "Insufficient permissions to delete authentication method for user $UserId."
                return [PSCustomObject]@{
                    Success        = $false
                    UserId         = $UserId
                    MethodsRemoved = $methodsRemoved
                    Error          = "Insufficient permissions to delete methods"
                }
            } else {
                Write-Verbose "Error deleting authentication method for user $UserId: $_"
                return [PSCustomObject]@{
                    Success        = $false
                    UserId         = $UserId
                    MethodsRemoved = $methodsRemoved
                    Error          = "Error deleting methods: $_"
                }
            }
        }
    }

    # Return success result if all methods were deleted
    return [PSCustomObject]@{
        Success        = $true
        UserId         = $UserId
        MethodsRemoved = $methodsRemoved
        Error          = ""
    }
}
```

---

### ✅ Key Features Implemented:

- **Revert Log Entry**: A `Write-Verbose` entry is logged before any destructive action is taken.
- **Graph API Integration**: Uses `Get-MgUserAuthenticationMethod` and `Remove-MgUserAuthenticationMethod` to interact with Microsoft Graph.
- **Error Handling**:
  - **404 (User Not Found)**: Returns an error message.
  - **403 (Insufficient Permissions)**: Returns an error message.
  - **Other Errors**: Returns a generic error message.
- **Return Object**: A structured `PSCustomObject` with properties `Success`, `UserId`, `MethodsRemoved`, and `Error`.
- **No Use of `Write-Host`**: All output is handled with `Write-Verbose` for progress and debugging.

---

### 📌 Notes:
- This function assumes that the user has already established a connection to Microsoft Graph using `Connect-MgGraph`. If not, the function will fail on the first API call.
- If any method deletion fails due to a `403` error, the function returns immediately, as it indicates the user lacks permissions to proceed.
- If a non-403 error occurs during deletion, it returns with the error message and the count of successfully removed methods.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ctx-short-ps | cold | run 1 | thinking: NO

**Tok/sec:** 37.9 &nbsp; **Wall sec:** 34.73 &nbsp; **Prompt tokens:** 25 &nbsp; **Output tokens:** 1255

**Response:**

Here's a concise PowerShell one-liner that lists all disabled Entra ID (formerly Azure AD) users, assuming the **AzureAD** module is installed and the user is authenticated:

```powershell
Get-AzureADUser -All | Where-Object { $_.AccountEnabled -eq $false } | Select-Object DisplayName, UserPrincipalName, Mail, AccountEnabled
```

---

### 🔍 Explanation:

- **`Get-AzureADUser -All`**: Retrieves all users from the directory (without pagination).
- **`Where-Object { $_.AccountEnabled -eq $false }`**: Filters only users who are **disabled** (i.e., `AccountEnabled` is `False`).
- **`Select-Object`**: Specifies the properties to display (you can customize these as needed).

---

### 📌 Notes:

- **Module Prerequisite**: The `AzureAD` module must be installed and imported. You can install it via:
  ```powershell
  Install-Module -Name AzureAD -Force
  ```
- **Authentication**: You must be logged into Azure AD via `Connect-AzureAD` before running this command.
- **Alternative**: If using the **Microsoft Graph** module, the command would be slightly different, but the `AzureAD` module is more straightforward for this specific task.

Let me know if you'd like to export the results to CSV or include additional properties!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:8b | ctx-short-ps | warm | run 1 | thinking: NO

**Tok/sec:** 37.6 &nbsp; **Wall sec:** 47.05 &nbsp; **Prompt tokens:** 25 &nbsp; **Output tokens:** 1762

**Response:**

Here is a PowerShell one-liner that lists all disabled Entra ID (formerly Azure AD) users, including their display names and user principal names:

```powershell
Import-Module AzureAD; Get-AzureADUser -All $true | Where-Object { $_.AccountEnabled -eq $false } | Select-Object DisplayName, UserPrincipalName
```

---

### 🔍 Explanation:

- **`Import-Module AzureAD`**: Ensures the Azure AD PowerShell module is loaded (required for the `Get-AzureADUser` command).
- **`Get-AzureADUser -All $true`**: Retrieves all users from the Azure AD directory. The `-All` parameter ensures all users are fetched, not just a subset.
- **`Where-Object { $_.AccountEnabled -eq $false }`**: Filters the result to include only users who are **disabled** (i.e., `AccountEnabled` is `False`).
- **`Select-Object DisplayName, UserPrincipalName`**: Limits the output to the display name and user principal name for clarity and brevity.

---

### ⚠️ Notes:
- This command assumes you're already authenticated to your Azure AD tenant. If not, you'll need to run `Connect-AzureAD` first.
- The `AzureAD` module is required, and it must be installed and imported.
- This script is intended for use in an environment with administrative access to the Azure AD tenant.

Let me know if you'd like to include additional properties or format the output differently!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | chat-explain | cold | run 1 | thinking: NO

**Tok/sec:** 22.5 &nbsp; **Wall sec:** 19.51 &nbsp; **Prompt tokens:** 41 &nbsp; **Output tokens:** 374

**Response:**

A homelab is a personal setup—using old hardware, virtual machines, or cloud tools—to experiment with IT systems safely. Think of it as your own "sandbox" for learning and testing. IT ops folks might use one to practice configuring servers, troubleshoot issues, or experiment with new tools without risking real workloads. It’s great for honing skills, testing disaster recovery plans, or even running a private cloud. Plus, it’s a way to stay sharp with emerging tech like Kubernetes or AI without needing company resources. No real stakes, just hands-on learning—perfect for growing your expertise and solving problems creatively.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | chat-explain | warm | run 1 | thinking: NO

**Tok/sec:** 22.7 &nbsp; **Wall sec:** 13.99 &nbsp; **Prompt tokens:** 41 &nbsp; **Output tokens:** 312

**Response:**

A homelab is like your own personal tech playground at home—basically, a setup of servers, networking gear, or virtual machines you use to experiment. For IT ops folks, it’s a safe space to test new tools, practice troubleshooting, or learn skills without messing up real systems. You can mess up, try new configs, or even simulate disasters and recover from them. It’s great for mastering cloud setups, automation, or security setups without risking your job. Plus, it’s cheaper than buying a bunch of gear for work. Think of it as a way to stay sharp, explore tech, and build confidence before diving into real-world chaos.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | chat-troubleshoot | cold | run 1 | thinking: NO

**Tok/sec:** 22.7 &nbsp; **Wall sec:** 33.32 &nbsp; **Prompt tokens:** 46 &nbsp; **Output tokens:** 688

**Response:**

Sure! Let's walk through this step by step, like we're troubleshooting together.  

**Step 1: Check if the internet is working at all**  
First, let’s make sure the laptop isn’t just having a general connectivity issue. Can you open a website (like Google or your company’s portal)? If the internet isn’t working at all, it might not be the VPN—it could be a problem with the network driver or a setting that got changed during the update.  

**Step 2: Restart the laptop**  
Sometimes, updates need a reboot to fully take effect. Let’s try restarting the laptop. After it boots back up, check if the VPN works. If it still doesn’t, we’ll move on to the next step.  

**Step 3: Check for driver updates or reinstall the network adapter**  
If the internet is working but the VPN still isn’t, the update might have caused a conflict with the network driver. Let’s go to **Settings > Update & Security > Windows Update** and click **Check for updates**. If there are updates available, install them and restart again. If that doesn’t help, we can try reinstalling the network adapter driver (but I’ll walk you through that if needed).  

Does that make sense? We’ll take it one step at a time! 😊

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | chat-troubleshoot | warm | run 1 | thinking: NO

**Tok/sec:** 22.7 &nbsp; **Wall sec:** 26.38 &nbsp; **Prompt tokens:** 46 &nbsp; **Output tokens:** 594

**Response:**

Sure! Let’s walk through this step by step like we’re talking over coffee.  

**Step 1: Check if the VPN client is still installed.**  
Have the user open the Start menu and search for theirVPN software (like "Cisco AnyConnect" or whatever they use). If it’s not there, the update might have uninstalled it or caused a conflict. If it’s missing, we’ll need to reinstall it from the company’s portal or the original installation file.  

**Step 2: Restart the laptop.**  
Sometimes updates require a reboot to apply properly. Even if the user did restart after the update, it’s worth doing it again. Let them shut the laptop down completely, wait 10 seconds, and power it back on. Then try theVPN again.  

**Step 3: Look for error messages.**  
When they try to connect to theVPN, do they see any pop-ups or messages? Even if it’s just a brief error, that can clue us in. For example, if it says "Connection failed" or "Firewall blocked," we’ll know where to look next. If there’s no message, maybe the issue is more subtle, like a driver or network setting.  

Does that make sense? We’ll tackle the next steps once we’ve ruled out these basics! ☕

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | chat-summarize | cold | run 1 | thinking: NO

**Tok/sec:** 22.9 &nbsp; **Wall sec:** 20.27 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 416

**Response:**

The certificate for the corporate VPN expired on June 1, 2026, causing a sharp rise in failed login attempts. Authentication failures increased from 2 to 340 per hour. A rollback of the certificate bundle is underway to resolve the issue.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | chat-summarize | warm | run 1 | thinking: NO

**Tok/sec:** 22.9 &nbsp; **Wall sec:** 11.33 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 254

**Response:**

A certificate for the corporate VPN expired on June 1, 2026, causing a sharp rise in authentication failures (from 2 to 340 per hour). A rollback of the certificate bundle is underway to resolve the issue and restore normal access. This affects user login reliability; the fix is in progress.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ps-graph-device-list | cold | run 1 | thinking: NO

**Tok/sec:** 21.0 &nbsp; **Wall sec:** 243.42 &nbsp; **Prompt tokens:** 65 &nbsp; **Output tokens:** 5068

**Response:**

```powershell
# Script to list Intune-managed Windows devices with last sync older than 7 days using Microsoft Graph

# Connect to Microsoft Graph with necessary permissions
Connect-MgGraph -Scopes "Device.Read.All"

# Calculate the date 7 days ago in UTC
$sevenDaysAgo = (Get-Date).AddDays(-7).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

# Retrieve Intune-managed Windows devices with last sync older than 7 days
$devices = Get-MgManagedDevice -Filter "deviceType eq 'windows' and lastSyncDateTime lt '$sevenDaysAgo'" -Select "deviceName,lastSyncDateTime,complianceState"

# Format and display the output with the required column names
$devices | Select-Object @{Name='DeviceName'; Expression={$_.deviceName}}, @{Name='LastSyncDateTime'; Expression={$_.lastSyncDateTime}}, @{Name='ComplianceState'; Expression={$_.complianceState}} | Format-Table -AutoSize
```

---

### **Explanation:**

- **Connect-MgGraph**: Establishes a session with Microsoft Graph using the required scope `Device.Read.All`, which is necessary to retrieve device information.
  
- **$sevenDaysAgo**: Calculates the date and time exactly 7 days ago using `AddDays(-7)` and converts it to UTC with `ToUniversalTime()`, then formats it as an ISO 8601 string for use in Graph filters.

- **Get-MgManagedDevice**: Retrieves managed devices from Intune. The filter:
  - `deviceType eq 'windows'` ensures only Windows devices are included.
  - `lastSyncDateTime lt '$sevenDaysAgo'` selects devices that have not synced in the last 7 days.
  - `-Select` specifies only the relevant properties: `deviceName`, `lastSyncDateTime`, and `complianceState`.

- **Select-Object**: Renames the properties to match the user's requested output names (`DeviceName`, `LastSyncDateTime`, `ComplianceState`) using calculated properties.

- **Format-Table -AutoSize**: Ensures the output is neatly formatted in a table with auto-adjusted column widths.

---

### **Requirements:**
- Install the [Microsoft Graph PowerShell SDK](https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation?view=graph-powershell-1.0).
- Ensure the user has the `Device.Read.All` permission in Azure AD.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ps-graph-device-list | warm | run 1 | thinking: NO

**Tok/sec:** 22.0 &nbsp; **Wall sec:** 110.96 &nbsp; **Prompt tokens:** 65 &nbsp; **Output tokens:** 2430

**Response:**

```powershell
# Script to list Intune-managed Windows devices with last sync older than 7 days using Microsoft Graph

# Connect to Microsoft Graph with the required scope
Connect-MgGraph -Scopes "Device.Read.All"

# Calculate the date 7 days ago in UTC
$sevenDaysAgo = (Get-Date).AddDays(-7).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')

# Fetch Intune-managed devices with last sync older than 7 days
$devices = Get-MgDeviceManagementManagedDevice -Filter "lastSyncDateTime lt '$sevenDaysAgo'" -Select deviceName, lastSyncDateTime, complianceState

# Output the results
$devices | ForEach-Object {
    [PSCustomObject]@{
        DeviceName       = $_.deviceName
        LastSyncDateTime = $_.lastSyncDateTime
        ComplianceState  = $_.complianceState
    }
} | Format-Table -AutoSize
```

---

### 🔍 **Explanation**

- **Authentication**: The script connects to Microsoft Graph with the `Device.Read.All` scope, which is necessary to read managed device information.
  
- **Date Calculation**: Uses `Get-Date` and `ToUniversalTime()` to ensure the date is in UTC format, matching the time format used by Microsoft Graph. The date is formatted using `'yyyy-MM-ddTHH:mm:ssZ'`, which is ISO 8601 compliant.

- **Filtering**: Uses the `-Filter` parameter to retrieve only those devices where `lastSyncDateTime` is older than 7 days.

- **Selecting Properties**: The `-Select` parameter is used to limit the returned data to `deviceName`, `lastSyncDateTime`, and `complianceState`, which are the required output fields.

- **Output Formatting**: Uses `Format-Table` to display the results in a clean, tabular format.

---

### ⚠️ **Notes**

- **Module Installation**: Ensure the `Microsoft.Graph` module is installed. If not, install it using:
  ```powershell
  Install-Module -Name Microsoft.Graph -Force
  ```

- **Authentication Prompt**: The first time this script is run, the user will be prompted to authenticate via the Microsoft login interface.

- **Pagination**: If the number of devices exceeds the page size limit (typically 100), additional logic may be needed to handle pagination. This script assumes a manageable number of results.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ps-graph-stale-users | cold | run 1 | thinking: NO

**Tok/sec:** 21.4 &nbsp; **Wall sec:** 183.99 &nbsp; **Prompt tokens:** 60 &nbsp; **Output tokens:** 3901

**Response:**

```powershell
# Connect to Microsoft Graph with the required scope
Connect-MgGraph -Scopes "User.Read.All"

# Calculate the cutoff date (90 days ago in UTC)
$cutoffDate = [DateTime]::UtcNow.AddDays(-90)
$filter = "accountEnabled eq true and (lastSignInDateTime le '$($cutoffDate.ToString("s"))' or lastSignInDateTime eq null)"

# Retrieve users matching the filter
$users = Get-MgUser -Filter $filter -All

# Prepare results array
$results = @()

# Process each user
foreach ($user in $users) {
    $results += [PSCustomObject]@{
        UPN                = $user.UserPrincipalName
        DisplayName        = $user.DisplayName
        LastSignInDateTime = $user.LastSignInDateTime
        AccountEnabled     = $user.AccountEnabled
    }
}

# Define output path
$outputPath = "C:\path\to\output.csv"

# Export results to CSV
$results | Export-Csv -Path $outputPath -NoTypeInformation

Write-Host "Results exported to $outputPath"
```

---

### ✅ **Explanation of Key Components**

- **Connect-MgGraph**: Authenticates the user with Microsoft Graph. It requires the `User.Read.All` scope to query user data.
- **Cutoff Date Calculation**: Uses `[DateTime]::UtcNow.AddDays(-90)` to get the date 90 days ago in UTC.
- **Filter Logic**: Uses OData query syntax to filter users who are enabled (`accountEnabled eq true`) and have not signed in for 90 days or have never signed in (`lastSignInDateTime le [date]` or `lastSignInDateTime eq null`).
- **Export to CSV**: The results are exported with the required fields: `UPN`, `DisplayName`, `LastSignInDateTime`, and `AccountEnabled`.

---

### 📌 **Notes**

- **Permissions**: Ensure the user running the script has the `User.Read.All` permission in Azure AD.
- **Module Installation**: If the `Microsoft.Graph` module is not installed, run `Install-Module Microsoft.Graph -Force` in an elevated PowerShell session.
- **Path Customization**: Replace `"C:\path\to\output.csv"` with the actual file path where you want to save the CSV output.

---

### 📊 **Output Example (CSV)**

```
"UPN","DisplayName","LastSignInDateTime","AccountEnabled"
"user1@example.com","John Doe","2023-07-01T12:34:56Z",true
"user2@example.com","Jane Smith",null,true
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ps-graph-stale-users | warm | run 1 | thinking: NO

**Tok/sec:** 21.5 &nbsp; **Wall sec:** 178.43 &nbsp; **Prompt tokens:** 60 &nbsp; **Output tokens:** 3822

**Response:**

```powershell
# Script to find Entra ID users who haven't signed in for 90 days and are still enabled, using Microsoft Graph

# Ensure the Microsoft Graph PowerShell SDK is installed
if (-not (Get-Module -ListAvailable -Name Microsoft.Graph)) {
    Write-Host "Installing Microsoft Graph PowerShell SDK..." -ForegroundColor Yellow
    Install-Module -Name Microsoft.Graph -Force -Scope CurrentUser
}

# Import the required module
Import-Module Microsoft.Graph

# Connect to Microsoft Graph with appropriate scope
Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
Connect-MgGraph -Scopes "User.Read.All"

# Calculate the date 90 days ago in UTC
$date90DaysAgo = (Get-Date).AddDays(-90).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

# Build the Graph filter query
$filter = "accountEnabled eq true and (lastSignInDateTime le '$date90DaysAgo' or lastSignInDateTime eq null)"

# Retrieve users matching the filter
Write-Host "Querying users who haven't signed in for 90 days..." -ForegroundColor Cyan
$users = Get-MgUser -Filter $filter -All

# Prepare results for export
$results = @()
foreach ($user in $users) {
    $results += [PSCustomObject]@{
        UPN                = $user.UserPrincipalName
        DisplayName        = $user.DisplayName
        LastSignInDateTime = $user.LastSignInDateTime
        AccountEnabled     = $user.AccountEnabled
    }
}

# Export results to CSV
$outputPath = "C:\path\to\output.csv"  # Update this path as needed
Write-Host "Exporting results to CSV: $outputPath" -ForegroundColor Cyan
$results | Export-Csv -Path $outputPath -NoTypeInformation

Write-Host "Script completed successfully." -ForegroundColor Green
```

---

### 🔍 **Explanation of Key Components**

- **Microsoft Graph SDK Installation:**  
  The script first checks if the Microsoft Graph PowerShell SDK is installed. If not, it installs it using `Install-Module`.

- **Authentication:**  
  It connects to Microsoft Graph using `Connect-MgGraph` with the `User.Read.All` scope, which is required to read user accounts.

- **Date Calculation:**  
  The script calculates the date 90 days ago using `AddDays(-90)` and converts it to **UTC** time with `ToUniversalTime()`. This is crucial because the `lastSignInDateTime` property is stored in **UTC**.

- **Graph Filter:**  
  The filter uses the Graph API's query language to:
  - Include only enabled users (`accountEnabled eq true`)
  - Include users who:
    - Haven't signed in in the last 90 days (`lastSignInDateTime le $date90DaysAgo`)
    - Or have never signed in at all (`lastSignInDateTime eq null`)

- **Pagination:**  
  The `-All` parameter ensures that all matching users are retrieved, even if the result spans multiple pages.

- **Exporting to CSV:**  
  Results are exported to a CSV file with the required columns: `UPN`, `DisplayName`, `LastSignInDateTime`, and `AccountEnabled`.

---

### 📌 **Notes**

- **Permissions:** Ensure the user running the script has **Global Administrator** or **User Administrator** permissions, or has been granted admin consent for the `User.Read.All` scope.
- **Path Customization:** Replace `"C:\path\to\output.csv"` with the actual file path you want to use for the CSV output.
- **Time Zone Consideration:** The script uses **UTC** to avoid time zone discrepancies.

---

### 📌 **Example CSV Output**

```csv
"UPN","DisplayName","LastSignInDateTime","AccountEnabled"
"john.doe@example.com","John Doe","2023-01-01T12:34:56Z",true
"jane.smith@example.com","Jane Smith",null,true
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ps-graph-app-assignment | cold | run 1 | thinking: NO

**Tok/sec:** 21.3 &nbsp; **Wall sec:** 206.75 &nbsp; **Prompt tokens:** 52 &nbsp; **Output tokens:** 4353

**Response:**

Here's a well-structured PowerShell function that uses the **Microsoft Graph PowerShell SDK** to retrieve the list of **groups** an **Intune app** is assigned to, along with the **assignment intent** (e.g., *required* or *available*). The function includes robust **error handling** for the case where the app is not found, and ensures the output is user-friendly and clean.

---

### ✅ **Function Overview**

- **Input**: A string representing the **display name** of the Intune app.
- **Output**: A list of **custom objects**, each containing:
  - `GroupName`: The name of the group the app is assigned to.
  - `Intent`: The assignment intent (e.g., `required` or `available`).
- **Error Handling**: 
  - Throws an error if the app is not found.
  - Catches and logs general exceptions during execution.

---

### 🔧 **PowerShell Function Code**

```powershell
function Get-IntuneAppGroups {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$DisplayName
    )

    try {
        # Step 1: Retrieve all Intune mobile apps with the given display name, expanding assignments
        $apps = Get-MgMobileApp -Filter "displayName eq '$DisplayName'" -Expand "assignments"

        # Step 2: Check if any app was found
        if ($apps.Count -eq 0) {
            throw "No Intune app found with the display name '$DisplayName'."
        }

        # Step 3: Process the first matching app (assuming one is intended)
        $app = $apps[0]
        $assignments = $app.Assignments

        # Step 4: Initialize result array
        $result = @()

        # Step 5: Iterate through each assignment
        foreach ($assignment in $assignments) {
            # Ensure the assignment has a valid group target
            if ($assignment.Target -and $assignment.Target.GroupId) {
                $groupId = $assignment.Target.GroupId

                # Step 6: Retrieve group name using Microsoft Graph
                try {
                    $group = Get-MgGroup -GroupId $groupId
                    $groupName = $group.DisplayName
                }
                catch {
                    Write-Warning "Failed to retrieve group name for group ID '$groupId': $_"
                    continue
                }

                # Step 7: Add to result
                $result += [PSCustomObject]@{
                    GroupName = $groupName
                    Intent    = $assignment.Intent
                }
            }
        }

        # Step 8: Return the results
        return $result
    }
    catch {
        Write-Error "An error occurred: $_"
        return $null
    }
}
```

---

### 📌 **Usage Example**

```powershell
# Connect to Microsoft Graph (ensure you're authenticated)
Connect-MgGraph -Scopes "DeviceManagementApps.Read.All", "Group.Read.All"

# Get groups assigned to an Intune app
$appGroups = Get-IntuneAppGroups -DisplayName "Contoso App"

# Output results
$appGroups | Format-Table GroupName, Intent
```

---

### 📝 **Notes**

- **Authentication**: Ensure you're connected to Microsoft Graph with the appropriate permissions:
  - `DeviceManagementApps.Read.All` (for Intune app data)
  - `Group.Read.All` (for retrieving group names)
- **Multiple Apps with Same Name**: This function currently returns the **first** app found with the given display name. You may want to enhance this for cases where multiple apps have the same name.
- **Error Handling**: If the group name cannot be retrieved (e.g., due to missing permissions or group deletion), the function logs a warning and continues.

---

This function is a robust and extensible tool for managing and auditing Intune app assignments in Microsoft 365 environments.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ps-graph-app-assignment | warm | run 1 | thinking: NO

**Tok/sec:** 21.8 &nbsp; **Wall sec:** 132.95 &nbsp; **Prompt tokens:** 52 &nbsp; **Output tokens:** 2890

**Response:**

Here's a well-documented PowerShell function that uses the Microsoft Graph API to retrieve the list of groups an Intune app is assigned to, along with the assignment intent (required or available). The function includes robust error handling, particularly for when the app is not found.

---

### ✅ **Function: Get-IntuneAppGroups**

```powershell
function Get-IntuneAppGroups {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true)]
        [string]$DisplayName
    )

    begin {
        # Ensure the user is connected to Microsoft Graph
        if (-not (Get-MgContext -ErrorAction SilentlyContinue)) {
            throw "You are not connected to Microsoft Graph. Please run 'Connect-MgGraph' first."
        }
    }

    process {
        try {
            # Query Microsoft Graph for the app by display name
            $url = "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps?$filter=displayName eq '$DisplayName'"
            $response = Invoke-MgGraphRequest -Method Get -Uri $url

            # Check if any apps were found
            if (-not $response.value) {
                throw "No app found with the display name '$DisplayName'."
            }

            # Handle multiple apps with the same display name
            if ($response.value.Count -gt 1) {
                Write-Warning "Multiple apps found with the display name '$DisplayName'. Using the first one."
            }

            # Extract the first app's ID
            $appId = $response.value[0].id

            # Query the assignments for the app
            $assignmentsUrl = "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps/$appId/assignments"
            $assignmentsResponse = Invoke-MgGraphRequest -Method Get -Uri $assignmentsUrl

            # Process each assignment
            $result = @()
            foreach ($assignment in $assignmentsResponse.value) {
                # Check if the assignment has a group target
                if ($assignment.target -and $assignment.target.group) {
                    $group = $assignment.target.group
                    $intent = $assignment.intent

                    $result += [PSCustomObject]@{
                        GroupId     = $group.id
                        GroupName   = $group.displayName
                        Intent      = $intent
                    }
                } else {
                    Write-Warning "Assignment does not have a valid group target."
                }
            }

            # Return the results
            return $result

        } catch {
            # Handle and re-throw any exceptions
            Write-Error "An error occurred: $($_.Exception.Message)"
            throw
        }
    }
}
```

---

### 📌 **Key Features**

- **Authentication**: Assumes the user is already connected via `Connect-MgGraph`. If not, the function throws an error.
- **Filtering by Display Name**: Uses the Microsoft Graph REST API to query for apps with a matching display name.
- **Handling Multiple Matches**: If multiple apps are found, a warning is issued and the first one is used.
- **Assignment Details**: Retrieves the group ID, group name, and assignment intent (`required` or `available`) for each assignment.
- **Error Handling**: Catches and re-throws any exceptions, including cases where the app is not found or the response is invalid.

---

### 🔍 **Example Usage**

```powershell
Connect-MgGraph -Scopes "DeviceManagementApps.Read.All"

# Get groups for an app named "Contoso App"
$appGroups = Get-IntuneAppGroups -DisplayName "Contoso App"

# Output the results
$appGroups | Format-Table -AutoSize
```

---

### 🛡️ **Permissions Required**

Ensure the user has the following Graph API permission:

- **Application Permission**: `DeviceManagementApps.Read.All`

---

### 📚 **Notes**

- This function assumes that the app assignments are made to groups. If other assignment types (e.g., users or devices) are used, they are ignored.
- It uses the `Invoke-MgGraphRequest` cmdlet from the Microsoft Graph PowerShell SDK. Make sure the SDK is installed with:

```powershell
Install-Module -Name Microsoft.Graph -Force
```

---

This function provides a reliable way to query Intune app assignments and is designed to be both robust and user-friendly.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | runbook-offboard | cold | run 1 | thinking: NO

**Tok/sec:** 22.3 &nbsp; **Wall sec:** 76.64 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 1664

**Response:**

### **Microsoft 365 / Intune Employee Offboarding Runbook**

| **Step** | **Action** | **Done** |
|----------|------------|----------|
| 1 | **Disable the User Account in Azure AD**<br> - Log in to the [Azure AD portal](https://portal.azure.com/).<br> - Navigate to **Azure Active Directory > Users > All Users**.<br> - Locate the user, select their account, and click **Disable**.<br> - Confirm the action to disable the account. | [ ] |
| 2 | **Revoke Active Sessions and Block Sign-In**<br> - In the Azure AD portal, go to **Security > Sign-ins**.<br> - Filter by the user’s account and revoke all active sessions.<br> - Apply a **Conditional Access policy** to block future sign-ins (e.g., "Block access for users with expired passwords" or "Block access for users outside of work hours"). | [ ] |
| 3 | **Remove Licenses and Groups**<br> - In Azure AD, go to **Users > All Users**.<br> - Select the user, click **Licenses**, and remove all assigned licenses.<br> - Remove the user from all **Azure AD groups**, **Microsoft 365 groups**, and **Teams**. | [ ] |
| 4 | **Wipe or Retire Devices in Intune**<br> - Log in to the [Microsoft Endpoint Manager admin center](https://endpoint.microsoft.com/).<br> - Go to **Devices > All devices**.<br> - Locate the user’s devices, select them, and click **Retire** (for company-owned devices) or **Wipe** (for company-owned or personal devices).<br> - Confirm the action to wipe or retire the device. | [ ] |
| 5 | **Archive the Mailbox in Exchange Online**<br> - Log in to the [Exchange admin center](https://admin.exchange.microsoft.com/).<br> - Navigate to **Recipients > Mailboxes**.<br> - Select the user’s mailbox, click **More options**, and choose **Archive mailbox** or **Move to retention policy** (if applicable).<br> - Confirm the mailbox is archived or moved to a retention plan. | [ ] |
| 6 | **Remove OneDrive for Business Content**<br> - Ensure the user’s OneDrive for Business site is either **archived** (via SharePoint admin center) or **deleted** (if no longer needed).<br> - Verify that all files have been transferred or retained as required. | [ ] |
| 7 | **Check for Pending Tasks or Approvals**<br> - Review any pending tasks, approvals, or workflows the user may have initiated.<br> - Transfer ownership of any shared resources (e.g., files, projects, or subscriptions). | [ ] |
| 8 | **Document and Communicate**<br> - Record the offboarding details in your HR or IT system.<br> - Notify the user (if applicable) and their manager of the offboarding completion.<br> - Retain logs or screenshots of completed actions for compliance. | [ ] |

---

### **Notes:**
- **Device Wiping:** For personal devices, ensure the user is informed about data loss and compliance requirements.
- **Mailbox Retention:** If the mailbox is not archived, ensure it is deleted after the retention period (per company policy).
- **Compliance:** Follow your organization’s data retention and privacy policies during the offboarding process.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | runbook-offboard | warm | run 1 | thinking: NO

**Tok/sec:** 22.4 &nbsp; **Wall sec:** 57.61 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 1287

**Response:**

### **Microsoft 365 / Intune Employee Offboarding Runbook**  
*(Use this checklist to ensure a secure and compliant offboarding process.)*  

| **Step** | **Action** | **Done** |
|----------|------------|----------|
| 1 | **Disable the user account** in Microsoft 365 Admin Center: <br> - Navigate to **Users > Active Users**. <br> - Select the user, click **Edit**, and set **Account Status** to **Disabled**. <br> - Remove the user from all groups (if necessary). | ☐ |
| 2 | **Revoke all active sessions** for the user: <br> - Use PowerShell: `Get-MsolUser -UserPrincipalName <user@domain.com> | Set-MsolUser -SessionLifetime 0` (forces immediate sign-out). <br> - Alternatively, use **Azure AD > Users > [User] > Revoke all sessions**. | ☐ |
| 3 | **Block sign-in** for the user: <br> - In **Azure AD > Users > [User] > Properties**, set **User account control** to **Blocked**. <br> - Confirm the user cannot access any Microsoft 365 services. | ☐ |
| 4 | **Wipe or retire the device(s)** in Microsoft Intune: <br> - Go to **Devices > All devices**, select the user’s device(s), and perform **Wipe device** (for company-owned devices) or **Retire device** (if the device is no longer used). <br> - Verify the device is removed from the inventory. | ☐ |
| 5 | **Archive the mailbox** (if required): <br> - In **Exchange Admin Center > Mailboxes**, select the user’s mailbox and apply an **archive retention policy** (e.g., move to archive or delete after 30 days). <br> - Ensure compliance with data retention policies. | ☐ |
| 6 | **Review and remove licenses** (if applicable): <br> - In **Microsoft 365 Admin Center > Users > [User] > Licenses**, remove any assigned licenses to prevent unnecessary costs. | ☐ |
| 7 | **Verify the user cannot access resources**: <br> - Attempt to log in to Microsoft 365, Intune, or Exchange with the user’s credentials. <br> - Confirm no access is granted. | ☐ |
| 8 | **Document the offboarding process** in your internal records: <br> - Note the date, actions taken, and any remaining tasks (e.g., pending device wipe). | ☐ |
| 9 | **Notify IT/HR teams** (if required): <br> - Share a summary of the offboarding steps and confirm completion. | ☐ |

---

**Notes:**  
- Replace `<user@domain.com>` with the actual user’s email address.  
- Ensure compliance with your organization’s data retention and privacy policies.  
- For hybrid environments, verify on-premises account disablement (if applicable).

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | runbook-cert-rotation | cold | run 1 | thinking: NO

**Tok/sec:** 22.2 &nbsp; **Wall sec:** 91.86 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 1991

**Response:**

# Runbook: Rotating an Expired SCEP Certificate Profile in Microsoft Intune

---

## **Purpose**  
Rotate an expired SCEP (Simple Certificate Enrollment Protocol) certificate profile in Microsoft Intune to ensure secure device enrollment and compliance. This runbook outlines steps to identify affected devices, update the profile, force a sync, and verify the change.

---

## **Scope**  
This runbook applies to environments using Intune for device management with SCEP certificate profiles. It assumes the certificate profile is expired and requires replacement with a new valid certificate.

---

## **Prerequisites**  
- Administrative access to the Microsoft 365 admin center and Intune.  
- Access to PowerShell (for advanced queries or automation).  
- A new SCEP certificate (issued by a trusted Certificate Authority, with updated details).  
- Change-control approval process in place (if required).  

---

## **Approval Requirements**  
- **Updating the SCEP certificate profile** and **removing the old profile** require **change-control approval** (e.g., from IT leadership or compliance teams).  
- **Communication with end-users** (e.g., informing them of potential disruptions during the update) may also require approval.  

---

## **Step-by-Step Procedure**  

### **Step 1: Identify Affected Devices**  
1. **Check Certificate Profile Status**:  
   - Navigate to **Microsoft 365 Admin Center > Devices > Configuration profiles > Certificates**.  
   - Locate the expired SCEP profile and review its **compliance status** and **device impact**.  

2. **Query Affected Devices**:  
   - Use **Intune Admin Center > Devices > All devices** to filter by:  
     - Devices with **"Certificate profile not compliant"** status.  
     - Devices reporting **SCEP enrollment errors** (check logs under **Reports > Device logs**).  
   - **Optional**: Use PowerShell to query devices:  
     ```powershell
     Get-IntuneDevice -Filter "deviceComplianceStatus eq 'NonCompliant'"
     ```  

---

### **Step 2: Prepare for Profile Update**  
1. **Backup the Old Profile**:  
   - Export the current SCEP profile configuration (e.g., for documentation or rollback).  

2. **Obtain New Certificate Details**:  
   - Ensure the new SCEP certificate includes:  
     - Valid CA URL (e.g., `https://new-ca-server/certsrv`).  
     - Correct subject name (e.g., `CN=Intune SCEP`).  
     - Expiry date (minimum 1 year).  

---

### **Step 3: Update the SCEP Certificate Profile**  
1. **Create a New SCEP Profile**:  
   - In **Intune Admin Center > Devices > Configuration profiles > Create profile**:  
     - Select **Certificate** > **SCEP**.  
     - Configure with the new CA URL, subject name, and other parameters.  
     - Assign the profile to the same **device groups** as the old profile.  

2. **Remove the Old Profile**:  
   - **Require change-control approval**.  
   - Navigate to **Intune Admin Center > Devices > Configuration profiles > [Expired Profile] > Delete**.  

---

### **Step 4: Force Sync on Affected Devices**  
1. **Trigger Policy Sync**:  
   - In **Intune Admin Center > Devices > All devices**:  
     - Select affected devices and use the **"Update device configuration"** action.  
   - **Alternative**: Use PowerShell to force sync:  
     ```powershell
     Update-IntuneDevice -DeviceId "device-id" -ForceSync $true
     ```  

2. **Notify Users (if required)**:  
   - Send a message to users via Microsoft Teams or email to prompt them to restart devices or re-enroll.  

---

### **Step 5: Verify the Update**  
1. **Check Profile Deployment**:  
   - Confirm the new SCEP profile is assigned and active in **Intune Admin Center**.  

2. **Validate Device Compliance**:  
   - In **Intune Admin Center > Reports > Device compliance**, ensure affected devices are now **compliant**.  

3. **Test Certificate Enrollment**:  
   - Use a test device to enroll with the new profile and verify certificate installation.  
   - Check logs for errors (e.g., **Reports > Device logs**).  

4. **Monitor for Issues**:  
   - Monitor **Intune Admin Center > Devices > All devices** for compliance status or errors over the next 24–48 hours.  

---

## **Post-Implementation**  
- **Document the change** in your organization’s change management system.  
- **Archive the old profile** configuration for audit purposes.  
- **Schedule a review** of SCEP certificate expiry dates (e.g., every 6 months).  

---

## **Notes**  
- **Change-control approval** is critical for profile deletion and replacement to avoid service disruptions.  
- If devices fail to sync, check the **new CA URL** and **firewall rules** allowing communication with the certificate authority.  
- For large-scale deployments, consider using **PowerShell or Graph API** for automation.  

--- 

**End of Runbook**  
Last Updated: [Insert Date]  
Author: [Your Name/Team]  
Contact: [Your Email/Support Channel]

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | runbook-cert-rotation | warm | run 1 | thinking: NO

**Tok/sec:** 22.0 &nbsp; **Wall sec:** 105.27 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 2312

**Response:**

# Runbook: Rotating an Expired SCEP Certificate Profile in Microsoft Intune

---

## **Overview**  
This runbook provides a step-by-step guide to rotate an expired SCEP (Simple Certificate Enrollment Protocol) certificate profile in Microsoft Intune. The process includes identifying affected devices, updating the profile, forcing a sync, and verifying the change. **Change-control approval is required for profile updates and certificate replacement**.

---

## **Prerequisites**  
1. **Access to Microsoft 365 Admin Center** and **Azure portal** (Intune).  
2. **Administrative privileges** in Intune (e.g., Global Administrator or Intune Administrator).  
3. **New SCEP certificate** (issued by a trusted Certificate Authority, with updated expiration date).  
4. **Change-control approval** (see Section 5).  
5. **PowerShell module** `Microsoft.Graph.DeviceManagement` (for advanced sync commands, if needed).  

---

## **Change-Control Requirements**  
- **Profile update**: Requires approval from the **IT Security or Compliance team** (see Step 3).  
- **Certificate replacement**: Requires approval from the **PKI (Public Key Infrastructure) team** (see Step 3).  

---

## **Step 1: Identify Affected Devices**  
**Objective**: Determine which devices are using the expired SCEP certificate profile.  

1. **Access Intune**:  
   - Go to [Azure Portal](https://portal.azure.com) > **Microsoft Entra ID** > **Device management** > **Configuration profiles**.  
   - Locate the expired SCEP certificate profile (check expiration date in the **Overview** tab).  

2. **Query Affected Devices**:  
   - Use **Intune Graph API** or **PowerShell** to list devices with the expired profile:  
     ```powershell  
     # Example PowerShell command (requires Graph API permissions)  
     Get-MgDeviceManagementDeviceConfigurationDeviceSummary -DeviceConfigurationId "PROFILE_ID"  
     ```  
   - Alternatively, filter devices in the **Intune Device Inventory** by compliance status or certificate expiration.  

3. **Document Affected Devices**:  
   - Export a list of affected devices (e.g., device names, groups, or serial numbers).  

---

## **Step 2: Update the SCEP Certificate Profile**  
**Objective**: Replace the expired SCEP certificate with a new one.  

1. **Obtain Change-Control Approval**:  
   - Submit a request to the **IT Security/Compliance team** for profile update approval.  
   - Submit a request to the **PKI team** for certificate replacement approval.  

2. **Create a New SCEP Profile**:  
   - In the **Azure portal**:  
     - Navigate to **Intune** > **Profiles** > **Create profile**.  
     - Select **Certificate** > **SCEP**.  
     - Configure the new profile with the updated certificate details (e.g., CA URL, subject name, expiration date).  
     - Assign the profile to the same device groups as the old profile.  

3. **Replace the Old Profile**:  
   - **Delete** the expired SCEP profile (only after confirming all devices have been updated).  
   - **Rename** the old profile to "Expired - [Profile Name]" for audit purposes.  

---

## **Step 3: Force a Sync for Affected Devices**  
**Objective**: Ensure devices retrieve the new certificate profile.  

1. **Use Intune Portal**:  
   - Navigate to **Intune** > **Devices** > **All devices**.  
   - Select affected devices > **Actions** > **Sync**.  

2. **Use PowerShell (Optional)**:  
   - Run the following command to force a sync for all devices:  
     ```powershell  
     Update-MgDeviceManagementDeviceConfigurationDeviceSummary -DeviceConfigurationId "NEW_PROFILE_ID"  
     ```  

3. **Note**: Forcing a sync may require **change-control approval** if it impacts a large number of devices or critical systems.  

---

## **Step 4: Verify the Rotation**  
**Objective**: Confirm that devices are using the new certificate.  

1. **Check Device Configuration**:  
   - Use **Intune Device Inventory** to verify the new profile is applied to all devices.  
   - Use **PowerShell** or **Graph API** to query device certificate status:  
     ```powershell  
     Get-MgDeviceManagementDeviceConfigurationDeviceSummary -DeviceConfigurationId "NEW_PROFILE_ID"  
     ```  

2. **Test Certificate Enrollment**:  
   - Enroll a **new device** using the updated profile to ensure the SCEP process works.  
   - Check the **device certificate store** (e.g., via remote desktop or device logs) for the new certificate.  

3. **Monitor Logs**:  
   - Review **Intune audit logs** (Azure portal > **Audit logs**) for errors during sync or enrollment.  

---

## **Post-Rotation Tasks**  
1. **Archive the Old Profile**:  
   - Rename and archive the expired profile for compliance and audit purposes.  

2. **Update Documentation**:  
   - Update internal documentation with the new certificate details and profile configuration.  

3. **Notify Stakeholders**:  
   - Inform the **IT Security**, **PKI**, and **end-users** teams of the change.  

---

## **Troubleshooting**  
- **Devices not syncing**:  
  - Check if the **device is compliant** or if **device management is enabled**.  
  - Verify the **network connectivity** to the SCEP server.  

- **Certificate enrollment failures**:  
  - Ensure the **new certificate** is properly configured in the SCEP profile.  
  - Check **CA server logs** for enrollment errors.  

- **Profile not applied**:  
  - Confirm the **device group assignments** are correct.  
  - Force a **device sync** again.  

---

## **Appendices**  
- **Change-Control Template**:  
  - Requestor: [Name]  
  - Action: Update SCEP certificate profile [PROFILE_NAME]  
  - Approval Required By: IT Security, PKI Team  
  - Estimated Downtime: [Timeframe]  

- **References**:  
  - [Intune SCEP Profile Configuration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/configure-scep-profiles)  
  - [Azure Graph API for Intune](https://learn.microsoft.com/en-us/graph/api/resources/intune-deviceconfig-resource-type?view=graph-rest-1.0)  

--- 

**End of Runbook**  
This document should be reviewed and updated annually or when certificate expiration dates change.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | script-daily-health | cold | run 1 | thinking: NO

**Tok/sec:** 20.6 &nbsp; **Wall sec:** 308.64 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 6308

**Response:**

```bash
#!/bin/bash

# Service status check for Ollama (assuming systemd service)
if systemctl is-active --quiet ollama 2>/dev/null; then
    echo "Service status: PASS"
else
    echo "Service status: FAIL"
fi

# Service status check for Open WebUI (assuming systemd service)
if systemctl is-active --quiet open-webui 2>/dev/null; then
    echo "Open WebUI service status: PASS"
else
    echo "Open WebUI service status: FAIL"
fi

# Disk usage check on root filesystem
disk_usage=$(df -h / | awk 'NR==2 {split($5, arr, "%"); usage=arr[1]; if (usage > 90) print "FAIL" else if (usage > 80) print "WARN" else print "PASS"}')
if [ -z "$disk_usage" ]; then
    echo "Disk usage: FAIL"
else
    echo "Disk usage: $disk_usage"
fi

# Ollama API responsiveness check
response_code=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:11434/api/tags 2>/dev/null)
if [ "$response_code" -eq 200 ]; then
    echo "Ollama API: PASS"
else
    echo "Ollama API: FAIL"
fi

# Docker container check for Ollama
if docker inspect --format='{{.State.Running}}' ollama 2>/dev/null | grep -q 'true'; then
    echo "Ollama container: PASS"
else
    echo "Ollama container: FAIL"
fi

# Docker container check for Open WebUI
if docker inspect --format='{{.State.Running}}' open-webui 2>/dev/null | grep -q 'true'; then
    echo "Open WebUI container: PASS"
else
    echo "Open WebUI container: FAIL"
fi
```

---

### ✅ **Usage Instructions**

1. **Save the Script**:  
   Save the above script as a file, e.g., `/usr/local/bin/health-check.sh`.

2. **Make It Executable**:  
   ```bash
   sudo chmod +x /usr/local/bin/health-check.sh
   ```

3. **Set Up a Daily Cron Job**:  
   Add the following line to your crontab (run `crontab -e`) to execute the script daily at 02:00 AM:
   ```bash
   0 2 * * * /usr/local/bin/health-check.sh > /var/log/health-check.log 2>&1
   ```

4. **Review Logs**:  
   Check the output in `/var/log/health-check.log` to review the daily health status.

---

### 📌 **Notes**
- **Service Names**: Ensure that `ollama` and `open-webui` are valid systemd service names on your system. If they're not, update the script accordingly.
- **Container Names**: Ensure that `ollama` and `open-webui` are the correct Docker container names. If not, adjust the script.
- **Disk Usage**: This script checks the root (`/`) filesystem. If your Docker data resides on a different partition, adjust the `df -h` command accordingly.
- **API Check**: The script assumes Ollama's API is running on `localhost:11434`. If it's on a different host or port, update the `curl` command.

---

### 📊 **Output Example**
```
Service status: PASS
Open WebUI service status: PASS
Disk usage: PASS
Ollama API: PASS
Ollama container: PASS
Open WebUI container: PASS
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | script-daily-health | warm | run 1 | thinking: NO

**Tok/sec:** 21.7 &nbsp; **Wall sec:** 151.45 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 3272

**Response:**

```bash
#!/bin/bash

# --- Configuration ---
OLLAMA_SERVICE="ollama"
OPENWEBUI_SERVICE="openwebui"
DISK_WARN_THRESHOLD=90
DISK_FAIL_THRESHOLD=100
OLLAMA_API_URL="http://localhost:11434/api/health"
OLLAMA_CONTAINER_NAME="ollama"
OPENWEBUI_CONTAINER_NAME="openwebui"

# --- Functions ---
check_service() {
    local service=$1
    if systemctl is-active --quiet "$service" 2>/dev/null; then
        echo "PASS - $service is running"
    else
        echo "FAIL - $service is not running"
    fi
}

check_disk_usage() {
    local threshold_warn=$1
    local threshold_fail=$2
    local usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ -z "$usage" ]; then
        echo "WARN - Could not determine disk usage"
        return
    fi
    if [ "$usage" -ge "$threshold_fail" ]; then
        echo "FAIL - Disk usage is $usage%"
    elif [ "$usage" -ge "$threshold_warn" ]; then
        echo "WARN - Disk usage is $usage%"
    else
        echo "PASS - Disk usage is $usage%"
    fi
}

check_ollama_api() {
    response=$(curl -s -o /dev/null -w "%{http_code}" "$OLLAMA_API_URL" 2>/dev/null)
    if [ "$response" -eq 200 ]; then
        echo "PASS - Ollama API is responsive"
    else
        echo "FAIL - Ollama API is not responsive (HTTP $response)"
    fi
}

check_docker_containers() {
    local ollama_status=$(docker inspect --format='{{.State.Running}}' "$OLLAMA_CONTAINER_NAME" 2>/dev/null | grep -q "true" && echo "running" || echo "not running")
    local openwebui_status=$(docker inspect --format='{{.State.Running}}' "$OPENWEBUI_CONTAINER_NAME" 2>/dev/null | grep -q "true" && echo "running" || echo "not running")

    if [ "$ollama_status" = "running" ] && [ "$openwebui_status" = "running" ]; then
        echo "PASS - Docker containers are running"
    else
        echo "FAIL - Docker containers are not running (Ollama: $ollama_status, Open WebUI: $openwebui_status)"
    fi
}

# --- Main ---
echo "Running health check..."

check_service "$OLLAMA_SERVICE"
check_service "$OPENWEBUI_SERVICE"
check_disk_usage "$DISK_WARN_THRESHOLD" "$DISK_FAIL_THRESHOLD"
check_ollama_api
check_docker_containers

echo "Health check completed."
```

---

### ✅ **Usage Instructions**

1. **Save the script** as `health_check.sh` and make it executable:
   ```bash
   chmod +x health_check.sh
   ```

2. **Run the script daily** using a cron job:
   ```bash
   crontab -e
   ```
   Add the following line to schedule it daily at 3:00 AM:
   ```bash
   0 3 * * * /path/to/health_check.sh >> /var/log/health_check.log 2>&1
   ```

3. **Review the log file** at `/var/log/health_check.log` for output.

---

### 📌 **Notes**

- **Service Names**: Modify `OLLAMA_SERVICE` and `OPENWEBUI_SERVICE` if your systemd service names differ.
- **Container Names**: Adjust `OLLAMA_CONTAINER_NAME` and `OPENWEBUI_CONTAINER_NAME` if your Docker container names are different.
- **API Endpoint**: If the Ollama API health endpoint differs, update `OLLAMA_API_URL`.

---

### 📊 **Output Format**

Each check outputs a single line with one of the following statuses:

- `PASS - [description]`
- `WARN - [description]`
- `FAIL - [description]`

Example:
```
PASS - ollama is running
FAIL - openwebui is not running
WARN - Disk usage is 85%
PASS - Ollama API is responsive
FAIL - Docker containers are not running (Ollama: not running, Open WebUI: not running)
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | clf-intent | cold | run 1 | thinking: NO

**Tok/sec:** 22.9 &nbsp; **Wall sec:** 15.03 &nbsp; **Prompt tokens:** 101 &nbsp; **Output tokens:** 292

**Response:**

{"category": "group-membership", "confidence": 0.95, "reasoning": "The request involves adding a user to a specific group, which falls under group-membership management."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | clf-intent | warm | run 1 | thinking: NO

**Tok/sec:** 22.9 &nbsp; **Wall sec:** 8.56 &nbsp; **Prompt tokens:** 101 &nbsp; **Output tokens:** 192

**Response:**

{"category": "group-membership", "confidence": 0.95, "reasoning": "The request involves adding a user to a specific group, which aligns with group-membership management."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | clf-risk | cold | run 1 | thinking: NO

**Tok/sec:** 22.9 &nbsp; **Wall sec:** 16.77 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 337

**Response:**

{"risk": "HIGH", "revertable": true, "reasoning": "Disabling MFA temporarily removes a critical security layer, increasing the risk of unauthorized access during the testing period."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | clf-risk | warm | run 1 | thinking: NO

**Tok/sec:** 22.8 &nbsp; **Wall sec:** 16.10 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 363

**Response:**

{"risk": "MEDIUM", "revertable": true, "reasoning": "Temporary MFA disablement increases account vulnerability during the window but can be re-enabled, posing moderate risk if exploited."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | clf-ambiguous | cold | run 1 | thinking: NO

**Tok/sec:** 22.9 &nbsp; **Wall sec:** 15.73 &nbsp; **Prompt tokens:** 100 &nbsp; **Output tokens:** 308

**Response:**

{"category": "needs-clarification", "confidence": 0.0, "reasoning": "The request lacks specific details about the user to be removed and the group they belong to.", "missing_info": ["User identifier", "Group name"]}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | clf-ambiguous | warm | run 1 | thinking: NO

**Tok/sec:** 22.9 &nbsp; **Wall sec:** 10.00 &nbsp; **Prompt tokens:** 100 &nbsp; **Output tokens:** 225

**Response:**

{"category": "needs-clarification", "confidence": 0.0, "reasoning": "The request does not specify which user or group is being referred to.", "missing_info": ["username", "group name"]}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ga-deprecated-module | cold | run 1 | thinking: NO

**Tok/sec:** 21.2 &nbsp; **Wall sec:** 209.04 &nbsp; **Prompt tokens:** 85 &nbsp; **Output tokens:** 4389

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
# Connect to Microsoft Graph with the required scope
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Calculate the date 60 days ago in UTC
$date60DaysAgo = (Get-Date).AddDays(-60).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ")

# Construct the filter to find enabled users who haven't signed in for 60 days or have never signed in
$filter = "accountEnabled eq true and (lastSignInDateTime le '$date60DaysAgo' or lastSignInDateTime eq null)"

# Retrieve the users with the required properties
$users = Get-MgUser -Filter $filter -Property "accountEnabled, lastSignInDateTime, userPrincipalName" -All $true

# Disable each user account
foreach ($user in $users) {
    Write-Host "Disabling user: $($user.UserPrincipalName)"
    Update-MgUser -UserId $user.Id -UserParameter @{accountEnabled = $false}
}
```

---

### ✅ **Description of the Script**

This PowerShell script uses the **Microsoft Graph PowerShell module** to perform the following actions:

1. **Connects to Microsoft Graph** with the required **`User.ReadWrite.All`** permission scope, which is necessary to **read and update user account statuses**.
2. **Calculates a date 60 days ago in UTC**, which is used in the filter to identify inactive users.
3. **Queries the Graph API** using `Get-MgUser` with a filter that:
   - Ensures the user is **enabled** (`accountEnabled eq true`).
   - Matches users whose **last sign-in date is older than 60 days** or who have **never signed in** (`lastSignInDateTime eq null`).
4. **Disables each user account** by calling `Update-MgUser` with the `accountEnabled` property set to **false**.

---

### 📌 **Permissions Required**

To run this script successfully, the user must have the following **Graph API permission**:

- **Scope:** `User.ReadWrite.All`  
  This scope allows the script to **read user information** and **disable user accounts**.

> 💡 **Note:** If the script is running under a **delegated permission**, the user must have **admin consent** for this scope.

---

### 📅 **Date Format Considerations**

- The `lastSignInDateTime` is stored in **UTC**, so the script calculates the 60-day threshold in **UTC** using `ToUniversalTime()`.
- The date is formatted as **ISO 8601** (`yyyy-MM-ddTHH:mm:ssZ`) to match the Graph API's expected date format.

---

### 🛠️ **Notes and Best Practices**

- **Pagination:** The `-All $true` parameter ensures that **all users** matching the filter are retrieved, even if the result set is large.
- **Logging:** This script outputs the **userPrincipalName** of each user being disabled using `Write-Host`. You may want to enhance this with logging to a file or console for audit purposes.
- **Testing:** Before disabling accounts, consider adding a **dry-run** or **confirmation prompt** to prevent unintended account disables.
- **Error Handling:** Consider wrapping the `Update-MgUser` call in a `try/catch` block to handle any API errors gracefully.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ga-deprecated-module | warm | run 1 | thinking: NO

**Tok/sec:** 21.4 &nbsp; **Wall sec:** 177.77 &nbsp; **Prompt tokens:** 85 &nbsp; **Output tokens:** 3803

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
# PowerShell Script to disable Entra ID users not signed in for 60 days using Microsoft Graph

# Ensure the Microsoft Graph module is installed
# Install-Module Microsoft.Graph -Force -Scope CurrentUser

# Connect to Microsoft Graph with the required permissions
Connect-MgGraph -Scopes "User.ReadWrite.All"

# Calculate the date 60 days ago in UTC
$date60DaysAgo = [DateTime]::UtcNow.AddDays(-60).ToString("yyyy-MM-ddTHH:mm:ssZ")

# Construct the filter to find enabled users who have not signed in for 60 days or have never signed in
$filter = "accountEnabled eq true and (lastSignInDateTime le '$date60DaysAgo' or lastSignInDateTime eq null)"

# Retrieve all users matching the filter, specifying necessary properties
$users = Get-MgUser -Filter $filter -Property "UserPrincipalName,accountEnabled,lastSignInDateTime" -All

# Disable each user found
foreach ($user in $users) {
    Write-Host "Disabling user: $($user.UserPrincipalName)"
    Update-MgUser -UserId $user.UserPrincipalName -AccountEnabled $false
}
```

---

### 🔐 **Required Graph Permissions**

- **Scope:** `User.ReadWrite.All`  
  - This scope is required to **read user data** and **disable user accounts** in Entra ID.

> ⚠️ **Admin Consent Required:** The `User.ReadWrite.All` scope must be granted by an administrator in the Azure AD tenant.

---

### 📌 **Notes**

- **UTC Time:** The script calculates the date 60 days ago using `[DateTime]::UtcNow` to ensure compatibility with the Graph API's expected UTC time format.
- **Pagination:** The `-All` parameter ensures all matching users are retrieved, even if they exceed the default page limit.
- **Filter Logic:** The filter includes users who have **never signed in** (`lastSignInDateTime eq null`) and those who haven't signed in for **60+ days** (`lastSignInDateTime le $date60DaysAgo`).
- **User Principal Name:** The script uses `UserPrincipalName` to uniquely identify and disable users via `Update-MgUser`.

---

### ⚠️ **Important**

- **Testing:** Before executing this script in production, **test it in a non-production environment** or use the `-WhatIf` parameter with `Update-MgUser` (if supported) to simulate the action without making changes.
- **Backup:** Consider exporting a list of users to be disabled before running the script for audit purposes.

---

### 🛠️ **Example Usage**

```powershell
# Run the script after connecting to Graph
.\DisableInactiveUsers.ps1
```

---

This script is designed to be efficient, secure, and compliant with Microsoft Graph best practices.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ga-param-names | cold | run 1 | thinking: NO

**Tok/sec:** 21.4 &nbsp; **Wall sec:** 186.41 &nbsp; **Prompt tokens:** 90 &nbsp; **Output tokens:** 3943

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
# Connect to Microsoft Graph with required scopes
Connect-MgGraph -Scopes "Group.ReadWrite.All", "User.Read.All"

# Define variables for the group ID and user's directory object ID
$groupId = "your-group-id-here"
$userDirectoryObjectId = "user-object-id-here"

try {
    # Add the user to the group
    New-MgGroupMember -GroupId $groupId -DirectoryObjectId $userDirectoryObjectId -ErrorAction Stop

    # Verify membership by checking the list of group members
    $members = Get-MgGroupMember -GroupId $groupId
    $isMember = $members | Where-Object { $_.Id -eq $userDirectoryObjectId }

    if ($isMember) {
        Write-Host "User added successfully and is a member of the group."
    } else {
        Write-Host "User added, but verification failed. User not found in group members."
    }
}
catch {
    # Extract the error message
    $errorMessage = $_.Exception.Message

    # Check for the specific error indicating the user is already a member
    if ($errorMessage -like "*Member with the specified ID already exists in the group*") {
        Write-Host "User is already a member of the group. No action taken."
    }
    else {
        Write-Host "An error occurred: $errorMessage"
    }
}
```

---

### 🔍 **Explanation**

- **Connect-MgGraph**: Establishes a connection to Microsoft Graph with the necessary permissions (`Group.ReadWrite.All` and `User.Read.All`) to add users to groups and verify memberships.
  
- **Variables**: `$groupId` and `$userDirectoryObjectId` are placeholders for the actual group and user object IDs. These should be replaced with real values when using the script.

- **Try Block**:
  - Uses `New-MgGroupMember` with the correct parameter names: `-GroupId` and `-DirectoryObjectId`.
  - Uses `-ErrorAction Stop` to ensure any error thrown by the cmdlet is caught by the `catch` block.

- **Verify Membership**:
  - After successfully adding the user, the script retrieves the group members using `Get-MgGroupMember`.
  - Filters the result to check if the user's object ID matches the one added.

- **Catch Block**:
  - Catches any exceptions thrown during the `New-MgGroupMember` operation.
  - Specifically checks for the Graph API error message: `"Member with the specified ID already exists in the group"`.
  - Outputs appropriate messages depending on whether the user is already a member or if a different error occurred.

---

### ✅ **Usage Notes**

- Ensure the **Microsoft Graph PowerShell SDK** is installed using:
  ```powershell
  Install-Module -Name Microsoft.Graph
  ```

- Replace the placeholder values for `$groupId` and `$userDirectoryObjectId` with actual values from your environment.

- The script assumes the user has the necessary permissions and has already authenticated via `Connect-MgGraph`.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ga-param-names | warm | run 1 | thinking: NO

**Tok/sec:** 21.8 &nbsp; **Wall sec:** 130.83 &nbsp; **Prompt tokens:** 90 &nbsp; **Output tokens:** 2843

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
# Connect to Microsoft Graph with the required scopes
Connect-MgGraph -Scopes "GroupMember.ReadWrite.All", "Group.Read.All"

# Define group and user identifiers
$groupId = "your-group-id-here"
$userDirectoryObjectId = "your-user-object-id-here"

# Attempt to add the user to the group
try {
    New-MgGroupMember -GroupId $groupId -DirectoryObjectId $userDirectoryObjectId
    Write-Host "User added to the group successfully."
} catch {
    # Check if the error is due to the user already being a member
    if ($_.Exception.Message -like "*already exists*") {
        Write-Host "User is already a member of the group. No action taken."
    } else {
        Write-Host "An error occurred while adding the user: $($_.Exception.Message)"
    }
}

# Verify the membership
try {
    $members = Get-MgGroupMember -GroupId $groupId
    $memberExists = $members | Where-Object { $_.Id -eq $userDirectoryObjectId }

    if ($memberExists) {
        Write-Host "Verification successful: User is a member of the group."
    } else {
        Write-Host "Verification failed: User is not a member of the group."
    }
} catch {
    Write-Host "An error occurred during verification: $($_.Exception.Message)"
}
```

---

### ✅ **Explanation of Key Components**

- **Authentication:**  
  `Connect-MgGraph` is used to authenticate with Microsoft Graph. The required scopes `GroupMember.ReadWrite.All` and `Group.Read.All` ensure the user has permissions to both add users to groups and read group members.

- **Adding a User to a Group:**  
  `New-MgGroupMember` is used with the correct parameters: `-GroupId` and `-DirectoryObjectId`. This ensures the user is added to the group.

- **Error Handling:**  
  A `try-catch` block is used to handle the specific Graph API error that occurs when the user is already a member of the group. The error message is checked for the phrase "*already exists*" to identify this scenario.

- **Verification:**  
  `Get-MgGroupMember` is used to retrieve the list of group members. The script filters the list to confirm the presence of the user by checking the `Id` property against the provided `userDirectoryObjectId`.

- **Robustness:**  
  Additional `try-catch` blocks are included for the verification step to handle any unexpected errors during the retrieval of group members.

---

### 📌 **Notes**

- **Permissions:** Ensure the user running the script has been granted the appropriate permissions in Azure AD.
- **Object IDs:** Replace the placeholder values (`your-group-id-here`, `your-user-object-id-here`) with actual Azure AD group and user object IDs.
- **Error Handling:** The script is designed to be resilient and informative, providing clear feedback for both success and failure scenarios.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3:14b | ga-pagination | cold | run 1 | thinking: NO

**Tok/sec:** 21.2 &nbsp; **Wall sec:** 213.75 &nbsp; **Prompt tokens:** 96 &nbsp; **Output tokens:** 4484

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct parameter names? (-GroupId and -DirectoryObjectId on New-MgGroupMember, NOT -MemberId or -UserId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

```powershell
# PowerShell Script to Retrieve All Intune-Managed Devices from Microsoft Graph

# --- Step 1: Connect to Microsoft Graph with Required Permissions ---
# Ensure the user is authenticated with the correct scope: DeviceManagement.Read.All
Connect-MgGraph -Scopes "DeviceManagement.Read.All"

# --- Step 2: Initialize Variables ---
$allDevices = @()
$uri = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"

# --- Step 3: Loop Through All Pages Until No More Results Are Found ---
do {
    # Make the API Request
    $response = Invoke-MgGraphRequest -Method GET -Uri $uri

    # Add the current page's devices to the list
    $allDevices += $response.value

    # Check for the next link
    $uri = $response.'@odata.nextLink'
} while ($uri -ne $null)

# --- Step 4: Output Total Device Count ---
$totalDevices = $allDevices.Count
Write-Output "Total Intune-managed devices: $totalDevices"

# --- Step 5: Export Devices to CSV File ---
$allDevices | Export-Csv -Path "IntuneDevices.csv" -NoTypeInformation

# --- Step 6: Output Completion Message ---
Write-Output "Intune-managed devices have been successfully exported to 'IntuneDevices.csv'."
```

---

### 📌 **Notes:**

- **Authentication**: The script uses `Connect-MgGraph` to authenticate the user. Ensure the user has been granted the `DeviceManagement.Read.All` permission in Azure AD.
- **Pagination Handling**: The script manually handles the `@odata.nextLink` property to iterate through all pages, ensuring all devices are retrieved even if they exceed the API's 1000 per page limit.
- **CSV Export**: The script exports the retrieved devices to a CSV file named `IntuneDevices.csv`, which can be opened in Excel or any CSV-compatible tool.
- **Error Handling**: For production use, consider adding error handling for API requests and authentication failures. This script assumes a successful connection and response from the Graph API.

---

### 📁 **Output:**
- **CSV File**: `IntuneDevices.csv` containing all device properties returned by the Graph API.
- **Console Output**: A message displaying the total number of devices and a confirmation that the export was completed.

---

This script ensures that all Intune-managed devices in the tenant are retrieved correctly, even when the dataset is large and requires pagination.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
