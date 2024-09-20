# Code version
[https://github.com/jochenvw/2024-hackathon/commit/75a740c70f5d6674f4ac828d5858ca63413469de](https://github.com/jochenvw/2024-hackathon/tree/10-include-link-to-arm-specification-github-repository-to-confirm-answer/src/lmgtfu-agent))

# Goal:
Automate the process of generating and validating ARM templates for a specified service and feauture. Extract and document key parameters and assess if policies can be enforced based on those parameters.

#### Tasks:
- [x] **Check the documented ARM specifications if a feauture configuration is possible
- [x] **Generate ARM template** using the Micrososft documentation for the specified service and feauture.
- [x] **The result is checked by the WAF (Well Architeced Framework) agent to check if it is in-line with WAF guidance.
- [x] **The results is checked by the Critic agent to validate correctness, like the parameters against the ARM specification.
- [x] **Output - ARM template** to fullfill the request from the user.
- [ ] **Output - Translate ARM template** into plain English for IT professionals, explaining each parameter/property.
- [x] **Output - Create a parameter overview table** detailing each parameter, its function, possible values, and defaults.
- [ ] *(ToDo)* **Check policy enforcement**: Investigate if policies can be written using the ARM template parameters.
- [ ] *(ToDo)* **Scale Out**: add this approach to the agent orchestrator to validate if a feauture is available for a list of Azure Services. For example which Azure Service support Private Endpoints..

#### Example:
"I have a question on Service X - Can this be done?" — The agent should verify feasibility based on the ARM specification, not just general documentation.

### Alternative
- create ARM templates with GitHub Copilot, this will generate the arm template only. We would like to validate it against the ARM documentation & WAF and use this orchestration in a wider task. 

# Question 1 example: Azure Backup and Azure Files
> Generate for me the ARM template to enable Azure Backup for Azure files storage.

## Result

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

# Question example 2: Private Endpoints and storage

## Question
> Generate for me the ARM template to enable private endpoints for Azure Storage. 

## Result

> The official [Azure documentation](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-template) and [template reference](https://learn.microsoft.com/en-us/azure/templates/microsoft.network/privateendpoints) provide confirmation and support for our solution. When you use Azure Private Endpoint, traffic between your virtual network and the service travels over the Microsoft network. This process eliminates exposure from the public internet. The ARM template solution provided in this task is compliant with the Azure Well-Architected Framework. In terms of operational excellence, the use of ARM templates allows for repeatable deployments, reducing manual and error-prone processes. By utilizing Private Endpoints for Azure Storage, you apply best practices in security and performance efficiency, ensuring data privacy and secure network traffic. 


```json
{
  "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "privateEndpointName": {
      "type": "string",
      "metadata": {
        "description": "Specifies the name of the private endpoint."
      }
    },
    "vnetName": {
      "type": "string",
      "metadata": {
        "description": "Specifies the name of the virtual network."
      }
    },
    "subnetName": {
      "type": "string",
      "metadata": {
        "description": "Specifies the name of the subnet."
      }
    },
    "privateLinkResourceName": {
      "type": "string",
      "metadata": {
        "description": "Specifies the name of the private link resource."
      }
    },
    "storageAccountName": {
      "type": "string",
      "metadata": {
        "description": "Specifies the name of the storage account."
      }
    }
  },
  "resources": [
    {
      "type": "Microsoft.Network/privateEndpoints",
      "apiVersion": "2020-04-01",
      "name": "[parameters('privateEndpointName')]",
      "location": "[resourceGroup().location]",
      "properties": {
        "subnet": {
          "id": "[resourceId('Microsoft.Network/virtualNetworks/subnets', parameters('vnetName'), parameters('subnetName'))]"
        },
        "privateLinkServiceConnections": [
          {
            "name": "[concat(parameters('privateEndpointName'), '/plsConnection')]",
            "properties": {
              "privateLinkServiceId": "[resourceId('Microsoft.Storage/storageAccounts', parameters('storageAccountName'))]",
              "groupIds": ["blob"]
            }
          }
        ]
      }
    }
  ]
}
```

| Parameter | Purpose | Potential Values | Default |
| --------- | ------- | ---------------- | ------- |
| privateEndpointName | Specifies the name of the private endpoint. | Any valid string value. | N/A |
| vnetName | Specifies the name of the virtual network. | Any valid string value. | N/A |
| subnetName | Specifies the name of the subnet. | Any valid string value. | N/A |
| privateLinkResourceName | Specifies the name of the private link resource. | Any valid string value. | N/A |
| storageAccountName | Specifies the name of the Azure Storage account. | Any valid string value. | N/A |

* **privateEndpointName**: This parameter is the name you want to assign to the private endpoint. When specifying a name, make sure it's unique to the resource group that the private endpoint is part of.
* **vnetName**: This parameter refers to the name of the virtual network that the private endpoint connects to. Ensure this virtual network exists and is valid before using it as a parameter.
* **subnetName**: The name of the subnet in the aforementioned virtual network. Private endpoints need a dedicated subnet to function correctly.
* **privateLinkResourceName**: This parameter is the name you want to assign to the private link service. It should be unique to the assignment and easily identifiable.
* **storageAccountName**: This parameter is the name of your Azure Storage account that the private endpoint connects to. The storage account needs to exist before you can connect to it via a private endpoint. 

Remember to replace these parameters with your actual values when you're ready to deploy the template. Be mindful of the naming conventions for each resource type as indicated in Azure documentation.

# Question example 3: ANF and Azure Backup

## Question
> Generate for me the ARM template to enable Azure Backup for Azure NetApp files.  

## Result

> As per the current Microsoft Documentation, there isn't a direct ARM template provided for Azure Backup for Azure NetApp Files. For setting up backups for Azure NetApp Files, you would need to manually set them up following the instructions provided in the [Microsoft Docs - Azure Backup](https://docs.microsoft.com/en-us/azure/backup/).
Remark: it also gives a default template to setup a recovery service vault, which is nice but not helpfull. ToDo: need to prompt the critic to remove this.


# Overall Observations
We did several test for also non existing combinations like:

Mistakes in Cosmos and App Service I believe. Maybe need to specify "Azure Backup Service" specifically? 
