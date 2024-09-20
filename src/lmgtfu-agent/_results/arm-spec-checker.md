# Code version
[https://github.com/jochenvw/2024-hackathon/commit/75a740c70f5d6674f4ac828d5858ca63413469de](https://github.com/jochenvw/2024-hackathon/commit/75a740c70f5d6674f4ac828d5858ca63413469de)

# Question
Generate for me the ARM template to enable Azure Backup for Azure files storage.

# Result

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "resources": [
        {
            "type": "Microsoft.RecoveryServices/vaults/backupPolicies",
            "apiVersion": "2024-04-30-preview",
            "name": "[parameters('policyName')]",
            "location": "[parameters('location')]",
            "properties": {
                "backupManagementType": "AzureStorage",
                "retentionPolicy": {
                    "retentionPolicyType": "[parameters('retentionPolicyType')]"
                    // Further properties based on the type of RetentionPolicy
                },
                "schedulePolicy": {
                    "schedulePolicyType": "[parameters('schedulePolicyType')]"
                    // Further properties based on the type of SchedulePolicy
                },
                "timeZone": "[parameters('timeZone')]",
                "vaultRetentionPolicy": {
                    "snapshotRetentionInDays": "[parameters('snapshotRetentionInDays')]",
                    "vaultRetention": {
                        "retentionPolicyType": "[parameters('vaultRetentionType')]"
                        // Further properties based on the type of RetentionPolicy
                    }
                },
                "workLoadType": "AzureFiles"
            }
        }
    ]
}
```


In this ARM template, below are the parameters that are used and their respective functions:

| Parameter                | Function                                                  | Value                         | Default        |
|-----------------------   |-----------------------------------------------------------|------------------------------ |----------------|
| policyName               | The name of the backup policy.                            | string                        |                |
| location                 | The location of the backup policy.                        | string                        |                |
| retentionPolicyType      | The type of the retention policy.                         | string                        |                |
| schedulePolicyType       | The type of the schedule policy.                          | string                        |                |
| timeZone                 | The timezone for the backup policy.                       | string                        |                |
| snapshotRetentionInDays  | The number of days the snapshot is retained.              | integer                       |                |
| vaultRetentionType       | The type of the vault retention policy.                   | string                        |                |
| workLoadType             | The type of the workload.                                 | string                        |                |

# Observation
Mistakes in Cosmos and App Service I believe. Maybe need to specify "Azure Backup Service" specifically? 
