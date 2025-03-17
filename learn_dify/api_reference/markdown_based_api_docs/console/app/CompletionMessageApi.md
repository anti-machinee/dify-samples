# CompletionMessageApi

## Description
- Use for completion app mode
- Use to generate messages from app generation service

## Argument
### inputs
### query
### files
### model_config
### response_mode
### retriever_from
### auto_generate_name
- Always set to false

## CURL
```bash
curl 'http://localhost/console/api/apps/56fe1832-85b1-493f-956e-011225da2ce4/completion-messages' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,vi;q=0.8,en-AU;q=0.7' \
  -H 'Connection: keep-alive' \
  -b $'_ga=GA1.1.1527468203.1720791978; _ga_R1FN4KJKJH=GS1.1.1720791977.1.1.1720793862.0.0.0; PGADMIN_LANGUAGE=en; pga4_session=033e72cd-7e66-4505-812a-89c6c6679d42\u0021FLwPfbIu9YkttoJApE+Ltadh9Uj66vrQexbqR2I+Wew=' \
  -H 'Origin: http://localhost' \
  -H 'Referer: http://localhost/app/56fe1832-85b1-493f-956e-011225da2ce4/configuration' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZWE0MjBiZmMtMTMxZi00OGY0LTljMGYtNWIxNzkyMDEzYzkyIiwiZXhwIjoxNzQwMjE3Njg5LCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.UJZwU7cJauShOuxjGdh3t5UzCQu6G5dwUJLhUshl5oo' \
  -H 'content-type: application/json' \
  -H 'sec-ch-ua: "Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw $'{"inputs":{"Target_code":"Java","default_input":"def main(): return 1"},"model_config":{"pre_prompt":"Providing translation capabilities in multiple programming languages, translating the user\'s input code into the programming language they need. Please translate the following code snippet to {{Target_code}}: When the information entered by the user is not a code snippet, prompt: Please enter a valid code snippet.{{default_input}}","prompt_type":"simple","chat_prompt_config":{},"completion_prompt_config":{},"user_input_form":[{"select":{"label":"Language","variable":"Target_code","required":true,"options":["Java","JavaScript","Swift","Go","Shell","PHP","Python","C","C#","Objective-C","Ruby","R"],"default":""}},{"paragraph":{"label":"default_input","variable":"default_input","required":true,"default":""}}],"dataset_query_variable":"","dataset_configs":{"retrieval_model":"single","datasets":{"datasets":[]},"top_k":4,"reranking_enable":false},"agent_mode":{"enabled":false,"tools":[]},"model":{"provider":"openai","name":"gpt-4o-mini-2024-07-18","mode":"chat","completion_params":{}},"more_like_this":{"enabled":false},"sensitive_word_avoidance":{"configs":[],"enabled":false,"type":""},"text_to_speech":{"enabled":false},"file_upload":{"image":{"detail":"high","enabled":false,"number_limits":3,"transfer_methods":["remote_url","local_file"]},"enabled":false,"allowed_file_types":[],"allowed_file_extensions":[".JPG",".JPEG",".PNG",".GIF",".WEBP",".SVG",".MP4",".MOV",".MPEG",".MPGA"],"allowed_file_upload_methods":["remote_url","local_file"],"number_limits":3,"fileUploadConfig":{"file_size_limit":15,"batch_count_limit":5,"image_file_size_limit":10,"video_file_size_limit":100,"audio_file_size_limit":50,"workflow_file_upload_limit":10}},"opening_statement":"","suggested_questions_after_answer":{"enabled":false},"speech_to_text":{"enabled":false},"retriever_resource":{"enabled":false}},"response_mode":"streaming"}'
```

## Payload
```bash
{
  "inputs": {
    "Target_code": "Java",
    "default_input": "def main(): return 1"
  },
  "model_config": {
    "pre_prompt": "Providing translation capabilities in multiple programming languages, translating the user's input code into the programming language they need. Please translate the following code snippet to {{Target_code}}: When the information entered by the user is not a code snippet, prompt: Please enter a valid code snippet.{{default_input}}",
    "prompt_type": "simple",
    "chat_prompt_config": {},
    "completion_prompt_config": {},
    "user_input_form": [
      {
        "select": {
          "label": "Language",
          "variable": "Target_code",
          "required": true,
          "options": [
            "Java",
            "JavaScript",
            "Swift",
            "Go",
            "Shell",
            "PHP",
            "Python",
            "C",
            "C#",
            "Objective-C",
            "Ruby",
            "R"
          ],
          "default": ""
        }
      },
      {
        "paragraph": {
          "label": "default_input",
          "variable": "default_input",
          "required": true,
          "default": ""
        }
      }
    ],
    "dataset_query_variable": "",
    "dataset_configs": {
      "retrieval_model": "single",
      "datasets": {
        "datasets": []
      },
      "top_k": 4,
      "reranking_enable": false
    },
    "agent_mode": {
      "enabled": false,
      "tools": []
    },
    "model": {
      "provider": "openai",
      "name": "gpt-4o-mini-2024-07-18",
      "mode": "chat",
      "completion_params": {}
    },
    "more_like_this": {
      "enabled": false
    },
    "sensitive_word_avoidance": {
      "configs": [],
      "enabled": false,
      "type": ""
    },
    "text_to_speech": {
      "enabled": false
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
    "opening_statement": "",
    "suggested_questions_after_answer": {
      "enabled": false
    },
    "speech_to_text": {
      "enabled": false
    },
    "retriever_resource": {
      "enabled": false
    }
  },
  "response_mode": "streaming"
}
```

## Response
```bash
data: {"event": "message", "message_id": "f02165f7-7681-4ac2-b6ca-64d1313b4d74", "created_at": 1740214934, "task_id": "25d911e2-f35b-4fe3-b779-21448223d45a", "id": "f02165f7-7681-4ac2-b6ca-64d1313b4d74", "answer": "To", "from_variable_selector": null}

......

data: {"event": "message_end", "message_id": "f02165f7-7681-4ac2-b6ca-64d1313b4d74", "created_at": 1740214934, "task_id": "25d911e2-f35b-4fe3-b779-21448223d45a", "id": "f02165f7-7681-4ac2-b6ca-64d1313b4d74", "metadata": {"usage": {"prompt_tokens": 64, "prompt_unit_price": "0.15", "prompt_price_unit": "0.000001", "prompt_price": "0.0000096", "completion_tokens": 382, "completion_unit_price": "0.60", "completion_price_unit": "0.000001", "completion_price": "0.0002292", "total_tokens": 446, "total_price": "0.0002388", "currency": "USD", "latency": 6.4755935780049185}}, "files": null}
```

## Analysis
### Validation
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
- generator or event stream
- Read for more information AppGenerateService
### Error handling
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
