# ChatMessageApi (POST)

## Description
- Use for chat and agent chat app mode
- Use to generate messages from app generation service

## Argument
### inputs
### query
### files
### model_config
### conversation_id
### parent_message_id
### response_mode
### retriever_from
### auto_generate_name
- Always set to false

## CURL
```bash
curl 'http://localhost/console/api/apps/13f717a8-aba2-4155-b139-817ca700651f/chat-messages' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,vi;q=0.8,en-AU;q=0.7' \
  -H 'Connection: keep-alive' \
  -b $'pga4_session=db94af4f-225c-49cd-ba4e-aa627020717d\u0021BPqOqFoeYNKnGh7roqj6UTGYp8Cy5ZZRKR9f7ezHwhc=; PGADMIN_LANGUAGE=en' \
  -H 'Origin: http://localhost' \
  -H 'Referer: http://localhost/app/13f717a8-aba2-4155-b139-817ca700651f/configuration' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDYxYTBkNTgtN2NhYy00MmUxLWI2ZWUtMGNkZjRiZWE4YTM2IiwiZXhwIjoxNzQwODMyODg4LCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.PyN2nZWUEPeRcNs9h7PdTxnkvdUHHuU7gJ8WW2Ko6cU' \
  -H 'content-type: application/json' \
  -H 'sec-ch-ua: "Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw '{"response_mode":"streaming","conversation_id":"","files":[],"query":"asdasdsad","inputs":{},"model_config":{"pre_prompt":"Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected code should be functional, efficient, and adhere to best practices in Python programming.","prompt_type":"simple","chat_prompt_config":{},"completion_prompt_config":{},"user_input_form":[],"dataset_query_variable":"","opening_statement":"","more_like_this":{"enabled":false},"suggested_questions":[],"suggested_questions_after_answer":{"enabled":false},"text_to_speech":{"enabled":false,"language":"","voice":""},"speech_to_text":{"enabled":false},"retriever_resource":{"enabled":false},"sensitive_word_avoidance":{"configs":[],"enabled":false,"type":""},"agent_mode":{"enabled":false,"max_iteration":5,"strategy":"function_call","tools":[]},"dataset_configs":{"retrieval_model":"single","datasets":{"datasets":[]},"top_k":4,"reranking_enable":false},"file_upload":{"image":{"detail":"high","enabled":false,"number_limits":3,"transfer_methods":["remote_url","local_file"]},"enabled":false,"allowed_file_types":[],"allowed_file_extensions":[".JPG",".JPEG",".PNG",".GIF",".WEBP",".SVG",".MP4",".MOV",".MPEG",".MPGA"],"allowed_file_upload_methods":["remote_url","local_file"],"number_limits":3,"fileUploadConfig":{"file_size_limit":15,"batch_count_limit":5,"image_file_size_limit":10,"video_file_size_limit":100,"audio_file_size_limit":50,"workflow_file_upload_limit":10}},"annotation_reply":{"enabled":false},"supportAnnotation":true,"appId":"13f717a8-aba2-4155-b139-817ca700651f","supportCitationHitInfo":true,"model":{"provider":"openai","name":"gpt-4o-mini-2024-07-18","mode":"chat","completion_params":{}}},"parent_message_id":null}'
```
## Payload
```bash
{
    "response_mode": "streaming",
    "conversation_id": "",
    "files": [],
    "query": "asdasdsad",
    "inputs": {},
    "model_config": {
        "pre_prompt": "Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected code should be functional, efficient, and adhere to best practices in Python programming.",
        "prompt_type": "simple",
        "chat_prompt_config": {},
        "completion_prompt_config": {},
        "user_input_form": [],
        "dataset_query_variable": "",
        "opening_statement": "",
        "more_like_this": {
            "enabled": false
        },
        "suggested_questions": [],
        "suggested_questions_after_answer": {
            "enabled": false
        },
        "text_to_speech": {
            "enabled": false,
            "language": "",
            "voice": ""
        },
        "speech_to_text": {
            "enabled": false
        },
        "retriever_resource": {
            "enabled": false
        },
        "sensitive_word_avoidance": {
            "configs": [],
            "enabled": false,
            "type": ""
        },
        "agent_mode": {
            "enabled": false,
            "max_iteration": 5,
            "strategy": "function_call",
            "tools": []
        },
        "dataset_configs": {
            "retrieval_model": "single",
            "datasets": {
                "datasets": []
            },
            "top_k": 4,
            "reranking_enable": false
        },
        "file_upload": {
            "image": {
                "detail": "high",
                "enabled": false,
                "number_limits": 3,
                "transfer_methods": [
                    "remote_url",
                    "local_file"
                ]
            },
            "enabled": false,
            "allowed_file_types": [],
            "allowed_file_extensions": [
                ".JPG",
                ".JPEG",
                ".PNG",
                ".GIF",
                ".WEBP",
                ".SVG",
                ".MP4",
                ".MOV",
                ".MPEG",
                ".MPGA"
            ],
            "allowed_file_upload_methods": [
                "remote_url",
                "local_file"
            ],
            "number_limits": 3,
            "fileUploadConfig": {
                "file_size_limit": 15,
                "batch_count_limit": 5,
                "image_file_size_limit": 10,
                "video_file_size_limit": 100,
                "audio_file_size_limit": 50,
                "workflow_file_upload_limit": 10
            }
        },
        "annotation_reply": {
            "enabled": false
        },
        "supportAnnotation": true,
        "appId": "13f717a8-aba2-4155-b139-817ca700651f",
        "supportCitationHitInfo": true,
        "model": {
            "provider": "openai",
            "name": "gpt-4o-mini-2024-07-18",
            "mode": "chat",
            "completion_params": {}
        }
    },
    "parent_message_id": null
}
```

## Response
- It is different from CompletionMessageApi by conversation_id
```bash
data: {"event": "message", "conversation_id": "0524ffca-4a81-41b9-ac1e-9c529200bf33", "message_id": "6ab5e1cc-8bf5-48c5-8a1f-4c5567fe16a7", "created_at": 1740830608, "task_id": "bb45861d-c453-4bca-ac22-09e9147bac57", "id": "6ab5e1cc-8bf5-48c5-8a1f-4c5567fe16a7", "answer": "It", "from_variable_selector": null}

......

data: {"event": "message_end", "conversation_id": "0524ffca-4a81-41b9-ac1e-9c529200bf33", "message_id": "6ab5e1cc-8bf5-48c5-8a1f-4c5567fe16a7", "created_at": 1740830608, "task_id": "bb45861d-c453-4bca-ac22-09e9147bac57", "id": "6ab5e1cc-8bf5-48c5-8a1f-4c5567fe16a7", "metadata": {"usage": {"prompt_tokens": 80, "prompt_unit_price": "0.15", "prompt_price_unit": "0.000001", "prompt_price": "0.0000120", "completion_tokens": 45, "completion_unit_price": "0.60", "completion_price_unit": "0.000001", "completion_price": "0.0000270", "total_tokens": 125, "total_price": "0.0000390", "currency": "USD", "latency": 0.9524665459994139}}, "files": null}
```

## Analysis
### Validation (Same as CompletionMessageApi)
- Validate setup
- Validate login
- Validate account initialization
- Get app model
### Action
- Check if response mode is streaming or blocking
- Get current user
- Get response of LLM from AppGenerateService
- Handle reponse of LLM generator by compact_generate_response
### Response
### Error handling (Same as CompletionMessageApi)
- ConversationNotExistsError
  - NotFound
- ConversationCompletedError
  - ConversationCompletedError
- AppModelConfigBrokenError
  - AppUnavailableError
- ProviderTokenNotInitError
  - ProviderNotInitializeError
- QuotaExceededError
  - ProviderQuotaExceededError
- ModelCurrentlyNotSupportError
  - ProviderModelCurrentlyNotSupportError
- InvokeError
  - CompletionRequestError
- ValueError
  - ValueError
- Exception
  - InternalServerError

# ChatMessageApi (GET)

## Description
- Get messages given conversation_id

## Argument
- No arguments

## CURL
```bash
curl 'http://localhost/console/api/apps/13f717a8-aba2-4155-b139-817ca700651f/chat-messages?conversation_id=0524ffca-4a81-41b9-ac1e-9c529200bf33' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,vi;q=0.8,en-AU;q=0.7' \
  -H 'Connection: keep-alive' \
  -b $'pga4_session=db94af4f-225c-49cd-ba4e-aa627020717d\u0021BPqOqFoeYNKnGh7roqj6UTGYp8Cy5ZZRKR9f7ezHwhc=; PGADMIN_LANGUAGE=en' \
  -H 'Referer: http://localhost/app/13f717a8-aba2-4155-b139-817ca700651f/configuration' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDYxYTBkNTgtN2NhYy00MmUxLWI2ZWUtMGNkZjRiZWE4YTM2IiwiZXhwIjoxNzQwODMyODg4LCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.PyN2nZWUEPeRcNs9h7PdTxnkvdUHHuU7gJ8WW2Ko6cU' \
  -H 'content-type: application/json' \
  -H 'sec-ch-ua: "Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

## Payload
```bash
conversation_id=0524ffca-4a81-41b9-ac1e-9c529200bf33
```

## Response
```bash
{
    "limit": 20,
    "has_more": false,
    "data": [
        {
            "id": "6ab5e1cc-8bf5-48c5-8a1f-4c5567fe16a7",
            "conversation_id": "0524ffca-4a81-41b9-ac1e-9c529200bf33",
            "inputs": {},
            "query": "asdasdsad",
            "message": [
                {
                    "role": "system",
                    "text": "Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected code should be functional, efficient, and adhere to best practices in Python programming.\n",
                    "files": []
                },
                {
                    "role": "user",
                    "text": "asdasdsad",
                    "files": []
                }
            ],
            "message_tokens": 80,
            "answer": "It seems that your message is not clear. If you're looking for help with a specific piece of Python code, please provide the code snippet you'd like me to analyze. I'll be happy to identify any issues and suggest corrections.",
            "answer_tokens": 45,
            "provider_response_latency": 0.9878950329994041,
            "from_source": "console",
            "from_end_user_id": null,
            "from_account_id": "061a0d58-7cac-42e1-b6ee-0cdf4bea8a36",
            "feedbacks": [],
            "workflow_run_id": null,
            "annotation": null,
            "annotation_hit_history": null,
            "created_at": 1740830608,
            "agent_thoughts": [],
            "message_files": [],
            "metadata": {},
            "status": "normal",
            "error": null,
            "parent_message_id": null
        }
    ]
}
```

## Analysis
- I cannot find code (based on version 0.15.3)