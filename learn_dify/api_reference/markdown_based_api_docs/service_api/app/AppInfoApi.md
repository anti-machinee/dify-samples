# AppInfoApi

## Description
- Get name, description and tags of the app

## CURL
```bash
curl \
-X GET 'http://localhost:5001/v1/info' \
-H 'Authorization: Bearer app-xAOUlilPbi09yywXlGnKP2LW'
```

## Response
```bash
{
  "name": "File Translation",
  "description": "",
  "tags": []
}
```

## Analysis
- Authorize by token in api_tokens table
