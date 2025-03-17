# AppParameterApi

## Description
- Get description about the app

## CURL
```bash
curl \
-X GET 'http://localhost:5001/v1/parameters' \
-H 'Authorization: Bearer app-xAOUlilPbi09yywXlGnKP2LW'
```

## Response
```bash
{
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
  "user_input_form": [
    {
      "file": {
        "allowed_file_extensions": [],
        "allowed_file_types": [
          "document"
        ],
        "allowed_file_upload_methods": [
          "local_file",
          "remote_url"
        ],
        "label": "Document to translate",
        "max_length": 5,
        "options": [],
        "required": true,
        "type": "file",
        "variable": "text"
      }
    },
    {
      "text-input": {
        "label": "Language to be translated in: ",
        "max_length": 48,
        "options": [],
        "required": true,
        "type": "text-input",
        "variable": "target_language"
      }
    }
  ],
  "sensitive_word_avoidance": {
    "enabled": false
  },
  "file_upload": {
    "image": {
      "enabled": false,
      "number_limits": 3,
      "transfer_methods": [
        "local_file",
        "remote_url"
      ]
    },
    "enabled": false,
    "allowed_file_types": [
      "image"
    ],
    "allowed_file_extensions": [
      ".JPG",
      ".JPEG",
      ".PNG",
      ".GIF",
      ".WEBP",
      ".SVG"
    ],
    "allowed_file_upload_methods": [
      "local_file",
      "remote_url"
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
  "system_parameters": {
    "image_file_size_limit": 10,
    "video_file_size_limit": 100,
    "audio_file_size_limit": 50,
    "file_size_limit": 15,
    "workflow_file_upload_limit": 10
  }
}
```

## Analysis
- Authorize by app token in api_tokens table
- Get workflow app
- Get feature dicts
