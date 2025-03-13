# AppApi

## Argument
- App model

## CURL
```bash
curl 'http://localhost/console/api/apps/13f717a8-aba2-4155-b139-817ca700651f' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,vi;q=0.8,en-AU;q=0.7' \
  -H 'Connection: keep-alive' \
  -b $'pga4_session=db94af4f-225c-49cd-ba4e-aa627020717d\u0021BPqOqFoeYNKnGh7roqj6UTGYp8Cy5ZZRKR9f7ezHwhc=; PGADMIN_LANGUAGE=en' \
  -H 'Referer: http://localhost/app/13f717a8-aba2-4155-b139-817ca700651f/configuration' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDYxYTBkNTgtN2NhYy00MmUxLWI2ZWUtMGNkZjRiZWE4YTM2IiwiZXhwIjoxNzQwODM2ODYyLCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.u8HHtV9tCsnmJRSakEw0eVo3q2kj5eM6_tCh2wH8w0w' \
  -H 'content-type: application/json' \
  -H 'sec-ch-ua: "Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

## Response
```bash
{
    "id": "13f717a8-aba2-4155-b139-817ca700651f",
    "name": "Python bug fixer",
    "description": "",
    "mode": "chat",
    "icon_type": "emoji",
    "icon": "\ud83d\udd27",
    "icon_background": "#EFF1F5",
    "icon_url": null,
    "enable_site": true,
    "enable_api": true,
    "model_config": {
        "opening_statement": "",
        "suggested_questions": [],
        "suggested_questions_after_answer": {
            "enabled": false
        },
        "speech_to_text": {
            "enabled": false
        },
        "text_to_speech": {
            "enabled": false,
            "language": "",
            "voice": ""
        },
        "retriever_resource": {
            "enabled": false
        },
        "annotation_reply": {
            "enabled": false
        },
        "more_like_this": {
            "enabled": false
        },
        "sensitive_word_avoidance": {
            "configs": [],
            "enabled": false,
            "type": ""
        },
        "external_data_tools": [],
        "model": {
            "completion_params": {
                "frequency_penalty": 0,
                "max_tokens": 512,
                "presence_penalty": 0,
                "stop": [],
                "temperature": 0,
                "top_p": 1
            },
            "mode": "chat",
            "name": "gpt-3.5-turbo",
            "provider": "openai"
        },
        "user_input_form": [],
        "dataset_query_variable": "",
        "pre_prompt": "Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected code should be functional, efficient, and adhere to best practices in Python programming.",
        "agent_mode": {
            "enabled": false,
            "max_iteration": 5,
            "strategy": "function_call",
            "tools": []
        },
        "prompt_type": "simple",
        "chat_prompt_config": {},
        "completion_prompt_config": {},
        "dataset_configs": {
            "datasets": {
                "datasets": []
            },
            "retrieval_model": "single"
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
            }
        },
        "created_by": "061a0d58-7cac-42e1-b6ee-0cdf4bea8a36",
        "created_at": 1740829333,
        "updated_by": "061a0d58-7cac-42e1-b6ee-0cdf4bea8a36",
        "updated_at": 1740829333
    },
    "workflow": null,
    "site": {
        "access_token": "Aejku6JsaE3nLUsM",
        "code": "Aejku6JsaE3nLUsM",
        "title": "Python bug fixer",
        "icon_type": "emoji",
        "icon": "\ud83d\udd27",
        "icon_background": "#EFF1F5",
        "icon_url": null,
        "description": null,
        "default_language": "en-US",
        "chat_color_theme": null,
        "chat_color_theme_inverted": false,
        "customize_domain": null,
        "copyright": null,
        "privacy_policy": null,
        "custom_disclaimer": "",
        "customize_token_strategy": "not_allow",
        "prompt_public": false,
        "app_base_url": "http://localhost",
        "show_workflow_steps": true,
        "use_icon_as_answer_icon": false,
        "created_by": "061a0d58-7cac-42e1-b6ee-0cdf4bea8a36",
        "created_at": 1740829333,
        "updated_by": "061a0d58-7cac-42e1-b6ee-0cdf4bea8a36",
        "updated_at": 1740829333
    },
    "api_base_url": "http://localhost/v1",
    "use_icon_as_answer_icon": false,
    "created_by": "061a0d58-7cac-42e1-b6ee-0cdf4bea8a36",
    "created_at": 1740829333,
    "updated_by": "061a0d58-7cac-42e1-b6ee-0cdf4bea8a36",
    "updated_at": 1740829333,
    "deleted_tools": []
}
```

## Analysis
### Validation
- Validate setup
- Validate login
- Validate account initialization
- Validate enterprise license 
- Get app model
### Serialization
- Serialize the return value into a structured API response format
- Data and its format of response are defined
### Action
- Initialize app service
- Get app model. Remember app model is retrieved from get_app_model decorator
