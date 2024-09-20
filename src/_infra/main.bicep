param loc string = 'swedencentral'
param resourcePrefix string = 'nl-stu-2024hack-'

resource openai_svc 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: '${resourcePrefix}openai'
  location: loc
  kind: 'OpenAI'
  sku: {
    name: 'S0'
  }
  properties: {}
}

resource store 'Microsoft.Search/searchServices@2024-03-01-preview' = {
  name: '${resourcePrefix}search'
  location: loc
  sku: {
    name: 'standard'
  }
  properties: {}
}

resource storageaccount 'Microsoft.Storage/storageAccounts@2023-04-01' = {
  name: replace('${resourcePrefix}store','-','')
  location: loc
  kind: 'StorageV2'
  sku: {
    name: 'Premium_LRS'
  }
}
