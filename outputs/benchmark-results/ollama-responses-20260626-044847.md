# Ollama Model Responses

Generated: 2026-06-26T04:48:47

Review each response below and score manually using the rubric:
| Dimension | Score 1-10 |
|---|---|
| Accuracy — facts, cmdlets, syntax correct? | |
| Completeness — fully answers the request? | |
| Format — clean and usable without editing? | |
| Hallucination risk — invented cmdlets or endpoints? | |
| Consistency — similar quality on repeat runs? | |

---

## gemma4:26b | chat-explain | cold | run 1 | thinking: NO

**Tok/sec:** 50.8 &nbsp; **Wall sec:** 48.03 &nbsp; **Prompt tokens:** 44 &nbsp; **Output tokens:** 717

**Response:**

Think of a homelab as your personal, high-tech playground. It’s a dedicated setup—ranging from an old laptop to a rack of enterprise servers—used to run services, host websites, or experiment with software.

For anyone in IT operations, it’s the ultimate "sandbox." In a professional setting, you can't exactly test a risky new configuration by breaking production. But in a homelab? You can. It’s where you safely break things to learn how they actually work. 

Whether you want to master Kubernetes, practice network segmentation, or automate deployments with Ansible, a homelab provides hands-on experience without the fear of an outage. It turns theoretical knowledge into practical muscle memory, making you much more confident and capable when handling real-world production environments.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | chat-explain | cold | run 2 | thinking: NO

**Tok/sec:** 49.7 &nbsp; **Wall sec:** 69.90 &nbsp; **Prompt tokens:** 44 &nbsp; **Output tokens:** 672

**Response:**

Think of a homelab as your own personal sandbox—a collection of servers, networking gear, and software running in your home that mimics an enterprise environment. It’s a dedicated space to play with tech without the fear of breaking anything at work.

For anyone in IT operations, it's an incredible learning tool. It provides a risk-free zone to experiment with new tools, test messy configurations, or practice automation like Terraform and Ansible. The best part? If you accidentally crash your entire network, there’s no 2 AM emergency call or angry boss—just a chance to troubleshoot and learn from the mistake. Ultimately, a homelab allows you to bridge the gap between theory and real-world expertise, building the confidence needed to manage complex production systems safely.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | chat-explain | cold | run 3 | thinking: NO

**Tok/sec:** 49.7 &nbsp; **Wall sec:** 80.02 &nbsp; **Prompt tokens:** 44 &nbsp; **Output tokens:** 735

**Response:**

Think of a homelab as your own private sandbox for technology. It’s a dedicated setup at home—using old PCs, tiny servers, or even Raspberry Pis—to run services like media servers, web hosting, or network tools.

For an IT professional, it’s the ultimate learning playground. In a production environment, you can't just "experiment" with a new Kubernetes cluster or mess with firewall rules; one mistake could cause a massive outage. A homelab lets you break things safely. It’s where you practice automation (like Ansible), test complex networking configurations, and master new tools before they ever touch company hardware.

Ultimately, it transforms theoretical knowledge into hands-on muscle memory. It is the most effective way to level up your skills and stay ahead of the curve without any real-world consequences.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | chat-troubleshoot | cold | run 1 | thinking: NO

**Tok/sec:** 48.4 &nbsp; **Wall sec:** 115.95 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 874

**Response:**

"Oh no, that is so frustrating! It feels like every time Windows updates, something else decides to stop working properly. Don't worry, though—we’ll figure this out. Let's try a few quick things to see if we can get you back online.

**First, let's just check the basics: are you actually able to get onto the internet otherwise?** Just try opening a random website, like Google or a news site, in your browser. I want to make sure your Wi-Fi is still talking to your router correctly before we dive into the VPN settings itself.

**Second, since this happened right after an update, let's try a 'brain reset.' Have you tried fully restarting your laptop yet?** Sometimes when Windows installs new files, it leaves some old processes hanging in the background, and a fresh restart is often all it takes to get everything synced up again. 

**Lastly, if you try to click 'Connect' and it fails, do you see any specific error message popping up on the screen?** Even if it looks like gibberish to you, if there’s an error code or a specific phrase like 'Authentication Failed' or 'Server Unreachable,' that tells me exactly which direction to look in—whether it's a password issue or a connection issue. 

Give those a quick try and let me know what happens!"

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | chat-troubleshoot | cold | run 2 | thinking: NO

**Tok/sec:** 48.0 &nbsp; **Wall sec:** 145.31 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 1056

**Response:**

"Oh man, I hate when that happens. Windows updates always seem to pick the most inconvenient times to break things! Don't worry, though, we’ll figure it out. Let’s try a few quick things first to see where the breakdown is happening.

**First, let’s check your basic internet connection.** Can you try opening a website—like Google or a news site—to see if your Wi-Fi is actually working? I just want to make sure the update didn't accidentally knock your laptop off the Wi-Fi entirely. If you can get to Google, then we know the internet is fine and it’s specifically just the VPN that's being grumpy.

**Second, even though it feels a bit cliché, have you done a full restart since the update finished?** Sometimes after an update, Windows is still 'cleaning up' some files in the background, and things like your VPN software might not be running quite right until the system has had a fresh start. If you haven’t restarted since the update completed, give that a shot and let me know if it changes anything.

**Lastly, when you try to click 'Connect,' does a specific error message pop up?** Does it say something like 'Invalid Credentials' or maybe 'Server Not Found'? If there’s any text or even a little error code on the screen, let me know exactly what it says. That tiny bit of info is like a clue for me—it tells me if the VPN is having trouble with your password or if it’s just struggling to find its way through the new update."

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | chat-troubleshoot | cold | run 3 | thinking: NO

**Tok/sec:** 48.7 &nbsp; **Wall sec:** 101.16 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 901

**Response:**

"Oh, I’m sorry to hear that—Windows updates always seem to happen at the most inconvenient times! Don't worry, we'll figure it out. Let’s try a few quick things first before we get into anything complicated.

**First, let’s just check your basic internet connection.** 

Can you try opening a regular website, like Google or a news site? I just want to make sure that your Wi-Fi is actually working and that the update didn't accidentally turn off your wireless adapter. If you can get to Google, then we know your internet is fine, and the issue is specifically just with the VPN app itself.

**Second, have you tried a full restart since the update finished?** 

I know it sounds cliché, but after a big Windows update, sometimes there are 'leftover' tasks running in the background that haven't quite settled yet. A fresh reboot can often kick the VPN service back into gear and tell the computer, 'Okay, everything is updated, now let's get back to work.' Give that a quick try if you haven't already.

**Third, when you try to click 'Connect,' does it give you a specific error message?** 

If it fails, does it say something like 'Invalid Password' or 'Server Not Found,' or does it just spin in a circle forever? If there's an error code or even just a specific sentence on the screen, let me know. That little bit of info is like a map for me—it tells me whether we need to look at your login details or if we need to fix the connection settings."

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | chat-summarize | cold | run 1 | thinking: NO

**Tok/sec:** 49.7 &nbsp; **Wall sec:** 114.48 &nbsp; **Prompt tokens:** 92 &nbsp; **Output tokens:** 1208

**Response:**

An expired security certificate on our corporate VPN has caused a significant spike in login failures, jumping from 2 to 340 per hour. This is likely preventing many employees from accessing the network. We are currently reverting the system to its previous working version to restore service as quickly as possible.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | chat-summarize | cold | run 2 | thinking: NO

**Tok/sec:** 49.3 &nbsp; **Wall sec:** 112.79 &nbsp; **Prompt tokens:** 92 &nbsp; **Output tokens:** 644

**Response:**

We are experiencing a major issue with the corporate VPN due to an expired security certificate. This has caused login failures to spike significantly, jumping from 2 to 340 per hour. To restore access as quickly as possible, we are currently reverting a recent update to the system. I will provide another update once service is stabilized.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | chat-summarize | cold | run 3 | thinking: NO

**Tok/sec:** 49.8 &nbsp; **Wall sec:** 98.88 &nbsp; **Prompt tokens:** 92 &nbsp; **Output tokens:** 744

**Response:**

A security certificate for our corporate VPN has expired, causing login failures to jump from just 2 per hour to 340 per hour. This is significantly impacting our employees' ability to connect to the network. We are currently reverting the system to its previous working state to restore access as quickly as possible.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ps-graph-device-list | cold | run 1 | thinking: NO

**Tok/sec:** 48.6 &nbsp; **Wall sec:** 140.98 &nbsp; **Prompt tokens:** 72 &nbsp; **Output tokens:** 1707

**Response:**

To achieve this efficiently, we need to calculate the date from 7 days ago in the **ISO 8601 format** (which Microsoft Graph requires) and then use an OData `$filter` expression. 

Using `-Filter` allows the Microsoft Graph server to do the heavy lifting, and `-Select` reduces the payload size by only downloading the necessary properties.

```powershell
# Requires Microsoft.Graph module
# Install-Module Microsoft.Graph -Scope CurrentUser

# 1. Connect to Microsoft Graph
# Required Scope: DeviceManagementManagedDevices.Read.All
Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"

# 2. Calculate the threshold date (7 days ago)
# Graph API requires ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ
$thresholdDate = (Get-Date).AddDays(-7).ToString("yyyy-MM-ddTHH:mm:ssZ")

Write-Host "Searching for Windows devices that haven't synced since: $thresholdDate" -ForegroundColor Cyan

# 3. Define the Filter and Select
# We filter by operatingSystem being 'Windows' AND lastSyncDateTime being less than or equal to our threshold
$filter = "operatingSystem eq 'Windows' and lastSyncDateTime le `$thresholdDate"
$select = "deviceName,lastSyncDateTime,complianceState"

try {
    # 4. Execute the query
    # We use -All to ensure we retrieve all matching records if there are many devices
    $staleDevices = Get-MgDeviceManagementManagedDevice -Filter $filter -Select $select -All

    if ($null -eq $staleDevices) {
        Write-Host "No stale Windows devices found." -ForegroundColor Green
    } else {
        # 5. Output the results
        $staleDevices | Select-Object @{Name="DeviceName"; Expression={$_.deviceName}}, 
                                      @{Name="LastSyncDateTime"; Expression={$_.lastSyncDateTime}}, 
                                      @{Name="ComplianceState"; Expression={$_.complianceState}} | 
                        Format-Table -AutoSize
        
        Write-Host "Found $($staleDevices.Count) stale devices." -ForegroundColor Yellow
    }
}
catch {
    Write-Error "An error occurred while querying Microsoft Graph: $_"
}
```

### Key Features of this Script:

1.  **Efficiency (Server-Side Filtering):** 
    *   The `-Filter` parameter uses an OData expression (`operatingSystem eq 'Windows' and lastSyncDateTime le ...`). This ensures that the Microsoft Graph server filters the data *before* it is sent over the internet to your computer, making the script significantly faster and lighter on bandwidth.
2.  **Minimal Payload (`-Select`):** 
    *   By using `-Select`, we instruct the API to only return the three specific properties requested. This prevents the "over-fetching" of hundreds of other device attributes (like serial numbers, manufacturer, etc.) that aren't needed for this report.
3.  **ISO 8601 Compliance:** 
    *   The script automatically converts the PowerShell `DateTime` object into the specific string format (`yyyy-MM-ddTHH:mm:ssZ`) that the Graph API expects for timestamp comparisons.
4.  **Scalability (`-All`):** 
    *   I included the `-All` parameter. By default, Graph API calls often return only the first 100-1000 results (pagination). Adding `-All` tells the SDK to automatically handle pagination tokens to fetch every single device that matches your criteria.

### Prerequisites:
*   **Module:** You must have the `Microsoft.Graph` module installed.
*   **Permissions:** When the login prompt appears, you must sign in with an account that has at least **Device Management Read** permissions (e.g., Intune Administrator or Global Reader).

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ps-graph-device-list | cold | run 2 | thinking: NO

**Tok/sec:** 46.4 &nbsp; **Wall sec:** 165.29 &nbsp; **Prompt tokens:** 72 &nbsp; **Output tokens:** 1533

**Response:**

To run this script, you will need the `Microsoft.Graph` PowerShell module installed and permissions to read Intune managed device data (`DeviceManagementManagedDevices.Read.All`).

Here is the complete script:

```powershell
# 1. Check if Microsoft.Graph module is installed
if (-not (Get-Module -ListAvailable Microsoft.Graph)) {
    Write-Error "The Microsoft.Graph module is required. Install it using: Install-Module Microsoft.Graph"
    return
}

# 2. Connect to Microsoft Graph
# We request the scope required to read managed devices
Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"

# 3. Calculate the threshold date (7 days ago)
# Microsoft Graph requires dates in ISO 8601 format (yyyy-MM-ddTHH:mm:ssZ)
$thresholdDate = (Get-Date).AddDays(-7).ToString("yyyy-MM-ddTHH:mm:ssZ")

Write-Host "Searching for Windows devices that haven't synced since: $thresholdDate" -ForegroundColor Cyan

# 4. Define the Filter and Select properties
# We filter by operatingSystem (Windows) AND lastSyncDateTime (less than our threshold)
$filter = "operatingSystem eq 'Windows' and lastSyncDateTime lt $thresholdDate"
$select = "deviceName,lastSyncDateTime,complianceState"

try {
    # 5. Execute the query
    # Get-MgDeviceManagementManagedDevice is the command for the managedDevices endpoint
    $staleDevices = Get-MgDeviceManagementManagedDevice -Filter $filter -Select $select -ErrorAction Stop

    if ($null -eq $staleDevices) {
        Write-Host "No Windows devices found matching the criteria." -ForegroundColor Yellow
    } else {
        # 6. Output the results
        $staleDevices | Select-Object `
            @{Name="DeviceName"; Expression={$_.DeviceName}}, 
            @{Name="LastSyncDateTime"; Expression={$_.LastSyncDateTime}}, 
            @{Name="ComplianceState"; Expression={$_.ComplianceState}} | 
        Format-Table -AutoSize
    }
}
catch {
    Write-Error "An error occurred while querying Microsoft Graph: $($_.Exception.Message)"
}

# Disconnect (Optional - uncomment if you want to close the session automatically)
# Disconnect-MgGraph
```

### How it works:

1.  **The Date Format:** Microsoft Graph's API is strict about date formats. We use `.ToString("yyyy-MM-ddTHH:mm:ssZ")` to ensure the date string is compatible with OData filtering.
2.  **The Filter (`-Filter`):** 
    *   Instead of downloading every device and then filtering in PowerShell (which is slow), we send the logic to the Microsoft Graph server. 
    *   `operatingSystem eq 'Windows'` ensures we don't get iOS or Android devices.
    *   `lastSyncDateTime lt $thresholdDate` tells the server to only send devices where the sync timestamp is *less than* (older than) our calculated date.
3.  **The Selection (`-Select`):** 
    *   We use `-Select` to limit the payload. This reduces network traffic and significantly improves performance by instructing Graph to only return the three specific properties we need.
4.  **The Output:** 
    *   I used a calculated property in `Select-Object` to ensure the table headers match exactly what you requested (`DeviceName`, `LastSyncDateTime`, `ComplianceState`), even if the underlying Graph object properties vary slightly in casing.

### Prerequisites:
Before running, ensure your environment is set up:
```powershell
# Install the module if you haven't already
Install-Module Microsoft.Graph -Scope CurrentUser
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ps-graph-device-list | cold | run 3 | thinking: NO

**Tok/sec:** 46.0 &nbsp; **Wall sec:** 188.47 &nbsp; **Prompt tokens:** 72 &nbsp; **Output tokens:** 1818

**Response:**

To run this script, you will need the `Microsoft.Graph` module installed and have at least **DeviceManagementManagedDevices.Read.All** permissions.

Here is the optimized PowerShell script.

```powershell
<#
.SYNOPSIS
    Lists Intune-managed Windows devices that haven't synced in the last 7 days.
    
.DESCRIPTION
    Uses Microsoft Graph to filter devices server-side for efficiency.
    Outputs: DeviceName, LastSyncDateTime, ComplianceState.
#>

# 1. Define the threshold (7 days ago)
$daysThreshold = 7
$thresholdDate = (Get-Date).AddDays(-$daysThreshold).ToString("yyyy-MM-ddTHH:mm:ssZ")

# 2. Connect to Microsoft Graph
# Required Scope: DeviceManagementManagedDevices.Read.All
Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"

try {
    Write-Host "Searching for Windows devices that haven't synced since $thresholdDate..." -ForegroundColor Cyan

    # 3. Execute the query
    # We use -Filter to perform the date comparison on the server side (OData filter)
    # We use -Property (which maps to $select) to only download necessary fields
    $devices = Get-MgDeviceManagementManagedDevice `
        -Filter "lastSyncDateTime lt $thresholdDate and operatingSystem eq 'Windows'" `
        -Property "deviceName", "lastSyncDateTime", "complianceState"

    # 4. Process Results
    if ($null -eq $devices) {
        Write-Host "No Windows devices found matching the criteria." -ForegroundColor Yellow
    }
    else {
        $results = $devices | Select-Object `
            @{Name="DeviceName"; Expression={$_.deviceName}}, 
            @{Name="LastSyncDateTime"; Expression={$_.lastSyncDateTime}}, 
            @{Name="ComplianceState"; Expression={$_.complianceState}}

        # Output to console
        $results | Format-Table -AutoSize

        # Optional: Export to CSV
        # $results | Export-Csv -Path "./OutdatedDevices.csv" -NoTypeInformation
        Write-Host "Search complete. Found $($results.Count) device(s)." -ForegroundColor Green
    }
}
catch {
    Write-Error "An error occurred: $($_.Exception.Message)"
}
finally {
    # Disconnect (Optional, uncomment if you want to close the session immediately)
    # Disconnect-MgGraph
}
```

### Key Technical Details:

1.  **Server-Side Filtering (`-Filter`)**: 
    *   Instead of downloading all devices and filtering them in PowerShell (which is slow), I used the OData `$filter` syntax directly in the Graph request. 
    *   `lastSyncDateTime lt $thresholdDate`: This tells Microsoft Graph to only send objects where the date is **L**ess **T**han our threshold.
    *   `operatingSystem eq 'Windows'`: Ensures we aren't looking at iOS, Android, or macOS devices.
2.  **Property Selection (`-Property`)**: 
    *   The `-Property` parameter in the `Microsoft.Graph` module translates to the `$select` statement in the Graph API. This reduces the network payload by instructing the server not to send large, unnecessary metadata properties for every device.
3.  **Date Formatting**: 
    *   Graph API requires dates in **ISO 8601** format (`yyyy-MM-ddTHH:mm:ssZ`). The script handles this conversion automatically using `.ToString("yyyy-MM-ddTHH:mm:ssZ")`.
4.  **Complexity Handling**:
    *   The script uses a `try/catch` block to handle potential API errors (like authentication failures or connectivity issues).

### Prerequisites for running:
If you haven't set up your environment yet, run these commands first:
```powershell
# Install the module
Install-Module Microsoft.Graph -Scope CurrentUser

# Set execution policy if necessary
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ps-graph-app-assignment | cold | run 1 | thinking: NO

**Tok/sec:** 45.3 &nbsp; **Wall sec:** 148.07 &nbsp; **Prompt tokens:** 58 &nbsp; **Output tokens:** 2262

**Response:**

To run this script, you will need the **Microsoft Graph PowerShell SDK** installed and an active connection to Microsoft Graph with at least `DeviceManagementApps.Read.All` and `Group.Read.All` permissions.

```powershell
function Get-IntuneAppAssignmentGroups {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, HelpMessage = "Enter the display name of the Intune App.")]
        [string]$AppName
    )

    process {
        try {
            Write-Verbose "Searching for application: $AppName"
            
            # 1. Find the mobile app by DisplayName using a filter
            # We use -Filter to let Graph do the heavy lifting instead of downloading all apps
            $filter = "displayName eq '$AppName'"
            $app = Get-MgDeviceAppManagementMobileApp -Filter $filter -ErrorAction Stop

            if (-not $app) {
                throw "Application with name '$AppName' was not found in Intune."
            }

            # 2. Check if there are any assignments
            if (-not $app.Assignments -or $app.Assignments.Count -eq 0) {
                Write-Warning "Application '$AppName' was found, but it has no assignments."
                return
            }

            $results = @()

            # 3. Iterate through the assignments
            foreach ($assignment in $app.Assignments) {
                # The assignment object contains 'Intent' (required/available) 
                # and 'Target' (which holds the groupId)
                $intent = $assignment.Intent
                
                # Intune assignments can target Users, Devices, or Groups.
                # We specifically look for GroupAssignmentTarget
                $targetType = $assignment.Target.AdditionalProperties["@odata.type"]

                if ($targetType -eq "#microsoft.graph.groupAssignmentTarget") {
                    $groupId = $assignment.Target.AdditionalProperties["groupId"]
                    
                    try {
                        # Fetch the group name using the ID found in the assignment
                        $group = Get-MgGroup -GroupId $groupId -ErrorAction Stop
                        
                        $results += [PSCustomObject]@{
                            AppName        = $app.DisplayName
                            GroupName      = $group.DisplayName
                            AssignmentType = $intent # 'required' or 'available'
                            GroupId        = $groupId
                        }
                    }
                    catch {
                        # Handle case where a group might have been deleted but the assignment remains
                        $results += [PSCustomObject]@{
                            AppName        = $app.DisplayName
                            GroupName      = "Unknown/Deleted Group ($groupId)"
                            AssignmentType = $intent
                            GroupId        = $groupId
                        }
                    }
                }
                else {
                    # This handles cases where the assignment is User-based or Device-based (not a group)
                    $results += [PSCustomObject]@{
                        AppName        = $app.DisplayName
                        GroupName      = "Non-Group Assignment ($targetType)"
                        AssignmentType = $intent
                        GroupId        = "N/A"
                    }
                }
            }

            return $results
        }
        catch [Microsoft.Graph.PowerShell.Models.MicrosoftGraphException] {
            Write-Error "A Graph API error occurred: $($_.Exception.Message)"
        }
        catch {
            Write-Error $_.Exception.Message
        }
    }
}

# --- Example Usage ---
# Connect-MgGraph -Scopes "DeviceManagementApps.Read.All", "Group.Read.All"
# Get-IntuneAppAssignmentGroups -AppName "Google Chrome" | Format-Table -AutoSize
```

### How it works:

1.  **The Filter**: Instead of using `Get-MgDeviceAppManagementMobileApp | Where-Object...`, which downloads every single app in your tenant (slow), I used the `-Filter` parameter. This performs the search on the Microsoft server side, making it significantly faster for large environments.
2.  **Error Handling**: 
    *   The `try/catch` block catches specific Graph API errors.
    *   It explicitly checks if `$app` is null and throws a custom "App not found" error.
    *   A nested `try/catch` is used when fetching the Group name. This is crucial because sometimes an assignment exists for a group that has since been deleted from Entra ID (orphaned assignments).
3.  **OData Type Checking**: In Microsoft Graph, assignments are polymorphic. The script checks `@odata.type` to ensure we are specifically looking at `#microsoft.graph.groupAssignmentTarget`. This prevents the script from crashing when it encounters "User" or "Device" assignments.
4.  **Output**: It returns a `PSCustomObject`, which allows you to pipe the results directly into `Format-Table`, `Export-Csv`, or `Out-GridView`.

### Prerequisites:
Before running, ensure you are authenticated:
```powershell
Connect-MgGraph -Scopes "DeviceManagementApps.Read.All", "Group.Read.All"
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ps-graph-app-assignment | cold | run 2 | thinking: NO

**Tok/sec:** 44.8 &nbsp; **Wall sec:** 128.84 &nbsp; **Prompt tokens:** 58 &nbsp; **Output tokens:** 2248

**Response:**

To run this function, you will need the **Microsoft.Graph** PowerShell module installed and must be connected with at least `DeviceManagementApps.Read.All` and `Group.Read.All` permissions.

Here is the complete function:

```powershell
function Get-IntuneAppGroupAssignments {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, HelpMessage = "Enter the display name of the Intune application.")]
        [string]$AppName
    )

    process {
        try {
            Write-Verbose "Searching for application: $AppName"
            
            # 1. Search for the mobile app by DisplayName using a filter
            # We use -Filter to ensure we are searching on the server side for efficiency
            $filter = "displayName eq '$AppName'"
            $app = Get-MgMobileApp -Filter $filter -ErrorAction Stop

            # 2. Check if the app was actually found
            if (-not $app) {
                throw "Application with name '$AppName' was not found in Intune."
            }

            # Handle case where multiple apps might have the same name (returns an array)
            $apps = @($app) 
            $results = @()

            foreach ($currentApp in $apps) {
                Write-Verbose "Processing app: $($currentApp.DisplayName) (ID: $($currentApp.Id))"

                # 3. Check if there are any assignments
                if (-not $currentApp.Assignments -or $currentApp.Assignments.Count -eq 0) {
                    Write-Warning "Application '$($currentApp.DisplayName)' has no assignments."
                    continue
                }

                foreach ($assignment in $currentApp.Assignments) {
                    # We are looking specifically for Group Assignments
                    # In Graph, the target type for a group is #microsoft.graph.groupAssignmentTarget
                    $targetType = $assignment.Target.AdditionalProperties['@odata.type']

                    if ($targetType -eq '#microsoft.graph.groupAssignmentTarget') {
                        $groupId = $assignment.Target.Id
                        
                        # 4. Retrieve Group Details (Name)
                        try {
                            $group = Get-MgGroup -GroupId $groupId -ErrorAction Stop
                            $groupName = $group.DisplayName
                        }
                        catch {
                            $groupName = "Unknown/Deleted Group ($groupId)"
                        }

                        # 5. Determine Intent (Required vs Available)
                        # The 'AssignmentMethod' property contains the intent
                        $intent = $assignment.AssignmentMethod

                        $results += [PSCustomObject]@{
                            DisplayName      = $currentApp.DisplayName
                            GroupName        = $groupName
                            GroupId          = $groupId
                            AssignmentIntent = $intent # Will return 'required' or 'available'
                        }
                    }
                }
            }

            if ($results.Count -eq 0) {
                Write-Host "No group assignments found for '$AppName'." -ForegroundColor Cyan
            }
            else {
                return $results
            }
        }
        catch [Microsoft.Graph.PowerShell.Models.MicrosoftGraphException] {
            Write-Error "Graph API Error: $($_.Exception.Message)"
        }
        catch {
            Write-Error $_.Exception.Message
        }
    }
}
```

### How to use it:

1.  **Connect to Microsoft Graph:**
    ```powershell
    Connect-MgGraph -Scopes "DeviceManagementApps.Read.All", "Group.Read.All"
    ```

2.  **Run the function:**
    ```powershell
    # Basic usage
    Get-IntuneAppGroupAssignments -AppName "Google Chrome"

    # To export to CSV
    Get-IntuneAppGroupAssignments -AppName "Microsoft Edge" | Export-Csv -Path "./AppAssignments.csv" -NoTypeInformation
    ```

### Key Features of this script:

*   **Efficient Filtering:** It uses the `-Filter` parameter in `Get-MgMobileApp`. This is much faster than downloading every app in your tenant and filtering locally with `Where-Object`.
*   **Error Handling:** 
    *   It specifically catches "App not found" and throws a clear, user-friendly error.
    *   It includes a `try-catch` block for the Group lookup, so if a group has been deleted from Entra ID but still exists in an Intune assignment, the script won't crash; it will simply label it as "Unknown/Deleted".
*   **Intent Detection:** It extracts the `AssignmentMethod` property, which is the standard Graph API way to distinguish between **Required** and **Available** (also known as "Available for enrolled devices").
*   **Object-Oriented Output:** Returns a `PSCustomObject`, making it easy to pipe to `Format-Table`, `Export-Csv`, or `Out-GridView`.
*   **Multi-App Support:** If you have two apps with the exact same name (rare, but possible), the script iterates through both rather than just picking the first one.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ps-graph-app-assignment | cold | run 3 | thinking: NO

**Tok/sec:** 44.9 &nbsp; **Wall sec:** 139.37 &nbsp; **Prompt tokens:** 58 &nbsp; **Output tokens:** 2276

**Response:**

To run this script, you will need the `Microsoft.Graph` PowerShell module installed and appropriate permissions (`DeviceManagementApps.Read.All` and `Group.Read.All`).

Here is the professional-grade function to achieve this.

```powershell
function Get-IntuneAppAssignmentDetails {
    <#
    .SYNOPSIS
        Retrieves a list of Azure AD Groups assigned to a specific Intune App and their assignment intent.

    .PARAMETER AppDisplayName
        The exact display name of the Intune application.

    .EXAMPLE
        Get-IntuneAppAssignmentDetails -AppDisplayName "Google Chrome"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, HelpMessage = "Enter the exact Display Name of the Intune App")]
        [string]$AppDisplayName
    )

    process {
        try {
            Write-Progress -Activity "Searching for App" -Status "Looking for: $AppDisplayName"
            
            # 1. Search for the application by DisplayName using a filter
            # We use -Filter to perform the search server-side for efficiency
            $app = Get-MgDeviceAppManagementMobileApp -Filter "displayName eq '$AppDisplayName'" -ErrorAction Stop

            if (-not $app) {
                throw "Application with name '$AppDisplayName' was not found in Intune."
            }

            # 2. Retrieve the assignments for the found app
            Write-Progress -Activity "Retrieving Assignments" -Status "Fetching assignment details..."
            $assignments = Get-MgDeviceAppManagementMobileAppAssignment -MobileAppId $app.Id -ErrorAction Stop

            if (-not $assignments) {
                Write-Warning "App '$AppDisplayName' found, but no assignments exist."
                return
            }

            $results = New-Object System.Collections.Generic.List[PSCustomObject]

            foreach ($assignment in $assignments) {
                # The 'Intent' property tells us if it is 'required' or 'available'
                $intent = $assignment.Intent 
                
                # In Graph, the target for group assignments is stored in the Target property
                # We need to extract the groupId from the AdditionalProperties
                $targetId = $assignment.Target.AdditionalProperties['groupId']

                if ($targetId) {
                    try {
                        $group = Get-MgGroup -GroupId $targetId -ErrorAction Stop
                        $groupName = $group.DisplayName
                    }
                    catch {
                        $groupName = "Unknown Group (ID: $targetId)"
                    }
                }
                else {
                    # Handle 'All Users' or 'All Devices' assignments where no specific GroupID is present
                    $groupName = "All Users/Devices"
                }

                # Create a custom object for the output
                $results.Add([PSCustomObject]@{
                    AppName          = $app.DisplayName
                    AssignmentIntent = $intent
                    GroupName        = $groupName
                    GroupId          = if ($targetId) { $targetId } else { "N/A" }
                })
            }

            return $results | Sort-Object AssignmentIntent

        }
        catch [Microsoft.Graph.GraphException] {
            Write-Error "A Microsoft Graph error occurred: $($_.Exception.Message)"
        }
        catch {
            Write-Error "An unexpected error occurred: $($_.Exception.Message)"
        }
        finally {
            Write-Progress -Activity "Searching for App" -Completed
        }
    }
}
```

### How to use it:

1.  **Connect to Graph:**
    Before running the function, ensure you are authenticated with the correct scopes.
    ```powershell
    Connect-MgGraph -Scopes "DeviceManagementApps.Read.All", "Group.Read.All"
    ```

2.  **Run the Function:**
    ```powershell
    # Example 1: Successful lookup
    $report = Get-IntuneAppAssignmentDetails -AppDisplayName "Microsoft Edge"
    $report | Format-Table -AutoSize

    # Example 2: Non-existent app (will trigger error handling)
    Get-IntuneAppAssignmentDetails -AppDisplayName "NonExistentApp123"
    ```

### Key Features of this Script:
*   **Server-Side Filtering:** It uses `-Filter "displayName eq '...'"` instead of downloading all apps and filtering locally. This is significantly faster in large environments.
*   **Error Handling:** 
    *   It specifically catches `GraphException` for API-related issues (like connectivity or permissions).
    *   It provides a custom error message if the app name does not match anything in your tenant.
    *   It handles "Unknown Groups" gracefully (in case a group was deleted but the assignment remains).
*   **Assignment Intent:** It explicitly extracts the `Intent` property, which distinguishes between **Required** and **Available** (Company Portal) assignments.
*   **All Users/Devices Handling:** If an app is assigned to "All Users," there is no `groupId`. The script detects this and labels it appropriately rather than crashing.
*   **User Experience:** Uses `Write-Progress` so the user knows the script is working during large lookups.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | runbook-offboard | cold | run 1 | thinking: NO

**Tok/sec:** 45.9 &nbsp; **Wall sec:** 143.22 &nbsp; **Prompt tokens:** 72 &nbsp; **Output tokens:** 1707

**Response:**

# Runbook: Employee Offboarding (Microsoft 365 & Intune)

**Purpose:** To ensure a secure, consistent, and auditable process for removing access and reclaiming assets when an employee leaves the organization.
**Scope:** Microsoft 365 Admin Center, Microsoft Entra ID (formerly Azure AD), and Microsoft Intune.
**Role Required:** Global Administrator or Privileged Role Administrator.

---

### Pre-Offboarding Checklist
* [ ] Confirm the exact termination time/date with HR.
* [ ] Identify if the mailbox needs to be converted to a Shared Mailbox.
* [ ] Determine if the user’s manager requires access to OneDrive files.
* [ ] Determine if the device is **Corporate-Owned** (Wipe) or **BYOD** (Retire).

---

### Offboarding Execution Steps

| Step # | Category | Action Name | Detailed Instructions | Done |
| :--- | :--- | :--- | :--- | :---: |
| **1** | **Identity** | **Block Sign-in** | Navigate to **Microsoft Entra ID** > Users > Select User. Under "Account," set **Block sign-in** to **Yes**. This prevents new authentication attempts. | [ ] |
| **2** | **Security** | **Revoke Refresh Tokens** | In the same Entra ID user profile, select **Revoke Sessions**. This kills all existing active sessions (Outlook mobile, browser tabs, etc.) immediately. | [/] |
| **3** | **Identity** | **Reset Password** | Change the user's password to a random, complex string. This serves as an extra layer of security in case "Block Sign-in" fails due to configuration errors. | [ ] |
| **4** | **Mailbox** | **Convert to Shared Mailbox** | Go to **M365 Admin Center** > Users > Active Users > Select User. Under the **Mail** tab, select **Convert to shared mailbox**. This allows you to keep the data without paying for a license. | [ ] |
| **5** | **Mailbox** | **Assign Permissions** | Add the user's Manager or a Delegate to the "Full Access" and "Send As" permissions of the newly created Shared Mailbox. | [ ] |
| **6** | **Data** | **OneDrive Delegation** | In M365 Admin Center, go to the user's profile > **OneDrive** tab. Select **Create link to files**. Grant the manager access to ensure company data is not lost. | [ ] |
| **7** | **Licensing**| **Remove Licenses** | Once the mailbox is converted and OneDrive is secured, navigate to **Licenses and Apps** in the user profile. Uncheck all M365 licenses (E3, E5, Business Premium, etc.) to reclaim them for new hires. | [ ] |
| **8** | **Intune** | **Device Management** | **IF Corporate-Owned:** Navigate to Intune > Devices > Select Device > **Wipe**. (This performs a factory reset and erases all data). <br>**IF BYOD/Personal:** Select **Retire**. (This removes only company apps/data, leaving personal photos/apps intact). | [ ] |
| **9** | **Security** | **Remove MFA Methods** | In Entra ID > Users > Authentication methods. Remove any registered phone numbers, Authenticator apps, or FIDO keys to clean up the directory. | [ ] |
| **10**| **Audit** | **Final Documentation** | Update the internal HR/IT ticket with the timestamp of completion and note any specific actions taken (e.g., "Mailbox converted to Shared"). | [ ] |

---

### Critical Troubleshooting & Notes

*   **The "Ghost Session" Risk:** Simply disabling an account does **not** always kick a user out of a mobile device immediately if they have valid OAuth tokens. **Step 2 (Revoke Sessions) is the most critical step for immediate security.**
*   **Wipe vs. Retire Warning:** Never select "Wipe" on a personal/BYOD device unless you intend to destroy the employee's personal photos and data. Always use "Retire" for non-corporate devices.
*   **Litigation Hold:** If your organization is under a legal hold, ensure you apply a **Litigation Hold** or an **eDiscovery Hold** *before* removing the license or converting the mailbox to prevent permanent deletion of items via retention policies.
*   **License Reclamation:** Do not delete the user account immediately. Wait at least 30 days (or per your company policy) before deleting the object from Entra ID, as deleting the user will also delete the Shared Mailbox and OneDrive content.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | runbook-offboard | cold | run 2 | thinking: NO

**Tok/sec:** 45.3 &nbsp; **Wall sec:** 124.44 &nbsp; **Prompt tokens:** 72 &nbsp; **Output tokens:** 1896

**Response:**

# Runbook: Employee Offboarding (Microsoft 365 & Intune)

**Purpose:** To ensure a secure, standardized, and complete revocation of access and preservation of data when an employee leaves the organization.
**Scope:** Identity management (Entra ID), Email/Data (Exchange/OneDrive), and Device Management (Intune).
**Owner:** IT Administration / Security Team
**Role Required:** Global Administrator or Privileged Role Administrator

---

### 📋 Offboarding Checklist

| Step # | Task Category | Action Description | Done |
| :--- | :--- | :--- | :---: |
| **1.0** | **Identity & Access** | **Immediate Lockdown Phase** | |
| 1.1 | Disable Account | Navigate to **Entra ID (Azure AD)** > Users. Select user and set `Account Enabled` to **No**. | [ ] |
| 1.2 | Block Sign-in | Ensure the "Block Sign-in" flag is set in Entra ID to prevent all authentication attempts. | [ ] |
| 1.3 | Revoke Sessions | In Entra ID, select the user and click **"Revoke Sessions."** This invalidates all active Refresh Tokens (stops active web/mobile sessions). | [ ] |
| 1.4 | Reset Password | Change the user's password to a long, random string to prevent any potential "forgot password" bypasses via MFA. | [ ] |
| 1.5 | Remove MFA Methods | Remove user phone numbers and authenticator apps from the user profile to prevent unauthorized recovery. | [ ] |
| **2.0** | **Data Preservation** | **Mailbox & OneDrive Management** | |
| 2.1 | Set Out-of-Office | Access the mailbox via Exchange Admin Center (EAC) and set an auto-reply directing inquiries to a manager/successor. | [ ] |
| 2.2 | Convert to Shared Mailbox | Convert the user mailbox to a **Shared Mailbox**. This allows you to keep the data without paying for a license. | [ ] |
| 2.3 | Delegate Access | Grant "Full Access" and "Send As" permissions for the new Shared Mailbox to the manager or successor. | [ ] |
| 2.4 | OneDrive Migration | Use the M365 Admin Center to grant the manager access to the user's OneDrive. Move critical files to a departmental SharePoint site. | [ ] |
| **3.0** | **Device Management** | **Endpoint Security (Intune)** | |
| 3.1 | Determine Strategy | **Decision Required:** Choose between **Wipe** or **Retire** based on ownership (see Decision Logic below). | [ ] |
| 3.2 | Execute Wipe/Retire | In **Microsoft Intune**, locate the device. Select **"Wipe"** (for company-owned) or **"Retire"** (for BYOD/Personal). | [ ] |
| 3.3 | Remove from Autopilot | If a company-owned device, remove the serial number from the Windows Autopilot deployment program to allow for reassignment. | [ ] |
| 3.4 | Remove from Groups | Remove the user from all Security Groups, Distribution Lists, and Microsoft 365 Groups to prevent "ghost" membership. | [ ] |
| **4.0** | **License & Cleanup** | **Finalization & Cost Optimization** | |
| 4.1 | Unassign Licenses | Once data is preserved (Step 2.0), navigate to the user profile and remove all M365/Intune licenses to reclaim them for new hires. | [ ] |
| 4.2 | Remove from Apps | Ensure any third-party SSO integrations (e.g., Salesforce, Adobe) managed via Entra ID are also disconnected. | [ ] |
| 4.3 | Final Deletion | **Wait 30–90 days** (per company retention policy). Once the retention period expires, permanently delete the user object from Entra ID. | [ ] |

---

### 🧠 Decision Logic: Wipe vs. Retire

When performing **Step 3.1**, use the following logic to ensure you do not accidentally destroy personal data on a BYOD device or leave company data on a corporate device.

#### **Option A: Wipe (Use for Company-Owned Devices)**
*   **Action:** Performs a factory reset. Erases all apps, settings, and data.
*   **Result:** The device returns to its original out-of-the-box state.
*   **When to use:** When the laptop or mobile device is being returned to IT for re-imaging/re-assignment.

#### **Option B: Retire (Use for BYOD / Personal Devices)**
*   **Action:** Removes only corporate resources (Managed Apps, Email profiles, Managed Wi-Fi settings).
*   **Result:** The user's personal photos, apps, and messages remain untouched; only the "Company Partition" is deleted.
*   **When to use:** When an employee uses their own iPhone/Android for work and you want to ensure no company data remains on their private device.

---

### ⚠️ Critical Warnings
*   **Never delete a user before converting their mailbox to Shared.** If you delete the user first, the mailbox is marked for deletion and will be permanently purged after the retention period ends.
*   **Revoke Sessions immediately.** Disabling an account does *not* always kick a user out of an active Outlook Web or Mobile session instantly; "Revoke Sessions" is the only way to force an immediate logout.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | runbook-offboard | cold | run 3 | thinking: NO

**Tok/sec:** 45.6 &nbsp; **Wall sec:** 127.05 &nbsp; **Prompt tokens:** 72 &nbsp; **Output tokens:** 1828

**Response:**

# Runbook: Employee Offboarding (Microsoft 365 & Intune)

**Purpose:** To ensure a secure, standardized, and complete removal of access and data for departing employees, preventing unauthorized access to corporate resources and ensuring data retention compliance.

**Owner:** IT Administration / Security Team
**Scope:** Microsoft Entra ID (Azure AD), Exchange Online, Microsoft Intune, and Microsoft 365 Business/Enterprise.

---

| Step # | Action Item | Detailed Instructions | Done [ ] |
| :--- | :--- | :--- | :---: |
| **1.0** | **Identity & Access Suspension** | **Immediate priority to prevent unauthorized login.** | |
| 1.1 | Block Sign-in | Navigate to **Microsoft Entra ID (Azure AD) > Users**. Select the user and set **"Block sign-in"** to **Yes**. This prevents new authentication attempts. | [ ] |
| 1.2 | Revoke Active Sessions | In the same User profile in Entra ID, select **"Revoke sessions."** This invalidates all current Refresh Tokens, forcing any currently logged-in devices/browsers to prompt for credentials (which will fail due to step 1.1). | [ ] |
| 1.3 | Reset Password | Change the user's password to a long, complex, random string. This serves as an extra layer of security in case "Block Sign-in" fails due to specific conditional access bypasses. | [ ]  |
| 1.4 | Remove MFA Methods | Navigate to **Authentication methods** for the user. Delete any registered phone numbers, Authenticator apps, or hardware keys to prevent the employee from using their personal device to regain entry via "forgot password" flows. | [ ] |
| **2.0** | **Data Preservation & Mailbox Management** | **Ensure business continuity and legal compliance.** | |
| 2.1 | Convert Mailbox to Shared | Navigate to **Exchange Admin Center > Mailboxes**. Select the user and select **"Convert to shared mailbox."** This allows you to keep the data accessible to managers without needing a paid license. | [ ] |
| 2.2 | Set Auto-Reply (OOF) | Configure an Out-of-Office message for the Shared Mailbox (e.g., *"Person X is no longer with the company. Please contact Y at [email]."*). | [ ] |
| 2.3 | Archive/Export Mailbox | If legal hold is required: Ensure **Litigation Hold** or **Retention Policy** is active. If not, export the mailbox to a `.PST` file via the Compliance Center if a permanent local backup is required by company policy. | [ ] |
| 2.4 | Transfer OneDrive Files | Navigate to the **Microsoft 365 Admin Center > Users**. Under the user's "OneDrive" tab, select **"Create link to files."** Provide this link to the manager/successor and ensure a delegate is assigned to access the content before the account is deleted. | [ ] |
| **3.0** | **Endpoint Management (Intune)** | **Secure physical hardware and corporate data.** | |
| 3.1 | Determine Wipe vs. Retire | **Analyze device ownership:** <br>• **Company Owned?** Use **Wipe**. <br>• **BYOD (Personal)?** Use **Retire**. | [ ] |
| 3.2 | Execute "Wipe" (Corp-Owned) | Navigate to **Intune (Endpoint Manager) > Devices**. Select the device and select **"Wipe."** This performs a factory reset, removing all apps and data. *Note: Use "Wipe with Autopilot reset" if you intend to re-deploy the device immediately.* | [ ] |
| 3.3 | Execute "Retire" (BYOD) | Navigate to **Intune > Devices**. Select the user's personal device and select **"Retire."** This removes only company-managed data, apps, and profiles, leaving the user's personal photos/data intact. | [ ] |
| 3.4 | Remove from Device Groups | Manually remove the user's device from any specific Entra ID security groups or Intune dynamic groups that grant special permissions. | [ ] |
| **4.0** | **Cleanup & License Recovery** | **Cost optimization and final audit.** | |
| 4.1 | Remove Licenses | Once the mailbox is converted to shared (Step 2.1) and OneDrive is transferred, navigate to **M365 Admin Center > Users** and remove all Microsoft 365 licenses (e.g., E3, Business Premium) to stop billing. | [ ] |
| 4.2 | Remove from Distribution Lists | Remove the user from all internal/external Distribution Groups and Microsoft 365 Groups to prevent "Ghost" emails being sent to them. | [ ] |
| 4.3 | Final Audit Log | Document the date, time, and admin name who completed the offboarding in your internal IT Ticketing system for compliance auditing. | [ ] |

---

### **Critical Reminders:**
*   **Legal Hold:** Before performing any "Wipe" or "Delete" actions, verify with Legal/HR if a **Litigation Hold** is active on this user. If a hold is active, do not delete the user account; only disable it.
*   **Third-Party Apps:** Don't forget to manually check for SSO-integrated apps (like Slack, Zoom, or Adobe) that may not be automatically disabled by Entra ID if they are managed outside of the M365 ecosystem.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | runbook-cert-rotation | cold | run 1 | thinking: NO

**Tok/sec:** 44.5 &nbsp; **Wall sec:** 131.02 &nbsp; **Prompt tokens:** 60 &nbsp; **Output tokens:** 2267

**Response:**

# Runbook: Rotating Expired SCEP Certificate Profile in Intune

**Document ID:** RB-INT-SCEP-001  
    **Version:** 1.0  
    **Status:** Operational  
    **Owner:** IT Infrastructure / PKI Team  
    **Scope:** All managed Windows, iOS, and Android devices utilizing SCEP for authentication (VPN, Wi-Fi, or Email).

---

## 1. Overview
This runbook outlines the procedure for updating an expired or expiring SCEP (Simple Certificate Enrollment Protocol) configuration profile in Microsoft Intune. This process is required when the underlying certificate template, CA (Certificate Authority) information, or SCEP URL has changed due to a renewal of the issuing Intermediate/Root CA.

## 2. Prerequisites & Roles
### 2.1 Roles & Responsibilities
*   **PKI Administrator:** Responsible for ensuring the new Certificate Template is published on the NDES/CA server.
*   **Intune Administrator:** Responsible for updating the configuration profile and monitoring deployment.
*   **Change Advisory Board (CAB):** Responsible for reviewing and approving the execution window.

### 2.2 Prerequisites
*   Access to **Microsoft Intune Admin Center**.
*   Access to **NDES (Network Device Enrollment Service)** or **Certificate Connector** server.
*   A newly created/updated Certificate Template on the Issuing CA.
*   The new SCEP URL and Subject Name requirements documented.

---

## 3. Phase 1: Identification & Impact Analysis
**Goal:** Determine how many devices will be impacted by the profile change.

1.  **Identify Affected Devices:**
    *   Log in to **Microsoft Intune Admin Center**.
    *   Navigate to **Devices** > **Configuration profiles**.
    *   Locate the existing SCEP certificate profile.
    *   Check the **Device Status** report for this profile to identify all devices currently receiving this configuration.
2.  **Audit Certificate Expiry:**
    *   Verify the expiration date of the *current* certificates on a sample of managed devices (via Intune device logs or manual check via `certmgr.msc` on a test Windows device).
3.  **Determine Scope:** 
    *   Export the list of targeted devices/groups to ensure no high-priority "VIP" groups are inadvertently excluded from the new profile.

---

## 4. Phase 2: Change Control & Preparation
**[⚠️ CHANGE CONTROL REQUIRED]**
*All steps in this phase must be documented in a formal Change Request (CR) and approved by the CAB before proceeding to Phase 3.*

1.  **Create Change Request:** Include the maintenance window, the impact of potential connectivity loss (if VPN/Wi-sFi fails), and the rollback plan.
2.  **Pre-Configuration (The "Shadow Profile" Method):**
    *   **Do not modify the existing profile yet.** 
    *   Create a **new** SCEP Certificate Profile in Intune.
    *   Configure the new settings (New CA certificate, updated SCEP URL, and new Template Name).
    *   Assign this new profile to a **Test Group** containing only non-critical/IT-owned devices.

---

## 5. Phase 3: Execution (The Rotation)
**[⚠️ CHANGE CONTROL REQUIRED]**

1.  **Pilot Deployment:**
    *   Monitor the **Test Group** for 24 hours.
    *   Verify that the new certificate is being issued successfully to test devices.
2.  **Production Transition:**
    *   Once the pilot is successful, locate the **Original (Expired) Profile**.
    *   **Option A (Update):** Modify the existing profile settings with the new parameters (This triggers an "Update" command to all devices).
    *   **Option B (Replacement - Recommended for large changes):** 
        *   Unassign the old profile from the production group.
        *   Assign the **new** profile to the production group.
3.  **Triggering Synchronization:**
    *   To accelerate the rotation, you may manually trigger a sync for critical devices:
        *   **Windows:** Use the "Sync" button in the Intune Portal under Device > Windows > Sync.
        *   **iOS/Android:** Send a "Remote Sync" command via the Intune console.

---

## 6. Phase 4: Verification & Post-Implementation
**Goal:** Confirm all devices have received the new certificate and the old one is decommissioned.

1.  **Monitor Intune Enrollment Status:**
    *   Navigate to **Devices** > **Configuration profiles** > [Your Profile].
    *   Check the **Succeeded**, **Error**, and **Conflict** counts. 
    *   Investigate any devices in the "Error" state (Common causes: NDES server unreachable or incorrect Template name).
2.  **Endpoint Verification (Manual Check):**
    *   On a sample of Windows devices, run `certlm.msc` (Local Computer Certificates).
    *   Verify that a new certificate exists under **Personal > Certificates** with the updated expiration date.
3.  **Service Validation:**
    *   Test VPN connectivity on a mobile device using the new certificate.
    *   Test Wi-Fi authentication (802.1X) on a laptop using the new certificate.
4.  **Cleanup:**
    *   Once 100% deployment is confirmed, delete or retire any obsolete/temporary test profiles created during Phase 2.

---

## 7. Rollback Plan
**If the deployment fails (e.g., devices lose connectivity and cannot sync):**

1.  **Immediate Action:** Re-assign the **Original Profile** (if it has not been deleted) to the production group.
2.  **Fallback Configuration:** If the original profile was modified, revert the settings in the Intune portal to the previous known-good configuration.
3.  **Communication:** Notify stakeholders of the service interruption and the restoration of the previous state.
4.  **Root Cause Analysis (RCA):** Inspect NDES/NDES logs and Intune `DeviceManagement-Enterprise-Diagnostics-Provider` event logs on a failed device to identify why the new profile failed.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | runbook-cert-rotation | cold | run 2 | thinking: NO

**Tok/sec:** 45.1 &nbsp; **Wall sec:** 181.74 &nbsp; **Prompt tokens:** 60 &nbsp; **Output tokens:** 2123

**Response:**

# Runbook: Rotating SCEP Certificate Profile in Microsoft Intune

**Document ID:** RB-INT-SCEP-001  
**Version:** 1.0  
**Status:** Final  
**Owner:** IT Infrastructure / Endpoint Management Team  
**Scope:** All managed devices (iOS, Android, Windows, macOS) relying on SCEP for authentication (Wi-Fi, VPN, Email).

---

## 1. Overview
This runbook outlines the procedure for replacing an expired or nearing-expiration SCEP (Simple Certificate Enrollment Protocol) certificate profile in Microsoft Intune. Because SCEP profiles govern the issuance of identities used for network access (VPN/802.1X), incorrect execution can result in widespread device disconnection from corporate resources.

## 2. Risk Assessment & Change Control
| Risk Level | Impact | Mitigation |
| :--- | :--- | :--- |
| **High** | Loss of connectivity to Wi-Fi, VPN, and Email for all managed devices. | Use a phased deployment (Test Group $\rightarrow$ Pilot $\rightarrow$ Production). |

> [!IMPORTANT]  
> **Change Control Requirement:** This procedure requires formal **Change Control Approval** prior to execution in the Production environment. The window must be scheduled during low-impact hours to minimize helpdesk volume.

---

## 3. Prerequisites
1.  **Administrator Access:** Intune Administrator and Certificate Authority (CA) Administrator roles.
2.  **Updated CA Template:** Ensure the new certificate template is active and configured on your Issuing CA (e.g., Microsoft ADCS).
3.  **SCEP Connector:** Access to the server hosting the **Microsoft Intune Certificate Connector** to verify service health.

---

/## 4. Execution Steps

### Phase 1: Identification of Affected Devices
*Goal: Determine the scope of the rotation.*

1.  **Check Profile Status:**
    *   Navigate to **Microsoft Intune Admin Center** > **Devices** > **Configuration profiles**.
    *   Locate the existing SCEP profile.
    *   Review the **Device Status** report to identify devices currently reporting "Error" or "Conflict."
2.  **Identify Expiring Certificates:**
    *   If using Log Analytics/Azure Monitor, run a KQL query against `IntuneDeviceCompliance` logs to find devices with certificate error codes related to SCEP enrollment.
3.  **Inventory Scope:**
    *   Export a list of all device groups currently assigned to the expiring SCEP profile.

### Phase 2: Preparation (The "Side-by-Side" Method)
*Note: Never simply edit an existing SCEP profile. Creating a new profile allows for a rollback and testing.*

1.  **Create New SCEP Profile:**
    *   Go to **Devices** > **Configuration profiles** > **Create profile**.
    *   Select Platform (e.g., iOS/iPadOS) and Profile Type: **Templates** > **SCEP certificate**.
    *   **Crucial:** Configure the new Subject Name and Key Usage exactly as required by your network infrastructure, but point to the updated/new CA template parameters.
2.  **Assign to Test Group:**
    *   Create a "Pilot" Entra ID (Azure AD) group containing non-critical test devices.
    *   Assign the **New SCEP Profile** to this Pilot group.

### Phase 3: Implementation (The Swap)
> [!CAUTION]  
> **Requires Change Control Approval.** This step moves the configuration from Test to Production.

1.  **Validate Pilot Success:**
    *   Wait 24–48 hours after deploying to the Pilot group.
    *   Verify that test devices have successfully received the new certificate.
2.  **Update Production Assignment:**
    *   Navigate to the **Old (Expired) SCEP Profile**.
    *   Go to **Assignments** and remove the "All Devices" or "Production" group.
    *   Navigate to the **New SCEP Profile**.
    *   Go to **Assignments** and add the "All Devices" or "Production" group.
3.  **Verify Connector Health:**
    *   Log into the server hosting the **Intune Certificate Connector**.
    *   Restart the `Microsoft Intune Certificate Connector` service to ensure any cached authentication tokens are refreshed.

### Phase 4: Forcing Synchronization
*Goal: Trigger devices to check in and download the new profile immediately.*

1.  **Remote Action (Intune Portal):**
    *   For critical/high-priority users, go to **Devices** > **All devices** > [Select Device] > **Remote actions** > **Sync**.
2.  **User-Initiated Sync (Manual):**
    *   **iOS/Android:** Instruct users to open the **Company Portal app** and tap **Check Status**.
    *   **Windows:** Go to **Settings** > **Accounts** > **Access work or school** > [Select Account] > **Info** > **Sync**.

### Phase 5: Verification & Cleanup
1.  **Monitor Deployment Success:**
    *   In Intune, monitor the **New SCEP Profile** $\rightarrow$ **Device Status** report.
    *   Success criteria: "Succeeded" status count should match your total device inventory.
2.  **Endpoint Certificate Inspection:**
    *   On a sample of test devices, manually inspect the certificate store (e.g., `certlm.msc` on Windows or Keychain Access on macOS) to verify the **Valid To** date reflects the new expiration period.
3.  **Decommission Old Profile:**
    *   Once 100% success is confirmed across all groups, mark the **Old SCEP Profile** as "Retired" or delete it to prevent configuration conflicts.

---

## 5. Rollback Plan
*In the event of widespread connectivity failure:*

1.  **Immediate Reversion:**
    *   Re-assign the **Old SCEP Profile** to the Production/All Devices group.
    *   Remove the **New SCEP Profile** from the Production/All Devices group.
2.  **Force Sync:** Perform a Remote Action **Sync** on all affected devices via the Intune portal.
3.  **Root Cause Analysis (RCA):** Do not attempt re-deployment until the mismatch between the SCEP profile settings and the CA template is identified and resolved.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | runbook-cert-rotation | cold | run 3 | thinking: NO

**Tok/sec:** 44.4 &nbsp; **Wall sec:** 134.32 &nbsp; **Prompt tokens:** 60 &nbsp; **Output tokens:** 2375

**Response:**

# Runbook: SCN Certificate Profile Rotation (Microsoft Intune)

**Document ID:** RB-INT-SCEP-001  
**Version:** 1.0  
**Status:** Final  
**Owner:** IT Infrastructure / Identity Management Team  

---

## 1. Overview
**Purpose:** This runbook provides a standardized procedure for rotating an expired or expiring SCEP (Simple Certificate Enrollment Protocol) certificate profile in Microsoft Intune to ensure uninterrupted authentication for Wi-Fi, VPN, and Email services.

**Scope:** All Intune-managed devices (Windows, iOS, Android) relying on the SCEP certificate profile for identity/authentication.

**Risk Level:** **High**. Failure to rotate correctly will result in widespread loss of network connectivity and service access for end-users.

---

## 2. Prerequisites & Permissions
### 2.1 Permissions Required
*   **Microsoft Intune Administrator** (to modify profiles and assignments).
*   **Certificate Authority (CA) Administrator** (to update templates/issuing certificates).
*   **NDES/SCEP Server Access** (to verify the Network Device Enrollment Service health).

### 2.2 Prerequisites
*   A new, valid Certificate Template must be prepared on the Microsoft CA.
*   The updated Root CA certificate (if a chain change is occurring) must be available in `.cer` format.
*   **Change Control Approval must be documented before proceeding.**

---

## 3. Change Management Notice
> [!CAUTION]
> **CRITICAL: This procedure requires formal Change Control approval.** 
> This task involves modifying security configurations that can trigger widespread device disconnection if the SCEP renewal fails. Do not proceed without an approved Change Request (CR) and a confirmed maintenance window.

---

## 4. Phase able 1: Identification & Assessment
*Goal: Determine the scale of impact and identify which devices are using the expiring profile.*

1.  **Identify Expiring Profiles:** 
    *   Log in to the [Microsoft Intune Admin Center](https://intune.microsoft.com).
    *   Navigate to **Devices** > **Configuration profiles**.
    *   Locate the SCEP profile in question and check the **Certificate Template** expiration date (if documented) or the expiration of the underlying CA certificate.
2.  **Identify Affected Devices:**
    *   Click on the specific SCEP Profile.
    *   Select **Device status**.
    *   Export the list of devices currently reporting "Succeeded" or "Pending" for this profile. This list serves as your baseline for verification.
3.  **Audit NDES Server:**
    *   Log in to the NDES/SCEP server.
    *   Verify that the NDES service is running and that the web enrollment URL is reachable.
    *   Confirm that the new certificate template is active and accessible by the NDES service account.

---

## 5. Phase 2: Implementation (The Rotation)
*Goal: Deploy the updated configuration to the devices.*

### Step 1: Update the Root/Intermediate CA (If applicable)
*If the rotation involves a new Root or Intermediate CA, you must first deploy the new Trusted Certificate profile to all devices via Intune before updating the SCMC profile.*

1.  Navigate to **Devices** > **Configuration profiles** > **Create profile**.
2.  Platform: **Windows/iOS/Android** (as applicable) | Profile Type: **Trusted certificate**.
3.  Upload the new `.cer` file.
4.  Assign this to a **Test Group** first, then to all devices.

### Step 2: Update the SCEP Profile
*Note: It is highly recommended to create a NEW SCEP profile rather than editing an existing one to prevent "orphaned" certificates on devices.*

1.  **Create New Profile:** Navigate to **Devices** > **Configuration profiles** > **Create profile**.
2.  **Template Type:** Select **SCEP certificate**.
3.  **Configuration:** 
    *   Enter the updated **Certificate Template Name**.
    *   Ensure the **Subject Name Format** and **Subject Alternative Name (SAN)** match the requirements of your existing infrastructure.
4.  **Assignment (The "Pilot" Phase):**
    *   Assign this new profile to a **Pilot/Test Group** containing non-critical, managed devices.
    *   **[CHANGE CONTROL REQUIREMENT]**: Do not assign to the "All Devices" group until the Pilot phase is successful.

---

ically 6. Phase 3: Force Sync & Deployment
*Goal: Trigger the device to check in and pull the new configuration.*

1.  **For Windows Devices (Manual/Remote):**
    *   **Option A (Remote):** In the Intune Portal, go to **Devices** > **All devices** > Select a Test Device > Select **Sync**.
    *   **Option B (On-Device):** Open **Settings** > **Accounts** > **Access work or school** > Click your account > **Info** > **Sync**.
2.  **For iOS/Android Devices:**
    *   Open the **Company Portal App** on the device.
    *   Go to **Settings** > **Sync**.

---

## 7. Phase 4: Verification & Cleanup
*Goal: Confirm successful enrollment and decommission old profiles.*

1.  **Verify Intune Status:**
    *   In the Intune Admin Center, monitor the **Device status** for the *new* SCEP profile.
    *   Ensure devices move from "Pending" to "Succeeded."
2.  **Verify On-Device Certificate:**
    *   **Windows:** Run `certlm.msc`. Check **Personal > Certificates**. Verify a new certificate exists with the updated expiration date.
    *   **iOS/Android:** Check the device's Certificate Store via Settings or a management app to ensure the new cert is present.
3.  **Verify Service Functionality:**
    *   Test Wi-Fi connectivity on a test device using the new certificate.
    *   Test VPN connection/Authentication.
4.  **Decommission Old Profile:**
    *   Once 100% of the fleet has successfully transitioned to the new profile, remove the assignment from the **Old SCEP Profile**.
    *   *Do not delete the old profile immediately; keep it unassigned for 24–48 hours as a fallback.*

---

## 8. Rollback Plan
**Trigger:** If the New SCEP profile fails to deploy or causes widespread authentication failures in the Pilot group.

1.  **Re-assign Old Profile:** Re-add the "All Devices" or "Test Group" assignment to the **Original SCEP Profile**.
2.  **Check NDES Logs:** Investigate the NDES/SCEP server logs (Event Viewer) to identify why the new template failed (e.g., permissions, template name mismatch).
3.  **Notify Stakeholders:** Inform the Change Management team that the deployment has been rolled back due to [Insert Reason].

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | script-daily-health | cold | run 1 | thinking: NO

**Tok/sec:** 44.6 &nbsp; **Wall sec:** 146.68 &nbsp; **Prompt tokens:** 70 &nbsp; **Output tokens:** 2005

**Response:**

To use this script, you can save it as `healthcheck.sh`, make it executable, and set it up as a cron job to run daily.

### The Health-Check Script

```bash
#!/bin/bash

# --- CONFIGURATION ---
# Threshold for disk usage warning (percentage)
DISK_THRESHOLD=85
# URL for Ollama API check
OLLAMA_API="http://localhost:11434/api/tags"
# List of Docker container names to monitor (adjust these to your actual container names)
DOCKER_CONTAINERS=("open-webui" "ollama")
# ---------------------

# Formatting colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "--- Health Check Report: $(date) ---"

# 1. CHECK OLLAMA SYSTEM SERVICE (Assumes systemd)
if systemctl is-active --quiet ollama; then
    echo -e "Ollama Service: ${GREEN}PASS${NC}"
else
    echo -e "Ollama Service: ${RED}FAIL${NC}"
fi

# 2. CHECK DISK USAGE (Root partition)
# Extracts percentage of the root filesystem usage
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$DISK_USAGE" -lt "$DISK_THRESHOLD" ]; then
    echo -e "Disk Usage: ${GREEN}PASS${NC} (${DISK_USAGE}%)"
elif [ "$DISK_USAGE" -ge "$DISK_THRESHOLD" ] && [ "$DISK_USAGE" -lt 95 ]; then
    echo -e "Disk Usage: ${YELLOW}WARN${NC} (${DISK_USAGE}%)"
else
    echo -e "Disk Usage: ${RED}FAIL${NC} (${DISK_USAGE}%)"
fi

# 3. CHECK OLLAMA API RESPONSIVENESS
# Uses curl to check if the API returns a 200 OK status
HTTP_STATUS=$(curl -s -o /dev/ NULL -w "%{http_code}" --max-time 5 "$OLLAMA_API")

if [ "$HTTP_STATUS" -eq 200 ]; then
    echo -e "Ollama API: ${GREEN}PASS${NC}"
else
    echo -e "Ollama API: ${RED}FAIL${NC} (Status: $HTTP_STATUS)"
fi

# 4. CHECK DOCKER CONTAINER STATE
for container in "${DOCKER_CONTAINERS[@]}"; do
    # Check if the container is running using docker inspect
    RUNNING=$(docker inspect -f '{{.State.Running}}' "$container" 2>/dev/null)
    
    if [ "$RUNNING" == "true" ]; then
        echo -e "Container [$container]: ${GREEN}PASS${NC}"
    else
        # Check if it exists at all to distinguish between FAIL and MISSING
        EXISTS=$(docker ps -a --filter "name=$container" --format '{{.Names}}')
        if [ -z "$EXISTS" ]; then
            echo -e "Container [$container]: ${RED}FAIL${NC} (Not Found)"
        else
            echo -e "Container [$container]: ${RED}FAIL${NC} (Stopped)"
        fi
    fi
done

echo "-------------------------------------------"
```

---

### Setup Instructions

#### 1. Create the file
Copy the code above into a file on your Ubuntu server:
```bash
nano ~/healthcheck.sh
```
*Paste the code, then press `Ctrl+O`, `Enter`, and `Ctrl+X` to save.*

#### 2. Make it executable
You must give the script permission to run:
```bash
chmod +x ~/healthcheck.sh
```

#### 3. Test it
Run the script manually to ensure everything is working as expected:
```bash
./healthcheck.sh
```

#### 4. Automate with Cron (Daily at 8:00 AM)
To make this "repeatable" and automated, add it to your crontab. This version will run the check and save the output to a log file in your home directory.

1. Open the crontab editor:
   ```bash
   crontab -e
   ```
2. Add this line at the bottom of the file:
   ```cron
   0 8 * * * /home/YOUR_USERNAME/healthcheck.sh >> /home/YOUR_USERNAME/homelab_health.log 2>&1
   ```
   *(Replace `YOUR_USERNAME` with your actual Ubuntu username.)*

### What this script monitors:
*   **Ollama Service:** Uses `systemctl` to ensure the backend engine is active in the background.
*   **Disk Usage:** Monitors the `/` partition. It will trigger a **WARN** if usage exceeds 85% and a **FAIL** if it exceeds 95%.
*   **API Responsiveness:** Sends a real HTTP request to your local Ollama instance. This is crucial because sometimes a service "looks" active but is actually frozen/unresponsive.
*   **Docker State:** Iterates through your specified containers (like Open WebUI) and checks if the state is explicitly `Running`.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | script-daily-health | cold | run 2 | thinking: NO

**Tok/sec:** 44.7 &nbsp; **Wall sec:** 198.17 &nbsp; **Prompt tokens:** 70 &nbsp; **Output tokens:** 2482

**Response:**

This script is designed to be lightweight and easy to run via terminal or as a cron job. It uses ANSI color codes so you can quickly spot issues (Green/Yellow/Red) when glancing at your logs.

### The Health-Check Script

Save this file as `healthcheck.sh`.

```bash
#!/bin/bash

# --- CONFIGURATION ---
# Thresholds for disk usage percentage
DISK_WARN=85
DISK_FAIL=95

# Name of your Open WebUI docker container
WEBUI_CONTAINER="open-webui"

# Ollama API endpoint (checking tags is a lightweight way to see if engine is alive)
OLLAMA_API="http://localhost:11<0xA0>434/api/tags"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "--- Homelab Health Check: $(date) ---"

# 1. CHECK DISK USAGE (Root partition)
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -ge "$DISK_FAIL" ]; then
    echo -e "Disk Usage: ${RED}FAIL${NC} (${DISK_USAGE}% used)"
elif [ "$DISK_USAGE" -ge "$DISK_WARN" ]; then
    echo -e "Disk Usage: ${YELLOW}WARN${NC} (${DISK_USAGE}% used)"
else
    echo -e "Disk Usage: ${GREEN}PASS${NC} (${DISK_USAGE}% used)"
fi

# 2. CHECK OLLAMA SYSTEMD SERVICE
if systemctl is-active --quiet ollama; then
    echo -e "Ollama Service: ${GREEN}PASS${NC}"
else
    echo -e "Ollama Service: ${RED}FAIL${NC} (Service Down)"
fi

# 3. CHECK DOCKER CONTAINER STATE (Open WebUI)
if [ "$(docker inspect -f '{{.State.Running}}' $WEBUI_CONTAINER 2>/dev/null)" == "true" ]; then
    echo -e "Open WebUI Container: ${GREEN}PASS${NC}"
else
    echo -e "Open WebUI Container: ${RED}FAIL${NC} (Container Stopped or Not Found)"
fi

# 4. CHECK OLLAMA API RESPONSIVENESS
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$OLLAMA_API")
if [ "$HTTP_STATUS" -eq 200 ]; then
    echo -e "Ollama API: ${GREEN}PASS${NC} (Status 200)"
elif [ "$HTTP_STATUS" -eq 000 ]; then
    echo -e "Ollama API: ${RED}FAIL${NC} (Connection Refused/Timeout)"
else
    echo -e "Ollama API: ${YELLOW}WARN${NC} (Status $HTTP_STATUS)"
fi

echo "-------------------------------------------"
```

---

### Setup Instructions

#### 1. Create the file
```bash
nano healthcheck.sh
# Paste the code above into the editor, then press Ctrl+O, Enter, and Ctrl+X
```

#### 2. Make it executable
You must give the script permission to run.
```bash
chmod +x healthcheck.sh
```

#### 3. Run it manually
```bash
./healthcheck.sh
```

**Example Output:**
> --- Homelab Health Check: Tue Oct 24 10:00:01 UTC 2023 ---
> Disk Usage: **PASS** (42% used)
> Ollama Service: **PASS**
> Open WebUI Container: **PASS**
> Ollama API: **PASS** (Status 200)
> -------------------------------------------

---

### Automating with Cron (Daily Reports)

If you want this to run automatically every morning at 8:00 AM and save the result to a log file, follow these steps:

1. Open your crontab editor:
   ```bash
   crontab -e
   ```

2. Add this line to the bottom (replace `/path/to/` with the actual path where you saved the script):
   ```bash
   00 08 * * * /path/to/healthcheck.sh >> /home/yourusername/homelab_health.log 2>&1
   ```

### How it works:
*   **Disk Check:** Uses `df` to parse the root partition usage. It triggers a **WARN** if you cross 85% (important because LLM models are huge and can fill disks quickly) and a **FAIL** at 95%.
*   **Service Check:** Uses `systemctl is-active`, which is the most reliable way to check if the background daemon is actually running on Ubuntu.
*   **Docker Check:** Uses `docker inspect` to query the internal state of the container specifically, rather than just checking if Docker itself is running.
*   **API Check:** Uses `curl` with a `--max-time 5` flag. This ensures that if Ollama is "frozen" (deadlocked), the script doesn't hang forever; it will report a failure after 5 seconds of silence.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | script-daily-health | cold | run 3 | thinking: NO

**Tok/sec:** 46.3 &nbsp; **Wall sec:** 146.95 &nbsp; **Prompt tokens:** 70 &nbsp; **Output tokens:** 1560

**Response:**

This script is designed to be lightweight, easy to read, and suitable for a `cron` job. It uses standard Linux tools (`systemctl`, `df`, `curl`, and `docker`) available on Ubuntu.

### The Health-Check Script

Create a file named `healthcheck.sh`:

```bash
#!/bin/bash

# --- CONFIGURATION ---
# Name of your Open WebUI docker container
CONTAINER_NAME="open-webui"
# Threshold for Disk Usage warnings (percentage)
DISK_WARN=85
DISK_FAIL=95
# Ollama API Endpoint
OLLAMA_API="http://localhost:11434/api/tags"

# --- LOGIC ---

# 1. Check Ollama Service Status
if systemctl is-active --quiet ollama; then
    echo "Ollama Service: PASS"
else
    echo "Ollama Service: FAIL"
fi

# 2. Check Disk Usage (Root Partition)
DISK_USAGE=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -lt "$DISK_WARN" ]; then
    echo "Disk Usage (${DISK_USAGE}%): PASS"
elif [ "$DISK_USAGE" -lt "$DISK_FAIL" ]; then
    echo "Disk Usage (${DISK_USAGE}%): WARN"
else
    echo "Disk Usage (${DISK_USAGE}%): FAIL"
fi

# 3. Check Ollama API Responsiveness
if curl -s --head "$OLLAMA_API" | grep "200 OK" > /dev/null; then
    echo "Ollama API: PASS"
else
    echo "Ollama API: FAIL"
fi

# 4. Check Docker Container State (Open WebUI)
if [ "$(docker inspect -f '{{.State.Running}}' $CONTAINER_NAME 2>/dev/null)" == "true" ]; then
    echo "Open WebUI Container: PASS"
else
    echo "Open WebUI Container: FAIL"
fi
```

---

### Setup Instructions

#### 1. Prepare the script
First, save the code above to your server. You can use `nano`:
```bash
nano ~/healthcheck.sh
```
*(Paste the code, then press `Ctrl+O`, `Enter`, and `Ctrl+X`)*

#### 2. Make it executable
You must give the script permission to run:
```bash
chmod +x ~/healthcheck.sh
```

#### 3. Test the script
Run it manually to ensure everything is reporting correctly:
```bash
./healthcheck.sh
```

**Expected Output (if everything is healthy):**
```text
Ollama Service: PASS
Disk Usage (42%): PASS
Ollama API: PASS
Open WebUI Container: PASS
```

#### 4. Automate it (Daily Cron Job)
To have this run automatically every morning at 8:00 AM and save the output to a log file, follow these steps:

1. Open your crontab editor:
   ```bash
   crontab -e
   ```
2. Add this line to the bottom of the file:
   ```bash
   00 08 * * * /home/YOUR_USERNAME/healthcheck.sh >> /home/YOUR_USERNAME/homelab_health.log 2>&1
   ```
   *(Replace `YOUR_USERNAME` with your actual Ubuntu username)*

### Features of this script:
*   **Zero Dependencies:** Uses only tools pre-installed on most Ubuntu/Docker environments.
*   **Silent Errors:** Redirects errors to `/dev/null` inside the checks so your log file stays clean and only shows the PASS/WARN/FAIL summary.
*   **API Validation:** Instead of just checking if the port is open, it actually requests the model list (`/api/tags`) to ensure the Ollama engine is actually processing requests.
*   **Threshold Aware:** It distinguishes between a "warning" (disk getting full) and a "failure" (disk critical).

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | clf-intent | cold | run 1 | thinking: NO

**Tok/sec:** 50.9 &nbsp; **Wall sec:** 64.03 &nbsp; **Prompt tokens:** 110 &nbsp; **Output tokens:** 419

**Response:**

{"category": "group-membership", "confidence": 1.0, "reasoning": "The request explicitly asks to add a user to a specific SharePoint group."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | clf-intent | cold | run 2 | thinking: NO

**Tok/sec:** 50.8 &nbsp; **Wall sec:** 69.41 &nbsp; **Prompt tokens:** 110 &nbsp; **Output tokens:** 463

**Response:**

{"category": "group-membership", "confidence": 1.0, "reasoning": "The request explicitly asks to add a user to a specific SharePoint group."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | clf-intent | cold | run 3 | thinking: NO

**Tok/sec:** 51.4 &nbsp; **Wall sec:** 81.67 &nbsp; **Prompt tokens:** 110 &nbsp; **Output tokens:** 396

**Response:**

{"category": "group-membership", "confidence": 1.0, "reasoning": "The request specifically asks to add a user to a predefined SharePoint group."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | clf-risk | cold | run 1 | thinking: NO

**Tok/sec:** 51.5 &nbsp; **Wall sec:** 78.75 &nbsp; **Prompt tokens:** 88 &nbsp; **Output tokens:** 349

**Response:**

{"risk": "HIGH", "revertable": true, "reasoning": "Disabling multi-factor authentication significantly increases the risk of unauthorized access via credential theft during the testing period."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | clf-risk | cold | run 2 | thinking: NO

**Tok/sec:** 50.8 &nbsp; **Wall sec:** 137.77 &nbsp; **Prompt tokens:** 88 &nbsp; **Output tokens:** 455

**Response:**

{"risk": "HIGH", "revertable": true, "reasoning": "Disabling multi-factor authentication significantly increases the account's vulnerability to unauthorized access via credential theft or phishing attacks."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | clf-risk | cold | run 3 | thinking: NO

**Tok/sec:** 51.0 &nbsp; **Wall sec:** 79.80 &nbsp; **Prompt tokens:** 88 &nbsp; **Output tokens:** 396

**Response:**

{"risk": "HIGH", "revertable": true, "reasoning": "Disabling MFA removes a critical layer of security, significantly increasing the risk of unauthorized account access during the testing period."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | clf-ambiguous | cold | run 1 | thinking: NO

**Tok/sec:** 50.3 &nbsp; **Wall sec:** 75.56 &nbsp; **Prompt tokens:** 107 &nbsp; **Output tokens:** 458

**Response:**

{"category": "needs-clarification", "confidence": 1.0, "reasoning": "The request does not specify which user needs to be removed or which group they should be removed from.", "missing_info": "user identity and group name"}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | clf-ambiguous | cold | run 2 | thinking: NO

**Tok/sec:** 46.9 &nbsp; **Wall sec:** 109.02 &nbsp; **Prompt tokens:** 107 &nbsp; **Output tokens:** 1530

**Response:**

{"category": "needs-clarification", "confidence": 1.0, "reasoning": "The request does not specify which user should be removed or which group they should be removed from.", "missing_info": ["user identity", "group name"]}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | clf-ambiguous | cold | run 3 | thinking: NO

**Tok/sec:** 49.7 &nbsp; **Wall sec:** 92.92 &nbsp; **Prompt tokens:** 107 &nbsp; **Output tokens:** 696

**Response:**

{"category": "needs-clarification", "confidence": 1.0, "reasoning": "The request does not specify which user needs to be removed or which group they should be removed from.", "missing_info": "user identity and group name"}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ga-param-names | cold | run 1 | thinking: NO

**Tok/sec:** 46.7 &nbsp; **Wall sec:** 127.45 &nbsp; **Prompt tokens:** 151 &nbsp; **Output tokens:** 1502

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

This script follows your specific requirements, using the correct `New-MgGroupMemberByRef` syntax and implementing targeted error handling to detect if the user is already a member of the group.

```powershell
# Parameters - Replace these with your actual IDs
$groupId = "00000000-0000-0000-0000-000000000000"
$userId  = "11111111-1111-1111-1111-111111111111"

# Define the OData ID required for the Reference pattern
$directoryObjectUri = "https://graph.microsoft.com/v1.0/directoryObjects/$userId"
$body = @{
    '@odata.id' = $directoryObjectMemberUri
}

try {
    Write-Host "Attempting to add user [$userId] to group [$groupId]..." -ForegroundColor Cyan

    # The correct call pattern as requested
    New-MgGroupMemberByRef -GroupId $groupId -BodyParameter @{'@odata.id' = $directoryObjectUri}
    
    Write-Host "Successfully added user to the group." -ForegroundColor Green
}
catch {
    # Check if the error is specifically because the member already exists
    # Graph API returns a 400 Bad Request with a message containing 'already exists'
    if ($_.Exception.Message -match "already exists" -or $_.Error.Error.Code -eq "Request_BadRequest") {
        Write-Warning "Notice: The user is already a member of this group."
    }
    else {
        Write-Error "An unexpected error occurred: $($_.Exception.Message)"
        exit
    }
}

# --- Verification Step ---
Write-Host "Verifying membership..." -ForegroundColor Cyan

try {
    # Fetch all members of the group to verify presence
    $members = Get-MgGroupMember -GroupId $groupId -All
    
    if ($members.Id -contains $userId) {
        Write-Host "Verification SUCCESS: User is present in the group membership list." -ForegroundColor Green
    }
    else {
        Write-Error "Verification FAILED: User was not found in the group membership list."
    }
}
catch {
    Write-Error "Failed to retrieve group members for verification: $($_.Exception.Message)"
}
```

### Key implementation details:

1.  **Required Syntax**: It uses `New-MgGroupMemberByRef` with the exact `-BodyParameter` structure required by the Graph API (`@odata.id`).
2.  **Strict Parameter Compliance**: It avoids all forbidden parameters (`-MemberId`, `-UserId`, etc.) and uses only the `$groupId` and `$BodyParameter`.
3.  **Specific Error Handling**: 
    *   It uses a `try-catch` block to intercept the API response.
    *   It performs a string match on `$_.Exception.Message` for "already exists" and checks the Graph error code `Request_BadRequest`, which is how Microsoft Graph signals a duplicate entry attempt.
4.  **Immediate Verification**: After the addition (or the "already exists" warning), it uses `Get-MgGroupMember -All` to scan the group's membership list and confirm the ID exists in that collection.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ga-param-names | cold | run 2 | thinking: NO

**Tok/sec:** 45.8 &nbsp; **Wall sec:** 142.86 &nbsp; **Prompt tokens:** 151 &nbsp; **Output tokens:** 1717

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here is the PowerShell script following your exact requirements and constraints.

```powershell
<#
.SYNOPSIS
    Adds a user to a Microsoft Entra (Azure AD) group using New-MgGroupMemberByRef 
    and verifies the membership.

.DESCRIPTION
    This script uses the specific OData reference pattern required by the Microsoft Graph SDK.
    It includes logic to handle the 'Conflict' error if the user is already a member.
#>

# --- Configuration ---
$groupId = "00000000-0000-0000-0000-000000000000" # Replace with your Group ID
$userId  = "11111111-1111-1111-1111-111111111111" # Replace with your User ID

# --- Execution ---

try {
    Write-Host "Attempting to add user '$userId' to group '$groupId'..." -ForegroundColor Cyan

    # Construct the required BodyParameter pattern
    $body = @{
        '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$userId"
    }

    # Perform the addition using the Ref method
    New-MgGroupMemberByRef -GroupId $groupId -BodyParameter $body | Out-Null
    
    Write-Host "Successfully added user to group." -ForegroundColor Green
}
catch {
    # Check if the error is specifically because the user is already a member
    # Graph API returns a 409 Conflict for existing memberships
    if ($_.Exception.Message -like "*already exists*" -or $_.Error.ErrorType -eq "Request_Conflict") {
        Write-Host "Note: User is already a member of this group. Skipping addition." -ForegroundColor Yellow
    }
    else {
        Write-Error "An unexpected error occurred while adding the user: $($_.Exception.Message)"
        return # Exit script if it's a different error (e.g., 403 Forbidden or 404 Not Found)
    }
}

# --- Verification Phase ---

Write-Host "Verifying membership..." -ForegroundColor Cyan

try {
    # Retrieve all members of the group to verify existence
    $groupMembers = Get-MgGroupMember -GroupId $groupId -All

    # Check if the specific userId exists in the returned collection
    if ($groupMembers.Id -contains $userId) {
        Write-Host "Verification SUCCESS: User is a member of the group." -ForegroundColor Green
    }
    else {
        Write-Error "Verification FAILED: User was not found in the group membership list."
    }
}
catch {
    Write-Error "Failed to perform verification: $($_.Exception.Message)"
}
```

### Key Implementation Details:

1.  **The Correct Pattern**: I used exactly `$body = @{'@odata.id' = 'https://graph.microsoft.com/v1.0/directoryObjects/' + $userId}` as requested to ensure the Graph API recognizes the object reference correctly.
2.  **Strict Compliance**: There are no uses of `New-MgGroupMember`, `-MemberId`, `-UserId`, or `-DirectoryObjectId`.
3.  **Specific Error Handling**: 
    *   The `catch` block inspects the exception message and the `ErrorType` property.
    *   When a user is already in a group, Microsoft Graph returns an error containing "already exists" (HTTP 409). The script catches this specifically to prevent the script from failing/crashing, treating it as a non-critical warning instead.
4.  **Verification Logic**: After the `try/catch` block, the script fetches the group's member list via `Get-MgGroupMember -All` and performs a Boolean check (`-contains`) against the `$userId`.
5.  **Prerequisites**: Ensure you have run `Connect-MgGraph` with the necessary permissions (`GroupMember.ReadWrite.All`) before running this script.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ga-param-names | cold | run 3 | thinking: NO

**Tok/sec:** 45.7 &nbsp; **Wall sec:** 112.31 &nbsp; **Prompt tokens:** 151 &nbsp; **Output tokens:** 1836

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

This PowerShell script follows your exact requirements, using the correct `@odata.id` reference pattern and implementing specific error handling to detect if the user is already a member of the group.

```powershell
<#
.SYNOPSIS
    Adds a user to a group using New-MgGroupMemberByRef and verifies membership.
    
.NOTES
    Requires Microsoft.Graph module.
    Ensure you have run Connect-MgGraph with 'GroupMember.ReadWrite.All' permissions.
#>

# Configuration - Replace these with your actual IDs
$groupId = "00000000-0000-0000-0000-000000000000"
$userId  = "11111111-1111-1111-1111-111111111111"

try {
    Write-Host "Attempting to add user $userId to group $groupId..." -ForegroundColor Cyan

    # Construct the body parameter as required by the Graph API reference pattern
    $body = @{
        '@odata.id' = "https://graph.com/v1.0/directoryObjects/$userId"
    }
    
    # Note: While the instruction requested 'https://graph.microsoft.com/...', 
    # Microsoft Graph standardizes on the full URI format for @odata.id references.
    $body['@odata.id'] = "https://graph.microsoft.com/v1.0/directoryObjects/$userId"

    # Execute the addition
    New-MgGroupMemberByRef -GroupId $groupId -BodyParameter $body | Out-Null
    
    Write-Host "Successfully added user to the group." -ForegroundColor Green
}
catch {
    # Access the underlying Graph error details
    $errorMessage = $_.Exception.Message
    
    # Check if the error is specifically because the member already exists
    # Graph API returns a 400 Bad Request with a message containing "already exists"
    if ($errorMessage -like "*already exists*" -or $_.Error.Error.Code -eq "Request_BadRequest") {
        Write-Warning "Notice: The user is already a member of this group."
    }
    else {
        Write-Error "An unexpected error occurred while adding the member: $($_.Exception.Message)"
        exit 1
    }
}

# --- Verification Logic ---
Write-Host "Verifying membership..." -ForegroundColor Cyan

try {
    # Retrieve all members of the group to verify
    $members = Get-MgGroupMember -GroupId $groupId -All
    
    if ($members.Id -contains $userId) {
        Write-Host "Verification SUCCESS: User is present in the group membership list." -ForegroundColor Green
    }
    else {
        Write-Error "Verification FAILED: User was not found in the group membership list."
        exit 1
    }
}
catch {
    Write-Error "Failed to verify membership due to an error retrieving group members: $($_.Exception.Message)"
    exit 1
}
```

### Key Implementation Details:

1.  **Correct API Pattern**: The script uses the mandatory `@odata.id` construction: 
    `@{'@odata.id' = 'https://graph.microsoft.com/v1.0/directoryObjects/' + $userId}`. This is necessary because `New-MgGroupMemberByRef` treats the body as a reference to an existing object in the directory, rather than a new object creation.
2.  **No Forbidden Parameters**: The script avoids `-MemberId`, `-UserId`, or any other deprecated/incorrect parameters as requested.
3.  **Specific Error Handling**: 
    *   The `catch` block inspects `$_.Exception.Message`. 
    *   When a user is already in a group, Microsoft Graph returns a `400 Bad Request` with the error string `"Member already exists"`. The script catches this specifically and converts it into a `Warning` rather than a script-terminating `Error`.
4.  **Immediate Verification**: After the `try/catch` block finishes (regardless of whether the user was *just* added or was *already* there), the script performs a lookup using `Get-MgGroupMember` to confirm the state of the group matches the desired outcome.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ga-pagination | cold | run 1 | thinking: NO

**Tok/sec:** 45.5 &nbsp; **Wall sec:** 138.71 &nbsp; **Prompt tokens:** 104 &nbsp; **Output tokens:** 2012

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

While the Microsoft Graph PowerShell SDK's `-All` parameter is designed to handle pagination automatically, in large-scale enterprise environments (10,000+ devices), manual pagination via `Invoke-MgGraphRequest` is often preferred to provide better control over memory management and error handling at each specific page boundary.

Below is a professional-grade script that implements **manual pagination** using the `@odata.nextLink` property as requested.

```powersESS
<#
.SYNOPSIS
    Retrieves all Intune managed devices using manual Graph API pagination.
    
.DESCRIPTION
    This script uses Invoke-MgGraphRequest to traverse the @odata.nextLink 
    property of the Microsoft Graph API to ensure every device in the tenant 
    is captured, regardless of page size limits.
#>

# --- Configuration ---
$ExportPath = "C:\Temp\IntuneDevices_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv"
$GraphEndpoint = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"

# --- Script Execution ---
try {
    # 1. Check Connection
    Write-Host "Checking Microsoft Graph connection..." -ForegroundColor Cyan
    $currentContext = Get-MgContext
    if (-not $currentContext) {
        Write-Error "No active Microsoft Graph connection found. Please run Connect-MgGraph first."
        return
    }

    $allDevices = New-Object System.Collections.Generic.List[PSObject]
    $nextLink = $GraphEndpoint
    $pageCount = 0

    Write-Host "Starting device retrieval..." -ForegroundColor Cyan

    # 2. Pagination Loop
    while ($null -ne $nextLink) {
        $pageCount++
        Write-Host "Fetching page $pageCount: $nextLink" -ForegroundColor Gray
        
        try {
            # Execute the request
            $response = Invoke-MSGraphRequest -Method GET -Uri $nextLink
            
            # Check if value exists in response
            if ($null -ne $response.value) {
                foreach ($device in $response.value) {
                    $allDevices.Add($device)
                }
            }

            # Update nextLink for the next iteration (This is the core logic requested)
            # If @odata.nextLink doesn't exist, it becomes null and the loop terminates
            $nextLink = $response.'@odata.nextLink'
        }
        catch {
            Write-Error "Error retrieving page $pageCount: $($_.Exception.Message)"
            break 
        }
    }

    # 3. Processing Results
    if ($allDevices.Count -gt 0) {
        Write-Host "`nSuccess!" -ForegroundColor Green
        Write-Host "Total Devices Found: $($allDevices.Count)" -ForegroundColor White

        # Flattening the object for CSV (Selecting specific useful properties)
        # Note: ManagedDevice objects contain nested properties; we select top-level ones here.
        $report = $allDevices | Select-Object `
            deviceName, 
            operatingSystem, 
            osVersion, 
            model, 
            manufacturer, 
            serialNumber, 
            userPrincipalName, 
            complianceState, 
            managedDeviceOwnerType, 
            azureADDeviceId,
            lastSyncDateTime

        # 4. Export to CSV
        $report | Export-Csv -Path $ExportPath -NoTypeInformation
        Write-Host "Report exported to: $ExportPath" -ForegroundColor Cyan
    }
    else {
        Write-Warning "No devices were retrieved. Check your permissions/scopes."
    }

}
catch {
    Write-Error "A critical error occurred: $($_.Exception.Message)"
}
finally {
    Write-Host "`nScript execution finished." -ForegroundColor Cyan
}

# Helper function wrapper to ensure consistency in naming 
function Invoke-MSGraphRequest {
    param (
        [Parameter(Mandatory=$true)][string]$Method,
        [Parameter(Mandatory=$true)][string]$Uri
    )
    return Invoke-MgGraphRequest -Method $Method -Uri $Uri
}
```

### Key Technical Explanations:

1.  **The `while ($null -ne $nextLink)` Loop**: This is the most critical part of the script. The variable `$nextLink` starts as the initial API URL. At the end of every loop iteration, we overwrite it with the value found in `@odata.nextLink`. When the API reaches the last page, that property becomes null/absent, and the loop exits naturally.
2.  **System.Collections.Generic.List**: Instead of using the standard PowerShell array (`$array += $item`), I used a `List[PSObject]`. Standard arrays in PowerShell are immutable; every time you use `+=`, PowerShell creates a complete copy of the entire array in memory. In a tenant with 50,000 devices, this causes massive performance degradation and high CPU usage. A `List` is mutable and significantly faster for large datasets.
3.  **Property Selection**: The Graph API returns many "noisy" properties (like raw JSON strings or system metadata). I included a `Select-Object` block to flatten the object into a clean, readable CSV format.
4.  **Error Handling**: The script includes a `Try/Catch` block specifically inside the loop. This ensures that if one page fails (due to a network hiccup), the script reports which page failed rather than simply crashing and losing all previously collected data.

### Requirements to run:
1.  **Module**: `Install-Module Microsoft.Graph -Scope CurrentUser`
2.  **Permissions**: You must authenticate with at least `DeviceManagementManagedDevices.Read.All`.
    *   Command: `Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"`

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ga-pagination | cold | run 2 | thinking: NO

**Tok/sec:** 45.7 &nbsp; **Wall sec:** 133.18 &nbsp; **Prompt tokens:** 104 &nbsp; **Output tokens:** 1957

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Below are two ways to achieve this. 

The first method uses the **built-in `-All` parameter**, which is the industry best practice because the SDK handles pagination logic internally. The second method uses **`Invoke-MgGraphRequest`**, which demonstrates the manual logic of following `@odata.nextLink` as requested in your prompt.

### Option 1: The Efficient Way (Using `-All`)
This is the recommended approach when using the Microsoft Graph PowerShell SDK. The `-All` parameter automatically detects the `@odata.nextLink` and iterates until all records are retrieved.

```powershell
# Required Module: Microsoft.Graph
# Required Permission: DeviceManagementManagedDevices.Read.All

Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"

Write-Host "Starting device retrieval using built-in pagination..." -ForegroundColor Cyan

try {
    # The -All parameter handles the @odata.nextLink logic automatically
    $allDevices = Get-MgDeviceManagementManagedDevice -All -ErrorAction Stop

    $deviceCount = $allDevices.Count
    Write-Host "Successfully retrieved $deviceCount devices." -ForegroundColor Green

    # Export to CSV
    $outputPath = "$PSScriptRoot\IntuneDevices_Automated.csv"
    $allDevices | Select-Object DeviceName, OperatingSystem, OSVersion, Model, Manufacturer, SerialNumber, ManagedDeviceOwnerType | 
        Export-Csv -Path $outputPath -NoTypeInformation

    Write-Host "Results exported to: $outputPath" -ForegroundColor Yellow
}
catch {
    Write-Error "An error occurred: $($_.Exception.Message)"
}
```

---

### Option 2: The Manual Way (Using `Invoke-MgGraphRequest`)
Use this version if you need to implement custom logic during the pagination process or if you are working with a raw REST implementation. This script explicitly checks for the `@odata.nextLink` property.

```powershell
# Required Module: Microsoft.Graph
# Required Permission: DeviceManagementManagedDevices.Read.All

Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"

$baseUrl = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"
$nextLink = $baseUrl
$allDevices = New-Object System.Collections.Generic.List[PSObject]

Write-Host "Starting manual pagination process..." -ForegroundColor Cyan

try {
    while ($null -ne $nextLink) {
        Write-Host "Fetching page: $nextLink" -ForegroundColor Gray
        
        # Perform the GET request
        $response = Invoke-MgGraphRequest -Method GET -Uri $nextLink
        
        # Add the current page's 'value' to our master list
        if ($null -ne $response.value) {
            foreach ($device in $response.value) {
                $allDevices.Add([PSCustomObject]$device)
            }
        }

        # Check if a nextLink property exists in the response
        $nextLink = $response.'@odata.nextLink'
    }

    $totalCount = $allDevices.Count
    Write-Host "`nRetrieval Complete!" -ForegroundColor Green
    Write-Host "Total devices found: $totalCount" -ForegroundColor White

    # Export to CSV
    if ($totalCount -gt 0) {
        $outputPath = "$PSSDScriptRoot\IntuneDevices_ManualPagination.csv"
        $allDevices | Select-Object deviceName, operatingSystem, osVersion, model, manufacturer, serialNumber | 
            Export-Csv -Path $outputPath -NoTypeInformation
        
        Write-Host "Data exported to: $outputPath" -ForegroundColor Yellow
    } else {
        Write-Warning "No devices were found to export."
    }
}
catch {
    Write-Error "An error occurred during pagination: $($_.Exception.Message)"
}
```

### Key Differences Explained:

1.  **The Loop Logic (`while`):** In Option 2, the script initializes `$nextLink` with the starting URL. The `while` loop continues as long as the Graph API returns a property named `@odata.nextLink`. Once the last page is reached, that property becomes null, and the loop terminates.
2.  **Data Storage (`System.Collections.Generic.List`):** In the manual script, I used a `.NET List` instead of a standard PowerShell array (`+=`). This is significantly faster and more memory-efficient when dealing with thousands of Intune devices, as it avoids recreating the entire array in memory on every loop iteration.
3.  **Complexity vs. Control:** 
    *   **Option 1** is cleaner and less prone to developer error (e.g., forgetting to parse the JSON).
    *   **Option 2** allows you to intercept each page. This is useful if you want to perform real-time logging of how many devices were fetched per "chunk" or if you need to handle specific API error codes mid-stream.

### Prerequisites for running:
1.  **Install Module:** `Install-Module Microsoft.Graph -Scope CurrentUser`
2.  **Permissions:** You must have at least **DeviceManagementManagedDevices.Read.All** permissions assigned to your account/app registration.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ga-pagination | cold | run 3 | thinking: NO

**Tok/sec:** 45.4 &nbsp; **Wall sec:** 119.68 &nbsp; **Prompt tokens:** 104 &nbsp; **Output tokens:** 1984

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Below are two versions of the script. 

**Version 1** is the recommended "Best Practice" approach using the built-in `-All` parameter, which automatically handles `@odata.nextLink`. 

**Version 2** is the "Manual" approach using `Invoke-MgGraphRequest`, as requested, to demonstrate how to manually iterate through pagination links.

### Prerequisites
Before running either script, ensure you have the module installed and are authenticated:
```powershell
Install-Module Microsoft.Graph -Scope CurrentUser
Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"
```

---

### Option 1: The Recommended Way (Using `-All`)
The `Microsoft.Graph` SDK is designed so that the `-All` switch handles all pagination logic, including checking for `@odata.nextLink`, internally. This is the most stable and least error-prone method.

```powershell
<#
.SYNOPSIS
    Retrieves all Intune managed devices using the built-in SDK pagination handler.
#>

$ExportPath = "C:\Temp\IntuneDevices_All.csv"

try {
    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
    # Ensure you are connected with required scopes before running
    
    Write-Host "Fetching all managed devices (handling pagination automatically)..." -ForegroundColor Cyan
    
    # The -All parameter handles the @odata.nextLink logic internally
    $Devices = Get-MgDeviceManagementManagedDevice -All -ErrorAction Stop

    if ($null -eq $Devices) {
        Write-Warning "No devices found."
        return
    }

    # Process results for CSV (selecting key properties to avoid deep-nesting issues in CSV)
    $Results = $Devices | Select-Object `
        DeviceName, 
        OperatingSystem, 
        OSVersion, 
        SerialNumber, 
        Model, 
        Manufacturer, 
        EmailAddress, 
        ComplianceState, 
        ManagedDeviceOwnerType, 
        LastSyncDateTime

    # Output results
    $Results | Export-Csv -Path $ExportPath -NoTypeInformation
    
    Write-Host "`nSuccess!" -ForegroundColor Green
    Write-Host "Total Devices Retrieved: $($Devices.Count)" -ForegroundColor Yellow
    Write-Host "Data exported to: $ExportPath" -ForegroundColor Yellow

}
catch {
    Write-Error "An error occurred: $($_.Exception.Message)"
}
```

---

### Option 2: The Manual Way (Using `Invoke-MgGraphRequest`)
Use this version if you need to perform highly customized logic on every single page request or if you are working in an environment where the SDK's high-level cmdlets are behaving unexpectedly.

```powershell
<#
.SYNOPSIS
    Retrieves all Intune managed devices by manually following @odata.nextLink.
#>

$ExportPath = "C:\Temp\IntuneDevices_Manual.csv"
$Uri = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"
$AllDevices = New-Object System.Collections.Generic.List[PSObject]

try {
    Write-Host "Starting manual pagination process..." -ForegroundColor Cyan

    while ($null -ne $Uri) {
        Write-Host "Fetching page: $Uri" -ForegroundColor Gray
        
        # Perform the REST API call
        $Response = Invoke-MgGraphRequest -Method GET -Uri $Uri
        
        # Add current page items to our master list
        if ($null -ne $Response.value) {
            foreach ($Device in $Response.value) {
                $AllDevices.Add($Device)
            }
        }

        # Check if a nextLink exists to continue the loop
        $Uri = $Response.'@odata.nextLink'
    }

    if ($AllDevices.Count -eq 0) {
        Write-Warning "No devices found."
    }
    else {
        # Exporting data
        $AllDevices | Export-Csv -Path $ExportPath -NoTypeInformation
        
        Write-Host "`nSuccess!" -ForegroundColor Green
        Write-Host "Total Devices Retrieved: $($AllDevices.Count)" -ForegroundColor Yellow
        Write-Host "Data exported to: $ExportPath" -ForegroundColor Yellow
    }
}
catch {
    Write-Error "An error occurred during manual pagination: $($_.Exception.Message)"
}
```

---

### Key Differences and Implementation Details

1.  **Pagination Logic**: 
    *   In **Option 1**, `Get-MgDeviceManagementManagedDevice -All` encapsulates a `do-while` loop that looks for the `@odata.nextLink` property behind the scenes. This is highly optimized by Microsoft.
    *   In **Option 2**, we explicitly check `$Response.'@odata.nextLink'`. If it exists, the `while` loop runs again using the new URL. When the property is missing (the last page), the loop terminates.

2.  **Data Collection**:
    *   I used `System.Collections.Generic.List[PSObject]` in Option 2. This is much more memory-efficient than using `$Array += $Item`, which creates a brand new copy of the entire array in memory every time an item is added.

3.  **Property Selection**:
    *   When exporting to CSV, I explicitly selected properties (in Option 1). Raw Graph objects often contain "heavy" nested objects (like `managedDeviceOwnerType` being a complex object rather than a string). Selecting specific strings ensures your CSV is readable and doesn't just say `Microsoft.Graph.PowerShell.Models...`.

4.  **Error Handling**:
    *   Both scripts are wrapped in `Try/Catch` blocks to capture authentication failures or network interruptions, which are common when iterating through large datasets.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ctx-short-ps | cold | run 1 | thinking: NO

**Tok/sec:** 47.7 &nbsp; **Wall sec:** 94.53 &nbsp; **Prompt tokens:** 31 &nbsp; **Output tokens:** 962

**Response:**

Since the `AzureAD` module is being deprecated, the modern and recommended way to do this is using the **Microsoft Graph PowerShell SDK**.

Here is the one-liner:

```powershell
Get-MgUser -Filter "accountEnabled eq false" -All | Select-Object DisplayName, UserPrincipalName
```

### Breakdown of the command:
*   **`Get-MgUser`**: The cmdlet used to retrieve user information from Microsoft Graph.
*   **`-Filter "accountEnabled eq false"`**: This is the most efficient way to do it because the filtering happens on the server side (Azure/Entra) rather than downloading all users and filtering locally on your machine. It specifically looks for accounts where the enabled status is false.
*   **`-All`**: Ensures that if you have more than 100 users, the command continues to loop through all pages of results (without this, it only returns the first page).
*   **`Select-Object DisplayName, UserPrincipalName`**: Cleans up the output so you only see the relevant names and login IDs.

---

### Prerequisites
If you haven't set up the environment yet, you will need to run these commands first:

1.  **Install the module** (if not already installed):
    ```powershell
    Install-Module Microsoft.Graph -Scope CurrentUser
    ```
2.  **Connect and Authenticate**:
    You need at least `User.Read.All` permissions.
    ```powershell
    Connect-MgGraph -Scopes "User.Read.All"
    ```

### Legacy Alternative (AzureAD Module)
If you are working in an older environment still using the deprecated **AzureAD** module, use this:

```powershell
Get-AzureADUser -Filter 'AccountEnabled -eq $false' | Select-Object DisplayName, UserPrincipalName
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ctx-short-ps | cold | run 2 | thinking: NO

**Tok/sec:** 48.7 &nbsp; **Wall sec:** 116.68 &nbsp; **Prompt tokens:** 31 &nbsp; **Output tokens:** 771

**Response:**

Since the `AzureAD` and `MSOnline` modules are being deprecated, you should use the **Microsoft Graph PowerShell SDK**. 

Here is the most efficient one-liner (using server-side filtering to ensure speed even in large tenants):

```powershell
Get-MgUser -Filter "AccountEnabled eq false" -All | Select-Object DisplayName, UserPrincipalName
```

### Explanation:
*   **`Get-MgUser`**: The standard cmdlet to retrieve users from Microsoft Graph.
*   **`-Filter "AccountEnabled eq false"`**: This is the most important part. By using the `-Filter` parameter, the filtering happens on the **Microsoft server side**. This is significantly faster and more efficient than downloading all users and filtering them locally with `Where-Object`.
*   **`-All`**: Ensures that the command retrieves every single disabled user, rather than just the first batch (pagination).
*   **`Select-Object DisplayName, UserPrincipalName`**: Cleans up the output so you only see the names and login IDs.

---

### Prerequisites
To run this, you must have the Microsoft Graph module installed and be connected with the correct permissions:

1.  **Install the module (if you haven't already):**
    ```powershell
    Install-Module Microsoft.Graph -Scope CurrentUser
    ```
2.  **Connect to your tenant:**
    (You need the `User.Read.All` permission)
    ```powershell
    Connect-MgGraph -Scopes "User.Read.All"
    ```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ctx-short-ps | cold | run 3 | thinking: NO

**Tok/sec:** 48.1 &nbsp; **Wall sec:** 84.27 &nbsp; **Prompt tokens:** 31 &nbsp; **Output tokens:** 844

**Response:**

Since the **AzureAD** module is being deprecated, the modern and recommended way to do this is using the **Microsoft Graph PowerShell SDK**.

### The Recommended Way (Microsoft Graph)
This version uses a server-side filter, making it much faster for large organizations because it only downloads the users that match the criteria.

```powershell
Get-MgUser -Filter "accountEnabled eq false" | Select-Object DisplayName, UserPrincipalName
```

**Prerequisites:**
*   You must have the `Microsoft.Graph` module installed.
*   You must be connected with the correct permissions: `Connect-MgGraph -Scopes "User.Read.All"`

---

### The Legacy Way (AzureAD Module)
If you are still using the older AzureAD module, use this one-liner:

```powershell
Get-AzureADUser -All $true | Where-Object {$_.AccountEnabled -eq $false} | Select-Object DisplayName, UserPrincipalName
```

### Why use `-Filter` instead of `Where-Object`?
In the **Microsoft Graph** example, I used `-Filter "accountEnabled eq false"`. 
*   **`-Filter` (Server-side):** The Microsoft server does the work and only sends the disabled users to your computer. This is extremely fast.
*   **`Where-Object` (Client-side):** Your computer downloads **every single user** in the entire company first, then looks through them one by one. If you have 10,000+ users, this will be very slow and may cause memory issues.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ctx-medium-ps | cold | run 1 | thinking: NO

**Tok/sec:** 45.9 &nbsp; **Wall sec:** 123.77 &nbsp; **Prompt tokens:** 154 &nbsp; **Output tokens:** 1687

**Response:**

```powershell
try {
    # FIX: Added 'AuditLog.Read.All' scope. 'User.Read.All' is insufficient to access the 'SignInActivity' property.
    Connect-MgGraph -Scopes 'User.Read.All', 'AuditLog.Read.All'

    # FIX: Used '-Filter' to perform the "AccountEnabled" check server-side. This prevents downloading every user in the tenant, significantly improving performance and reducing memory usage.
    # FIX: Included '-Property' to fetch 'SignInActivity' during the initial call. 
    # FIX: Removed the Get-MgUser call from inside the loop (the "N+1" problem). Calling the API once for all users instead of once per user prevents hitting Graph API throttling limits (42Turns/Too Many Requests).
    $users = Get-MgUser -All -Filter "accountEnabled eq false" -Property "DisplayName", "Id", "AccountEnabled", "SignInActivity"

    if ($null -eq $users) {
        Write-Host "No disabled users found." -ForegroundColor Cyan
        return
    }

    # FIX: Changed output from a formatted string to [PSCustomObject]. 
    # Returning objects instead of strings allows the user to pipe the results to 'Export-Csv', 'Out-GridView', or 'Format-Table'.
    $results = foreach ($user in $users) {
        try {
            [PSCustomObject]@{
                DisplayName        = $user.DisplayName
                AccountEnabled     = $user.AccountEnabled
                LastSignInDateTime = $user.SignInActivity.LastSignInDateTime
            }
        } catch {
            # FIX: Added error handling inside the loop to ensure one failed user record doesn't crash the entire script.
            Write-Error "Error processing user $($user.Id): $($_.Exception.Message)"
        }
    }

    # Output the final collection to the pipeline
    $results
} catch {
    # FIX: Added top-level try-catch to handle connection failures or authentication errors.
    Write-Error "A critical error occurred during script execution: $($_.Exception.Message)"
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ctx-medium-ps | cold | run 2 | thinking: NO

**Tok/sec:** 46.8 &nbsp; **Wall sec:** 124.34 &nbsp; **Prompt tokens:** 154 &nbsp; **Output tokens:** 1214

**Response:**

```powershell
try {
    # FIX: Added 'AuditLog.Read.All' scope; 'User.Read.All' is insufficient to access SignInActivity property.
    # FIX: Wrapped connection in try/catch to handle authentication failures or lack of permissions.
    Connect-MgGraph -Scopes 'User.Read.All', 'AuditLog.Read.All'

    # FIX: Added '-Property' parameter to the initial call. 
    # By default, Get-MgUser does not return AccountEnabled or SignInActivity.
    # Fetching all properties here prevents the need for a second API call inside the loop (improves performance from O(n) to O(1)).
    $users = Get-MgUser -All -Property 'id', 'displayName', 'accountEnabled', 'signInActivity'

    if ($null -eq $users) {
        Write-Warning "No users found or error retrieving users."
        return
    }

    # FIX: Changed output to a collection of PSCustomObjects instead of raw strings.
    # This allows the output to be easily piped to Export-Csv, Format-Table, or Select-Object.
    $results = foreach ($user in $users) {
        # Note: AccountEnabled can be null; checking specifically for $false handles disabled accounts.
        if ($user.AccountEnabled -eq $false) {
            [PSCustomObject]@{
                DisplayName        = $user.DisplayName
                # FIX: Access property directly from the pre-fetched $user object to avoid redundant Get-MgUser calls.
                # Added a null check for LastSignInDateTime to prevent empty/ugly output.
                LastSignInDateTime = if ($null -ne $user.SignInActivity) { $user.SignInActivity.LastSignInDateTime } else { "Never" }
            }
        }
    }

    # Output the final collection
    $results | Format-Table -AutoSize

} catch {
    # FIX: Added global error handling to capture and report API or connection errors.
    Write-Error "An error occurred: $($_.Exception.Message)"
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ctx-medium-ps | cold | run 3 | thinking: NO

**Tok/sec:** 46.5 &nbsp; **Wall sec:** 93.13 &nbsp; **Prompt tokens:** 154 &nbsp; **Output tokens:** 1466

**Response:**

```powershell
try {
    # FIX 1: Added 'AuditLog.Read.All' scope. Accessing 'SignInActivity' requires this specific permission; 'User.Read.All' is insufficient.
    Connect-MgGraph -Scopes 'User.Read.All', 'AuditLog.Read.All'

    # FIX 2: Used -Filter to perform the "AccountEnabled" check on the server side. This significantly reduces data transfer and local processing time.
    # FIX 3: Added -Property to include 'signInActivity' in the initial request. The original script suffered from the "N+1" problem (making a new API call for every user), which causes severe throttling and slow performance.
    $userParams = @{
        Filter    = "accountEnabled eq false"
        All       = $true
        Property  = 'id', 'displayName', 'accountEnabled', 'signInActivity'
    }

    $disabledUsers = Get-MgUser @userParams

    foreach ($user in $disabledUsers) {
        # FIX 4: Instead of Write-Output (string), we return a [PSCustomObject]. 
        # This allows the output to be piped to Format-Table, Export-Csv, or Out-GridView.
        [PSCustomObject]@{
            DisplayName        = $user.DisplayName
            AccountEnabled     = $user.AccountEnabled
            LastSignInDateTime = $user.SignInActivity.LastSignInDateTime
        }
    }
}
catch {
    # FIX 5: Added basic error handling to capture and report API connection or execution failures.
    Write-Error "An error occurred during script execution: $($_.Exception.Message)"
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ctx-long-ps | cold | run 1 | thinking: NO

**Tok/sec:** 44.4 &nbsp; **Wall sec:** 152.63 &nbsp; **Prompt tokens:** 685 &nbsp; **Output tokens:** 2131

**Response:**

```powershell
# Module: GraphOps.psm1
# Purpose: Common Graph operations for Intune and Entra ID management using Microsoft Graph SDK

function Connect-GraphOps {
    <#
    .SYNOPSIS
        Authenticates to Microsoft Graph using Client Credentials flow.
    .PARAMETER TenantId
        The Azure AD Tenant ID.
    .PARAMETER ClientId
        The Application (Client) ID.
    .PARAMETER ClientSecret
        The Client Secret for the application.
    .EXAMPLE
        Connect-GraphOps -TenantId "0000-0000" -ClientId "1111-1111" -ClientSecret "password"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$TenantId,

        [Parameter(Mandatory = $true)]
        [string]$ClientId,

        [Parameter(Mandatory = $true)]
        [string]$ClientSecret
    )

    try {
        $secString = ConvertTo-SecureString -String $ClientSecret -AsPlainText -Force
        $credential = New-Object System.Management.Automation.PSCredential($ClientId, $secString)
        
        Connect-MgGraph -TenantId $TenantlyId -Credential $credential -ErrorAction Stop
        Write-Information "Successfully connected to Microsoft Graph." -InformationAction Continue
    }
    catch {
        Write-Error "Failed to connect to Microsoft Graph: $($_.Exception.Message)"
        throw
    }
}

function Get-StaleDevices {
    <#
    .SYNOPSIS
        Retrieves Intune managed devices that have not synced within a specified number of days.
    .PARAMETER Days
        The number of days of inactivity to look for. Defaults to 7.
    .EXAMPLE
        Get-StaleDevices -Days 14
    #>
    param(
        [int]$Days = 7
    )

    try {
        $cutoff = (Get-Date).AddDays(-$Days)
        # Using -All to ensure we bypass pagination limits present in raw REST calls
        $devices = Get-MgDeviceManagementManagedDevice -All -ErrorAction Stop
        
        $devices | Where-Object { [datetime]$_.LastSyncDateTime -lt $cutoff }
    }
    catch {
        Write-Error "Failed to retrieve managed devices: $($_.Exception.Message)"
    }
}

function Add-UserToGroup {
    <#
    .SYNOPSIS
        Adds a user to a specific Entra ID group.
    .PARAMETER UserId
        The Object ID of the User.
    .PARAMETER GroupId
        The Object ID of the Group.
    .EXAMPLE
        Add-UserToGroup -UserId "user-guid" -GroupId "group-guid"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    try {
        $params = @{
            "@odata.id" = "https://graph.microsoft.com/v1.0/directoryObjects/$UserId"
        }
        New-MgGroupMemberByRef -GroupId $GroupId -BodyParameter $params -ErrorAction Stop
        Write-Information "User $UserId added to group $GroupId." -InformationAction Continue
    }
    catch {
        Write-Error "Failed to add user to group: $($_.Exception.Message)"
    }
}

function Remove-UserFromGroup {
    <#
    .SYNOPSIS
        Removes a user from a specific Entra ID group.
    .PARAMETER UserId
        The Object ID of the User.
    .PARAMETER GroupId
        The Object ID of the Group.
    .EXAMPLE
        Remove-UserFromGroup -UserId "user-guid" -GroupId "group-guid"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    try {
        Remove-MgGroupMemberByRef -GroupId $GroupId -DirectoryObjectId $UserId -ErrorAction Stop
        Write-Information "User $UserId removed from group $GroupId." -InformationationAction Continue
    }
    catch {
        Write-Error "Failed to remove user from group: $($_.Exception.Message)"
    }
}

function Get-UserLicenses {
    <#
    .SYNOPSIS
        Retrieves the SKU details of licenses assigned to a specific user.
    .PARAMETER UserId
        The User Principal Name (UPN) or Object ID of the user.
    .EXAMPLE
        Get-UserLicenses -UserId "admin@contoso.com"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    try {
        $licenseDetails = Get-MgUserLicenseDetail -UserId $UserId -ErrorAction Stop
        $licenseDetails | Select-Object -Property SkuPartNumber, SkuId
    }
    catch {
        Write-Error "Failed to retrieve licenses for user $UserId: $($_.Exception.Message)"
    }
}

Export-ModuleMember -Function Connect-GraphOps, Get-StaleDevices, Add-UserToGroup, Remove-UserFromGroup, Get-UserLicenses
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ctx-long-ps | cold | run 2 | thinking: NO

**Tok/sec:** 44.1 &nbsp; **Wall sec:** 163.08 &nbsp; **Prompt tokens:** 685 &nbsp; **Output tokens:** 2212

**Response:**

```powershell
# Module: GraphOps.psm1
# Purpose: Common Graph operations for Intune and Entra ID management using Microsoft Graph SDK

function Connect-GraphSession {
    <#
    .SYNOPSIS
        Authenticates to Microsoft Graph using Service Principal credentials.
    .DESCRIPTION
        Uses the Microsoft Graph SDK to establish a connection via Client Secret. 
        This replaces manual OAuth2 token management with the built-in SDK context.
    .PARAMETER TenantId
        The Azure AD Tenant ID.
    .PARAMETER ClientId
        The Application (Client) ID of the registered app.
    .PARAMETER ClientSecret
        The Client Secret of the registered app.
    .EXAMPLE
        Connect-GraphSession -TenantId "tenant-id" -ClientId "client-id" -ClientSecret "secret-value"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$TenantId,

        [Parameter(Mandatory = $true)]
        [string]$ClientId,

        [Parameter(Mandatory = $true)]
        [string]$ClientSecret
    )

    try {
        $secureSecret = ConvertTo-SecureString -String $ClientSecret -AsPlainText -Force
        $credential = New-Object System.Management.Automation.PSCredential($ClientId, $secureSecret)
        
        Connect-MgGraph -TenantId $TenantId -Credential $credential -ErrorAction Stop
        Write-Host "Successfully connected to Microsoft Graph." -ForegroundColor Green
    }
    catch {
        Write-Error "Failed to connect to Microsoft Graph: $($_.Exception.Message)"
    }
}

function Get-StaleDevices {
    <#
    .SYNOPSIS
        Retrieves Intune managed devices that haven't synced in the last 7 days.
    .DESCRIPTION
        Uses server-side filtering via the Microsoft Graph SDK to efficiently identify stale devices.
    .EXAMPLE
        Get-StaleDevices
    #>
    try {
        $cutoff = (Get-Date).AddDays(-7).ToString("yyyy-MM-ddTHH:mm:ssZ")
        # Using -Filter is significantly more efficient than filtering client-side with Where-Object
        Get-MgDeviceManagementManagedDevice -Filter "lastSyncDateTime lt $cutoff" -ErrorAction Stop
    }
    catch {
        Write-Error "Failed to retrieve stale devices: $($_.Exception.Message)"
    }
}

function Add-UserToGroup {
    <#
    .SYNOPSIS
        Adds a user to a specific Entra ID group.
    .PARAMETER UserId
        The Object ID of the user.
    .PARAMETER GroupId
        The Object ID of the group.
    .EXAMPLE
        Add-UserToGroup -UserId "user-uuid" -GroupId "group-uuid"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    try {
        $params = @{
            '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$UserId"
        }
        New-MgGroupMemberByRef -GroupId $GroupId -BodyParameter $params -ErrorAction Stop
        Write-Host "User $UserId added to group $GroupId successfully." -ForegroundColor Green
    }
    catch {
        Write-Error "Failed to add user to group: $($_.Exception.Message)"
    }
}

function Remove-UserFromGroup {
    <#
    .SYNOPSIS
        Removes a user from a specific Entra ID group.
    .PARAMETER UserId
        The Object ID of the user.
    .PARAMETER GroupId
        The Object ID of the group.
    .EXAMPLE
        Remove-UserFromGroup -UserId "user-uuid" -GroupId "group-uuid"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    try {
        Remove-MgGroupMemberByRef -GroupId $GroupId -DirectoryObjectId $UserId -ErrorAction Stop
        Write-Host "User $UserId removed from group $GroupId successfully." -inheritDoc
    }
    catch {
        Write-Error "Failed to remove user from group: $($_.Exception.Message)"
    }
}

function Get-UserLicenses {
    <#
    .SYNOPSIS
        Retrieves the SKU part numbers and IDs for a specific user.
    .PARAMETER UPN
        The User Principal Name (UPN) of the target user.
    .EXAMPLE
        Get-UserLicenses -UPN "admin@contoso.com"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UPN
    )

    try {
        # The SDK automatically resolves UPNs to User IDs for many cmdlets
        Get-MgUserLicenseDetail -UserId $UPN -ErrorAction Stop | Select-Object SkuPartNumber, SkuId
    }
    catch {
        Write-Error "Failed to retrieve licenses for user $UPN: $($_.Exception.Message)"
    }
}

Export-ModuleMember -Function Connect-GraphSession, Get-StaleDevices, Add-UserToGroup, Remove-UserFromGroup, Get-UserLicenses
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## gemma4:26b | ctx-long-ps | cold | run 3 | thinking: NO

**Tok/sec:** 43.2 &nbsp; **Wall sec:** 156.80 &nbsp; **Prompt tokens:** 685 &nbsp; **Output tokens:** 2415

**Response:**

```powershell
# Module: GraphOps.psm1
# Purpose: Common Graph operations for Intune and Entra ID management using Microsoft.Graph SDK

function Connect-GraphSession {
    <#
    .SYNOPSIS
        Authenticates to Microsoft Graph using Client Credentials.
    .DESCRIPTION
        Uses the Microsoft Graph SDK to establish a session using a Tenant ID, Client ID, and Client Secret.
    .PARAMETER TenantId
        The Azure AD Tenant ID.
    .PARAMETER ClientId
        The Application (Client) ID.
        .PARAMETER ClientSecret
        The Client Secret for the application.
    .EXAMPLE
        Connect-GraphSession -TenantId "0000-0000" -ClientId "1111-1111" -ClientSecret "password"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$TenantId,

        [Parameter(Mandatory = $true)]
        [string]$ClientId,

        [Parameter(Mandatory = $true)]
        [string]$ClientSecret
    )

    try {
        $body = @{
            grant_type    = 'client_credentials'
            client_id     = $ClientId
            client_secret = $ClientSecret
            scope         = 'https://graph.microsoft.com/.default'
        }
        $tokenResponse = Invoke-RestMethod -Uri "https://login.microsoftonline.com/$TenantId/oauth2/v2.0/token" -Method Post -Body $body
        
        # Connect to Graph using the acquired access token to avoid global variable dependencies
        Connect-MgGraph -AccessToken $tokenResponse.access_token
        Write-Host "Successfully connected to Microsoft Graph." -ForegroundColor Green
    }
    catch {
        Write-Error "Failed to connect to Microsoft Graph: $($_.Exception.Message)"
    }
}

function Get-StaleDevices {
    <#
    .SYNOPSIS
        Retrieves Intune managed devices that have not synced in the last 7 days.
    .DESCRIPTION
        Queries Microsoft Graph for all managed devices and filters based on the LastSyncDateTime property.
    .EXAMPLE
        Get-StaleDevices
    #>
    try {
        $cutoff = (Get-Date).AddDays(-7)
        # Use -All to handle pagination automatically via SDK
        $devices = Get-MgDeviceManagementManagedDevice -All 
        
        $devices | Where-Object { [datetime]$_.LastSyncDateTime -lt $cutoff }
    }
    catch {
        Write-Error "Error retrieving stale devices: $($_.Exception.Message)"
    }
}

function Add-UserToGroup {
    <#
    .SYNOPSIS
        Adds a user to a specific Entra ID group.
    .DESCRIPTION
        Uses the Microsoft Graph SDK to add a member to a group using the user's ID or UPN.
    .PARAMETER UserId
        The Object ID of the user.
    .PARAMETER GroupId
        The Object ID of the group.
    .EXAMPLE
        Add-UserToGroup -UserId "user@domain.com" -GroupId "group-uuid"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    try {
        $params = @{
            "@odata.id" = "https://graph.microsoft.com/v1.0/directoryObjects/$UserId"
        }
        New-MgGroupMemberByRef -GroupId $GroupId -BodyParameter $params
        Write-Host "User $UserId added to group $GroupId successfully." -ForegroundColor Green
    }
    catch {
        Write-Error "Failed to add user to group: $($_.Exception $^{Exception.Message})"
    }
}

function Remove-UserFromGroup {
    <#
    .SYNOPSIS
        Removes a user from a specific Entra ID group.
    .DESCRIPTION
        Uses the Microsoft Graph SDK to remove a member from a group via their Object ID.
    .PARAMETER UserId
        The Object ID of the user.
    .PARAMETER GroupId
        The Object ID of the group.
    .EXAMPLE
        Remove-UserFromGroup -UserId "user-uuid" -GroupId "group-uuid"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    try {
        Remove-MgGroupMemberByRef -GroupId $GroupId -DirectoryObjectId $UserId
        Write-Host "User $UserId removed from group $GroupId successfully." -ForegroundColor Green
    }
    catch {
        Write-Error "Failed to remove user from group: $($_.Exception.Message)"
    }
}

function Get-UserLicenses {
    <#
    .SYNOPSIS
        Retrieves the license details for a specific user.
    .DESCRIPTION
        Queries the Graph API for the SKU part numbers and IDs assigned to a given User Principal Name (UPN).
    .PARAMETER UPN
        The User Principal Name of the user.
    .EXAMPLE
        Get-UserLicenses -UPN "admin@contoso.com"
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$UPN
    )

    try {
        # Get-MgUserLicenseDetail handles the specific endpoint for license details
        Get-MgUserLicenseDetail -UserId $UPN | Select-Object SkuPartNumber, SkuId
    }
    catch {
        Write-Error "Failed to retrieve licenses for user $UPN: $($_.Exception.Message)"
    }
}

Export-ModuleMember -Function Connect-GraphSession, Get-StaleDevices, Add-UserToGroup, Remove-UserFromGroup, Get-UserLicenses
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | chat-explain | cold | run 1 | thinking: NO

**Tok/sec:** 57.5 &nbsp; **Wall sec:** 37.04 &nbsp; **Prompt tokens:** 41 &nbsp; **Output tokens:** 1515

**Response:**

A homelab is basically your own personal tech playground at home—a mix of servers, routers, switches, and virtual machines you build to experiment outside of work constraints. For IT ops pros, it’s a total game-changer. Instead of worrying about breaking production or waiting for change-management approval, you get a safe sandbox to test tools like Kubernetes or Terraform, practice disaster recovery, or automate workflows with real hardware. It’s the perfect place to keep your skills sharp, prep for certs, and tinker with bleeding-edge tech without corporate red tape. Plus, debugging something at 10 PM in your own lab is way more rewarding (and less stressful) than scrambling through a production ticket queue. Think of it as continuous, hands-on training you control—powered by curiosity instead of a SLA.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | chat-explain | cold | run 2 | thinking: NO

**Tok/sec:** 58.3 &nbsp; **Wall sec:** 29.87 &nbsp; **Prompt tokens:** 41 &nbsp; **Output tokens:** 1221

**Response:**

Think of a homelab as your personal IT playground—a dedicated setup in your home where you can tinker with servers, networking gear, and software without worrying about breaking production at work. For an IT operations pro, it’s basically a risk-free sandbox. You can test new cloud platforms, practice automating deployments with Ansible or Terraform, experiment with security hardening, or just learn a Linux distro when daytime tickets keep you busy. It sharpens your troubleshooting instincts, helps you build real projects for your portfolio, and keeps your skills current without waiting on corporate training budgets or change windows. Plus, you get to “fail forward” safely—learning from broken configs instead of just avoiding them. In short, it’s the ultimate way to turn curiosity into career growth on your own time and terms.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | chat-explain | cold | run 3 | thinking: NO

**Tok/sec:** 58.5 &nbsp; **Wall sec:** 23.03 &nbsp; **Prompt tokens:** 41 &nbsp; **Output tokens:** 824

**Response:**

A homelab is basically your own mini-data center at home—usually a mix of servers, switches, or virtual machines where you can safely tinker with technology. 

For IT operations professionals, it’s a risk-free sandbox. You can experiment with infrastructure-as-code, test new monitoring or automation tools, simulate failovers, and troubleshoot networking issues without the nightmare of breaking production systems. It keeps your skills sharp between projects, lets you explore open-source alternatives to expensive enterprise software, and even powers useful personal services like home media or file servers. 

Plus, a well-documented homelab is a fantastic way to demonstrate hands-on experience during interviews or performance reviews. Think of it as your personal tech gym: the more you play in it, the stronger your instincts become—backed up by snapshots and version control!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | chat-troubleshoot | cold | run 1 | thinking: NO

**Tok/sec:** 53.2 &nbsp; **Wall sec:** 48.74 &nbsp; **Prompt tokens:** 46 &nbsp; **Output tokens:** 2119

**Response:**

Hey, no worries—this is actually super common after Windows updates. Let’s tackle it step-by-step, starting with the simplest and safest checks. Here’s how I’d walk through it with you:

**Step 1: Confirm your regular internet works, then give the VPN app a clean restart**  
First, let’s make sure we’re not accidentally chasing two problems at once. Open your browser and try loading a couple of normal websites or logging into an unrelated work portal. If those load fine, your internet is good, which usually means the VPN app just got left in a slightly "confused" state by the update. Completely close out of the VPN program (right-click its icon near your clock and pick *Quit* or *Exit*, not just minimize it), wait about 10 seconds, then open it fresh. This alone fixes most post-update connection bumps.

**Step 2: Do a full laptop restart**  
If that didn’t clear it up, let’s give Windows a proper reset. I know it’s tempting to just close the lid or click *Restart* from the Start menu, but those sometimes just pause background processes instead of clearing them. A full shutdown and power-on wipes out those temporary update files that can accidentally block your network handshakes. Just go to *Start > Power > Restart*, wait for it to boot up completely, and try connecting again.

**Step 3: Run Windows’ built-in network detective**  
Now we’ll let Windows look under the hood for us. Right-click the little Wi-Fi or plug icon near your clock, choose *Troubleshoot settings*, and click *Network Adapter*. Windows will automatically scan for settings that the update might have accidentally flipped and walk you through a few "Apply this fix" clicks. It’s basically a guided cleanup crew that resets your connection profile without touching anything important.

How does that sound? Want to kick off with Step 1 together, or would you prefer to jump into a quick screen share so I can guide you through it in real time?

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | chat-troubleshoot | cold | run 2 | thinking: NO

**Tok/sec:** 54.2 &nbsp; **Wall sec:** 41.19 &nbsp; **Prompt tokens:** 46 &nbsp; **Output tokens:** 1744

**Response:**

Got it—let’s walk through this together, step by step. Windows updates often change things behind the scenes without announcing it, so we’ll start simple and work our way toward the fix:

**Step 1: Double-check your regular internet first.**  
Sometimes an update quietly resets or tweaks your Wi-Fi/Ethernet drivers, which would naturally block the VPN too. Could you try opening your browser and loading a couple of normal websites like Google or YouTube? Just want to make sure your basic connection is still solid before we dive into the VPN specifically.

**Step 2: Do a full restart and note what happens.**  
Next, please shut down your laptop completely and power it back on—not just closing the lid or hitting sleep. A fresh start clears out temporary glitches the update might have left behind and refreshes how your computer talks to networks. Once it’s back up, try connecting to the VPN again and tell me exactly what you see. Even a quick photo of any pop-up or error message would be incredibly helpful!

**Step 3: Check the VPN app and do a quick network refresh.**  
If your internet is working fine but the VPN still won’t connect, I’ll take a closer look at the VPN software itself. Updates can occasionally change security or routing settings that confuse older or unpatched VPN apps. I’ll make sure the app is up to date, verify your connection profile is still intact, and if needed, reset your network configuration on Windows—which basically just asks your computer to rebuild its “connection roadmap.” This routine usually clears up most post-update VPN hiccups without affecting your files or passwords.

How does that sound? We’ll take it one step at a time, and I’ll guide you through exactly what to click along the way.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | chat-troubleshoot | cold | run 3 | thinking: NO

**Tok/sec:** 52.8 &nbsp; **Wall sec:** 47.74 &nbsp; **Prompt tokens:** 46 &nbsp; **Output tokens:** 2064

**Response:**

Alright, here’s how I’d walk them through it without overwhelming them:

**Step 1: Let’s make sure the internet itself is still healthy.**  
Before we dive into VPN settings, I’d just have them open a browser and try loading two or three normal sites—like their email, a news page, maybe their company intranet. If those load fine, that’s actually good news: it tells us the update didn’t break the actual network connection, so the problem is probably just with the VPN app or its configuration. But if nothing loads at all, then we know the update likely touched something deeper, like the network adapter or Windows’ routing tables, and we’d pivot to fixing the base connection first.

**Step 2: See what Windows and the VPN are actually complaining about.**  
Next, I’d ask them to pay close attention to any error message that pops up when they try to connect, or even just sit with the VPN app open for a minute. Those little messages or spinning icons are like breadcrumbs—they’ll tell us whether it’s failing at login, getting dropped mid-connection, or if Windows has lost track of the VPN client entirely. Sometimes after an update, background services just need a quick wake-up call, so we’d also check that the VPN-related service is running (we can do this in the Services app) and make sure it’s set to start automatically when they boot up.

**Step 3: Let Windows sort out common post-update hiccups, then refresh the client.**  
For the third step, I’d skip guessing and just let Windows run its built-in network troubleshooter. They can find it under Settings > System > Troubleshoot > Other troubleshooters, hit “Run” next to “Network Adapter,” and let it scan for outdated drivers, misconfigured protocols, or temporary cache glitches that updates often leave behind. While that’s working, we’d also give the VPN app a proper restart (not just closing the window—actually exiting it from the system tray). If it still acts up afterward, we’d check if IT has pushed a newer version of the client to match the Windows build, since updates sometimes temporarily break compatibility until the software catches up.

That’s usually enough to either fix it on the spot or give us a clear starting point for the next round of troubleshooting. Want me to draft a quick message I can send them with these steps?

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | chat-summarize | cold | run 1 | thinking: NO

**Tok/sec:** 53.1 &nbsp; **Wall sec:** 47.98 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 2083

**Response:**

Our corporate VPN security certificate expired, causing failed logins to spike from 2 to 340 per hour. IT is currently restoring a valid backup file to resolve the issue. Employees may experience temporary access delays. We’re tracking progress and will update you once service is fully restored.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | chat-summarize | cold | run 2 | thinking: NO

**Tok/sec:** 54.8 &nbsp; **Wall sec:** 34.39 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 1389

**Response:**

We are experiencing widespread VPN login failures due to a security certificate error. Authentication rejections have surged from 2 per hour to 340 per hour, severely disrupting user access. Our team is actively reverting a recent certificate update to resolve the issue. Restoration efforts are underway; no action required on your part.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | chat-summarize | cold | run 3 | thinking: NO

**Tok/sec:** 54.6 &nbsp; **Wall sec:** 38.85 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 1629

**Response:**

The corporate VPN security certificate expired on June 1, causing a massive spike in connection failures (jumping from 2 to 340 per hour). Employees are currently unable to connect to the company network remotely. IT is actively restoring the previous valid certificates to resolve the issue. Service should resume once the fix completes.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ps-graph-device-list | cold | run 1 | thinking: NO

**Tok/sec:** 51.8 &nbsp; **Wall sec:** 104.32 &nbsp; **Prompt tokens:** 65 &nbsp; **Output tokens:** 4940

**Response:**

Here's a complete, production-ready PowerShell script that meets your requirements:

```powershell
<#
.SYNOPSIS
    Lists all Intune-managed Windows devices where the last sync is older than 7 days.
.DESCRIPTION
    Uses the Microsoft.Graph module to query the /deviceManagement/managedDevices endpoint.
    Applies -Filter and -Select as requested, handles pagination with -All, and formats output.
.NOTES
    Requires: Install-Module Microsoft.Graph.DeviceManagement.ManagedDevices
              RunConnect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"
#>

# 1. Ensure connected to Microsoft Graph
if (-not (Get-MgContext)) {
    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
    Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All" -NoWelcome
}

# 2. Calculate cutoff date (7 days ago) in UTC RFC3339 format required by OData/Graph API
$cutoffDate = (Get-Date).ToUniversalTime().AddDays(-7).ToString("yyyy-MM-ddTHH:mm:ssZ")

# 3. Define OData filter string
#    'ne null' ensures we only evaluate devices that have actually synced at least once
$filter = "lastSyncDateTime ne null and lastSyncDateTime lt '$cutoffDate'"

# 4. Query Graph API using -Filter and -Select, expand results across all pages with -All
Get-MgDeviceManagementManagedDevice -Filter $filter -Select deviceName, lastSyncDateTime, complianceState -All |
    Select-Object deviceName, lastSyncDateTime, complianceState |
    Format-Table -AutoSize

# Optional: Export to CSV instead of console output
# Get-MgDeviceManagementManagedDevice ... | Export-Csv -Path "OldSyncDevices.csv" -NoTypeInformation -Encoding UTF8
```

### Key Implementation Details:
1. **`-Filter`**: Uses OData v4 syntax compatible with Graph API `v1.0`. The date is formatted to RFC3339 (`yyyy-MM-ddTHH:mm:ssZ`) which Graph expects for datetimeoffset comparisons.
2. **`-Select`**: Fetches only the three requested properties from the endpoint, reducing payload size and improving performance.
3. **`-All`**: Intune environments often contain hundreds/thousands of devices. `-All` handles Graph's implicit pagination automatically.
4. **Null Handling**: Added `ne null` to the filter so devices that have never synced (where `lastSyncDateTime` is `null`) are excluded from the results, matching the semantic meaning of "last sync is older than 7 days".
5. **Output Formatting**: `Select-Object` ensures the exact column names requested are passed through, and `Format-Table -AutoSize` provides a clean console view.

### Prerequisites:
```powershell
# Run once per environment
Install-Module Microsoft.Graph.DeviceManagement.ManagedDevices -Force -Scope CurrentUser
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ps-graph-device-list | cold | run 2 | thinking: NO

**Tok/sec:** 51.7 &nbsp; **Wall sec:** 113.10 &nbsp; **Prompt tokens:** 65 &nbsp; **Output tokens:** 5385

**Response:**

Here's a complete, production-ready PowerShell script that meets your requirements. It uses the modern `Microsoft.Graph` module, applies OData filtering, reduces payload size with `-Select`, and handles Graph API pagination automatically.

```powershell
#Requires -Modules Microsoft.Graph

# Ensure you're connected to Microsoft Graph
if (-not (Get-MgContext)) {
    Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"
}

# Calculate the cutoff date (7 days ago) in UTC ISO 8601 format required by Graph API
$cutoffDate = [datetime]::UtcNow.AddDays(-7).ToString("yyyy-MM-ddTHH:mm:ssZ")

# Construct OData filter: Windows devices only + lastSync older than 7 days
$filter = "osType eq 'Windows' and lastSyncDateTime le '$cutoffDate'"

# Retrieve devices using -Filter and -Select, with -All to traverse all API pages
Get-MgDeviceManagementManagedDevice `
    -Filter $filter `
    -Select @('deviceName', 'lastSyncDateTime', 'complianceState') `
    -All |
    Select-Object @{N='DeviceName';E={$_.deviceName}},
                  @{N='LastSyncDateTime';E={$_.lastSyncDateTime}},
                  @{N='ComplianceState';E={$_.complianceState}} |
    Format-Table -AutoSize

# Clean up session (optional but recommended for scripts)
Disconnect-MgGraph -ErrorAction SilentlyContinue
```

### Key Features:
1. **`-Filter`**: Uses native OData syntax to push filtering to the server (`osType eq 'Windows' and lastSyncDateTime le '<date>'`). This reduces bandwidth and improves performance.
2. **`-Select`**: Explicitly requests only the three needed properties. Graph API will omit all other device data, significantly speeding up execution for large environments.
3. **`-All`**: Microsoft Graph defaults to 20 results per page. `-All` automatically handles `$skiptoken` pagination so you get every matching device without manual loops.
4. **Date Handling**: Uses `[datetime]::UtcNow.AddDays(-7)` and formats it to UTC ISO 8601 (`yyyy-MM-ddTHH:mm:ssZ`), which is strictly required by the Graph API for accurate datetime comparisons.
5. **Output Formatting**: Maps the Graph camelCase properties to your requested PascalCase headers exactly as specified.

### Prerequisites:
- Run with an account that has `DeviceManagementManagedDevices.Read.All` or `DeviceManagementManagedDevices.ReadWrite.All` application or delegated permissions in Entra ID (Azure AD).
- Module version 2.x+: `Install-Module Microsoft.Graph -Scope CurrentUser`

> 💡 **Note**: Devices with a `null` last sync date are intentionally excluded by the `le` operator. If you want to include devices that have *never* synced, append `or lastSyncDateTime eq null` to the filter string.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ps-graph-device-list | cold | run 3 | thinking: NO

**Tok/sec:** 51.6 &nbsp; **Wall sec:** 109.29 &nbsp; **Prompt tokens:** 65 &nbsp; **Output tokens:** 5178

**Response:**

Here's a complete, production-ready PowerShell script using the `Microsoft.Graph` module. It leverages OData `-Filter` for server-side narrowing and `Select-Object` (the PowerShell equivalent of `-Select`) for clean output formatting.

```powershell
#Requires -Modules Microsoft.Graph.DeviceManagement
Import-Module Microsoft.Graph.DeviceManagement

# 1. Authenticate to Microsoft Graph with required permissions
# Note: In production, consider using Connect-MgGraph -TenantId <id> or device code flow
Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"

# 2. Calculate the cutoff date (7 days ago) in ISO 8601 format required by OData
$cutoffDate = (Get-Date).ToUniversalTime().AddDays(-7).ToString("o")

# 3. Build the OData filter string
$filter = "osType eq 'Windows' and lastSyncDateTime lt $cutoffDate"

# 4. Query Intune managed devices
# -Filter: Applies server-side OData filtering
# -All: Handles pagination automatically across large tenant inventories
Get-MgDeviceManagementManagedDevice -Filter $filter -All | 
    # Output only the requested columns using Select-Object (-Select)
    Select-Object DeviceName, LastSyncDateTime, ComplianceState | 
    Format-Table -AutoSize
```

### 🔑 Key Implementation Notes:
| Feature | Implementation Details |
|--------|------------------------|
| **`-Filter`** | Uses OData v4 syntax directly in the Graph endpoint. Filters out non-Windows devices and devices synced within the last 7 days at the API level, reducing payload size & latency. |
| **Date Format** | Graph requires ISO 8601 (`yyyy-MM-ddTHH:mm:ss.fffffff+zz:z` or `Z`). `.ToString("o")` guarantees strict compliance across all PowerShell versions/timezones. |
| **`-Select` / Output** | `Select-Object` is PowerShell's native `-Select` mechanism. It extracts exactly `DeviceName`, `LastSyncDateTime`, and `ComplianceState` from the Graph object graph before formatting. |
| **Pagination** | `-All` ensures the cmdlet handles `$skiptoken` pagination automatically, returning all matching devices regardless of tenant size. |
| **Scopes** | `DeviceManagementManagedDevices.Read.All` is the minimum required permission for Intune device inventory. |

### 💡 Optional: Server-Side Property Selection (`$select`)
If you're working with very large environments (>10k devices) and want to minimize network payload, Microsoft.Graph v2+ supports OData `$select` via the `-Property` parameter:
```powershell
Get-MgDeviceManagementManagedDevice -Filter $filter -Property DeviceName,LastSyncDateTime,ComplianceState -All |
    Select-Object DeviceName, LastSyncDateTime, ComplianceState | Format-Table -AutoSize
```
*(The original script already works perfectly for 95%+ of use cases. Use `-Property` only if you profile and confirm network overhead is a bottleneck.)*

### 📦 Prerequisites
1. Install the module: `Install-Module Microsoft.Graph.DeviceManagement -Scope CurrentUser`
2. Run in PowerShell 7+ or Windows PowerShell 5.1
3. Ensure your account has the **Intune Reader** role or delegated Graph permissions assigned in Entra ID.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ps-graph-app-assignment | cold | run 1 | thinking: NO

**Tok/sec:** 52.2 &nbsp; **Wall sec:** 92.63 &nbsp; **Prompt tokens:** 52 &nbsp; **Output tokens:** 4383

**Response:**

Here's a complete, production-ready PowerShell function using the Microsoft Graph REST API via `Invoke-MgGraphRequest`. It includes robust error handling, group resolution, pagination support, and clear intent mapping.

```powershell
function Get-IntuneAppAssignments {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory = $true, HelpMessage = 'Display name of the Intune app to query')]
        [ValidateNotNullOrEmpty()]
        [string]$AppName
    )

    # 1. Find the app by display name
    $appUri = "https://graph.microsoft.com/beta/deviceAppManagement/mobileApps?`$filter=displayName eq '$AppName'&`$top=1"
    
    try {
        $apps = Invoke-MgGraphRequest -Uri $appUri -Method Get
    }
    catch {
        throw "Failed to connect to Microsoft Graph or retrieve app data. Check your authentication and permissions. Error: $_"
    }

    # Explicit error handling for app not found
    if (-not $apps.value -or $apps.value.Count -eq 0) {
        throw "App with display name '$AppName' was not found in Intune. Verify the exact display name or check if it's a Win32/Office deployment (requires different Graph endpoints)."
    }

    $appId = $apps.value[0].id
    Write-Verbose "Found app: $($apps.value[0].displayName) (ID: $appId)"

    # 2. Retrieve assignments with pagination support
    $assignmentsUri = "https://graph.microsoft.com/beta/deviceAppManagement/mobileApps/$appId/assignments"
    $allAssignments = @()

    do {
        try {
            $pageData = Invoke-MgGraphRequest -Uri $assignmentsUri -Method Get
        }
        catch {
            throw "Failed to retrieve assignments for app '$AppName'. Error: $_"
        }

        if ($pageData.value) {
            $allAssignments += $pageData.value
        }
        $assignmentsUri = $pageData.'@odata.nextLink'
    } while ($assignmentsUri)

    # 3. Process assignments and resolve group names
    $results = foreach ($assignment in $allAssignments) {
        # Only process group-based assignments (skip user/device direct assignments)
        if ($assignment.target.'@odata.type' -ne '#microsoft.graph.groupAssignmentTarget') {
            continue
        }

        $groupId = $assignment.target.groupId
        $intent = $assignment.intent
        
        # Resolve Group ID to Display Name
        $groupUri = "https://graph.microsoft.com/beta/groups/$groupId"
        try {
            $groupObj = Invoke-MgGraphRequest -Uri $groupUri -Method Get
            $groupName = if ($groupObj.displayName) { $groupObj.displayName } else { '<Unknown Group>' }
        }
        catch {
            $groupName = '<Failed to resolve group (check permissions)>'
        }

        # Normalize intent for readability
        $normalizedIntent = switch ($intent.ToLower()) {
            'required'         { 'Required' }
            'available'        { 'Available' }
            'enforceAvailable' { 'Enforce Available' }
            default            { $intent }
        }

        [PSCustomObject]@{
            AppDisplayName   = $apps.value[0].displayName
            GroupName        = $groupName
            GroupId          = $groupId
            AssignmentIntent = $normalizedIntent
        }
    }

    # 4. Return results or informational message
    if ($results.Count -eq 0) {
        Write-Warning "No group-based assignments found for app '$AppName'."
        return @()
    }

    return $results
}
```

### 🔑 Prerequisites & Permissions
1. **Module**: Requires `Microsoft.Graph` PowerShell module (`Install-Module Microsoft.Graph`)
2. **Authentication**: Run `Connect-MgGraph -Scopes "DeviceManagementManagedApps.Read.All","Group.Read.All"` before calling the function.
3. **Required API Scopes**:
   - `DeviceManagementManagedApps.Read.All` (or `.ManagedDevices.Read.All`)
   - `Group.Read.All`

### 📝 Usage Example
```powershell
# Query assignments for a specific app
$assignments = Get-IntuneAppAssignments -AppName "Contoso Mobile App"

# Display results in a formatted table
$assignments | Format-Table -AutoSize

# Export to CSV
$assignments | Export-Csv -Path "C:\Temp\IntuneApp_Assignments.csv" -NoTypeInformation -Encoding UTF8
```

### 💡 Notes
- **Graph Version**: Uses `/beta` because Intune app assignment metadata is fully supported there. For production, you can swap to `/v1.0` once Microsoft stabilizes the endpoint for your specific app type.
- **App Types Covered**: This queries `mobileApps`, which includes iOS, Android, macOS, Office Apps, and modern management apps. If you're specifically looking for **Win32** or **Microsoft Store** deployments, change the base URI to `/beta/deviceAppManagement/win32AndWindowsStoreApps`.
- **Target Types**: The function intentionally filters out direct user or device assignments (only returns `groupAssignmentTarget`). If you need those, remove the `$odata.type` check.
- **Pagination**: Built-in loop handles scenarios where an app has >100 group assignments.

Let me know if you need it adapted for Win32 apps, PowerShell SDK v2 cmdlets, or to output additional metadata (like eligibility filtering).

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ps-graph-app-assignment | cold | run 2 | thinking: NO

**Tok/sec:** 51.6 &nbsp; **Wall sec:** 133.69 &nbsp; **Prompt tokens:** 52 &nbsp; **Output tokens:** 6446

**Response:**

Here's a production-ready PowerShell function that uses the Microsoft Graph API (via `Invoke-MgGraphRequest`) to locate an Intune app by display name, retrieve its group assignments, and resolve group display names with proper error handling and pagination support.

```powershell
function Get-IntuneAppAssignments {
    <#
    .SYNOPSIS
        Retrieves the groups assigned to a specific Intune mobile application.
    .DESCRIPTION
        Queries Microsoft Graph for an app matching the provided display name,
        fetches its assignments, filters for group targets, and resolves group 
        display names. Returns a list of custom objects containing Group ID, 
        Group Name, Assignment Intent (required vs available), and source.
    .PARAMETER AppName
        The exact display name of the Intune application to search for.
    .EXAMPLE
        Get-IntuneAppAssignments -AppName "Contoso Line of Business App"
    .NOTES
        Requires Microsoft.Graph.Authentication module.
        Required Graph Permissions: DeviceManagementManagedApps.Read.All, Directory.Read.All
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, ValueFromPipeline = $true)]
        [ValidateNotNullOrEmpty()]
        [string]$AppName,

        [switch]$SkipAuthCheck
    )

    begin {
        if (-not (Get-Module -Name Microsoft.Graph.Authentication)) {
            throw "Please install the Microsoft.Graph module: Install-Module Microsoft.Graph"
        }
    }

    process {
        # 1. Handle Authentication
        if (-not $SkipAuthCheck) {
            if ((Get-MgContext).Account -eq $null) {
                try {
                    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
                    Connect-MgGraph -Scopes "DeviceManagementManagedApps.Read.All", "Directory.Read.All"
                } catch {
                    throw "Failed to authenticate to Microsoft Graph. Ensure you have valid credentials and required permissions.`nError: $_"
                }
            }
        }

        # 2. Find the App by Display Name
        $safeAppName = $AppName.Replace("'", "''") # OData requires escaping single quotes
        $appUri = "https://graph.microsoft.com/beta/deviceAppManagement/mobileApps?`$filter=displayName eq '$safeAppName'&`$select=id,displayName"

        try {
            $appResponse = Invoke-MgGraphRequest -Uri $appUri -Method Get
            if (-not $appResponse.value -or $appResponse.value.Count -eq 0) {
                throw "App with display name '$AppName' was not found in Intune."
            } elseif ($appResponse.value.Count -gt 1) {
                Write-Warning "Multiple apps matched '$AppName'. Using the first result: $($appResponse.value[0].displayName)"
            }
        } catch {
            throw "Error searching for app '$AppName': $_"
        }

        $resolvedAppId   = $appResponse.value[0].id
        $resolvedAppName = $appResponse.value[0].displayName

        # 3. Retrieve Assignments (with pagination)
        $assignmentsUri = "https://graph.microsoft.com/beta/deviceAppManagement/mobileApps/$resolvedAppId/assignments"
        $allAssignments = @()
        
        try {
            do {
                $page = Invoke-MgGraphRequest -Uri $assignmentsUri -Method Get
                $allAssignments += $page.value
                $assignmentsUri = $page.'@odata.nextLink'
            } while ($assignmentsUri)
        } catch {
            throw "Failed to retrieve assignments for app '$resolvedAppName'. Error: $_"
        }

        if (-not $allAssignments) {
            Write-Host "No assignments found for app: '$resolvedAppName'" -ForegroundColor Yellow
            return @()
        }

        # 4. Filter Group Assignments & Resolve Names
        $results = foreach ($assignment in $allAssignments) {
            # Only process group assignment targets
            if ($assignment.target.'@odata.type' -ne '#microsoft.graph.groupAssignmentTarget') { continue }

            $groupId = $assignment.target.groupId
            $intent  = $assignment.intent

            # Resolve Group Display Name (single call per group)
            $groupName = "Unresolved"
            try {
                $groupUri = "https://graph.microsoft.com/beta/groups/$groupId?`$select=displayName"
                $groupResp = Invoke-MgGraphRequest -Uri $groupUri -Method Get
                $groupName = $groupResp.displayName
            } catch {
                Write-Verbose "Could not resolve group ID: $groupId"
            }

            [PSCustomObject]@{
                AppName   = $resolvedAppName
                GroupId   = $groupId
                GroupName = $groupName
                Intent    = $intent # 'required' or 'availableWithoutEnrollment'
                Source    = $assignment.source
            }
        }

        if ($results.Count -eq 0) {
            Write-Host "App '$resolvedAppName' has no group assignments." -ForegroundColor Yellow
        } else {
            Write-Host "Found $($results.Count) group assignment(s) for app: '$resolvedAppName'" -ForegroundColor Green
        }

        return $results
    }
}
```

### 🔑 Key Features
1. **OData-Safe Querying**: Properly escapes single quotes and uses `$select` to minimize payload size.
2. **Pagination Support**: Handles large assignment collections gracefully using `@odata.nextLink`.
3. **Group Name Resolution**: Automatically resolves `groupId` to human-readable `GroupName` via a secondary Graph call.
4. **Intent Mapping**: Returns the exact Graph API intent value (`required` or `availableWithoutEnrollment`). Note: The Intune portal sometimes labels available deployments as "Available", but Graph standardizes it.
5. **Error Handling**: 
   - Fails fast on auth issues or missing permissions
   - Explicit 404 handling for missing apps
   - Safe fallbacks when group resolution fails (e.g., deleted/deprovisioned groups)

### 📦 Requirements & Setup
```powershell
# Install module if needed
Install-Module Microsoft.Graph -Force

# Import module
Import-Module Microsoft.Graph.Authentication

# Run function (auto-connects if not already connected)
Get-IntuneAppAssignments -AppName "Your Intune App Name" | Format-Table AppName, GroupName, Intent, Source -AutoSize
```

### 🔐 Required Permissions
Ensure your authenticated account has at least these delegated or application permissions:
- `DeviceManagementManagedApps.Read.All`
- `Directory.Read.All`

### 💡 Usage Tips
- **Case Sensitivity**: OData `eq` is case-insensitive by default in Graph, but exact matches work best.
- **Performance**: If an app has hundreds of groups, resolution will take additional API calls. You can skip name resolution by modifying the inner `try/catch` to just return `$groupId`.
- **Multiple Apps**: If multiple apps share the same display name, the function logs a warning and uses the first result. Add `-Filter "appType eq 'windowsStoreApp'"` or similar to the app URI if disambiguation is needed.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ps-graph-app-assignment | cold | run 3 | thinking: NO

**Tok/sec:** 51.5 &nbsp; **Wall sec:** 143.16 &nbsp; **Prompt tokens:** 52 &nbsp; **Output tokens:** 6914

**Response:**

Here's a production-ready PowerShell function that meets your requirements. It uses the Microsoft Graph API, handles pagination, filters for group assignments specifically, safely resolves group details, and includes explicit error handling for missing apps.

```powershell
function Get-IntuneAppGroupAssignments {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true, HelpMessage='The exact display name of the Intune app')]
        [string]$AppName
    )

    # Verify Graph connection
    $ctx = Get-MgContext
    if (-not $ctx -or -not $ctx.Account.Id) {
        throw "Not authenticated to Microsoft Graph. Please run: Connect-MgGraph -Scopes 'DeviceManagementApps.Read.All'"
    }

    try {
        # 1. Search for the app by display name
        $encodedName = [uri]::EscapeDataString($AppName)
        $appsUri = "https://graph.microsoft.com/beta/deviceAppManagement/mobileApps?`$filter=displayName eq '$encodedName'&`$select=id,displayName"
        $appsResp = Invoke-MgGraphRequest -Method GET -Uri $appsUri

        if ($appsResp.'@odata.count' -eq 0 -or (-not $appsResp.value)) {
            throw "Intune app with display name '$AppName' was not found."
        }

        # Handle multiple matches (gracefully pick first, warn user)
        if ($appsResp.'@odata.count' -gt 1) {
            Write-Warning "Multiple apps match '$AppName'. Using the first result: $($appsResp.value[0].displayName)"
        }

        $appId = $appsResp.value[0].id

        # 2. Fetch assignments (with pagination support)
        $assignmentsUri = "https://graph.microsoft.com/beta/deviceAppManagement/mobileApps/$appId/assignments"
        $allAssignments = @()
        do {
            $assignResp = Invoke-MgGraphRequest -Method GET -Uri $assignmentsUri
            $allAssignments += $assignResp.value
            if ($assignResp.'@odata.nextLink') {
                $assignmentsUri = $assignResp.'@odata.nextLink'
            } else {
                break
            }
        } while ($true)

        # 3. Filter for group assignments only & resolve group details
        $results = @()
        foreach ($assignment in $allAssignments) {
            # Only process explicit group assignments (ignores all-users, device filters, etc.)
            if ($assignment.target.'@odata.type' -eq '#microsoft.graph.groupAssignmentTarget') {
                $groupId = $assignment.target.mobileAppGroupId
                
                if ($groupId) {
                    try {
                        $groupUri = "https://graph.microsoft.com/beta/groups/$groupId"
                        $group = Invoke-MgGraphRequest -Method GET -Uri $groupUri
                        
                        $results += [PSCustomObject]@{
                            AppName            = $appsResp.value[0].displayName
                            Intent             = $assignment.intent
                            GroupId            = $groupId
                            GroupDisplayName   = $group.displayName
                            GroupType          = if ($group.groupTypes) { $group.groupTypes -join ',' } else { 'Security/Distribution' }
                        }
                    } catch {
                        # Handle deleted groups or permission gaps gracefully
                        $results += [PSCustomObject]@{
                            AppName            = $appsResp.value[0].displayName
                            Intent             = $assignment.intent
                            GroupId            = $groupId
                            GroupDisplayName   = 'Unknown (Permission Denied or Deleted)'
                            GroupType          = 'N/A'
                        }
                    }
                }
            }
        }

        # 4. Output results
        if ($results.Count -eq 0) {
            Write-Information "No group assignments found for app '$AppName'." -InformationAction Continue
        } else {
            return $results | Sort-Object Intent, GroupDisplayName
        }

    } catch [System.Management.Automation.MethodInvocationException], [System.Net.WebException] {
        # Catch specific Graph/API errors
        Write-Error "Graph API Error: $_"
    } catch {
        Write-Error "Unexpected error: $_"
    }
}
```

### 🔑 Key Features
1. **Explicit App Not Found Handling**: Throws a clear, actionable error if the display name yields zero results.
2. **Pagination Aware**: Recursively follows `@odata.nextLink` so apps with 100+ assignments aren't truncated.
3. **Group-Only Filtering**: Checks `@odata.type` to strictly return `#microsoft.graph.groupAssignmentTarget`, ignoring device, user, or filter-based targets.
4. **Graceful Group Resolution**: Wraps group lookups in a try/catch to handle soft-deleted groups or permission restrictions without breaking the entire function.
5. **Intent Mapping**: Returns the raw Graph intent (`required` or `available`) which aligns with the Intune console.

### 📋 Prerequisites & Usage
```powershell
# Install if needed (run once)
Install-Module Microsoft.Graph.Intune -Scope CurrentUser

# Connect with required scopes
Connect-MgGraph -Scopes "DeviceManagementApps.Read.All"

# Run the function
Get-IntuneAppGroupAssignments -AppName "Contoso Line of Business App" | Format-Table
```

### ⚠️ Notes
- Uses `/beta` endpoint for maximum Intune compatibility. If your tenant enforces strict version policies, change `https://graph.microsoft.com/beta/` to `https://graph.microsoft.com/v1.0/`.
- Requires `DeviceManagementApps.Read.All` and `Group.Read.All` delegated or application permissions.
- Display name matching is case-insensitive per Graph default behavior, but exact matches prevent ambiguous results. Use wildcards in the prompt or pass the exact console name for best results.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | runbook-offboard | cold | run 1 | thinking: NO

**Tok/sec:** 52.6 &nbsp; **Wall sec:** 74.77 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 3463

**Response:**

# Runbook: Employee Offboarding (Microsoft 365 / Intune)

**Runbook ID:** OFFBOARD-M365-001  
**Owner:** IT Operations / Identity Management  
**Last Updated:** 2024-05-22  
**Risk Level:** High (Data loss risk if licenses/devices removed prematurely; compliance risk if data is not secured).

---

## ⚠️ Critical Prerequisites & Warnings
*   **Access Required:** Global Admin or User Administrator rights for M365/Entra ID; Intune Administrator; Exchange Online Management rights.
*   **Wipe Caution:** Device wiping requires the device to be online. If the user has immediate notice, they may wipe their own device before this step completes. Coordinate timing carefully.
*   **Archiving vs. Retention:** Modern environments use **Retention Policies** rather than manual mailbox archiving. Consult with architecture before enabling In-Place Archiving, as it requires a specific license (Exchange Online Archiving). If no archive license exists, use a Microsoft 365 retention policy.
*   **Licensing:** Do not remove licenses until data handover and archiving are confirmed to avoid accidental mailbox locking or deletion.

---

## 📋 Offboarding Execution Checklist

### Phase 1: Preparation & Data Handover
| # | Action Steps | Done |
| :-- | :--- | :-: |
| **1.1** | **Notify Stakeholders:** Confirm offboarding date with manager and security team. | [ ] |
| **1.2** | **Mailbox Forwarding (Optional):** If required by policy, set up mailbox forwarding to the manager or successor in Exchange Admin Center. *Note: Remove forward immediately upon final deletion.* | [ ] |
| **1.3** | **SharePoint/OneDrive Ownership:** Update ownership of shared resources. Transfer OneDrive content if mandated by policy. Ensure compliance with data retention policies for cloud storage. | [ ] |
| **1.4** | **Calendar Sharing:** Grant "Editor" access to the user's calendar to the successor for transition handover. | [ ] |

### Phase 2: Identity & Access Control (Entra ID / M365)
| # | Action Steps | Done |
| :-- | :--- | :-: |
| **2.1** | **Block Sign-In:**<br>1. Go to **Microsoft 365 Admin Center** > **Users** > **Active users**.<br>2. Select the user.<br>3. On the **Account** tab, check **Block sign-in** and select **Yes**.<br>4. Click **Save changes**. | [ ] |
| **2.2** | **Hide from GAL:** (Recommended)<br>1. With the user still selected in M365 Admin Center, go to the **Account** tab.<br>2. Check **Hide from address lists** and select **Yes**.<br>3. Click **Save changes**. | [ ] |
| **2.3** | **Revoke All Active Sessions:**<br>1. In the user profile in M365 Admin Center, click **More actions** > **Revoke sign-in sessions**.<br>2. Confirm the warning to force logout across all devices/apps immediately.<br><br>*Alternative via PowerShell:* `Revoke-AzureADUserAllRefreshToken -ObjectId <UserPrincipalName>` | [ ] |
| **2.4** | **Remove from Security Groups:** Remove the user from distribution lists, security groups, and Azure AD Direct Access assignments to prevent residual permissions. | [ ] |

### Phase 3: Mailbox Archiving & Retention
| # | Action Steps | Done |
| :-- | :--- | :-: |
| **3.1** | **Enable In-Place Archive:**<br>1. Go to **Exchange Admin Center** > **Recipients** > **Mailboxes**.<br>2. Find and select the user.<br>3. Under **Mailbox features**, locate **In-Place Archive**.<br>4. Click **Turn on**. Assign a license if prompted and not already assigned.<br><br>*Verification:* Check that the archive mailbox is "Ready" in the Exchange portal. | [ ] |
| **3.2** | **Apply Retention Policy (If applicable):**<br>1. Go to **Microsoft Purview compliance portal** > **Sensitivity labels** or **Retention policies**.<br>2. Ensure a retention policy is assigned to the mailbox that preserves emails for the required legal/compliance period (e.g., 7 years). | [ ] |
| **3.3** | **Verify Archive Access:** Confirm via Outlook/OWA that the archive mailbox is visible and accessible for the successor or manager. | [ ] |

### Phase 4: Device Management (Intune)
| # | Action Steps | Done |
| :-- | :--- | :-: |
| **4.1** | **Locate Device(s):**<br>1. Go to **Intune Admin Center** > **Devices** > **All devices**.<br>2. Filter by the user's name/UPN to identify all enrolled devices. | [ ] |
| **4.2** | **Determine Action:** Based on company policy:<br>*   **Wipe:** Device must be returned and sanitized. Removes all data, apps, and corporate profiles.<br>*   **Retire:** Device is kept by user. Removes only corporate data, MDM profile, and enterprise apps; personal data remains. | [ ] |
| **4.3** | **Execute Action (Per Device):**<br>1. Select the device in Intune.<br>2. Click **Device actions** > Choose **Wipe device** OR **Retire device**.<br>3. Add a comment (e.g., "Offboarding - [Date]") and confirm.<br><br>*Note:* The status will show as pending until the device checks in. Monitor for completion. | [ ] |
| **4.4** | **Verify Retention Status:**<br>1. In Intune, check the **Device compliance** and **Inventory** tab to ensure the device status updates to "Not Compliant" or "Retired". | [ ] |

### Phase 5: Cleanup & Licensing
| # | Action Steps | Done |
| :-- | :--- | :-: |
| **5.1** | **Remove Licenses:**<br>1. Return to **M365 Admin Center** > **Users** > **Active users**.<br>2. Select user > **Licenses and apps** tab.<br>3. Unassign all licenses (Exchange, Intune, Office 365 E3/E5, etc.).<br>*Note:* Licenses may take up to 24 hours to be fully removed from the system. | [ ] |
| **5.2** | **Mailbox Delete/Retention:**<br>1. If retaining mailbox indefinitely: Leave object disabled.<br>2. If deleting after retention period: Mark for deletion in Exchange Portal (becomes recoverable for 30 days). | [ ] |
| **5.3** | **Final Verification:**<br>1. Attempt to login as the user (should fail with "Account Disabled").<br>2. Verify device no longer appears as active in Intune after grace period.<br>3. Confirm archive mailbox is retained per policy. | [ ] |
| **5.4** | **Documentation:** Update HR records and access review logs. Close the offboarding ticket. | [ ] |

---

## 🔧 Troubleshooting & Notes
*   **Intune Wipe Fails:** If a device fails to wipe, ensure it is connected to Wi-Fi. You may need to send the command again or physically reset the device.
*   **Archive License Error:** If enabling archive fails due to licensing, you may need to assign an "Exchange Online Archiving" add-on license before turning on the feature, then remove it after (depending on tenant configuration).
*   **Session Revocation Delay:** Sometimes MFA prompts or cached tokens can cause brief re-authentication. Session revocation forces a token refresh; if the user is in the process of logging in during revocation, they may get one more prompt before being blocked.
*   **Shared Mailbox Migration:** If this role is transitioning to a shared mailbox, configure delegation and licensing changes *before* removing the user license to prevent data loss.

## 📜 Sign-Off
**Executed By:** __________________________  
**Date:** _______________  
**Approved By:** __________________________

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | runbook-offboard | cold | run 2 | thinking: NO

**Tok/sec:** 51.9 &nbsp; **Wall sec:** 84.85 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 3937

**Response:**

# Microsoft 365 / Intune Employee Offboarding Runbook

> **Purpose:** Standardized, auditable procedure for securely offboarding users from Microsoft Entra ID, Exchange Online, and Intune.
> **Prerequisites:** HR termination ticket, manager approval, backup/export of critical files (OneDrive/SharePoint), conditional access policy review.
> **Note:** "Disabling the account" and "Blocking sign-in" are functionally identical in modern Microsoft Entra ID. Both actions are covered in Step 1 below.

| # | Action / Description | Instructions & Commands | Done |
|---|----------------------|-------------------------|------|
| 1 | **Disable Account & Block Sign-in** | 1. Go to [Microsoft Entra admin center](https://entra.microsoft.com) → Identity → Users → All users.<br>2. Select the user → **Account** tab.<br>3. Under **Account enabled**, toggle to **No** (or set **Block sign-in** = Yes).<br>4. Click **Save**. <br>⚠️ *This prevents all future authentication but does not terminate existing sessions.* | `[ ]` |
| 2 | **Revoke Active Sessions** | **Portal:** User profile → **Sign-in activity** → ⋮ **More actions** → **Revoke all active sessions**.<br>**PowerShell (Recommended):**<br>`Connect-MgGraph -Scopes "User.RevokeSessions.All"`<br>`Revoke-MgUserSignInSession -UserId "<userPrincipalName>"`<br>✅ Verify sign-in activity log shows `0` active tokens. | `[ ]` |
| 3 | **Archive Mailbox** | 1. Go to [Exchange admin center](https://admin.exchange.microsoft.com) → Recipients → Mailboxes.<br>2. Select user → **Mailbox features** → **Archive mailbox** → **Enable**.<br>3. Choose *Standard* or *In-Place* archive based on licensing (requires Exchange Online Plan 1/2 or E3/E5).<br>4. If retention is required: set retention tags, grant delegated permissions, or configure forwarding rules before license removal.<br>✅ Confirm status shows **Active** (may take up to 60 mins). | `[ ]` |
| 4 | **Wipe/Retire Device via Intune** | 1. Go to [Intune admin center](https://intune.microsoft.com) → Devices → All devices.<br>2. Search user’s device → Select → **More actions**:<br>&nbsp;&nbsp;• **Retire & wipe corporate data** (keeps personal apps/files)<br>&nbsp;&nbsp;• **Wipe and delete** (full format, corporate-owned only)<br>3. Monitor **Device status** until `Compliant` / `Deleted`.<br>4. Remove device record from Intune after successful wipe to free license slot. | `[ ]` |
| 5 | **Clean Up Licenses, Groups & Access** | • **Licenses:** Entra → Users → `<user>` → Licenses → **Remove all** (or reassign).<br>• **Groups:** Entra → Groups → Review membership → Remove from all security/M365 groups.<br>• **App Registrations/Spouse:** Check `Enterprise applications` → `My apps` access for user-specific app registrations; remove or transfer ownership.<br>• **Service accounts/Automation:** Update runbooks, SPNs, or connected systems referencing the account. | `[ ]` |
| 6 | **Post-Offboarding Verification & Documentation** | ✅ Run verification checklist:<br>1. Sign-in blocked (`Get-MgUser -UserId "<UPN>" -Property signInActivity | Select signInActivity`)<br>2. All sessions revoked (0 active tokens in audit log)<br>3. Mailbox archive Active & accessible by delegate<br>4. Device wiped/retired & removed from Intune inventory<br>5. Licenses freed, groups cleared, access transfers confirmed<br>📄 Log completion in ticketing system with timestamps, commands run, and approver sign-off. Archive this runbook. | `[ ]` |

### 🔑 Quick Reference Notes
| Scenario | Recommended Action |
|----------|-------------------|
| **Company-owned device** | Use `Wipe and delete` in Intune to perform secure format before asset return. |
| **BYOD / Personal device** | Use `Retire & wipe corporate data` to preserve user privacy while removing MDM/MAM policies, apps, and profiles. |
| **Mailbox retention > 30 days** | Convert mailbox to *Shared Mailbox* first, then archive, before removing licenses (retention expires after license removal). |
| **Automated Offboarding** | Consider Microsoft Graph API or Power Automate flows for conditional access removal, session revocation, and device wipe triggers. |

> ⚠️ **Critical:** Never remove licenses or disable accounts before confirming data archival, delegation transfers, and backup completion. This runbook should be executed within 15 minutes of the employee’s offboarding trigger to minimize security exposure.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | runbook-offboard | cold | run 3 | thinking: NO

**Tok/sec:** 51.7 &nbsp; **Wall sec:** 83.12 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 3828

**Response:**

# Microsoft 365 / Intune Employee Offboarding Runbook

| Step | Action / Procedure | Target System | Done |
|------|-------------------|---------------|------|
| **1** | **Archive Mailbox**<br>• Navigate to Exchange Admin Center → Recipients → Mailboxes.<br>• Select the offboarding user → Unified Archiving (or In-Place Archive).<br>• Enable archive. If already enabled, verify status shows `Connected` (not `Synchronizing`).<br>• *Note:* Archive requires an active Exchange license. Ensure license remains assigned until archive is fully provisioned. | Exchange Admin Center / M365 Portal | ☐ |
| **2** | **Revoke Active Sessions**<br>• Go to Entra admin center → Identity → Users → Select user.<br>• On the Account tab, click **Revoke sessions** (or navigate to Sign-in logs → Filter by UPN → Revoke).<br>• Confirm prompt. This invalidates all refresh tokens and forces re-authentication on next attempt.<br>• Verify in Sign-in logs that new authentication attempts return `Refresh token revoked`. | Microsoft Entra ID | ☐ |
| **3** | **Block Sign-In**<br>• In the same Entra user profile, locate the **Block sign-in** toggle at the top of the overview page.<br>• Set to **Yes** and Save. This is immediate and prevents all authentication (interactive & non-interactive).<br>• Verify via Sign-in logs that attempts now fail with `Sign-in blocked by admin`. | Microsoft Entra ID | ☐ |
| **4** | **Disable Account**<br>• In the user's profile → Account tab → Set **Account enabled** to **No**.<br>• This permanently removes login capability and detaches conditional access/policy bindings.<br>• *Note:* Keep account disabled (not deleted) for 30–90 days per policy to allow mailbox recovery, group reassignment, or audit trace. | Microsoft Entra ID | ☐ |
| **5** | **Wipe or Retire Device(s)**<br>• Go to Intune admin center → Devices → All devices.<br>• Filter by enrolled user → Select target device(s).<br>• Choose action based on policy:<br>  - **Wipe**: Factory reset, deletes personal & corporate data. Use for lost/stolen/high-risk.<br>  - **Retire**: Removes Intune enrollment & corporate apps/profiles only. Retains personal data. Use for standard returns.<br>• Confirm and monitor device status until it shows `Wiped` or `Retired`. | Microsoft Intune | ☐ |
| **6** | **Post-Offboarding Cleanup**<br>• Remove all M365/Intune licenses (except archive license if retention is active).<br>• Remove from security groups, Azure AD roles, and delegated admin grants.<br>• Update shared resource ownership (Teams chats, SharePoint, OneDrive, Planner).<br>• Document completion in HR/IT offboarding tracker. | M365 Admin Center / Entra ID | ☐ |

### 🔐 Execution Notes
- **Order Matters:** Archive first to preserve data while licenses are active. Revoke sessions before blocking/disabling to catch any lingering background syncs.
- **Compliance Holds:** If litigation/legal holds apply, enable `Retention Policy` or `Litigation Hold` before mailbox archive steps.
- **Device Sync Window:** Wipe/Retire commands may take 15–60 mins to process depending on device connectivity & Intune service health.
- **Auditing:** All actions are captured in Entra ID Audit Logs, Intune Activity Log, and Exchange Mailbox audit log. Export logs for compliance documentation.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | runbook-cert-rotation | cold | run 1 | thinking: NO

**Tok/sec:** 51.7 &nbsp; **Wall sec:** 80.22 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 3682

**Response:**

## Runbook: Rotate Expired SCEP Certificate Profile in Microsoft Intune

| **Document Info** | **Details** |
| :--- | :--- |
| **Runbook Title** | Rotate Expired SCEP Certificate Profile in Intune |
| **Owner** | Identity & Access Management / MDM Admin Team |
| **Risk Level** | **High** – Improper execution may result in mass device outages (Wi-Fi, Auth, App access). |
| **Change Control** | **REQUIRED** – Must follow ITIL Change Management process. See approval section below. |
| **Duration** | 30–60 Minutes (+ Sync lag time) |
| **Prerequisites** | • Admin Center Global Admin or Intune Administrator rights.<br>• Access to NDES/ADCS (if SCEP is CA-backed).<br>• Test device assigned to the policy group. |

---

### 🛑 Change Control Approval Notes
**[MANDATORY]** This procedure affects device configuration and certificate issuance infrastructure.
1.  **Request:** Create a Standard or Emergency Change Request based on outage status.
2.  **Approval:** Requires approval from:
    *   **Mdm/Identity Lead:** For profile logic validation.
    *   **PKI/Certification Authority Owner:** To verify backend NDES/ADCS readiness (if applicable).
    *   **Service Desk Manager:** Notification of potential device sync issues or user impact during rollout.
3.  **Notification:** Communicate maintenance window to users if automated enrollment is disrupted.

---

### Phase 1: Identification & Assessment
*Goal: Determine the scope of impact and verify backend readiness.*

#### Step 1.1: Identify Affected Devices
1.  Log in to **Microsoft Intune Admin Center**.
2.  Navigate to **Reports** > **Device configuration** > **Details**.
3.  In the filter pane, search for the expired profile name.
4.  Click the profile to view assignments.
5.  Navigate to **Certificates** report:
    *   Go to **Reports** > **Devices** > **Certificates**.
    *   Filter by **Certificate Source**: `SCEP`.
    *   Filter by **Profile Name**: Select your profile.
    *   Check **Status** for failures or devices with expiration dates close to the current date.
6.  *Output:* Document count of affected devices and critical user groups (e.g., Executives, Kiosk).

#### Step 1.2: Verify Backend PKI / NDES Status
*Note: Updating Intune alone is insufficient if the backend credential or template is mismatched.*
1.  If using **NDES/ADCS**, verify the NDES server is healthy.
2.  Ensure the **Certificate Template** is available and permissions allow the machine/service account to request/renew certificates.
3.  *Check:* Request a test certificate via PowerShell on the NDES endpoint to ensure issuance works.

---

### Phase 2: Profile Rotation Procedure
*Goal: Update the SCEP profile configuration and trigger renewal.*

**[CHANGE CONTROL CHECKPOINT]** Confirm Change ID is active and approvals are recorded.

#### Step 2.1: Backup Current Configuration (Optional but Recommended)
1.  Export current profile settings or take a screenshot of the **Configuration** tab for rollback reference.

#### Step 2.2: Update SCEP Profile in Intune
1.  Navigate to **Devices** > **Configuration profiles**.
2.  Locate and select the expired SCEP profile.
3.  Click **Properties**.
    *   **Update Name:** Append `_ROTATED_[Date]` or update per naming convention.
    *   **Description:** Update with Change Request ID.
4.  Click **Configuration settings** > **Edit**.
5.  **Critical SCEP Configuration Checks:**
    *   **Key Storage Provider:** Ensure `Microsoft Software Key Storage Provider` is selected.
    *   **Key Type:** Ensure key type matches original (usually `RSA`).
    *   **Key Size:** Verify size remains consistent to avoid key mismatch errors.
    *   **Renewal:** Ensure **Certificate renewal** is checked.
        *   *Best Practice:* Set **Days before expiration** to a value appropriate for your rotation schedule (e.g., 15 days).
6.  Click **OK**, then **Save**.

#### Step 2.3: Verify Assignments
1.  Go to **Assignments**.
2.  Confirm target groups are still active and correct.
3.  *Action:* If the profile was duplicated, delete the old/expired profile reference if legacy, or ensure the new profile supersedes the old one based on priority settings (SCEP profiles generally do not supersede; both may coexist causing key collisions).
    *   *Recommendation:* **Do not** simply create a second active SCEP profile for the same device unless designed for split-phase. Update the existing profile to renew.

---

### Phase 3: Force Sync & Trigger Renewal
*Goal: Ensure devices receive the update and begin the renewal process.*

#### Step 3.1: Force Cloud Policy Refresh
*Devices will update automatically on their next sync, but this runbook requires immediate action.*
1.  Navigate to **Devices** > **Managed devices**.
2.  Select a **Test Device** first.
3.  Click **Sync** > **Cloud policy channel status**.
4.  Click **Refresh device configuration and monitoring policies**.
5.  *Repeat for Target Devices:*
    *   For small groups: Repeat manually per device or use the "Assign to Group" feature to re-trigger sync via group membership change (toggle assignment off/on).
    *   *Script Alternative:* If available, use `Invoke-IntuneManagementExtensionRefresh` on managed devices via PowerShell/Graph.

#### Step 3.2: Monitor Intune Status
1.  Return to the SCEP Profile > **Overview**.
2.  Monitor the **Success/Failure** metrics in real-time.
3.  Wait for device reports to populate (may take 5–10 minutes).

---

### Phase 4: Verification
*Goal: Confirm certificate health and device functionality.*

#### Step 4.1: Verify Certificate on Device
1.  On the test device, open **Certificate Manager** (`certlm.msc`).
2.  Navigate to **Personal** > **Certificates**.
3.  Locate the SCEP certificate.
4.  Confirm:
    *   **Valid From/To:** Expiration is updated.
    *   **Issuer:** Matches NDES/ADCS issuer.
    *   **Key Usage:** Correct for intended purpose (e.g., Client Auth, Encryption).

#### Step 4.2: Verify Intune Health
1.  In Intune, go to the Profile > **Overview** tab.
2.  Confirm **Total Devices**: Successful count matches expected.
3.  Check **Errors**: Filter by error type. Common false positives include `DeviceNotEnrolled` or `PolicyChannelFailed`; investigate actual certificate errors like `KeyContainerDoesNotExist`.

#### Step 4.3: Validate Functional Connectivity
*Perform for critical user groups if possible.*
1.  Test Wi-Fi connectivity (if SCEP used for Wi-Fi auth).
2.  Test Outlook/Exchange ActiveSync connectivity.
3.  Test SSO to Azure AD / Identity Provider applications.

---

### Phase 5: Rollback Plan
*Execute if critical failures occur during validation.*

1.  **Policy Revert:** If the new configuration causes key corruption, revert properties in Intune to previous state and Save.
2.  **Certificate Cleanup:** On affected devices, clear certificates via **Settings** > **Accounts** > **Access work or school** > **Disconnect** (if re-enrollment is safe) or manually remove cert from `certlm.msc` and trigger policy refresh.
3.  **NDES Check:** If errors indicate `CertReq failed`, rollback NDES changes immediately and restore previous template permissions.
4.  **Change Request:** Update Change Request with failure details. Initiate incident if user impact persists.

---

### Troubleshooting & Known Issues
| Issue | Potential Cause | Resolution |
| :--- | :--- | :--- |
| **Key Mismatch / Key Storage Provider Error** | Profile attributes changed (Key size/type) or NDES credential mismatch. | Ensure key attributes match exactly. Verify NDES `WebEnroll.config` permissions. |
| **Certificate not renewed on device** | Device did not sync or SCEP protocol error. | Manually refresh policy. Check `IntuneManagementExtension.log` on device for errors. |
| **Multiple Certificates for same user/device** | Profile added without removing old reference; NDES issued new cert without detecting renewal. | Ensure `Renewal` flag is set in Intune. Verify NDES template allows certificate renewal. |
| **High Error Count after Sync** | Mass sync overwhelmed NDES or CA queue. | Stagger syncs by disabling assignments and re-enabling groups in batches over 1 hour. |

---

### Post-Implementation Sign-off
*Completed by Role:* _________________  
*Date/Time:* _______________________  
*Verification Result:* ☐ Success  ☐ Partial  ☐ Failed (Rollback Initiated)  

**Change Request Closeout:** Update Change Record with verification results and link to Intune report screenshots.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | runbook-cert-rotation | cold | run 2 | thinking: NO

**Tok/sec:** 52.5 &nbsp; **Wall sec:** 75.62 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 3497

**Response:**

# Runbook: Rotate Expired SCEP Certificate Profile in Microsoft Intune

| **Metadata** | |
| :--- | :--- |
| **Title** | SCEP Certificate Profile Rotation & Renewal |
| **System** | Microsoft Intune / Entra ID / AD CS (ADCS) |
| **Role Required** | Intune Administrator, PKI Administrator |
| **Estimated Duration** | 30–60 Minutes |
| **Risk Level** | Medium (Network/Certificate Impact) |
| **Last Updated** | YYYY-MM-DD |

---

## ⚠️ Critical Safety Notices
1.  **Certificate Rotation Scope:** This procedure applies when the SCEP configuration is expiring, the Certificate Template has changed, or the underlying ADCS infrastructure requires a CA rotation requiring new SCEP enrollment access points.
2.  **Service Disruption:** Misconfiguration can block devices from enrolling or connecting to Wi-Fi/network resources that rely on this certificate profile.
3.  **Change Control:** All steps marked with **[CHANGE CONTROL]** require a documented Change Request (CR) and approval per organizational policy before execution.

---

## 1. Prerequisites
*   Access to Microsoft Intune Portal (`intune.microsoft.com`).
*   Read/Write access to the PKI Console or ADCS Server.
*   PowerShell with `IntunePowerShellModule` installed (optional but recommended).
*   Current SCEP Profile ID and Certificate Template Name.
*   **Approved Change Request** for modifying certificate infrastructure or mass profile reassignment.

---

## 2. Identify Affected Devices & Validate Scope

### 2.1. Verify SCEP Profile Expiration/Status
1.  Navigate to **Devices** > **Configuration profiles**.
2.  Select the affected SCEP profile.
3.  Click **Monitoring** > **Device status**.
    *   Check for devices reporting `Error` or `Warning` related to certificate expiration.
4.  Click **Monitoring** > **Profile install status**.
    *   Identify devices where the profile is not installed or failed validation.

### 2.2. Identify Devices Requiring Immediate Attention
> **Runbook Step:** Target devices that are currently expiring within <7 days or have already failed authentication due to cert expiry.

*   **Portal Method:** Use the device list filtered by `Configuration profiles` status. Export CSV for reporting.
*   **PowerShell Method:**
    ```powershell
    # Identify profile ID first
    $Profile = Get-IntuneDeviceEnrollmentConfiguration -Filter "microsoft.graph.scepCertificateConfiguration" | Where-Object {$_.DisplayName -eq "<Profile Name>"}
    
    # Get devices with specific error codes related to expiration (Example code 542873601 for cert issue)
    # Note: Intune API allows filtering, but exporting and parsing is often faster for large fleets.
    $Devices = Get-IntuneManagedDevice -Filter "configurationProfileInstallStates/any(x:x/profileId eq '$($Profile.Id)' and x/installError eq '542873601')"
    ```

---

## 3. Prepare Rotation Changes [CHANGE CONTROL]

> **[CHANGE CONTROL REQUIRED]**: Do not proceed without an approved CR for modifying the SCEP profile, Certificate Template, or Enrollment Access Point URLs.

### 3.1. Backup Current Configuration
*   Export the current SCEP configuration settings (Template name, Key Size, URL, EAP config XML if applicable) to a secure location.
*   Document the `Enrollment Access Point URL` and `EAP Configuration XML`.

### 3.2. Update ADCS / Certificate Template
*   *If rotating due to CA change:* Ensure the new CA certificate is trusted by the SCEP endpoint service account.
*   *If updating template permissions:* Request changes to the **Certificate Template** properties (e.g., Key Usage, Enrollment permissions) via the PKI team.
*   **Action:** Update the `CN=CertificateTemplate` on the ADCS server if required by the rotation scope.
*   **Validation:** Test a manual SCEP enrollment from a test device against the updated template/URL.

---

## 4. Execute Profile Rotation

> **Best Practice:** Create a **new** profile and remove the old one to avoid configuration conflicts during transition, rather than editing in-place. If editing in-place is required, ensure "Re-enroll existing certificates" is handled correctly.

### Option A: Deploy New Profile (Recommended)
1.  Navigate to **Devices** > **Configuration profiles** > **Create profile**.
    *   Platform: Windows / macOS / iOS & iPadOS (as applicable).
    *   Profile type: **Certificate policies and identifiers** > **SCEP Certificate**.
2.  Configure the SCEP settings:
    *   **Enrollment Access Point URL:** Update to new endpoint if rotated.
    *   **EAP Configuration XML:** Paste updated XML if required by CA rotation.
    *   **Certificate Template Name:** Update if template name changed.
    *   **Key Size / Algorithm:** Update per security policy.
3.  **Assignments:**
    *   **Group A (Test Group):** Assign to a small pilot group containing <5 devices representing all impacted device types.
    *   **Action:** **[CHANGE CONTROL REQUIRED]** Confirm CR approval before assigning to Production groups.

### Option B: Update Existing Profile
1.  Select the existing SCEP profile.
2.  Click **Properties**.
3.  Update fields (URL, Template, Key Size).
4.  **Crucial Setting:** Ensure **"Re-enroll existing certificates"** is configured as needed. If this is left default, devices may keep the old cert until it expires or manual intervention is required.
5.  **Assignments:** Review and save. Changes propagate automatically over time; force sync for testing.

---

## 5. Force Sync & Validate on Test Group

### 5.1. Force Device Sync
*   **Manual:** On test device, go to **Settings** > **Accounts** > **Access work or school** (or **Enrollment status**) > **Sync**.
*   **PowerShell (Remote):**
    ```powershell
    Invoke-IntuneDeviceSync -DeviceId "<Test_Device_ID>"
    ```

### 5.2. Validate Certificate Installation
1.  On a test device, open `certlm.msc` (or `certmgr.msc`).
2.  Navigate to **Personal** > **Certificates**.
3.  Verify:
    *   [x] New certificate is present.
    *   [x] Issuer matches the new CA.
    *   [x] Validity period is correct (e.g., new expiration date).
    *   [x] Key Usage includes intended usages (Client Auth, etc.).
4.  **Wi-Fi/Network Verification:** Attempt to connect to a resource requiring this certificate (e.g., Corporate Wi-Fi) and verify connectivity.

---

## 6. Production Deployment & Verification

### 6.1. Rollout to Production
1.  If Test Group validation passes:
    *   Remove devices from the Test Assignment group (if using Option A).
    *   Assign profile to **Production Groups**.
2.  Monitor **Monitoring** > **Device status** for spikes in errors.

### 6.2. Broad Verification
1.  Wait 4–8 hours for natural sync cycles, or script a force sync for critical devices.
2.  **Intune Reporting:**
    *   Check **Profile install status**. Success rate should be >95% within 24 hours.
    *   Check **Device compliance** logs for any SCEP-related violations.
3.  **Certificate Validation:**
    ```powershell
    # Example script to check certificate health on a device (requires local admin or remote session)
    $Cert = Get-ChildItem -Path Cert:\LocalMachine\My | Where-Object {$_.Issuer -like "*NewCA*"}
    Write-Host "Device:" $env:COMPUTERNAME "Cert Valid To:" $Cert.NotAfter
    ```

---

## 7. Rollback Plan [CHANGE CONTROL]

> **[CHANGE CONTROL REQUIRED]**: Rollback operations require approval if they affect production availability.

1.  **If new profile fails:**
    *   Remove the new SCEP profile assignment from all production groups immediately.
    *   Re-assign the previous version of the profile (if valid/backup exists).
    *   If using Option B, revert property changes to backup values.
2.  **Device Remediation:**
    *   Instruct users to delete the expired certificate (`certlm.msc` > Delete) and run `scepclient.exe /renew` or force a profile sync if auto-renewal is broken.
3.  **Communication:** Notify affected stakeholders of rollback status via Change Management tools.

---

## 8. Post-Implementation Checklist

*   [ ] SCEP Profile monitoring shows healthy status for >95% of devices.
*   [ ] Test devices successfully connected to Wi-Fi/Network resources using new cert.
*   [ ] Intune Compliance policies reporting "Compliant" regarding certificate requirements.
*   [ ] Change Request closed in ITSM tool.
*   [ ] Notification sent to helpdesk with known issues/resolution steps (if applicable).

---

## 9. Troubleshooting Common Issues

| Symptom | Potential Cause | Resolution |
| :--- | :--- | :--- |
| Devices report "SCEP URL not found" | Incorrect Enrollment Access Point URL or firewall block. | Verify URL accessibility from device subnet. Check SCEP endpoint logs on ADCS for 404 errors. |
| Certificate issued but invalid usage | Template configuration mismatch. | Review AD CS Template properties; ensure "Enroll" permissions include the device group/OU. |
| `scepclient.exe` fails with error 13 | Authentication failure between Intune and CA. | Check **Enrollment Service Point** authentication settings in ADCS manager. Verify TLS certificate on SCEP endpoint. |
| Profile stays "Pending" | Device blocked by Conditional Access or MDM policy. | Review Conditional Access policies; check device health for blockers. |

---

**End of Runbook**

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | runbook-cert-rotation | cold | run 3 | thinking: NO

**Tok/sec:** 52.4 &nbsp; **Wall sec:** 78.73 &nbsp; **Prompt tokens:** 53 &nbsp; **Output tokens:** 3657

**Response:**

# Runbook: Rotate Expired SCEP Certificate Profile in Microsoft Intune

| **Document Info** | |
| :--- | :--- |
| **Runbook Title** | Rotation of Expired SCEP Certificate Profile |
| **Component** | Microsoft Intune / PKI Infrastructure |
| **Risk Level** | **Medium-High** (Affects device authentication, WiFi, Email, and App access) |
| **Estimated Duration** | 45–60 Minutes (excluding CA interaction time) |
| **Owner** | MDM/Certificate Administration Team |
| **Last Reviewed** | YYYY-MM-DD |

---

## ⚠️ Change Control & Approval Matrix

| Step Category | Action | Requires Change Control? | Notes |
| :--- | :--- | :---: | :--- |
| **Assessment** | Identify affected devices / Export list | No | Informational. |
| **Preparation** | Create new SCEP profile in Test Group | No | Configuration change within sandbox/pilot. |
| **Deployment** | Assign new profile to Production Group | **YES** | Deployment of certificate configurations requires approval to prevent mass lockout or re-enrollment storms. |
| **Enrollment** | Update Enrollment Profile assignments | **YES** | If the certificate ID changes, linked enrollment profiles may be affected. |
| **Cleanup** | Disable/Delete old profile | No | Post-verification housekeeping. |

> **💡 Critical Warning:** Never disable or delete the current SCEP profile until the new profile is verified on a significant subset of devices. Doing so will cause immediate certificate expiration for all devices, resulting in mass connectivity and authentication failures.

---

## 1. Prerequisites
-   **Roles:** Global Administrator, Intune Admin, or Certificate Manager role in Azure AD / Entra ID.
-   **Access:** Access to the on-premises/Cloud CA (if specific CA certificate updates are required alongside SCEP).
-   **Test Group:** A pre-defined security group containing a representative sample of devices (e.g., 3–5% of total, spanning OS types and users).
-   **CA Requirements:** Ensure the underlying CA is healthy and capable of issuing certificates for the duration specified.

---

## 2. Phase 1: Identify Affected Devices & Current State

**Goal:** Quantify scope and establish a baseline of device health.

1.  Navigate to **Microsoft Intune Admin Center** > **Devices** > **Configuration profiles**.
2.  Select the expired **SCEP Certificate Profile**.
3.  Click **Monitoring** > **Devices** (or **Reports** depending on portal version).
4.  Export the report to CSV.
5.  **Analyze Report:**
    -   Count total devices assigned.
    -   Filter by status: `Enrolled`, `Failed`, `Not Started`.
    -   *Action:* If >10% are already in `Failed` status, investigate pre-existing issues before rotation.
6.  **Verify CA Connectivity:**
    -   Open the SCEP profile settings.
    -   Note the **SCEP Server URL**, **Authenticator**, and **CA Certificate**.
    -   Ensure the CA certificate chain is valid on the Intune managed device(s).

---

## 3. Phase 2: Create New Profile (Test Group)

**Goal:** Deploy a renewed profile with extended validity to a controlled pilot group.

1.  Click **+ Create** > **Profile** > **Platform**: Select OS (e.g., Windows, iOS/iPadOS).
2.  **Profile type**: Select **SCEP**.
3.  **Basics**:
    -   Name: `SCEP-Renew-[Date]-PROD` (e.g., `SCEP-Renew-20231027`).
    -   Description: `Rotation of expired SCEP profile. Validity extended to [New Date].`
4.  **Configuration Settings**:
    -   ⚠️ **Crucial:** Copy all settings from the old profile exactly (Subject Name format, Extension certificates, Key usage, etc.).
    -   Modify only the fields requiring change:
        -   `Certificate validity period`: Set to new expiration date.
        -   `Serial number generation`: Keep as `Automatic` or match previous setting.
        -   `CA certificate`: Update if the CA cert itself is rotating; otherwise, keep same thumbprint/URL.
5.  **Assignments**:
    -   Add your **Test Group** to Required (or Included).
    -   **Do not assign to All Devices yet.**
6.  Review + Create.

---

## 4. Phase 3: Force Sync & Wait Time

**Goal:** Trigger certificate issuance on pilot devices.

### A. Force Device Sync
1.  Navigate to **Devices** > **All devices**.
2.  Select a device from the Test Group.
3.  Click **Sync** > **Yes**.
4.  Repeat for all devices in the Test Group.
    -   *Automation Option:* Use PowerShell `Invoke-IntuneDeviceSync` if preferred.
5.  **Wait Time:** Allow **15–30 minutes** for SCEP handshake, CA issuance, and re-enrollment to complete.

### B. Monitor Issuance Logs (Optional but Recommended)
1.  Check the Intune logs or CA event viewer for successful certificate requests from pilot devices.
2.  Ensure no `SCEP Server URL` connectivity errors occur during this window.

---

## 5. Phase 4: Verification

**Goal:** Confirm new certificates are installed and valid.

1.  **Intune Portal Check:**
    -   Return to the **New SCEP Profile** > **Monitoring** > **Devices**.
    -   Verify Status is `Enrolled` with `Certificate Expiration` date in the future.
    -   Ensure no new errors appear.
2.  **Manual Device Validation (Sample Device):**
    -   On a pilot device, open CMD/PowerShell.
    -   Run `certutil -store my`.
    -   Verify:
        -   Issuer matches the CA.
        -   Expiration date is updated.
        -   Subject contains expected identity strings.
3.  **Functionality Check:**
    -   Test WiFi, Email (EAS), and any apps protected by device authentication.
    -   Verify no re-enrollment loops are occurring in `Configuration Manager Logs` or `CertificateEnroll.log`.

---

## 6. Phase 5: Production Rollout

**Approval Required: Change Control Ticket Approved ✅**

1.  **Expand Scope:**
    -   Edit the **New SCEP Profile**.
    -   Add **All Devices** (or relevant production groups) to Required assignments.
    -   *Best Practice:* If using "Update Assignment," ensure the old profile is removed or disabled to prevent conflicts.
2.  **Monitor Deployment:**
    -   Watch the Monitoring dashboard for spikes in `Failed` statuses during the rollout window.
    -   Allow **1–4 hours** depending on fleet size and network conditions.

---

## 7. Phase 6: Decommission Old Profile

1.  Wait until at least **95%** of devices report `Enrolled` on the new profile.
2.  Edit the **Old/Expired SCEP Profile**.
3.  Remove all assignments (or disable via "Delete").
4.  *Recommendation:* Keep the old profile in a disabled state for **7 days** as a rollback reference before permanent deletion.

---

## 🚨 Rollback Plan

| Scenario | Action |
| :--- | :--- |
| **Mass Failure on New Profile** | 1. Immediately remove production assignments from the new profile.<br>2. Add assignments back to the old profile (if disabled but not deleted).<br>3. Force sync all devices to revert to previous state. |
| **CA Connectivity Issue** | 1. Verify CA health and network connectivity from Intune gateway.<br>2. If CA is down, pause rotation and open incident ticket with PKI team.<br>3. Do not force sync until CA is restored. |
| **Re-enrollment Storm** | 1. Reduce assignment scope to smaller groups.<br>2. Check for device-specific errors (e.g., invalid key usage).<br>3. Adjust payload and retest. |

---

## 🔧 Troubleshooting & Tips

-   **SCEP Authenticator:** If the authenticator is a string/password, ensure it is updated in both Intune and the CA SCEP configuration if rotated.
-   **Wi-Fi Profile Conflicts:** Ensure the Wi-Fi/Email configuration profiles referencing this certificate are compatible with the new SAN/Subject requirements. Changing `Subject Name Format` often breaks existing profiles; test thoroughly.
-   **Device Logs:** On Windows, check `%ProgramData%\Microsoft\Crypto\RSA\MachineKeys` or Event Viewer > Applications and Services Logs > Microsoft > Windows > CertificateServices-Client.
-   **iOS/iPadOS:** Check `Profile Manager` settings on the device for error messages if enrollment fails silently.

---

## ✅ Sign-off

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Requester** | | | |
| **Change Approver** | | | |
| **Executor** | | | |
| **Verifier** | | | |

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | script-daily-health | cold | run 1 | thinking: NO

**Tok/sec:** 51.4 &nbsp; **Wall sec:** 65.00 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 2876

**Response:**

Here is a robust, repeatable bash script designed for an Ubuntu homelab. It checks the required metrics, handles thresholds, and outputs clean one-line summaries suitable for cron logging or terminal output.

### `homelab-healthcheck.sh`

```bash
#!/usr/bin/env bash
# ==============================================================================
# Homelab Daily Health Check Script
# Checks: Ollama Service, Disk Usage, Ollama API, Open WebUI Docker Container
# Platform: Ubuntu
# Usage: bash homelab-healthcheck.sh
# ==============================================================================

set -o pipefail

# --------------------------- Configuration ------------------------------------
CONTAINER_NAME="open-webui"       # Change if your container name differs
DISK_WARN_THRESHOLD=80            # Warning level (%)
DISK_FAIL_THRESHOLD=90            # Critical failure level (%)
OLLAMA_API_URL="http://localhost:11434/api/tags"  # Ollama API endpoint
OLLAMA_TIMEOUT=5                  # Seconds to wait for API response

# --------------------------- Helper Functions ---------------------------------
print_result() {
    # Output format: [STATUS] CHECK_NAME - Details
    local status="$1" check="$2" detail="$3"
    echo "[$status] $check - $detail"
}

# --------------------------- Checks -------------------------------------------

# 1. Ollama Service Status (systemd)
check_service() {
    if systemctl is-active --quiet ollama; then
        print_result "PASS" "Service" "Ollama systemd service is active."
    else
        print_result "FAIL" "Service" "Ollama systemd service is inactive or failed."
    fi
}

# 2. Disk Usage (Root partition by default)
check_disk() {
    # Get usage percentage of root (/). Adjust mount point if models are on a different disk.
    local percent
    percent=$(df / | awk 'NR==2 {gsub(/%/,""); print $5}')

    if [[ -z "$percent" ]]; then
        print_result "FAIL" "Disk" "Unable to read disk usage."
        return
    fi

    if (( percent >= DISK_FAIL_THRESHOLD )); then
        print_result "FAIL" "Disk" "Usage critical: ${percent}% (>90%)."
    elif (( percent >= DISK_WARN_THRESHOLD )); then
        print_result "WARN" "Disk" "Usage high: ${percent}% (>80%)."
    else
        print_result "PASS" "Disk" "Usage healthy: ${percent}%."
    fi
}

# 3. Ollama API Responsiveness
check_api() {
    local http_code
    # Request tags to verify both connectivity and model availability
    http_code=$(curl -s -o /dev/null -w "%{http_code}" --max-time "$OLLAMA_TIMEOUT" "$OLLAMA_API_URL" 2>/dev/null || echo "000")

    if [[ "$http_code" == "200" ]]; then
        print_result "PASS" "API" "Ollama responded successfully (HTTP 200)."
    elif [[ "$http_code" == "000" ]]; then
        print_result "FAIL" "API" "Connection failed or timeout."
    else
        print_result "FAIL" "API" "Unexpected response: HTTP $http_code."
    fi
}

# 4. Docker Container State (Open WebUI)
check_docker() {
    local status
    # Query container state safely
    status=$(docker inspect --format='{{.State.Status}}' "$CONTAINER_NAME" 2>/dev/null || echo "not_found")

    if [[ "$status" == "running" ]]; then
        print_result "PASS" "Docker" "Container '$CONTAINER_NAME' is running."
    else
        print_result "FAIL" "Docker" "Container status: $status."
    fi
}

# --------------------------- Execution ----------------------------------------
echo "--- Homelab Health Check ---"
check_service
check_disk
check_api
check_docker
echo "--- End of Health Check ---"
```

### Installation & Usage

1.  **Save the script**:
    ```bash
    mkdir -p ~/homelab-scripts
    nano ~/homelab-scripts/homelab-healthcheck.sh
    # Paste content above, save and exit
    chmod +x ~/homelab-scripts/homelab-healthcheck.sh
    ```

2.  **Manual Test**:
    ```bash
    bash ~/homelab-scripts/homelab-healthcheck.sh
    ```

3.  **Automate Daily via Cron**:
    Edit crontab: `crontab -e`
    Add line to run daily at 8 AM and log results:
    ```cron
    0 8 * * * /usr/bin/bash /home/YOUR_USER/homelab-scripts/homelab-healthcheck.sh >> /var/log/homelab-health.log 2>&1
    ```

### Notes
- **Disk Check**: The script checks the root `/` partition by default. If your Ollama models are stored on a separate mount (e.g., `/data`), change `df /` to `df /data` in the script.
- **Docker Container**: Ensure `$CONTAINER_NAME` matches your actual Open WebUI container name (verify with `docker ps`).
- **Ollama Service**: This assumes Ollama was installed via the official installer which registers `ollama.service`. If you use a custom service name, update the `systemctl` command.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | script-daily-health | cold | run 2 | thinking: NO

**Tok/sec:** 51.8 &nbsp; **Wall sec:** 120.00 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 5751

**Response:**

Here's a production-ready, idempotent Bash script tailored for your requirements. It includes configurable parameters, consistent one-line output formatting, and safe error handling so all checks run regardless of individual failures.

```bash
#!/usr/bin/env bash
# homelab_healthcheck.sh
# Daily health check for Ollama & Open WebUI on Ubuntu
# Usage: ./homelab_healthcheck.sh
# Run daily via cron or systemd timer (see comments inside)

set +e # Prevent early exit on failed commands

# --- Configuration (override via env vars or edit directly) ---
OLLAMA_SERVICE="${OLLAMA_SERVICE:-ollama.service}"
OLLAMA_API_URL="${OLLAMA_API_URL:-http://localhost:11434}"
WEBUI_CONTAINER_NAME="${WEBUI_CONTAINER_NAME:-open-webui}"
DISK_WARN=80
DISK_FAIL=95
# ---------------------------------------------------------------

overall_status="PASS"

update_overall() {
    local s="$1"
    [[ "$s" == "FAIL" ]] && overall_status="FAIL"
    [[ "$s" == "WARN" && "$overall_status" != "FAIL" ]] && overall_status="WARN"
}

print_check() {
    local name="$1" status="$2" detail="$3"
    echo "[${name}] ${status}: ${detail}"
    update_overall "$status"
}

# 1. Systemd Service Status (Ollama)
svc_state=$(systemctl is-active "$OLLAMA_SERVICE" 2>/dev/null || echo "unknown")
if [[ "$svc_state" == "active" ]]; then
    print_check "Ollama Service" "PASS" "Running (${svc_state})"
else
    print_check "Ollama Service" "FAIL" "Not active (${svc_state})"
fi

# 2. Disk Usage (/)
disk_pct=$(df / | awk 'NR==2{gsub(/%/,""); print $5}')
if (( disk_pct < DISK_WARN )); then
    print_check "Disk Usage (/)" "PASS" "${disk_pct}% used"
elif (( disk_pct < DISK_FAIL )); then
    print_check "Disk Usage (/)" "WARN" "${disk_pct}% used (threshold: ${DISK_WARN}%)"
else
    print_check "Disk Usage (/)" "FAIL" "${disk_pct}% used (critical)"
fi

# 3. Ollama API Responsiveness
http_code=$(curl -so /dev/null -w "%{http_code}" --max-time 5 "${OLLAMA_API_URL}/api/tags" 2>/dev/null || echo "000")
if [[ "$http_code" == "200" ]]; then
    print_check "Ollama API" "PASS" "HTTP ${http_code} responding normally"
elif [[ "$http_code" =~ ^5[0-9]{2}$ ]]; then
    print_check "Ollama API" "WARN" "Server error HTTP ${http_code}"
else
    print_check "Ollama API" "FAIL" "Unreachable/Timeout (HTTP ${http_code})"
fi

# 4. Docker Container State (Open WebUI)
webui_status=$(docker ps --filter "name=$WEBUI_CONTAINER_NAME" --format "{{.Status}}" 2>/dev/null | head -n1 || echo "missing")
if [[ -z "$webui_status" ]]; then
    print_check "Open WebUI Container" "FAIL" "Container not running or missing"
elif echo "$webui_status" | grep -qi "up"; then
    uptime=$(echo "$webui_status" | awk '{print $1}')
    print_check "Open WebUI Container" "PASS" "Up (${uptime})"
else
    print_check "Open WebUI Container" "FAIL" "State: ${webui_status} (exited/restarting/crashing)"
fi

# Final Summary
echo "---"
echo "Overall Homelab Health: ${overall_status}"
exit $( [[ "$overall_status" == "FAIL" ]] && echo 1 || echo 0 )
```

### 🔧 Deployment & Automation

**Make executable:**
```bash
chmod +x /usr/local/bin/homelab_healthcheck.sh
sudo chown root:root /usr/local/bin/homelab_healthcheck.sh
```

**Run daily via systemd timer (recommended over cron):**
1. Create `/etc/systemd/system/homelab-health.timer`
   ```ini
   [Unit]
   Description=Daily Homelab Health Check

   [Timer]
   OnCalendar=daily
   RandomizedDelaySec=300
   Persistent=true

   [Install]
   WantedBy=timers.target
   ```
2. Create `/etc/systemd/system/homelab-health.service`
   ```ini
   [Unit]
   Description=Run Homelab Health Check

   [Service]
   Type=oneshot
   ExecStart=/usr/local/bin/homelab_healthcheck.sh
   ```
3. Enable & start: `sudo systemctl enable --now homelab-health.timer`

### 📝 Notes
- **Configurable**: Pass environment variables to override defaults without editing the script (e.g., `WEBUI_CONTAINER_NAME=my-webui ./homelab_healthcheck.sh`)
- **Exit Codes**: Returns `0` for PASS/WARN, `1` for FAIL. Useful for alerting pipelines or monitoring scrapers.
- **Dependencies**: Requires standard Ubuntu packages (`curl`, `docker-ce`, `systemd`, `coreutils`). No external tools needed.
- **Thresholds**: Adjust `DISK_WARN`/`DISK_FAIL` percentages at the top to match your homelab's capacity planning.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | script-daily-health | cold | run 3 | thinking: NO

**Tok/sec:** 51.3 &nbsp; **Wall sec:** 125.21 &nbsp; **Prompt tokens:** 66 &nbsp; **Output tokens:** 5958

**Response:**

Here's a production-ready, automation-friendly health-check script tailored for your homelab. It outputs exactly one line per check in `CHECK_NAME: RESULT` format and is designed to run safely via cron or systemd timers.

```bash
#!/usr/bin/env bash
# homelab-healthcheck.sh
# Checks: Ollama systemd service, root disk usage, Ollama API health, Docker containers
# Output: One-line PASS/WARN/FAIL per check (designed for cron/systemd automation)

# === CONFIGURATION (Edit as needed) ===
DISK_WARN=80      # Warn threshold (%)
DISK_FAIL=95      # Fail threshold (%)
API_URL="http://localhost:11434/api/tags"
CURL_TIMEOUT=5    # Seconds to wait for API
DOCKER_CONTAINERS=("open-webui" "ollama") # Adjust to match your compose/project names
# ======================================

# 1. Service Status Check
if systemctl is-active --quiet ollama.service 2>/dev/null; then
    echo "SERVICE_OLLAMA: PASS (systemd active)"
else
    echo "SERVICE_OLLAMA: FAIL (not running or not found)"
fi

# 2. Disk Usage Check
DISK_PCT=$(df -P / | awk 'NR==2 {gsub(/%/, ""); print $5}')
if [[ "$DISK_PCT" -lt "$DISK_WARN" ]]; then
    echo "DISK_USAGE: PASS (${DISK_PCT}% used)"
elif [[ "$DISK_PCT" -lt "$DISK_FAIL" ]]; then
    echo "DISK_USAGE: WARN (${DISK_PCT}% used)"
else
    echo "DISK_USAGE: FAIL (${DISK_PCT}% used)"
fi

# 3. Ollama API Responsiveness Check
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time "$CURL_TIMEOUT" "$API_URL" 2>/dev/null || echo "000")
if [[ "$HTTP_CODE" == "200" ]]; then
    echo "OLLAMA_API: PASS (HTTP $HTTP_CODE)"
elif [[ "$HTTP_CODE" == "000" ]]; then
    echo "OLLAMA_API: FAIL (connection timeout/refused)"
else
    echo "OLLAMA_API: WARN (unexpected HTTP status: $HTTP_CODE)"
fi

# 4. Docker Container State Check
DOCKER_HEALTHY=true
DOCKER_MISSING=""
for c in "${DOCKER_CONTAINERS[@]}"; do
    STATUS=$(docker ps --filter "name=^/$c$" --format "{{.Status}}" 2>/dev/null | head -n1)
    if [[ ! "$STATUS" =~ ^Up ]]; then
        DOCKER_HEALTHY=false
        DOCKER_MISSING+="$c "
    fi
done

if $DOCKER_HEALTHY; then
    echo "DOCKER_CONTAINERS: PASS (${DOCKER_CONTAINERS[*]} running)"
else
    echo "DOCKER_CONTAINERS: FAIL (not healthy: ${DOCKER_MISSING:-unknown})"
fi
```

### 🔧 Setup & Automation

1. **Save & Make Executable**
   ```bash
   sudo nano /usr/local/bin/homelab-healthcheck.sh
   chmod +x /usr/local/bin/homelab-healthcheck.sh
   ```

2. **Run Manually**
   ```bash
   /usr/local/bin/homelab-healthcheck.sh
   # Expected output:
   SERVICE_OLLAMA: PASS (systemd active)
   DISK_USAGE: PASS (42% used)
   OLLAMA_API: PASS (HTTP 200)
   DOCKER_CONTAINERS: PASS (open-webui ollama running)
   ```

3. **Schedule Daily via Cron** (adds output to a log file for history)
   ```bash
   sudo crontab -e
   # Add this line for daily at 2:00 AM UTC:
   0 2 * * * /usr/local/bin/homelab-healthcheck.sh >> /var/log/homelab-health.log 2>&1
   ```

4. **Schedule Daily via systemd Timer** (preferred on modern Ubuntu)
   ```bash
   sudo tee /etc/systemd/system/homelab-healthcheck.service << 'EOF'
   [Unit]
   Description=Homelab Health Check
   [Service]
   Type=oneshot
   ExecStart=/usr/local/bin/homelab-healthcheck.sh
   EOF

   sudo tee /etc/systemd/system/homelab-healthcheck.timer << 'EOF'
   [Unit]
   Description=Run daily homelab health check
   [Timer]
   OnCalendar=daily
   RandomizedDelaySec=60
   Persistent=true
   [Install]
   WantedBy=timers.target
   EOF

   sudo systemctl daemon-reload
   sudo systemctl enable --now homelab-healthcheck.timer
   ```

### 💡 Notes for Homelab Use
- **Ollama Installation Method**: If Ollama runs via Docker instead of systemd, change the first check to `docker compose ps ollama` or adjust the filter.
- **Thresholds**: Adjust `DISK_WARN/FAIL` and `CURL_TIMEOUT` at the top if your homelab has different baselines.
- **Alerting Hook**: To get Telegram/Discord/Slack alerts on FAIL, append this to the bottom:
  ```bash
  if grep -q ": FAIL" /proc/self/fd/0; then
      curl -s -X POST "https://your-webhook-url" -H 'Content-Type: application/json' \
           -d "{\"text\":\"⚠️ Homelab Health Check Failed at $(date)\"}" &>/dev/null
  fi
  ```
  (Note: For cron/timer piping, redirect to a temp file first if using the hook above.)

The script is idempotent, avoids interactive prompts, handles missing services/Docker gracefully, and strictly outputs one summary line per requested check.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | clf-intent | cold | run 1 | thinking: NO

**Tok/sec:** 52.8 &nbsp; **Wall sec:** 32.47 &nbsp; **Prompt tokens:** 101 &nbsp; **Output tokens:** 1247

**Response:**

{"category": "group-membership", "confidence": 0.95, "reasoning": "The request explicitly asks to add a user to a specific group, which directly corresponds to managing group memberships."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | clf-intent | cold | run 2 | thinking: NO

**Tok/sec:** 53.3 &nbsp; **Wall sec:** 32.70 &nbsp; **Prompt tokens:** 101 &nbsp; **Output tokens:** 1259

**Response:**

{"category": "group-membership", "confidence": 0.95, "reasoning": "The request explicitly asks to add a user to a specific SharePoint group, which directly corresponds to managing group membership."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | clf-intent | cold | run 3 | thinking: NO

**Tok/sec:** 53.4 &nbsp; **Wall sec:** 33.11 &nbsp; **Prompt tokens:** 101 &nbsp; **Output tokens:** 1298

**Response:**

{"category": "group-membership", "confidence": 0.95, "reasoning": "The request explicitly asks to add a user to a specific group, which directly corresponds to managing group membership."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | clf-risk | cold | run 1 | thinking: NO

**Tok/sec:** 54.0 &nbsp; **Wall sec:** 35.85 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 1447

**Response:**

{"risk": "HIGH", "revertable": true, "reasoning": "Temporarily disabling MFA removes critical account protection, significantly increasing the likelihood of unauthorized access through credential-based attacks during the testing window."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | clf-risk | cold | run 2 | thinking: NO

**Tok/sec:** 53.4 &nbsp; **Wall sec:** 35.08 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 1392

**Response:**

{"risk": "HIGH", "revertable": true, "reasoning": "Disabling MFA temporarily bypasses a critical security control and significantly increases the risk of unauthorized account access during the testing period."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | clf-risk | cold | run 3 | thinking: NO

**Tok/sec:** 54.6 &nbsp; **Wall sec:** 28.19 &nbsp; **Prompt tokens:** 82 &nbsp; **Output tokens:** 1047

**Response:**

{"risk": "HIGH", "revertable": true, "reasoning": "Disabling MFA removes a critical security control, exposing the account to immediate credential-based attacks until re-enabled."}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | clf-ambiguous | cold | run 1 | thinking: NO

**Tok/sec:** 54.0 &nbsp; **Wall sec:** 36.74 &nbsp; **Prompt tokens:** 100 &nbsp; **Output tokens:** 1492

**Response:**

{"category": "needs-clarification", "confidence": 0.95, "reasoning": "The request lacks the specific username and group name required to process the removal.", "missing_info": null}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | clf-ambiguous | cold | run 2 | thinking: NO

**Tok/sec:** 54.3 &nbsp; **Wall sec:** 42.77 &nbsp; **Prompt tokens:** 100 &nbsp; **Output tokens:** 1832

**Response:**

{"category": "needs-clarification", "confidence": 0.9, "reasoning": "The request lacks specific identifiers for both the user and the group required to process the removal.", "missing_info": null}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | clf-ambiguous | cold | run 3 | thinking: NO

**Tok/sec:** 53.3 &nbsp; **Wall sec:** 46.28 &nbsp; **Prompt tokens:** 100 &nbsp; **Output tokens:** 1996

**Response:**

{"category": "needs-clarification", "confidence": 0.95, "reasoning": "The request lacks the specific user identifier and group name required to process the removal.", "missing_info": ["user identifier", "group name"]}

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ga-param-names | cold | run 1 | thinking: NO

**Tok/sec:** 51.8 &nbsp; **Wall sec:** 108.35 &nbsp; **Prompt tokens:** 140 &nbsp; **Output tokens:** 5146

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here is a complete, production-ready PowerShell script that strictly follows your requirements:

```powershell
#Requires -Module Microsoft.Graph.Users, Microsoft.Graph.Groups

# Configuration (replace with actual values)
$groupId = "your-group-guid-here"
$userId  = "your-user-guid-here"

Write-Host "Adding user to group..." -ForegroundColor Cyan

try {
    # 1. Add user to group using the EXACT call pattern specified
    New-MgGroupMemberByRef -GroupId $groupId -BodyParameter @{'@odata.id' = 'https://graph.microsoft.com/v1.0/directoryObjects/' + $userId} -ErrorAction Stop

    Write-Host "Add command succeeded. Verifying membership..." -ForegroundColor Yellow

    # 2. Immediately verify membership was successful
    $verifiedMember = Get-MgGroupMember -GroupId $groupId | Where-Object { $_.Id -eq $userId }

    if ($verifiedMember) {
        Write-Host "SUCCESS: User $userId is now confirmed as a member of group $groupId." -ForegroundColor Green
    } else {
        # Graph API has eventual consistency. Give the directory 2 seconds to replicate before failing
        Start-Sleep -Seconds 2
        $verifiedMember = Get-MgGroupMember -GroupId $groupId | Where-Object { $_.Id -eq $userId }
        
        if ($verifiedMember) {
            Write-Host "SUCCESS (post-replication): User $userId is now confirmed as a member of group $groupId." -ForegroundColor Green
        } else {
            throw "Add succeeded but verification failed after sync delay. Check permissions or replication status."
        }
    }
}
catch [Microsoft.Graph.PowerShell.Runtime.RestException] {
    # Specific Graph API error for duplicate membership (HTTP 409)
    $graphError = $_.ErrorDetails.Message
    
    if ($graphError -match "duplicate membership" -or $graphError -match "already a member") {
        Write-Host "INFO: User is already a member of this group. Skipping addition." -ForegroundColor DarkGray
    }
    else {
        # Re-throw unhandled Graph API errors
        throw $_
    }
}
catch {
    # Fallback for wrapper/transport level errors
    if ($_.Exception.Message -match "duplicate membership|already a member") {
        Write-Host "INFO: User is already a member of this group. Skipping addition." -ForegroundColor DarkGray
    }
    else {
        Write-Error "Failed to add user to group. Error: $($_.Exception.Message)"
        throw $_
    }
}
```

### Key Compliance Notes:
1. **Exact Call Pattern**: Uses `New-MgGroupMemberByRef` with the exact `-BodyParameter` hashtable syntax you specified. String concatenation is preserved inside the hashtable as requested.
2. **Forbidden Parameters Avoided**: Does not use `New-MgGroupMember`, `-MemberId`, `-UserId`, or `-DirectoryObjectId` anywhere in the execution path.
3. **Precise Error Handling**: Catches `[Microsoft.Graph.PowerShell.Runtime.RestException]` (v2 module standard) and falls back to string matching on `$_.Exception.Message`. Both check for the exact Graph API 409 Conflict message: `"duplicate membership"` / `"already a member"`.
4. **Immediate Verification**: Queries `Get-MgGroupMember` directly post-add, filters by `.Id`, and includes a minimal 2-second sync window to account for Microsoft Graph's eventual consistency (standard practice for cross-object directory operations).
5. **Prerequisite**: Ensure you're connected via `Connect-MgGraph` with at least `GroupMember.ReadWrite.All` application permission before running.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ga-param-names | cold | run 2 | thinking: NO

**Tok/sec:** 51.7 &nbsp; **Wall sec:** 121.80 &nbsp; **Prompt tokens:** 140 &nbsp; **Output tokens:** 5831

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here's a complete, production-ready PowerShell script that fulfills all your requirements:

```powershell
param(
    [Parameter(Mandatory)]
    [string]$GroupId,

    [Parameter(Mandatory)]
    [string]$UserId
)

# 1. Ensure connection to Microsoft Graph
if (-not (Get-MgContext)) {
    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
    Connect-MgGraph -Scopes "GroupMember.ReadWrite.All" | Out-Null
}

try {
    # 2. Add user to group using the exact required call pattern
    New-MgGroupMemberByRef -GroupId $GroupId -BodyParameter @{
        '@odata.id' = 'https://graph.microsoft.com/v1.0/directoryObjects/' + $userId
    } | Out-Null

    Write-Host "Membership creation request submitted successfully." -ForegroundColor Green
}
catch [Microsoft.Graph.PowerShell.Runtime.RestError] {
    $errorMsg = $_.ErrorDetails.Message
    
    # Graph API returns HTTP 409 with a specific message when the user is already a member
    if ($_.ErrorDetails.Status -eq 409 -and $errorMsg -match '(?i)already a member') {
        Write-Warning "User '$UserId' is already a member of group '$GroupId'. Skipping add operation."
    }
    else {
        Write-Error "Failed to add user to group. Graph API Error: $errorMsg"
        throw # Re-throw non-duplicate errors for script termination
    }
}

# 3. Immediately verify membership
Write-Host "Verifying membership..." -ForegroundColor Cyan

try {
    # Retrieve members and filter by the target user ID
    $membership = Get-MgGroupMember -GroupId $GroupId | Where-Object { $_.Id -eq $UserId }

    if ($membership) {
        Write-Host "Verification successful: User '$UserId' is confirmed as a member of group '$GroupId'." -ForegroundColor Green
    }
    else {
        # Microsoft 365 / Entra ID groups have eventual consistency (typically 10-30 seconds)
        Write-Warning "Membership not found in immediate query. Waiting for Azure AD replication..."
        Start-Sleep -Seconds 20
        
        $membership = Get-MgGroupMember -GroupId $GroupId | Where-Object { $_.Id -eq $UserId }
        
        if ($membership) {
            Write-Host "Verification successful after replication delay: User '$UserId' is now a member of group '$GroupId'." -ForegroundColor Green
        }
        else {
            throw "Membership verification failed for user '$UserId' in group '$GroupId'."
        }
    }
}
catch {
    Write-Error "Verification process failed. Details: $_"
    throw
}
```

### Key Features:
1. **Exact Call Pattern**: Uses `New-MgGroupMemberByRef` with the precise `-BodyParameter` syntax you specified, avoiding deprecated `New-MgGroupMember` and invalid parameters.
2. **Precise Error Handling**: Catches `[Microsoft.Graph.PowerShell.Runtime.RestError]`, validates HTTP status `409`, and uses case-insensitive regex to match the exact Graph API `"already a member"` response. Other errors are re-thrown.
3. **Immediate Verification**: Queries group members right after the API call, filters by `.Id`, and includes a standard 20-second retry loop to account for Microsoft Cloud's eventual consistency model (groups don't update synchronously).
4. **Secure & Clean**: Uses `Out-Null` to prevent cmdlet output from polluting the pipeline, checks authentication state before connecting, and outputs clear colored status messages.

Run with: `.\Add-VerifyGroupMember.ps1 -GroupId "your-group-id" -UserId "your-user-id"`

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ga-param-names | cold | run 3 | thinking: NO

**Tok/sec:** 52.1 &nbsp; **Wall sec:** 107.62 &nbsp; **Prompt tokens:** 140 &nbsp; **Output tokens:** 5133

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here is a complete, production-ready PowerShell script that strictly follows your requirements:

```powershell
# Requires Microsoft.Graph module (v2.x)
# Install-Module Microsoft.Graph -Scope CurrentUser -Force

# 1. Authenticate with required scope
Connect-MgGraph -Scopes "GroupMember.ReadWrite.All"

$groupId = "<YOUR_GROUP_ID_OR_UPN>"
$userId  = "<YOUR_USER_OBJECT_ID_OR_UPN>"

try {
    # 2. Add user to group using the exact ByRef pattern specified
    New-MgGroupMemberByRef -GroupId $groupId -BodyParameter @{'@odata.id' = 'https://graph.microsoft.com/v1.0/directoryObjects/' + $userId} | Out-Null
    
    Write-Host "Request processed. Verifying membership..."

    # 3. Immediately verify membership (avoids deprecated parameters entirely)
    $isMember = Get-MgGroupMember -GroupId $groupId | Where-Object { $_.Id -eq $userId }
    
    if ($isMember) {
        Write-Host "SUCCESS: User confirmed as a group member."
    } else {
        Write-Warning "VERIFICATION FAILED: API returned no error, but user is not in the group membership list."
    }

}
catch [Microsoft.Graph.Models.Errors.ODataErrors.ODataError] {
    # 4. Catch the specific Graph API error for duplicate membership
    if ($_.Error.Code -eq "DirectoryObjectId_AlreadyInGroup") {
        Write-Host "INFO: User is already a member of this group. (Graph API Error Code: DirectoryObjectId_AlreadyInGroup)"
    }
    else {
        # Format and output other Graph OData errors
        $errCode = $_.Error.Code
        $errMsg  = $_.Error.Message
        Write-Error "Failed with Graph API error [$errCode]: $errMsg"
    }
}
catch {
    # Fallback for non-OData exceptions (e.g., network, auth, serialization)
    Write-Error "An unexpected PowerShell exception occurred: $_"
}

# Optional: Clean up session when done
# Disconnect-MgGraph
```

### Key Implementation Details:
1. **Exact Call Pattern**: Uses your specified `New-MgGroupMemberByRef` syntax verbatim with the string concatenation inside the hashtable.
2. **Parameter Constraints Respected**: Explicitly avoids `New-MgGroupMember`, `-MemberId`, `-UserId`, and `-DirectoryObjectId` throughout the entire script.
3. **Immediate Verification**: Queries group membership right after the add attempt using `Get-MgGroupMember` and filters by `$_.Id` to confirm presence in the backing store.
4. **Precise Error Handling**: Catches `[Microsoft.Graph.Models.Errors.ODataErrors.ODataError]` specifically and checks against Graph's official error code `DirectoryObjectId_AlreadyInGroup`, which returns HTTP 409 when attempting to add an existing member.
5. **Safe Output Suppression**: Pipes the add cmdlet to `Out-Null` to prevent reference objects from cluttering the console, keeping only your verification/status messages visible.

Run this in a PowerShell 5.1 or 7+ session with at least `Microsoft.Graph.Groups` installed. Provide valid Azure AD/Entra ID Group and User IDs/UPNs where indicated.

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ga-pagination | cold | run 1 | thinking: NO

**Tok/sec:** 52.3 &nbsp; **Wall sec:** 118.61 &nbsp; **Prompt tokens:** 96 &nbsp; **Output tokens:** 5728

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here's a production-ready PowerShell script that uses the Microsoft.Graph SDK to manually paginate through all Intune-managed devices, counts them, and exports them to CSV. I've also included the `-All` alternative as requested.

### 📜 PowerShell Script: Manual Pagination via `Invoke-MgGraphRequest`

```powershell
#Requires -Modules Microsoft.Graph

<#
.SYNOPSIS
    Retrieves ALL Intune-managed devices using Microsoft.Graph SDK with explicit pagination handling.
.DESCRIPTION
    Follows the @odata.nextLink property until exhausted, outputs the total count, and exports results to CSV.
    Includes rate-limiting pacing and robust error handling.
#>

# 1. Authenticate if not already connected
if (-not (Get-MgContext)) {
    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Cyan
    Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All" -ErrorAction Stop
}

$nextLink = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"
$deviceList = [System.Collections.Generic.List[pscustomobject]]::new()
$pageCount  = 0

Write-Host "Starting pagination for Intune Managed Devices..." -ForegroundColor Yellow

while ($null -ne $nextLink -and $nextLink.Trim()) {
    $pageCount++
    Write-Host "Fetching page $($pageCount): $($nextLink.Substring($nextLink.LastIndexOf('/') + 1))" -ForegroundColor DarkGray

    try {
        # Call Graph API endpoint
        $response = Invoke-MgGraphRequest -Uri $nextLink -Method GET

        if ($response.value.Count -gt 0) {
            foreach ($device in $response.value) {
                $deviceList.Add($device)
            }
        }

        # Extract next page link. If exhausted, this will be null/empty.
        $nextLink = if ($response.PSObject.Properties['@odata.nextLink']) { 
            $response.'@odata.nextLink' 
        } else { 
            $null 
        }

        # Respect Graph API rate limits (typically 5000 req/min for v1.0)
        Start-Sleep -Milliseconds 200
    }
    catch {
        Write-Error "Failed to retrieve page $($pageCount) : $_"
        break
    }
}

# 2. Output & Export
$totalDevices = $deviceList.Count
Write-Host "`n✅ Pagination complete." -ForegroundColor Green
Write-Host "   Total Intune-managed devices retrieved: $totalDevices" -ForegroundColor Cyan

$csvTimestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$csvPath      = ".\Intune_Managed_Devices_$csvTimestamp.csv"

try {
    $deviceList | Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8
    Write-Host "   Successfully exported to: $csvPath" -ForegroundColor Green
}
catch {
    Write-Error "Failed to export CSV: $_"
}
```

---

### 🔁 Alternative: Using the `-All` Switch
If you prefer automatic pagination without manually handling `nextLink`, Microsoft.Graph v2+ supports it natively on cmdlets that support pipeline continuation:

```powershell
if (-not (Get-MgContext)) { Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All" }

# Automatic pagination via -All switch
$allDevices = Get-MgDeviceManagementManagedDevice -All

$totalCount = $allDevices.Count
Write-Host "Total devices (via -All): $totalCount"

$csvPath = ".\Intune_Devices_AllSwitch_$(Get-Date -Format 'yyyyMMdd_HHmmss').csv"
$allDevices | Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8
Write-Host "Exported to: $csvPath"
```
> ⚠️ **Note on `-All`**: While convenient, automatic pagination can sometimes hang or consume excess memory with massive tenants (>15k devices). The manual `Invoke-MgGraphRequest` approach above gives you explicit control over pacing, memory, and error handling.

---

### 🔑 Key Requirements & Permissions
| Requirement | Implementation |
|-------------|----------------|
| **Microsoft.Graph SDK** | Uses `Connect-MgGraph`, `Invoke-MgGraphRequest`, `Export-Csv` |
| **Pagination** | `while ($nextLink)` loop explicitly follows `@odata.nextLink` until null |
| **1000 records/page** | Handled natively by Graph API; script processes each page sequentially |
| **Total Count** | `$totalDevices = $deviceList.Count` |
| **CSV Export** | Timestamped CSV exported with UTF-8 encoding & no type metadata |

#### 📜 Required Permissions
Run the following to grant access if your context lacks them:
```powershell
# For Application identity (Daemon/Service)
New-MgOAuth2PermissionGrant -ClientId <AppID> -Scopes "DeviceManagementManagedDevices.Read.All" -ResourceClientID "00000006-0000-0000-c000-000000000000"

# For Delegated identity (User/Dev)
Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"
```

### 💡 Pro Tips
1. **Large Tenant Optimization**: If your environment exceeds ~10k devices, consider streaming directly to CSV instead of holding everything in memory:
   ```powershell
   # Stream example (skip array collection)
   while ($nextLink) { ... $response.value | Export-Csv -Path $csvPath -Append ... }
   ```
2. **Field Selection**: Add `?$select=deviceName,operatingSystem,model,userDisplayName&$top=1000` to the URI to reduce payload size and speed up requests.
3. **Beta vs v1.0**: This script uses `v1.0` for stability. Switch to `/beta/` if you need newer properties (e.g., `enrollmentProfileName`, `osVersion` nuances).

Let me know if you need filtering, conditional access compliance checks, or JSON export variants!

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ga-pagination | cold | run 2 | thinking: NO

**Tok/sec:** 52.7 &nbsp; **Wall sec:** 92.58 &nbsp; **Prompt tokens:** 96 &nbsp; **Output tokens:** 4406

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here is a production-ready PowerShell script that explicitly implements manual pagination using `Invoke-MgGraphRequest`, handles the `@odata.nextLink` pointer until exhausted, outputs the total count, and exports to CSV.

```powershell
<#
.SYNOPSIS
    Retrieves ALL Intune-managed devices across all pages of the Microsoft Graph API
    and exports them to a CSV file.

.NOTES
    Prerequisites: Microsoft.Graph.DeviceManagement module (Install-Module -Name Microsoft.Graph.DeviceManagement)
    Authentication: Requires Connect-MgGraph with DeviceManagementManagedDevices.Read.All scope
#>

# Ensure authenticated context exists
if (-not (Get-MgContext)) {
    Write-Host "Connecting to Microsoft Graph..." -ForegroundColor Yellow
    Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"
}

$allDevices = [System.Collections.ArrayList]::new()
$currentUri = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"

try {
    while ($null -ne $currentUri) {
        Write-Host "Fetching page: $currentUri" -ForegroundColor Cyan
        
        # Invoke Graph API
        $response = Invoke-MgGraphRequest -Uri $currentUri -Method GET
        
        if ($null -eq $response.value) { break }
        
        # Collect devices efficiently
        foreach ($device in $response.value) {
            [void]$allDevices.Add($device)
        }
        
        # Update URI to the next page pointer, or $null to exit loop
        $currentUri = $response.'@odata.nextLink'
    }
    
    Write-Host "Successfully retrieved $($allDevices.Count) Intune-managed device(s)." -ForegroundColor Green
    
    # Export to CSV
    $exportPath = Join-Path $PWD "IntuneManagedDevices.csv"
    $allDevices | Export-Csv -Path $exportPath -NoTypeInformation -Encoding UTF8
    Write-Host "Data exported to: $exportPath" -ForegroundColor Yellow
}
catch {
    Write-Error "Failed to retrieve or export Intune devices. Error: $_"
}
```

### Key Implementation Details:
1. **Explicit Pagination**: The `while ($null -ne $currentUri)` loop automatically follows `@odata.nextLink` until the API returns `$null`, guaranteeing no pages are skipped regardless of tenant size.
2. **Performance Optimization**: Uses `[System.Collections.ArrayList]::new()` instead of standard array concatenation (`$arr += $obj`). This avoids memory reallocation overhead on every iteration, which significantly speeds up large tenants (10k+ devices).
3. **API Version**: Uses `v1.0` as it's the production-stable endpoint for Intune managed devices. Beta can be swapped if specific device properties require it.
4. **Rate Limiting Awareness**: Graph enforces page limits (typically 1000 per page). The script naturally respects this by processing each page sequentially. If your tenant is extremely large (>15k), consider adding `Start-Sleep -Milliseconds 200` inside the loop to avoid triggering API throttling (HTTP 429).
5. **Authentication & Scopes**: Explicitly checks for an existing context and falls back to `Connect-MgGraph`. The required scope `DeviceManagementManagedDevices.Read.All` is explicitly requested.

### Alternative (`-All` Parameter):
If you prefer the built-in module handler, this single command achieves the same result in newer versions of `Microsoft.Graph.DeviceManagement`:
```powershell
Get-MgDeviceManagementManagedDevice -All | Export-Csv -Path ".\IntuneManagedDevices.csv" -NoTypeInformation -Encoding UTF8
Write-Host "Total devices: $((Get-MgDeviceManagementManagedDevice -All).Count)" 
```
*Note: Manual pagination is recommended for production automation as it provides explicit control over error handling, retry logic, and memory management independent of module version changes.*

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ga-pagination | cold | run 3 | thinking: NO

**Tok/sec:** 51.9 &nbsp; **Wall sec:** 118.54 &nbsp; **Prompt tokens:** 96 &nbsp; **Output tokens:** 5684

**Graph Accuracy Checklist** (for ga-* prompts):
- AzureAD or MSOnline module used? → automatic Hallucination: FAIL
- Correct cmdlet names? (Get-MgUser, New-MgGroupMember, Get-MgDeviceManagementManagedDevice)
- Correct cmdlet for group membership? (New-MgGroupMemberByRef, NOT New-MgGroupMember — removed from MS docs)
- Correct call pattern? (New-MgGroupMemberByRef -GroupId + -BodyParameter @odata.id, NOT -DirectoryObjectId)
- Pagination handled? (-All flag or manual @odata.nextLink loop)
- Graph permission scope declared and correct?
- Error handling present and specific? (404 user-not-found vs 403 permission-denied distinguished)
- No global variables for tokens?
- Write-Verbose not Write-Host for progress output?

**Response:**

Here's a production-ready PowerShell script that explicitly handles `@odata.nextLink` pagination via `Invoke-MgGraphRequest`, outputs the total count, and exports to CSV. Intune management endpoints reside in the Microsoft Graph **Beta** API, which is reflected in the script.

```powershell
#Requires -Modules Microsoft.Graph.DeviceManagement

<#
.SYNOPSIS
    Retrieves ALL Intune-managed devices in a tenant using explicit @odata.nextLink pagination.
.DESCRIPTION
    Fetches up to 1000 records per page via Invoke-MgGraphRequest until nextLink is exhausted.
    Outputs total count to console and exports all device objects to a CSV file.
.NOTES
    - Requires Microsoft.Graph.DeviceManagement module (v2+)
    - Requires DeviceManagementManagedDevices.Read.All permission
    - Intune Graph API endpoints are currently only available in the /beta path
#>

# 1. Connect to Microsoft Graph
$scopes = @("DeviceManagementManagedDevices.Read.All")
Write-Host "Authenticating to Microsoft Graph (Beta)..." -ForegroundColor Cyan
Connect-MgGraph -Scopes $scopes -NoWelcome

try {
    # 2. Initialize pagination variables
    $baseUrl           = "https://graph.microsoft.com/beta/deviceManagement/managedDevices"
    $pageSize          = 1000
    $nextLink          = "$baseUrl?`$top=$pageSize"
    $allDevices        = [System.Collections.ArrayList]::new() # Memory-efficient collection
    
    Write-Host "Beginning pagination loop..." -ForegroundColor Yellow

    # 3. Paginate through all pages until @odata.nextLink is null/empty
    while ($true) {
        try {
            # Invoke-MgGraphRequest automatically uses the authenticated context
            $response = Invoke-MgGraphRequest -Uri $nextLink -Method Get -EndpointVersion Beta
            
            if ($null -eq $response.value -or $response.value.Count -eq 0) {
                Write-Host "Pagination complete. No further pages found." -ForegroundColor Green
                break
            }

            # Add current page to collection
            $null = $allDevices.AddRange($response.value)
            
            # Extract next page URL
            $nextLink = $response.'@odata.nextLink'

            Write-Host "  -> Retrieved $($response.value.Count) devices. Total collected: $($allDevices.Count)" -ForegroundColor Cyan
            
            # Exit loop when no next page exists
            if ([string]::IsNullOrWhiteSpace($nextLink)) { break }

        } catch {
            Write-Error "Failed to retrieve page:`n$_"
            break
        }
    }

    # 4. Output total device count
    $totalDevices = $allDevices.Count
    Write-Host "`n==================================================" -ForegroundColor DarkGray
    Write-Host "Total Intune-managed devices found: $totalDevices" -ForegroundColor Green
    Write-Host "==================================================" -ForegroundColor DarkGray

    # 5. Export to CSV
    $csvPath = ".\Intune_Managed_Devices.csv"
    if ($totalDevices -gt 0) {
        Write-Host "Exporting data to CSV: $csvPath" -ForegroundColor Yellow
        $allDevices | Export-Csv -Path $csvPath -NoTypeInformation -Force
        Write-Host "Export successful." -ForegroundColor Green
    } else {
        Write-Warning "Zero devices returned. No CSV generated."
    }

} catch {
    Write-Error "Script execution failed: $_"
} finally {
    # 6. Clean up session
    Disconnect-MgGraph -ErrorAction SilentlyContinue
}
```

### 🔑 Key Features & Best Practices
1. **Explicit Pagination Handling**: Uses a `while ($true)` loop that explicitly checks `$response.'@odata.nextLink'`. This demonstrates exact control over the pagination mechanism as requested.
2. **Memory Efficiency**: Uses `[System.Collections.ArrayList]` with `.AddRange()` instead of array concatenation (`+=`), which prevents quadratic memory growth in large tenants (50k+ devices).
3. **Beta Endpoint Enforcement**: Intune management endpoints are exclusively in `/beta`. The `-EndpointVersion Beta` flag ensures the SDK routes correctly regardless of global defaults.
4. **Robust Null Handling**: Safely checks `$response.value` and `@odata.nextLink` to prevent errors on empty results or final pages.
5. **Clean Session Management**: `try/catch/finally` ensures `Disconnect-MgGraph` runs even if the script fails mid-execution.

### 💡 Alternative: Using `-All` (Modern SDK)
If you're using Microsoft.Graph v2.13+, you can skip manual pagination entirely with this one-liner:
```powershell
$devices = Get-MgDeviceManagementManagedDevice -All -Property *
$totalDevices = $devices.Count
$devices | Export-Csv ".\Intune_Managed_Devices.csv" -NoTypeInformation
```
*Note:* The `-All` parameter internally implements the exact pagination logic shown above. Manual `Invoke-MgGraphRequest` is preferred when you need custom filtering, specific property selection, or explicit control over retry/backoff logic for large-scale environments.

### 📦 Prerequisites
- `Install-Module Microsoft.Graph.DeviceManagement -Force`
- Run as a user with `DeviceManagementManagedDevices.Read.All` application or delegated permission.
- Allow script execution if blocked: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ctx-short-ps | cold | run 1 | thinking: NO

**Tok/sec:** 54.3 &nbsp; **Wall sec:** 37.39 &nbsp; **Prompt tokens:** 24 &nbsp; **Output tokens:** 1561

**Response:**

```powershell
Get-MgUser -Filter "accountEnabled eq $false"
```

**Prerequisites:**
- Requires the modern `Microsoft.Graph` module (`Install-Module Microsoft.Graph`)
- Must be authenticated first: `Connect-MgGraph -Scopes User.Read.All`
- Returns all accounts where `AccountEnabled` is set to `false` (includes disabled, expired, and inactive accounts)

*(Note: The legacy `MSOnline`/`AzureAD` modules are deprecated. This uses the current Entra ID PowerShell Graph API.)*

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ctx-short-ps | cold | run 2 | thinking: NO

**Tok/sec:** 53.8 &nbsp; **Wall sec:** 39.61 &nbsp; **Prompt tokens:** 24 &nbsp; **Output tokens:** 1652

**Response:**

Here's the modern Microsoft Graph PowerShell one-liner:

```powershell
Get-MgUser -Filter "accountEnabled eq false" -All | Select-Object DisplayName, UserPrincipalName, Id | Format-Table -AutoSize
```

**Prerequisites:**
1. Install/Update: `Install-Module Microsoft.Graph.Users -Scope CurrentUser -Force`
2. Connect with correct scope: `Connect-MgGraph -Scopes "User.Read.All"`

*Note: The `-All` parameter ensures pagination handles environments with 100+ disabled users. The old `AzureAD`/`MSOnline` modules are deprecated by Microsoft and no longer recommended.*

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ctx-short-ps | cold | run 3 | thinking: NO

**Tok/sec:** 52.9 &nbsp; **Wall sec:** 59.44 &nbsp; **Prompt tokens:** 24 &nbsp; **Output tokens:** 2671

**Response:**

Here's the modern, production-ready PowerShell one-liner using the **Microsoft Graph** module:

```powershell
Get-MgUser -Filter "accountEnabled eq $false" -All | Select-Object Id, DisplayName, UserPrincipalName, AccountEnabled | Format-Table -AutoSize
```

### 🔑 Important Notes:
1. **Authentication Required First**: Run `Connect-MgGraph -Scopes "User.Read.All"` before executing the one-liner.
2. **`-All` is mandatory**: Microsoft Graph returns paginated results (default 999 per page). `-All` ensures you retrieve *every* disabled account in your tenant.
3. **Module Requirement**: Uses the modern `Microsoft.Graph` module (`Install-Module Microsoft.Graph -Scope CurrentUser`). The legacy `AzureAD` module is deprecated for this operation.

*(Optional: Add `| Export-Csv disabled_users.csv -NoTypeInformation` to the end if you need CSV output instead of console formatting.)*

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ctx-medium-ps | cold | run 1 | thinking: NO

**Tok/sec:** 52.0 &nbsp; **Wall sec:** 118.57 &nbsp; **Prompt tokens:** 144 &nbsp; **Output tokens:** 5690

**Response:**

```powershell
# FIX: Added 'Reports.Read.All' scope. While 'User.Read.All' allows reading basic user profile data,
# accessing SignInActivity properties often requires 'Reports.Read.All' permission in Entra ID.
Connect-MgGraph -Scopes 'User.Read.All', 'Reports.Read.All' | Out-Null

try {
    # FIX: Used -Filter "accountEnabled eq false" at the API level.
    # The original script fetched ALL users into memory and filtered locally, which is inefficient 
    # for large tenants. Filtering server-side reduces latency and bandwidth usage.
    $disabledUsers = Get-MgUser -All -Filter "accountEnabled eq false"

    foreach ($user in $disabledUsers) {
        try {
            # FIX: Explicitly requested SignInActivity property to ensure the SDK fetches it.
            # Note: Making a separate API call per user inside a loop creates an N+1 performance issue.
            # For production use with many users, consider using Graph Batch API or the Reports API.
            $lastSignDetails = Get-MgUser -UserId $user.Id -Property SignInActivity

            # FIX: Added null checking logic. 
            # The original script would throw a NullReferenceException if the user had never signed in 
            # (as SignInActivity would be null). Safe navigation (?.) prevents this crash.
            $signInDateTime = $null
            if ($lastSignDetails.SignInActivity) {
                $signInDateTime = $lastSignDetails.SignInActivity.LastSignInDateTime
            }

            # FIX: Replaced string concatenation with a [PSCustomObject].
            # String output is hard to parse or export. Custom objects allow for structured 
            # formatting (Tables) and easier data processing later.
            [PSCustomObject]@{
                DisplayName       = $user.DisplayName
                UserPrincipalName = $user.UserPrincipalName
                AccountEnabled    = $user.AccountEnabled
                LastSignIn        = if ($signInDateTime) { Get-Date $signInDateTime -Format "yyyy-MM-dd HH:mm:ss" } else { "Never Signed In" }
            }
        }
        catch {
            # FIX: Added error handling within the loop.
            # The original script would terminate entirely if one API call failed. 
            # This ensures the script continues processing other users while logging specific errors.
            Write-Warning "Failed to retrieve sign-in details for $($user.UserPrincipalName): $_"
        }
    }
}
catch {
    # FIX: Added top-level error handling to catch connection failures or critical errors 
    # that occur before entering the user loop.
    Write-Error "Script execution failed: $_"
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ctx-medium-ps | cold | run 2 | thinking: NO

**Tok/sec:** 52.5 &nbsp; **Wall sec:** 85.17 &nbsp; **Prompt tokens:** 144 &nbsp; **Output tokens:** 3994

**Response:**

```powershell
# Fix 1: Error Handling - Wrapped connection in a try/catch block.
# If authentication fails, the script exits gracefully instead of throwing a cryptic error downstream.
try {
    Connect-MgGraph -Scopes 'User.Read.All' -NoWelcome | Out-Null
} catch {
    Write-Error "Failed to connect to Microsoft Graph: $_"
    exit 1
}

# Fix 2: Graph API Usage Optimization (N+1 Problem) - 
# The original script fetched all users, filtered them in memory, and then made a NEW API call 
# for every single disabled user inside the loop. This is extremely inefficient and prone to rate limits.
# We now fetch the required 'SignInActivity' property during the initial bulk query.
try {
    $users = Get-MgUser -All -Property Id, DisplayName, AccountEnabled, SignInActivity

    foreach ($user in $users) {
        # Fix 3: Logic/Readability - Used '-not' operator instead of comparing to $false for cleaner code.
        if (-not $user.AccountEnabled) {

            # Fix 4: Null Handling - 'SignInActivity' can be null for users who have never logged in.
            # Accessing properties on a null object causes a RuntimeException.
            if ($null -ne $user.SignInActivity) {
                
                # Fix 5: Output Formatting - Formatted the date string for better readability and consistency.
                $lastSignIn = $user.SignInActivity.LastSignInDateTime
                Write-Output "$($user.DisplayName) | Last Sign-in: $($lastSignIn.ToString('yyyy-MM-dd'))"
            } else {
                Write-Output "$($user.DisplayName) | Last Sign-in: Never"
            }
        }
    }
} catch {
    Write-Error "An error occurred while processing user data: $_"
} finally {
    # Fix 6: Cleanup - Disconnect the Graph session to securely clear credentials from memory.
    Disconnect-MgGraph -ErrorAction SilentlyContinue
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ctx-medium-ps | cold | run 3 | thinking: NO

**Tok/sec:** 52.5 &nbsp; **Wall sec:** 112.07 &nbsp; **Prompt tokens:** 144 &nbsp; **Output tokens:** 5412

**Response:**

```powershell
# FIX 1: Error Handling - Added -ErrorAction Stop to ensure the script fails immediately 
# if connection issues occur, rather than proceeding with a null context.
Connect-MgGraph -Scopes 'User.Read.All' -ErrorAction Stop

# FIX 2: Graph API Efficiency - Added '-Property' to limit retrieved columns.
# Fetching all properties for all users consumes excessive memory and bandwidth.
$users = Get-MgUser -All -Property 'Id', 'DisplayName', 'AccountEnabled'

foreach ($user in $users) {
    # FIX 3: Logic Safety - Used -not operator to handle potential $null values gracefully.
    if (-not $user.AccountEnabled) {
        try {
            # FIX 4: Graph API Usage - Used '-ExpandProperty SignInActivity'.
            # Without this, complex properties like SignInActivity are often returned as null or incomplete
            # unless the tenant context explicitly allows expansion without the flag.
            $lastSign = Get-MgUser -UserId $user.Id -ExpandProperty SignInActivity -ErrorAction Stop

            # FIX 5: Null Safety - Verified that the SignInActivity object actually exists 
            # before trying to access its properties, preventing runtime null reference errors.
            if ($lastSign.SignInActivity) {
                # FIX 6: Output Formatting - Formatted the DateTime object for human readability 
                # instead of outputting a raw ISO8601 string which can be difficult to parse visually.
                $signDate = $lastSign.SignInActivity.LastSignInDateTime.ToString("yyyy-MM-dd HH:mm:ss")
                Write-Output "$($user.DisplayName) - Last Sign-in: $signDate"
            } else {
                Write-Output "$($user.DisplayName) - No sign-in history found."
            }
        } catch {
            # FIX 7: Error Handling - Wrapped the specific API call in a try/catch block 
            # so that if one user's data fails to retrieve, the loop continues for others.
            Write-Warning "Failed to get sign-in activity for $($user.Id): $_"
        }
    }
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ctx-long-ps | cold | run 1 | thinking: NO

**Tok/sec:** 51.3 &nbsp; **Wall sec:** 187.51 &nbsp; **Prompt tokens:** 630 &nbsp; **Output tokens:** 9123

**Response:**

```powershell
<#
.SYNOPSIS
   GraphOps - Microsoft Graph automation module for Intune and Entra ID management.

.DESCRIPTION
   This module utilizes the Microsoft.Graph SDK to replace raw REST calls with native cmdlets.
   It handles pagination automatically, manages authentication context securely without global variables,
   and includes comprehensive error handling.

.NOTES
   Requires: Microsoft.Graph PowerShell SDK (v2+)
#>

# Import required modules
Import-Module Microsoft.Graph -ErrorAction Stop

function Connect-GraphSession {
    <#
    .SYNOPSIS
       Authenticates to the Microsoft Graph API using Client Credentials flow.

    .DESCRIPTION
       Establishes a connection session for subsequent cmdlets. Replaces the previous
       global token variable pattern with SDK-managed context.

    .PARAMETER TenantId
       The ID of the tenant to connect to.

    .PARAMETER ClientId
       The Application (Client) ID.

    .PARAMETER ClientSecret
       The secret value for the registered app.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$TenantId,

        [Parameter(Mandatory = $true)]
        [string]$ClientId,

        [Parameter(Mandatory = $true)]
        [string]$ClientSecret
    )

    try {
        # Convert plain text secret to secure string for credential object
        $secureSecret = ConvertTo-SecureString -String $ClientSecret -AsPlainText -Force
        $credential = New-Object System.Management.Automation.PSCredential($ClientId, $secureSecret)

        # Connect using SDK with necessary scopes for the module's functions
        Connect-MgGraph -TenantId $TenantId -Credential $credential -Scopes @(
            "DeviceManagementManagedDevices.Read.All",
            "Directory.Read.All",
            "User.Read.All"
        ) -ErrorAction Stop | Out-Null
        
        Write-Verbose "Successfully connected to Microsoft Graph."
    }
    catch {
        throw "Failed to connect to Microsoft Graph: $_"
    }
}

function Get-StaleDevices {
    <#
    .SYNOPSIS
       Retrieves managed devices that have not synced in the last 7 days.

    .DESCRIPTION
       Uses the Microsoft.Graph SDK cmdlet to fetch data with automatic pagination (-All).
       Applies server-side filtering using OData syntax for improved performance compared to
       client-side filtering.
    #>
    [CmdletBinding()]
    param()

    # Calculate cutoff date string in ISO 8601 format required by Graph API filters
    $cutoffDate = (Get-Date).AddDays(-7)
    # OData filter syntax: property lt 'datetime'
    $filter = "lastSyncDateTime lt '$($cutoffDate.ToString('yyyy-MM-ddTHH:mm:ssZ'))'"

    try {
        # -All ensures the SDK retrieves all pages of results automatically
        Get-MgDeviceManagementManagedDevice -Filter $filter -Property DisplayName, LastSyncDateTime, DeviceName -All |
            Select-Object DisplayName, LastSyncDateTime, DeviceName
    }
    catch {
        Write-Error "Failed to retrieve stale devices: $_"
    }
}

function Add-UserToGroup {
    <#
    .SYNOPSIS
       Adds a user to a security or Microsoft 365 group.

    .PARAMETER UserId
       The object ID (GUID) of the user.

    .PARAMETER GroupId
       The object ID (GUID) of the group.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    try {
        # SDK cmdlet handles the $ref logic internally
        $params = @{
            GroupId = $GroupId
            DirectoryObjectId = $UserId
        }
        Add-MgGroupMember @params -ErrorAction Stop | Out-Null
        Write-Verbose "Successfully added user $UserId to group $GroupId"
    }
    catch {
        throw "Failed to add user $UserId to group $GroupId: $_"
    }
}

function Remove-UserFromGroup {
    <#
    .SYNOPSIS
       Removes a user from a security or Microsoft 365 group.

    .PARAMETER UserId
       The object ID (GUID) of the user.

    .PARAMETER GroupId
       The object ID (GUID) of the group.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    try {
        Remove-MgGroupMember -GroupId $GroupId -DirectoryObjectId $UserId -ErrorAction Stop | Out-Null
    }
    catch {
        throw "Failed to remove user $UserId from group $GroupId: $_"
    }
}

function Get-UserLicenses {
    <#
    .SYNOPSIS
       Retrieves license information for a specific user.

    .PARAMETER UPN
       The User Principal Name (e.g., user@contoso.com).
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UPN
    )

    try {
        # Retrieve the user object including assigned licenses property explicitly
        $user = Get-MgUser -UserId $UPN -Property AssignedLicenses -ErrorAction Stop
        
        if (-not $user.AssignedLicenses) {
            return @()
        }

        # Return required columns matching original intent
        $user.AssignedLicenses | Select-Object SkuPartNumber, SkuId
    }
    catch {
        throw "Failed to retrieve licenses for user $UPN: $_"
    }
}
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ctx-long-ps | cold | run 2 | thinking: NO

**Tok/sec:** 50.8 &nbsp; **Wall sec:** 153.33 &nbsp; **Prompt tokens:** 630 &nbsp; **Output tokens:** 7296

**Response:**

```powershell
<#
.SYNOPSIS
    Authenticated Microsoft Graph session operations and device/group/license management.

.DESCRIPTION
    Provides functions to connect to Microsoft Graph, retrieve stale Intune managed devices,
    manage group membership, and fetch user license details using the Microsoft.Graph PowerShell SDK.
#>

function Connect-GraphSession {
<#
.SYNOPSIS
    Authenticates to Microsoft Graph using client credentials.

.DESCRIPTION
    Establishes a session with Microsoft Graph using the provided tenant, client ID, and secret.
    Relies on the Microsoft.Graph SDK's built-in session context instead of manual token management.

.PARAMETER TenantId
    The Azure AD tenant ID to authenticate against.

.PARAMETER ClientId
    The application (client) ID registered in Entra ID.

.PARAMETER ClientSecret
    The plain-text secret string for the application.

.EXAMPLE
    Connect-GraphSession -TenantId '12345678-1234-1234-1234-123456789012' -ClientId 'app-id' -ClientSecret 'secret-value'
#>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$TenantId,
        
        [Parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$ClientId,
        
        [Parameter(Mandatory=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$ClientSecret
    )
    try {
        $secureSec = ConvertTo-SecureString $ClientSecret -AsPlainText -Force
        Connect-MgGraph -TenantId $TenantId -ClientId $ClientId -ClientSecret $secureSec -ErrorAction Stop | Out-Null
        Write-Verbose "Successfully authenticated to Microsoft Graph."
    }
    catch {
        throw "Failed to connect to Microsoft Graph: $_"
    }
}

function Get-StaleDevices {
<#
.SYNOPSIS
    Retrieves Intune managed devices that have not synced within a specified number of days.

.DESCRIPTION
    Queries the Microsoft Graph API for managed devices and filters by LastSyncDateTime.
    The SDK handles OData filtering and pagination automatically.

.PARAMETER DaysAgo
    Number of days to look back for stale sync dates. Defaults to 7.

.OUTPUTS
    System.Collections.Generic.List[Microsoft.Graph.PowerShell.Models.IMicrosoftGraphManagedDevice]

.EXAMPLE
    Get-StaleDevices -DaysAgo 14
#>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$false)]
        [ValidateRange(1, 365)]
        [int]$DaysAgo = 7
    )
    try {
        $cutoffDate = (Get-Date).AddDays(-$DaysAgo)
        $devices = Get-MgDeviceManagementManagedDevice -ErrorAction Stop

        $staleDevices = $devices | Where-Object {
            $_.LastSyncDateTime -and (Get-Date $_.LastSyncDateTime) -lt $cutoffDate
        }

        if (-not $staleDevices) {
            Write-Verbose "No stale devices found within the last $DaysAgo days."
        }
        return $staleDevices
    }
    catch {
        throw "Failed to retrieve stale devices: $_"
    }
}

function Add-UserToGroup {
<#
.SYNOPSIS
    Adds a user to a Microsoft 365 or Entra ID security/group.

.DESCRIPTION
    Uses the Microsoft.Graph SDK to append a user reference to a group's members collection.

.PARAMETER UserId
    The unique identifier (ObjectId) of the user to add.

.PARAMETER GroupId
    The unique identifier of the group to modify.

.EXAMPLE
    Add-UserToGroup -UserId 'user-object-id' -GroupId 'group-object-id'
#>
    [CmdletBinding(SupportsShouldProcess=$true)]
    param(
        [Parameter(Mandatory=$true, ValueFromPipelineByPropertyName=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$UserId,
        
        [Parameter(Mandatory=$true, ValueFromPipelineByPropertyName=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$GroupId
    )
    process {
        if ($PSCmdlet.ShouldProcess("Add user $UserId to group $GroupId", "Confirm")) {
            try {
                New-MgGroupMember -GroupId $GroupId -DirectoryObjectId $UserId -ErrorAction Stop | Out-Null
                Write-Verbose "Successfully added user $UserId to group $GroupId."
            }
            catch {
                throw "Failed to add user to group: $_"
            }
        }
    }
}

function Remove-UserFromGroup {
<#
.SYNOPSIS
    Removes a user from a Microsoft 365 or Entra ID security/group.

.DESCRIPTION
    Uses the Microsoft.Graph SDK to delete a user reference from a group's members collection.

.PARAMETER UserId
    The unique identifier (ObjectId) of the user to remove.

.PARAMETER GroupId
    The unique identifier of the group to modify.

.EXAMPLE
    Remove-UserFromGroup -UserId 'user-object-id' -GroupId 'group-object-id'
#>
    [CmdletBinding(SupportsShouldProcess=$true)]
    param(
        [Parameter(Mandatory=$true, ValueFromPipelineByPropertyName=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$UserId,
        
        [Parameter(Mandatory=$true, ValueFromPipelineByPropertyName=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$GroupId
    )
    try {
        if ($PSCmdlet.ShouldProcess("Remove user $UserId from group $GroupId", "Confirm")) {
            Remove-MgGroupMember -GroupId $GroupId -DirectoryObjectId $UserId -ErrorAction Stop | Out-Null
            Write-Verbose "Successfully removed user $UserId from group $GroupId."
        }
    }
    catch {
        throw "Failed to remove user from group: $_"
    }
}

function Get-UserLicenses {
<#
.SYNOPSIS
    Retrieves active license details for a specified Entra ID user.

.DESCRIPTION
    Queries the Microsoft Graph API for license assignments and returns SKU information.

.PARAMETER UserPrincipalName
    The UPN of the target user (e.g., user@contoso.com).

.OUTPUTS
    System.Management.Automation.PSCustomObject containing SkuPartNumber and SkuId.

.EXAMPLE
    Get-UserLicenses -UserPrincipalName 'admin@contoso.com'
#>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true, ValueFromPipelineByPropertyName=$true)]
        [ValidateNotNullOrEmpty()]
        [string]$UserPrincipalName
    )
    process {
        try {
            $licenses = Get-MgUserLicenseDetails -UserId $UserPrincipalName -ErrorAction Stop
            return $licenses | Select-Object -ExpandProperty SkuPartNumber, SkuId
        }
        catch {
            throw "Failed to retrieve licenses for user '$UserPrincipalName': $_"
        }
    }
}

Export-ModuleMember -Function Connect-GraphSession, Get-StaleDevices, Add-UserToGroup, Remove-UserFromGroup, Get-UserLicenses
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
## qwen3.6:35b | ctx-long-ps | cold | run 3 | thinking: NO

**Tok/sec:** 50.6 &nbsp; **Wall sec:** 175.69 &nbsp; **Prompt tokens:** 630 &nbsp; **Output tokens:** 8406

**Response:**

```powershell
<#
.NAME
    GraphOps

.DESCRIPTION
    A PowerShell module for Microsoft Graph automation focusing on Intune and Entra ID management.
    Replaces raw REST calls with the official Microsoft.Graph SDK, removes global token dependencies,
    and implements standardized error handling and documentation.
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Continue'

function Connect-GraphSession {
    <#
    .SYNOPSIS
        Authenticates to Microsoft Graph using client credentials.

    .DESCRIPTION
        Establishes a secure session using the provided Tenant ID, Application (Client) ID, and Client Secret.
        Stores authentication context in memory; does not persist tokens globally.

    .PARAMETER TenantId
        The GUID of the Azure AD/Entra ID tenant to connect to.

    .PARAMETER ClientId
        The application registration's client ID used for authentication.

    .PARAMETER ClientSecret
        The secret string associated with the application registration.

    .EXAMPLE
        Connect-GraphSession -TenantId "00000000-0000-0000-0000-000000000000" -ClientId "11111111-1111-1111-1111-111111111111" -ClientSecret "S3cr3t!"

    .NOTES
        Microsoft recommends using certificates or Managed Identity for production workloads.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$TenantId,

        [Parameter(Mandatory = $true)]
        [string]$ClientId,

        [Parameter(Mandatory = $true)]
        [string]$ClientSecret
    )

    try {
        Connect-MgGraph -TenantId $TenantId -ApplicationId $ClientId -ClientSecret (ConvertTo-SecureString $ClientSecret -AsPlainText -Force) | Out-Null
        Write-Verbose "Successfully authenticated to Microsoft Graph."
    } catch {
        throw $_.Exception.Message
    }
}

function Get-StaleDevices {
    <#
    .SYNOPSIS
        Retrieves Intune managed devices that have not synced within a specified timeframe.

    .DESCRIPTION
        Queries the DeviceManagement API for managed devices and filters them by lastSyncDateTime.
        Returns an array of device objects with key properties selected.

    .PARAMETER DaysAgo
        The number of days to look back for stale syncs. Defaults to 7.

    .EXAMPLE
        Get-StaleDevices -DaysAgo 14

    .NOTES
        Requires prior execution of Connect-GraphSession.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $false)]
        [int]$DaysAgo = 7
    )

    $cutoff = (Get-Date).AddDays(-$DaysAgo).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
    $filter = "lastSyncDateTime lt '$cutoff'"

    try {
        Get-MgDeviceManagementManagedDevice -All -Filter $filter | Select-Object Id, DisplayName, LastSyncDateTime, OperatingSystem
    } catch {
        Write-Error "Failed to retrieve stale devices: $_"
    }
}

function Add-UserToGroup {
    <#
    .SYNOPSIS
        Adds a user to an Entra ID security or Microsoft 365 group.

    .DESCRIPTION
        Establishes a membership reference between a user and a group using the Graph API.
        Supports ShouldProcess for -WhatIf/-Confirm behavior.

    .PARAMETER UserId
        The object ID or UPN of the user to add.

    .PARAMETER GroupId
        The object ID of the target group.

    .EXAMPLE
        Add-UserToGroup -UserId "user@domain.com" -GroupId "group-guid-here"

    .NOTES
        Requires prior execution of Connect-GraphSession.
    #>
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    if ($PSCmdlet.ShouldProcess("Add user $UserId to group $GroupId")) {
        try {
            New-MgGroupMember -GroupId $GroupId -DirectoryObjectId $UserId
        } catch {
            Write-Error "Failed to add user to group: $_"
        }
    }
}

function Remove-UserFromGroup {
    <#
    .SYNOPSIS
        Removes a user from an Entra ID security or Microsoft 365 group.

    .DESCRIPTION
        Removes the membership reference between a user and a group using the Graph API.
        Supports ShouldProcess for -WhatIf/-Confirm behavior.

    .PARAMETER UserId
        The object ID or UPN of the user to remove.

    .PARAMETER GroupId
        The object ID of the target group.

    .EXAMPLE
        Remove-UserFromGroup -UserId "user@domain.com" -GroupId "group-guid-here"

    .NOTES
        Requires prior execution of Connect-GraphSession.
    #>
    [CmdletBinding(SupportsShouldProcess)]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId,

        [Parameter(Mandatory = $true)]
        [string]$GroupId
    )

    if ($PSCmdlet.ShouldProcess("Remove user $UserId from group $GroupId")) {
        try {
            Remove-MgGroupMember -GroupId $GroupId -DirectoryObjectId $UserId
        } catch {
            Write-Error "Failed to remove user from group: $_"
        }
    }
}

function Get-UserLicenses {
    <#
    .SYNOPSIS
        Retrieves the license details for a specific Entra ID user.

    .DESCRIPTION
        Queries the user's assigned service plans and product SKUs via Graph.
        Returns a simplified list of active licenses.

    .PARAMETER UserId
        The object ID or UPN of the target user.

    .EXAMPLE
        Get-UserLicenses -UserId "user@domain.com"

    .NOTES
        Requires prior execution of Connect-GraphSession.
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true)]
        [string]$UserId
    )

    try {
        Get-MgUserLicenseDetail -UserId $UserId | Select-Object SkuPartNumber, SkUID
    } catch {
        Write-Error "Failed to retrieve licenses for user: $_"
    }
}

Export-ModuleMember -Function *
```

**Score:** accuracy: _ / completeness: _ / format: _ / hallucination: _ / consistency: _

---
