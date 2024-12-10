# Flux Enterprise Objects

Flux Enterprise Objects is secure API for retrieving information on Flogistix units on a customers location. 

The Flux Enterprise Objects API is secured by Auth0 and the client must authorize to Auth0 and retrieve a Bearer Token that is to be used on API calls to retrieve records.

The base url of the Flux Enterprise Objects is as follows:  
Development - `https://dev-api.axil.ai/axil/enterprise-objects/`  
Production - `https://api.axil.ai/axil/enterprise-objects/`  

### Get Asset Info  
HTTP Verb: `GET`  
Url: `https://dev-api.axil.ai/axil/enterprise-objects/assets/{netsuite-id}`  
Body: None  
Response:
```
{
  "netsuiteId": {Internal Id},
  "name": "{Unit-Name}",
  "organization": {
    "netsuiteId": {Internal Organization Id},
    "name": "{Customer Organization Name}",
    "orgId": {Internal Id}
  },
  "site": {
    "netsuiteId": {Internal Id},
    "name": "{Customer Site Name}",
    "siteId": {Internal Id}
  },
  "operatingArea": {
    "netsuiteId": {Internal Id},
    "name": "{Operating Area Location}"
  },
  "mechanic": {
    "netsuiteId": {Internal Id},
    "name": "{Mechanic Name}",
    "email": "{Mechanic Email}",
    "phone": "{Mechanic Phone}"
  },
  "transferOrderStatusId": {Internal Transfer Order Status Id},
  "transferOrderStatus": "{Internal Transfer Order Status}",
  "assetTypeId": {Internal Asset Type Id},
  "assetType": "{Internal Asset Type}",
  "ipAddress": "{IP Address}",
  "id": {Internal Id},
  "deviceId": {Internal Device Id},
  "ipInfo": {
    "port": "{Communication Port}"
  },
  "connectivityInfo": {
    "lastUpdatedBy": "{User Last Verified Connection Status}",
    "status": "{Last Connection Status}",
    "lastUpdateTime": {Unix Timestamp of Last Connection Check}
  },
  "assetId": {Asset Id from Flux Realtime}
}
```

### Searching by Key
HTTP Verb: `GET`  
Url: `https://dev-api.axil.ai/axil/enterprise-objects/assets?{dict_key}={value}`
Example: `https://dev-api.axil.ai/axil/enterprise-objects/assets?driver=GED`
`https://dev-api.axil.ai/axil/enterprise-objects/assets?name=12345`
Body: None 
This can return any list of units or specific unit that match the property you provided. For example, you can get the list of all of the units that have a driver of GED, the single unit with the name = 12345, etc.

### Search Asset Info  
When searching for units, the default is to only return 20 assets. The rest of the assets are paged through a queryString parameter called `page`. This allows the consumer to search through all of the results by incereasing the page number. This is an optional item, and is zero based i.e. starts at 0.


HTTP Verb: `GET`  
Url: `https://dev-api.axil.ai/axil/enterprise-objects/assets?search={search criteria}&page={page Number}`  
Body: None  
Response:
```
{
  "totalCount": {result count},
  "assets": [
    {
      "netsuiteId": {Internal Id},
      "name": "{Unit-Name}",
      "organization": {
        "netsuiteId": {Internal Organization Id},
        "name": "{Customer Organization Name}",
        "orgId": {Internal Id}
      },
      "site": {
        "netsuiteId": {Internal Id},
        "name": "{Customer Site Name}",
        "siteId": {Internal Id}
      },
      "operatingArea": {
        "netsuiteId": {Internal Id},
        "name": "{Operating Area Location}"
      },
      "mechanic": {
        "netsuiteId": {Internal Id},
        "name": "{Mechanic Name}",
        "email": "{Mechanic Email}",
        "phone": "{Mechanic Phone}"
      },
      "transferOrderStatusId": {Internal Transfer Order Status Id},
      "transferOrderStatus": "{Internal Transfer Order Status}",
      "assetTypeId": {Internal Asset Type Id},
      "assetType": "{Internal Asset Type}",
      "ipAddress": "{IP Address}",
      "id": {Internal Id},
      "deviceId": {Internal Device Id},
      "ipInfo": {
        "port": "{Communication Port}"
      },
      "connectivityInfo": {
        "lastUpdatedBy": "{User Last Verified Connection Status}",
        "status": "{Last Connection Status}",
        "lastUpdateTime": {Unix Timestamp of Last Connection Check}
      },
      "assetId": {Asset Id from Flux Realtime}
    },
    {
      ... possibly multiple ...
    }
  ],
  "executionTime": "{Time took to run search}"
}
```

### All Assets
To return all of the unit information for your company, you can use the /all endpoint.
This will have a similar respoonse as the search functionality. You can also utilize a size query parameter to get all results.

HTTP Verb: `GET`  
Url: `https://dev-api.axil.ai/axil/enterprise-objects/all`
Body: None  
Response:
```
{
  "totalCount": {result count},
  "assets": [
    {
      "netsuiteId": {Internal Id},
      "name": "{Unit-Name}",
      "organization": {
        "netsuiteId": {Internal Organization Id},
        "name": "{Customer Organization Name}",
        "orgId": {Internal Id}
      },
      "site": {
        "netsuiteId": {Internal Id},
        "name": "{Customer Site Name}",
        "siteId": {Internal Id}
      },
      "operatingArea": {
        "netsuiteId": {Internal Id},
        "name": "{Operating Area Location}"
      },
      "mechanic": {
        "netsuiteId": {Internal Id},
        "name": "{Mechanic Name}",
        "email": "{Mechanic Email}",
        "phone": "{Mechanic Phone}"
      },
      "transferOrderStatusId": {Internal Transfer Order Status Id},
      "transferOrderStatus": "{Internal Transfer Order Status}",
      "assetTypeId": {Internal Asset Type Id},
      "assetType": "{Internal Asset Type}",
      "ipAddress": "{IP Address}",
      "id": {Internal Id},
      "deviceId": {Internal Device Id},
      "ipInfo": {
        "port": "{Communication Port}"
      },
      "connectivityInfo": {
        "lastUpdatedBy": "{User Last Verified Connection Status}",
        "status": "{Last Connection Status}",
        "lastUpdateTime": {Unix Timestamp of Last Connection Check}
      },
      "assetId": {Asset Id from Flux Realtime}
    },
    {
      ... possibly multiple ...
    }
  ],
  "executionTime": "{Time took to run search}"
}
```
