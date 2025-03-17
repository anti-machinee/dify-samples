# AppMetaApi

## Description
- Get description about the app

## CURL
```bash
curl \
-X GET 'http://localhost:5001/v1/meta' \
-H 'Authorization: Bearer app-xAOUlilPbi09yywXlGnKP2LW'
```

## Response
```bash
{
  "tool_icons": {
    "crawl_job": "/console/api/workspaces/current/tool-provider/builtin/firecrawl/icon"
  }
}
```

## Analysis
- Authorize by token in api_tokens table
