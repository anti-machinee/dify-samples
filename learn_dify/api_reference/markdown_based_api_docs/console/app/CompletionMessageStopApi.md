# CompletionMessageStopApi

## Description
- Use for completion app mode
- Use to stop generating messages
- Apply for streaming response mode

## Argument
### task_id

## CURL
```bash
curl --location --request POST 'http://localhost/console/api/apps/da1a97da-ba11-4c57-a414-7d2b1284fa31/completion-messages/bffd7a9f-1561-4e11-956c-fb722d5b2f8e/stop' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDYxYTBkNTgtN2NhYy00MmUxLWI2ZWUtMGNkZjRiZWE4YTM2IiwiZXhwIjoxNzQwNzg4MTY5LCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.KJt9Kn-Zn6tqI1Y9g0oM9kQFSCjqZkUZGOTqAHF0evE'
```

## Payload
- No payload

## Response
```bash
{
    "result": "success"
}
```

## Analysis (Same as ChatMessageStopApi)
### Validation
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