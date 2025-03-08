# ChatMessageStopApi

## Description
- Use for completion app mode
- Use to stop generating messages
- Apply for streaming response mode

## Argument
### task_id

## CURL
```bash
curl --location --request POST 'http://localhost/console/api/apps/13f717a8-aba2-4155-b139-817ca700651f/chat-messages/bb45861d-c453-4bca-ac22-09e9147bac57/stop' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDYxYTBkNTgtN2NhYy00MmUxLWI2ZWUtMGNkZjRiZWE4YTM2IiwiZXhwIjoxNzQwODMyODg4LCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.PyN2nZWUEPeRcNs9h7PdTxnkvdUHHuU7gJ8WW2Ko6cU'
```

## Payload
- No payload

## Response
```bash
{
    "result": "success"
}
```

## Analysis
### Validation (Same as CompletionMessageApi)
- Validate setup
- Validate login
- Validate account initialization
- Get app model
### Action
- Set stop flag to task by set_stop_flag
### Response
- Always return success message
### Error handling
- Do not handle any error
