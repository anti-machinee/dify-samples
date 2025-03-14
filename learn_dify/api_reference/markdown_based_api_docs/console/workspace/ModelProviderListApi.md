# ModelProviderListApi

## Argument
- model_type

## CURL
```bash
curl 'http://localhost/console/api/workspaces/current/model-providers' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,vi;q=0.8,en-AU;q=0.7' \
  -H 'Connection: keep-alive' \
  -b $'pga4_session=b6535706-ae8a-443e-bdfd-dca89424b322\u00211FLgJJKrucRIi/k85oqB7CGBV1TL51eyl1J0/zkrDJM=' \
  -H 'Referer: http://localhost/app/f3f6d21f-a90d-4d55-8973-b81d56cebdcf/configuration' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDYxYTBkNTgtN2NhYy00MmUxLWI2ZWUtMGNkZjRiZWE4YTM2IiwiZXhwIjoxNzQxOTIxMDQ5LCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.y0P_Po-dZJ6Q8uHNigRO1gXIsI6QO8fA2ybdguZKpw8' \
  -H 'content-type: application/json' \
  -H 'sec-ch-ua: "Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

## Response
```bash
{
  "data": [
    {
      "provider": "openai",
      "label": {
        "zh_Hans": "OpenAI",
        "en_US": "OpenAI"
      },
      "description": {
        "zh_Hans": "OpenAI 提供的模型，例如 GPT-3.5-Turbo 和 GPT-4。",
        "en_US": "Models provided by OpenAI, such as GPT-3.5-Turbo and GPT-4."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/openai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/openai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/openai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/openai/icon_large/en_US"
      },
      "background": "#E5E7EB",
      "help": {
        "title": {
          "zh_Hans": "从 OpenAI 获取 API Key",
          "en_US": "Get your API Key from OpenAI"
        },
        "url": {
          "zh_Hans": "https://platform.openai.com/account/api-keys",
          "en_US": "https://platform.openai.com/account/api-keys"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "speech2text",
        "moderation",
        "tts"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "openai_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "openai_organization",
            "label": {
              "zh_Hans": "组织 ID",
              "en_US": "Organization"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的组织 ID",
              "en_US": "Enter your Organization ID"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "openai_api_base",
            "label": {
              "zh_Hans": "API Base",
              "en_US": "API Base"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Base, 如：https://api.openai.com",
              "en_US": "Enter your API Base, e.g. https://api.openai.com"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "openai_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "openai_organization",
            "label": {
              "zh_Hans": "组织 ID",
              "en_US": "Organization"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的组织 ID",
              "en_US": "Enter your Organization ID"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "openai_api_base",
            "label": {
              "zh_Hans": "API Base",
              "en_US": "API Base"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Base",
              "en_US": "Enter your API Base"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "active"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "anthropic",
      "label": {
        "zh_Hans": "Anthropic",
        "en_US": "Anthropic"
      },
      "description": {
        "zh_Hans": "Anthropic 的强大模型，例如 Claude 3。",
        "en_US": "Anthropic’s powerful models, such as Claude 3."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/anthropic/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/anthropic/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/anthropic/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/anthropic/icon_large/en_US"
      },
      "background": "#F0F0EB",
      "help": {
        "title": {
          "zh_Hans": "从 Anthropic 获取 API Key",
          "en_US": "Get your API Key from Anthropic"
        },
        "url": {
          "zh_Hans": "https://console.anthropic.com/account/keys",
          "en_US": "https://console.anthropic.com/account/keys"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "anthropic_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "anthropic_api_url",
            "label": {
              "zh_Hans": "API URL",
              "en_US": "API URL"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API URL",
              "en_US": "Enter your API URL"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "azure_openai",
      "label": {
        "zh_Hans": "Azure OpenAI Service Model",
        "en_US": "Azure OpenAI Service Model"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/azure_openai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/azure_openai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/azure_openai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/azure_openai/icon_large/en_US"
      },
      "background": "#E3F0FF",
      "help": {
        "title": {
          "zh_Hans": "从 Azure 获取 API Key",
          "en_US": "Get your API key from Azure"
        },
        "url": {
          "zh_Hans": "https://azure.microsoft.com/en-us/products/ai-services/openai-service",
          "en_US": "https://azure.microsoft.com/en-us/products/ai-services/openai-service"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "speech2text",
        "tts"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "部署名称",
            "en_US": "Deployment Name"
          },
          "placeholder": {
            "zh_Hans": "在此输入您的部署名称，与 Azure 部署名称匹配。",
            "en_US": "Enter your Deployment Name here, matching the Azure deployment name."
          }
        },
        "credential_form_schemas": [
          {
            "variable": "openai_api_base",
            "label": {
              "zh_Hans": "API 域名",
              "en_US": "API Endpoint URL"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API 域名，如：https://example.com/xxx",
              "en_US": "Enter your API Endpoint, eg: https://example.com/xxx"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "openai_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API key here"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "openai_api_version",
            "label": {
              "zh_Hans": "API 版本",
              "en_US": "API Version"
            },
            "type": "select",
            "required": true,
            "default": null,
            "options": [
              {
                "label": {
                  "zh_Hans": "2024-10-01-preview",
                  "en_US": "2024-10-01-preview"
                },
                "value": "2024-10-01-preview",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-09-01-preview",
                  "en_US": "2024-09-01-preview"
                },
                "value": "2024-09-01-preview",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-08-01-preview",
                  "en_US": "2024-08-01-preview"
                },
                "value": "2024-08-01-preview",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-07-01-preview",
                  "en_US": "2024-07-01-preview"
                },
                "value": "2024-07-01-preview",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-05-01-preview",
                  "en_US": "2024-05-01-preview"
                },
                "value": "2024-05-01-preview",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-04-01-preview",
                  "en_US": "2024-04-01-preview"
                },
                "value": "2024-04-01-preview",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-03-01-preview",
                  "en_US": "2024-03-01-preview"
                },
                "value": "2024-03-01-preview",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-02-15-preview",
                  "en_US": "2024-02-15-preview"
                },
                "value": "2024-02-15-preview",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2023-12-01-preview",
                  "en_US": "2023-12-01-preview"
                },
                "value": "2023-12-01-preview",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-02-01",
                  "en_US": "2024-02-01"
                },
                "value": "2024-02-01",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-06-01",
                  "en_US": "2024-06-01"
                },
                "value": "2024-06-01",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "2024-10-21",
                  "en_US": "2024-10-21"
                },
                "value": "2024-10-21",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "在此选择您的 API 版本",
              "en_US": "Select your API Version here"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "base_model_name",
            "label": {
              "zh_Hans": "基础模型",
              "en_US": "Base Model"
            },
            "type": "select",
            "required": true,
            "default": null,
            "options": [
              {
                "label": {
                  "zh_Hans": "gpt-35-turbo",
                  "en_US": "gpt-35-turbo"
                },
                "value": "gpt-35-turbo",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-35-turbo-0125",
                  "en_US": "gpt-35-turbo-0125"
                },
                "value": "gpt-35-turbo-0125",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-35-turbo-16k",
                  "en_US": "gpt-35-turbo-16k"
                },
                "value": "gpt-35-turbo-16k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4",
                  "en_US": "gpt-4"
                },
                "value": "gpt-4",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4-32k",
                  "en_US": "gpt-4-32k"
                },
                "value": "gpt-4-32k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "o1-mini",
                  "en_US": "o1-mini"
                },
                "value": "o1-mini",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "o1-preview",
                  "en_US": "o1-preview"
                },
                "value": "o1-preview",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4o-mini",
                  "en_US": "gpt-4o-mini"
                },
                "value": "gpt-4o-mini",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4o-mini-2024-07-18",
                  "en_US": "gpt-4o-mini-2024-07-18"
                },
                "value": "gpt-4o-mini-2024-07-18",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4o",
                  "en_US": "gpt-4o"
                },
                "value": "gpt-4o",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4o-2024-05-13",
                  "en_US": "gpt-4o-2024-05-13"
                },
                "value": "gpt-4o-2024-05-13",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4o-2024-08-06",
                  "en_US": "gpt-4o-2024-08-06"
                },
                "value": "gpt-4o-2024-08-06",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4o-2024-11-20",
                  "en_US": "gpt-4o-2024-11-20"
                },
                "value": "gpt-4o-2024-11-20",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4-turbo",
                  "en_US": "gpt-4-turbo"
                },
                "value": "gpt-4-turbo",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4-turbo-2024-04-09",
                  "en_US": "gpt-4-turbo-2024-04-09"
                },
                "value": "gpt-4-turbo-2024-04-09",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4-0125-preview",
                  "en_US": "gpt-4-0125-preview"
                },
                "value": "gpt-4-0125-preview",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4-1106-preview",
                  "en_US": "gpt-4-1106-preview"
                },
                "value": "gpt-4-1106-preview",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-4-vision-preview",
                  "en_US": "gpt-4-vision-preview"
                },
                "value": "gpt-4-vision-preview",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "gpt-35-turbo-instruct",
                  "en_US": "gpt-35-turbo-instruct"
                },
                "value": "gpt-35-turbo-instruct",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "text-embedding-ada-002",
                  "en_US": "text-embedding-ada-002"
                },
                "value": "text-embedding-ada-002",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "text-embedding"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "text-embedding-3-small",
                  "en_US": "text-embedding-3-small"
                },
                "value": "text-embedding-3-small",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "text-embedding"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "text-embedding-3-large",
                  "en_US": "text-embedding-3-large"
                },
                "value": "text-embedding-3-large",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "text-embedding"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "whisper-1",
                  "en_US": "whisper-1"
                },
                "value": "whisper-1",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "speech2text"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "tts-1",
                  "en_US": "tts-1"
                },
                "value": "tts-1",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "tts"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "tts-1-hd",
                  "en_US": "tts-1-hd"
                },
                "value": "tts-1-hd",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "tts"
                  }
                ]
              }
            ],
            "placeholder": {
              "zh_Hans": "在此输入您的模型版本",
              "en_US": "Enter your model version"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "google",
      "label": {
        "zh_Hans": "Google",
        "en_US": "Google"
      },
      "description": {
        "zh_Hans": "谷歌提供的 Gemini 模型.",
        "en_US": "Google's Gemini model."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/google/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/google/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/google/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/google/icon_large/en_US"
      },
      "background": "#FCFDFF",
      "help": {
        "title": {
          "zh_Hans": "从 Google 获取 API Key",
          "en_US": "Get your API Key from Google"
        },
        "url": {
          "zh_Hans": "https://ai.google.dev/",
          "en_US": "https://ai.google.dev/"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "google_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "vertex_ai",
      "label": {
        "zh_Hans": "Vertex AI | Google Cloud Platform",
        "en_US": "Vertex AI | Google Cloud Platform"
      },
      "description": {
        "zh_Hans": "Vertex AI in Google Cloud Platform.",
        "en_US": "Vertex AI in Google Cloud Platform."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/vertex_ai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/vertex_ai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/vertex_ai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/vertex_ai/icon_large/en_US"
      },
      "background": "#FCFDFF",
      "help": {
        "title": {
          "zh_Hans": "Get your Access Details from Google",
          "en_US": "Get your Access Details from Google"
        },
        "url": {
          "zh_Hans": "https://cloud.google.com/vertex-ai/",
          "en_US": "https://cloud.google.com/vertex-ai/"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "vertex_project_id",
            "label": {
              "zh_Hans": "Project ID",
              "en_US": "Project ID"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Enter your Google Cloud Project ID",
              "en_US": "Enter your Google Cloud Project ID"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "vertex_location",
            "label": {
              "zh_Hans": "Location",
              "en_US": "Location"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Enter your Google Cloud Location",
              "en_US": "Enter your Google Cloud Location"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "vertex_service_account_key",
            "label": {
              "zh_Hans": "Service Account Key (Leave blank if you use Application Default Credentials)",
              "en_US": "Service Account Key (Leave blank if you use Application Default Credentials)"
            },
            "type": "secret-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Enter your Google Cloud Service Account Key in base64 format",
              "en_US": "Enter your Google Cloud Service Account Key in base64 format"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "nvidia",
      "label": {
        "zh_Hans": "API Catalog",
        "en_US": "API Catalog"
      },
      "description": {
        "zh_Hans": "API Catalog",
        "en_US": "API Catalog"
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/nvidia/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/nvidia/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/nvidia/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/nvidia/icon_large/en_US"
      },
      "background": "#FFFFFF",
      "help": {
        "title": {
          "zh_Hans": "从 NVIDIA 获取 API Key",
          "en_US": "Get your API Key from NVIDIA"
        },
        "url": {
          "zh_Hans": "https://build.nvidia.com/explore/discover",
          "en_US": "https://build.nvidia.com/explore/discover"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "nvidia_nim",
      "label": {
        "zh_Hans": "NVIDIA NIM",
        "en_US": "NVIDIA NIM"
      },
      "description": {
        "zh_Hans": "NVIDIA NIM，一组易于使用的模型推理微服务。",
        "en_US": "NVIDIA NIM, a set of easy-to-use inference microservices."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/nvidia_nim/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/nvidia_nim/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/nvidia_nim/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/nvidia_nim/icon_large/en_US"
      },
      "background": "#EFFDFD",
      "help": {
        "title": {
          "zh_Hans": "了解 NVIDIA NIM 更多信息",
          "en_US": "Learn more about NVIDIA NIM"
        },
        "url": {
          "zh_Hans": "https://www.nvidia.com/en-us/ai/",
          "en_US": "https://www.nvidia.com/en-us/ai/"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型全称",
            "en_US": "Enter full model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "endpoint_url",
            "label": {
              "zh_Hans": "API endpoint URL",
              "en_US": "API endpoint URL"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Base URL, e.g. http://192.168.1.100:8000/v1",
              "en_US": "Base URL, e.g. http://192.168.1.100:8000/v1"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "Completion mode",
              "en_US": "Completion mode"
            },
            "type": "select",
            "required": false,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择对话类型",
              "en_US": "Select completion mode"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens_to_sample",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "cohere",
      "label": {
        "zh_Hans": "Cohere",
        "en_US": "Cohere"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/cohere/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/cohere/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/cohere/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/cohere/icon_large/en_US"
      },
      "background": "#ECE9E3",
      "help": {
        "title": {
          "zh_Hans": "从 cohere 获取 API Key",
          "en_US": "Get your API key from cohere"
        },
        "url": {
          "zh_Hans": "https://dashboard.cohere.com/api-keys",
          "en_US": "https://dashboard.cohere.com/api-keys"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "base_url",
            "label": {
              "zh_Hans": "API Base",
              "en_US": "API Base"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Base，如 https://api.cohere.ai/v1",
              "en_US": "Enter your API Base, e.g. https://api.cohere.ai/v1"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "Completion mode",
              "en_US": "Completion mode"
            },
            "type": "select",
            "required": false,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择对话类型",
              "en_US": "Select completion mode"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "base_url",
            "label": {
              "zh_Hans": "API Base",
              "en_US": "API Base"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Base，如 https://api.cohere.ai/v1",
              "en_US": "Enter your API Base, e.g. https://api.cohere.ai/v1"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "upstage",
      "label": {
        "zh_Hans": "Upstage",
        "en_US": "Upstage"
      },
      "description": {
        "zh_Hans": "Upstage 提供的模型，例如 Solar-1-mini-chat.",
        "en_US": "Models provided by Upstage, such as Solar-1-mini-chat."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/upstage/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/upstage/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/upstage/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/upstage/icon_large/en_US"
      },
      "background": "#FFFFF",
      "help": {
        "title": {
          "zh_Hans": "从 Upstage 获取 API Key",
          "en_US": "Get your API Key from Upstage"
        },
        "url": {
          "zh_Hans": "https://console.upstage.ai/api-keys",
          "en_US": "https://console.upstage.ai/api-keys"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "upstage_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "upstage_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "bedrock",
      "label": {
        "zh_Hans": "AWS",
        "en_US": "AWS"
      },
      "description": {
        "zh_Hans": "AWS Bedrock's models.",
        "en_US": "AWS Bedrock's models."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/bedrock/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/bedrock/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/bedrock/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/bedrock/icon_large/en_US"
      },
      "background": "#FCFDFF",
      "help": {
        "title": {
          "zh_Hans": "Get your Access Key and Secret Access Key from AWS Console",
          "en_US": "Get your Access Key and Secret Access Key from AWS Console"
        },
        "url": {
          "zh_Hans": "https://console.aws.amazon.com/",
          "en_US": "https://console.aws.amazon.com/"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "aws_access_key_id",
            "label": {
              "zh_Hans": "Access Key",
              "en_US": "Access Key (If not provided, credentials are obtained from the running environment.)"
            },
            "type": "secret-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Access Key",
              "en_US": "Enter your Access Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "aws_secret_access_key",
            "label": {
              "zh_Hans": "Secret Access Key",
              "en_US": "Secret Access Key"
            },
            "type": "secret-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Secret Access Key",
              "en_US": "Enter your Secret Access Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "aws_region",
            "label": {
              "zh_Hans": "AWS 地区",
              "en_US": "AWS Region"
            },
            "type": "select",
            "required": true,
            "default": "us-east-1",
            "options": [
              {
                "label": {
                  "zh_Hans": "美国东部 (弗吉尼亚北部)",
                  "en_US": "US East (N. Virginia)"
                },
                "value": "us-east-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "美国东部 (弗吉尼亚北部)",
                  "en_US": "US East (Ohio)"
                },
                "value": "us-east-2",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "美国西部 (俄勒冈州)",
                  "en_US": "US West (Oregon)"
                },
                "value": "us-west-2",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "亚太地区（孟买）",
                  "en_US": "Asia Pacific (Mumbai)"
                },
                "value": "ap-south-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "亚太地区 (新加坡)",
                  "en_US": "Asia Pacific (Singapore)"
                },
                "value": "ap-southeast-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "亚太地区 (悉尼)",
                  "en_US": "Asia Pacific (Sydney)"
                },
                "value": "ap-southeast-2",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "亚太地区 (东京)",
                  "en_US": "Asia Pacific (Tokyo)"
                },
                "value": "ap-northeast-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "亚太地区（首尔）",
                  "en_US": "Asia Pacific (Seoul)"
                },
                "value": "ap-northeast-2",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "加拿大（中部）",
                  "en_US": "Canada (Central)"
                },
                "value": "ca-central-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "欧洲 (法兰克福)",
                  "en_US": "Europe (Frankfurt)"
                },
                "value": "eu-central-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "欧洲（爱尔兰）",
                  "en_US": "Europe (Ireland)"
                },
                "value": "eu-west-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "欧洲西部 (伦敦)",
                  "en_US": "Europe (London)"
                },
                "value": "eu-west-2",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "欧洲（巴黎）",
                  "en_US": "Europe (Paris)"
                },
                "value": "eu-west-3",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "南美洲（圣保罗）",
                  "en_US": "South America (São Paulo)"
                },
                "value": "sa-east-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "AWS GovCloud (US-West)",
                  "en_US": "AWS GovCloud (US-West)"
                },
                "value": "us-gov-west-1",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "model_for_validation",
            "label": {
              "zh_Hans": "可用模型名称",
              "en_US": "Available Model Name"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "为了进行验证，请输入一个您可用的模型名称 (例如：amazon.titan-text-lite-v1)",
              "en_US": "A model you have access to (e.g. amazon.titan-text-lite-v1) for validation."
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "togetherai",
      "label": {
        "zh_Hans": "together.ai",
        "en_US": "together.ai"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/togetherai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/togetherai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/togetherai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/togetherai/icon_large/en_US"
      },
      "background": "#F1EFED",
      "help": {
        "title": {
          "zh_Hans": "从 together.ai 获取 API Key",
          "en_US": "Get your API key from together.ai"
        },
        "url": {
          "zh_Hans": "https://api.together.xyz/",
          "en_US": "https://api.together.xyz/"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型全称",
            "en_US": "Enter full model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "Completion mode",
              "en_US": "Completion mode"
            },
            "type": "select",
            "required": false,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择对话类型",
              "en_US": "Select completion mode"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens_to_sample",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "openrouter",
      "label": {
        "zh_Hans": "OpenRouter",
        "en_US": "OpenRouter"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/openrouter/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/openrouter/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/openrouter/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/openrouter/icon_large/en_US"
      },
      "background": "#F1EFED",
      "help": {
        "title": {
          "zh_Hans": "从 openrouter.ai 获取 API Key",
          "en_US": "Get your API key from openrouter.ai"
        },
        "url": {
          "zh_Hans": "https://openrouter.ai/keys",
          "en_US": "https://openrouter.ai/keys"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型全称",
            "en_US": "Enter full model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "Completion mode",
              "en_US": "Completion mode"
            },
            "type": "select",
            "required": false,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择对话类型",
              "en_US": "Select completion mode"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens_to_sample",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "vision_support",
            "label": {
              "zh_Hans": "是否支持 Vision",
              "en_US": "Vision Support"
            },
            "type": "radio",
            "required": false,
            "default": "no_support",
            "options": [
              {
                "label": {
                  "zh_Hans": "是",
                  "en_US": "Yes"
                },
                "value": "support",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "否",
                  "en_US": "No"
                },
                "value": "no_support",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "ollama",
      "label": {
        "zh_Hans": "Ollama",
        "en_US": "Ollama"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/ollama/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/ollama/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/ollama/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/ollama/icon_large/en_US"
      },
      "background": "#F9FAFB",
      "help": {
        "title": {
          "zh_Hans": "如何集成 Ollama",
          "en_US": "How to integrate with Ollama"
        },
        "url": {
          "zh_Hans": "https://docs.dify.ai/tutorials/model-configuration/ollama",
          "en_US": "https://docs.dify.ai/tutorials/model-configuration/ollama"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "base_url",
            "label": {
              "zh_Hans": "基础 URL",
              "en_US": "Base URL"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Ollama server 的基础 URL，例如 http://192.168.1.100:11434",
              "en_US": "Base url of Ollama server, e.g. http://192.168.1.100:11434"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "模型类型",
              "en_US": "Completion mode"
            },
            "type": "select",
            "required": true,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择对话类型",
              "en_US": "Select completion mode"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "vision_support",
            "label": {
              "zh_Hans": "是否支持 Vision",
              "en_US": "Vision support"
            },
            "type": "radio",
            "required": false,
            "default": "false",
            "options": [
              {
                "label": {
                  "zh_Hans": "是",
                  "en_US": "Yes"
                },
                "value": "true",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "否",
                  "en_US": "No"
                },
                "value": "false",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "function_call_support",
            "label": {
              "zh_Hans": "是否支持函数调用",
              "en_US": "Function call support"
            },
            "type": "radio",
            "required": false,
            "default": "false",
            "options": [
              {
                "label": {
                  "zh_Hans": "是",
                  "en_US": "Yes"
                },
                "value": "true",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "否",
                  "en_US": "No"
                },
                "value": "false",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "mistralai",
      "label": {
        "zh_Hans": "MistralAI",
        "en_US": "MistralAI"
      },
      "description": {
        "zh_Hans": "MistralAI 提供的模型，例如 open-mistral-7b 和 mistral-large-latest。",
        "en_US": "Models provided by MistralAI, such as open-mistral-7b and mistral-large-latest."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/mistralai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/mistralai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/mistralai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/mistralai/icon_large/en_US"
      },
      "background": "#FFFFFF",
      "help": {
        "title": {
          "zh_Hans": "从 MistralAI 获取 API Key",
          "en_US": "Get your API Key from MistralAI"
        },
        "url": {
          "zh_Hans": "https://console.mistral.ai/api-keys/",
          "en_US": "https://console.mistral.ai/api-keys/"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "groq",
      "label": {
        "zh_Hans": "GroqCloud",
        "en_US": "GroqCloud"
      },
      "description": {
        "zh_Hans": "GroqCloud 提供对 Groq Cloud API 的访问，其中托管了 LLama2 和 Mixtral 等模型。",
        "en_US": "GroqCloud provides access to the Groq Cloud API, which hosts models like LLama2 and Mixtral."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/groq/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/groq/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/groq/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/groq/icon_large/en_US"
      },
      "background": "#F5F5F4",
      "help": {
        "title": {
          "zh_Hans": "从 GroqCloud 获取 API Key",
          "en_US": "Get your API Key from GroqCloud"
        },
        "url": {
          "zh_Hans": "https://console.groq.com/",
          "en_US": "https://console.groq.com/"
        }
      },
      "supported_model_types": [
        "llm",
        "speech2text"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "replicate",
      "label": {
        "zh_Hans": "Replicate",
        "en_US": "Replicate"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/replicate/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/replicate/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/replicate/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/replicate/icon_large/en_US"
      },
      "background": "#E5E7EB",
      "help": {
        "title": {
          "zh_Hans": "从 Replicate 获取 API Key",
          "en_US": "Get your API Key from Replicate"
        },
        "url": {
          "zh_Hans": "https://replicate.com/account/api-tokens",
          "en_US": "https://replicate.com/account/api-tokens"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": null
        },
        "credential_form_schemas": [
          {
            "variable": "replicate_api_token",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Replicate API Key",
              "en_US": "Enter your Replicate API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "model_version",
            "label": {
              "zh_Hans": "Model Version",
              "en_US": "Model Version"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型版本，默认为最新版本",
              "en_US": "Enter your model version, default to the latest version"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "huggingface_hub",
      "label": {
        "zh_Hans": "Hugging Face Model",
        "en_US": "Hugging Face Model"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/huggingface_hub/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/huggingface_hub/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/huggingface_hub/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/huggingface_hub/icon_large/en_US"
      },
      "background": "#FFF8DC",
      "help": {
        "title": {
          "zh_Hans": "从 Hugging Face Hub 获取 API Key",
          "en_US": "Get your API key from Hugging Face Hub"
        },
        "url": {
          "zh_Hans": "https://huggingface.co/settings/tokens",
          "en_US": "https://huggingface.co/settings/tokens"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": null
        },
        "credential_form_schemas": [
          {
            "variable": "huggingfacehub_api_type",
            "label": {
              "zh_Hans": "端点类型",
              "en_US": "Endpoint Type"
            },
            "type": "radio",
            "required": true,
            "default": "hosted_inference_api",
            "options": [
              {
                "label": {
                  "zh_Hans": "Hosted Inference API",
                  "en_US": "Hosted Inference API"
                },
                "value": "hosted_inference_api",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "Inference Endpoints",
                  "en_US": "Inference Endpoints"
                },
                "value": "inference_endpoints",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "huggingfacehub_api_token",
            "label": {
              "zh_Hans": "API Token",
              "en_US": "API Token"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Hugging Face Hub API Token",
              "en_US": "Enter your Hugging Face Hub API Token here"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "huggingface_namespace",
            "label": {
              "zh_Hans": "用户名 / 组织名称",
              "en_US": "User Name / Organization Name"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的用户名 / 组织名称",
              "en_US": "Enter your User Name / Organization Name here"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "text-embedding"
              },
              {
                "variable": "huggingfacehub_api_type",
                "value": "inference_endpoints"
              }
            ]
          },
          {
            "variable": "huggingfacehub_endpoint_url",
            "label": {
              "zh_Hans": "端点 URL",
              "en_US": "Endpoint URL"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的端点 URL",
              "en_US": "Enter your Endpoint URL here"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "huggingfacehub_api_type",
                "value": "inference_endpoints"
              }
            ]
          },
          {
            "variable": "task_type",
            "label": {
              "zh_Hans": "Task",
              "en_US": "Task"
            },
            "type": "select",
            "required": true,
            "default": null,
            "options": [
              {
                "label": {
                  "zh_Hans": "Text-to-Text Generation",
                  "en_US": "Text-to-Text Generation"
                },
                "value": "text2text-generation",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "文本生成",
                  "en_US": "Text Generation"
                },
                "value": "text-generation",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Feature Extraction",
                  "en_US": "Feature Extraction"
                },
                "value": "feature-extraction",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "text-embedding"
                  }
                ]
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "huggingfacehub_api_type",
                "value": "inference_endpoints"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "xinference",
      "label": {
        "zh_Hans": "Xorbits Inference",
        "en_US": "Xorbits Inference"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/xinference/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/xinference/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/xinference/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/xinference/icon_large/en_US"
      },
      "background": "#FAF5FF",
      "help": {
        "title": {
          "zh_Hans": "如何部署 Xinference",
          "en_US": "How to deploy Xinference"
        },
        "url": {
          "zh_Hans": "https://github.com/xorbitsai/inference",
          "en_US": "https://github.com/xorbitsai/inference"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank",
        "speech2text",
        "tts"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "server_url",
            "label": {
              "zh_Hans": "服务器URL",
              "en_US": "Server url"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入Xinference的服务器地址，如 http://192.168.1.100:9997",
              "en_US": "Enter the url of your Xinference, e.g. http://192.168.1.100:9997"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "model_uid",
            "label": {
              "zh_Hans": "模型UID",
              "en_US": "Model uid"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的Model UID",
              "en_US": "Enter the model uid"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API密钥",
              "en_US": "API key"
            },
            "type": "secret-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的API密钥",
              "en_US": "Enter the api key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "invoke_timeout",
            "label": {
              "zh_Hans": "调用超时时间 (单位:秒)",
              "en_US": "invoke timeout (unit:second)"
            },
            "type": "text-input",
            "required": true,
            "default": "60",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入调用超时时间",
              "en_US": "Enter invoke timeout value"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_retries",
            "label": {
              "zh_Hans": "调用重试次数",
              "en_US": "max retries"
            },
            "type": "text-input",
            "required": true,
            "default": "3",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入调用重试次数",
              "en_US": "Enter max retries"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "triton_inference_server",
      "label": {
        "zh_Hans": "Triton Inference Server",
        "en_US": "Triton Inference Server"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/triton_inference_server/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/triton_inference_server/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/triton_inference_server/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/triton_inference_server/icon_large/en_US"
      },
      "background": "#EFFDFD",
      "help": {
        "title": {
          "zh_Hans": "如何部署 Triton Inference Server",
          "en_US": "How to deploy Triton Inference Server"
        },
        "url": {
          "zh_Hans": "https://github.com/triton-inference-server/server",
          "en_US": "https://github.com/triton-inference-server/server"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "server_url",
            "label": {
              "zh_Hans": "服务器URL",
              "en_US": "Server url"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入 Triton Inference Server 的服务器地址，如 http://192.168.1.100:8000",
              "en_US": "Enter the url of your Triton Inference Server, e.g. http://192.168.1.100:8000"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "上下文大小",
              "en_US": "Context size"
            },
            "type": "text-input",
            "required": true,
            "default": "2048",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的上下文大小",
              "en_US": "Enter the context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "completion_type",
            "label": {
              "zh_Hans": "补全类型",
              "en_US": "Model type"
            },
            "type": "select",
            "required": true,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全模型",
                  "en_US": "Completion model"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话模型",
                  "en_US": "Chat model"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "在此输入您的补全类型",
              "en_US": "Enter the completion type"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "stream",
            "label": {
              "zh_Hans": "流式输出",
              "en_US": "Stream output"
            },
            "type": "select",
            "required": true,
            "default": "true",
            "options": [
              {
                "label": {
                  "zh_Hans": "是",
                  "en_US": "Yes"
                },
                "value": "true",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "否",
                  "en_US": "No"
                },
                "value": "false",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "是否支持流式输出",
              "en_US": "Whether to support stream output"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "zhipuai",
      "label": {
        "zh_Hans": "智谱 AI",
        "en_US": "ZHIPU AI"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/zhipuai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/zhipuai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/zhipuai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/zhipuai/icon_large/en_US"
      },
      "background": "#EFF1FE",
      "help": {
        "title": {
          "zh_Hans": "从智谱 AI 获取 API Key",
          "en_US": "Get your API key from ZHIPU AI"
        },
        "url": {
          "zh_Hans": "https://open.bigmodel.cn/usercenter/apikeys",
          "en_US": "https://open.bigmodel.cn/usercenter/apikeys"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "APIKey",
              "en_US": "APIKey"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 APIKey",
              "en_US": "Enter your APIKey"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "baichuan",
      "label": {
        "zh_Hans": "Baichuan",
        "en_US": "Baichuan"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/baichuan/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/baichuan/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/baichuan/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/baichuan/icon_large/en_US"
      },
      "background": "#FFF6F2",
      "help": {
        "title": {
          "zh_Hans": "从百川智能获取您的 API Key",
          "en_US": "Get your API Key from BAICHUAN AI"
        },
        "url": {
          "zh_Hans": "https://www.baichuan-ai.com",
          "en_US": "https://www.baichuan-ai.com"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "spark",
      "label": {
        "zh_Hans": "讯飞星火",
        "en_US": "iFLYTEK SPARK"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/spark/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/spark/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/spark/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/spark/icon_large/en_US"
      },
      "background": "#EBF8FF",
      "help": {
        "title": {
          "zh_Hans": "从讯飞星火获取 API Keys",
          "en_US": "Get your API key from iFLYTEK SPARK"
        },
        "url": {
          "zh_Hans": "https://www.xfyun.cn/solutions/xinghuoAPI",
          "en_US": "https://www.xfyun.cn/solutions/xinghuoAPI"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "app_id",
            "label": {
              "zh_Hans": "APPID",
              "en_US": "APPID"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 APPID",
              "en_US": "Enter your APPID"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "api_secret",
            "label": {
              "zh_Hans": "APISecret",
              "en_US": "APISecret"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 APISecret",
              "en_US": "Enter your APISecret"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "APIKey",
              "en_US": "APIKey"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 APIKey",
              "en_US": "Enter your APIKey"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "minimax",
      "label": {
        "zh_Hans": "Minimax",
        "en_US": "Minimax"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/minimax/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/minimax/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/minimax/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/minimax/icon_large/en_US"
      },
      "background": "#FFEFEF",
      "help": {
        "title": {
          "zh_Hans": "从 Minimax 获取您的 API Key",
          "en_US": "Get your API Key from Minimax"
        },
        "url": {
          "zh_Hans": "https://api.minimax.chat/user-center/basic-information/interface-key",
          "en_US": "https://api.minimax.chat/user-center/basic-information/interface-key"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "minimax_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "minimax_group_id",
            "label": {
              "zh_Hans": "Group ID",
              "en_US": "Group ID"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Group ID",
              "en_US": "Enter your group ID"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "tongyi",
      "label": {
        "zh_Hans": "通义千问",
        "en_US": "TONGYI"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/tongyi/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/tongyi/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/tongyi/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/tongyi/icon_large/en_US"
      },
      "background": "#EFF1FE",
      "help": {
        "title": {
          "zh_Hans": "从阿里云百炼获取 API Key",
          "en_US": "Get your API key from AliCloud"
        },
        "url": {
          "zh_Hans": "https://bailian.console.aliyun.com/?apiKey=1#/api-key",
          "en_US": "https://bailian.console.aliyun.com/?apiKey=1#/api-key"
        }
      },
      "supported_model_types": [
        "llm",
        "tts",
        "text-embedding",
        "rerank"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "dashscope_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "dashscope_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "function_calling_type",
            "label": {
              "zh_Hans": "Function calling",
              "en_US": "Function calling"
            },
            "type": "select",
            "required": false,
            "default": "no_call",
            "options": [
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not Support"
                },
                "value": "no_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "支持",
                  "en_US": "Support"
                },
                "value": "function_call",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "wenxin",
      "label": {
        "zh_Hans": "文心一言",
        "en_US": "WenXin"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/wenxin/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/wenxin/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/wenxin/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/wenxin/icon_large/en_US"
      },
      "background": "#E8F5FE",
      "help": {
        "title": {
          "zh_Hans": "从文心一言获取您的 API Key",
          "en_US": "Get your API Key from WenXin"
        },
        "url": {
          "zh_Hans": "https://cloud.baidu.com/wenxin.html",
          "en_US": "https://cloud.baidu.com/wenxin.html"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "secret_key",
            "label": {
              "zh_Hans": "Secret Key",
              "en_US": "Secret Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Secret Key",
              "en_US": "Enter your Secret Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "moonshot",
      "label": {
        "zh_Hans": "月之暗面",
        "en_US": "Moonshot"
      },
      "description": {
        "zh_Hans": "Moonshot 提供的模型，例如 moonshot-v1-8k、moonshot-v1-32k 和 moonshot-v1-128k。",
        "en_US": "Models provided by Moonshot, such as moonshot-v1-8k, moonshot-v1-32k, and moonshot-v1-128k."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/moonshot/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/moonshot/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/moonshot/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/moonshot/icon_large/en_US"
      },
      "background": "#FFFFFF",
      "help": {
        "title": {
          "zh_Hans": "从 Moonshot 获取 API Key",
          "en_US": "Get your API Key from Moonshot"
        },
        "url": {
          "zh_Hans": "https://platform.moonshot.cn/console/api-keys",
          "en_US": "https://platform.moonshot.cn/console/api-keys"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "endpoint_url",
            "label": {
              "zh_Hans": "API Base",
              "en_US": "API Base"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Base URL, 如：https://api.moonshot.cn/v1",
              "en_US": "Base URL, e.g. https://api.moonshot.cn/v1"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "function_calling_type",
            "label": {
              "zh_Hans": "Function calling",
              "en_US": "Function calling"
            },
            "type": "select",
            "required": false,
            "default": "no_call",
            "options": [
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not supported"
                },
                "value": "no_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "Tool Call",
                  "en_US": "Tool Call"
                },
                "value": "tool_call",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "tencent",
      "label": {
        "zh_Hans": "腾讯云",
        "en_US": "Tencent"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/tencent/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/tencent/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/tencent/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/tencent/icon_large/en_US"
      },
      "background": "#E5E7EB",
      "help": {
        "title": {
          "zh_Hans": "从腾讯云获取 API Key",
          "en_US": "Get your API key from Tencent AI"
        },
        "url": {
          "zh_Hans": "https://cloud.tencent.com/product/asr",
          "en_US": "https://cloud.tencent.com/product/asr"
        }
      },
      "supported_model_types": [
        "speech2text"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "app_id",
            "label": {
              "zh_Hans": "APPID",
              "en_US": "APPID"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的腾讯语音识别服务的 APPID",
              "en_US": "Enter the APPID of your Tencent Cloud ASR service"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "secret_id",
            "label": {
              "zh_Hans": "SecretId",
              "en_US": "SecretId"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的腾讯语音识别服务的 SecretId",
              "en_US": "Enter the SecretId of your Tencent Cloud ASR service"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "secret_key",
            "label": {
              "zh_Hans": "SecretKey",
              "en_US": "SecretKey"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的腾讯语音识别服务的 SecretKey",
              "en_US": "Enter the SecretKey of your Tencent Cloud ASR service"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "jina",
      "label": {
        "zh_Hans": "Jina AI",
        "en_US": "Jina AI"
      },
      "description": {
        "zh_Hans": "Embedding and Rerank Model Supported",
        "en_US": "Embedding and Rerank Model Supported"
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/jina/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/jina/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/jina/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/jina/icon_large/en_US"
      },
      "background": "#EFFDFD",
      "help": {
        "title": {
          "zh_Hans": "从 Jina AI 获取 API Key",
          "en_US": "Get your API key from Jina AI"
        },
        "url": {
          "zh_Hans": "https://jina.ai/",
          "en_US": "https://jina.ai/"
        }
      },
      "supported_model_types": [
        "text-embedding",
        "rerank"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "base_url",
            "label": {
              "zh_Hans": "服务器 URL",
              "en_US": "Base URL"
            },
            "type": "text-input",
            "required": true,
            "default": "https://api.jina.ai/v1",
            "options": null,
            "placeholder": {
              "zh_Hans": "Base URL, e.g. https://api.jina.ai/v1",
              "en_US": "Base URL, e.g. https://api.jina.ai/v1"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "上下文大小",
              "en_US": "Context size"
            },
            "type": "text-input",
            "required": false,
            "default": "8192",
            "options": null,
            "placeholder": {
              "zh_Hans": "输入上下文大小",
              "en_US": "Enter context size"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "chatglm",
      "label": {
        "zh_Hans": "ChatGLM",
        "en_US": "ChatGLM"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/chatglm/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/chatglm/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/chatglm/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/chatglm/icon_large/en_US"
      },
      "background": "#F4F7FF",
      "help": {
        "title": {
          "zh_Hans": "部署您的本地 ChatGLM",
          "en_US": "Deploy ChatGLM to your local"
        },
        "url": {
          "zh_Hans": "https://github.com/THUDM/ChatGLM3",
          "en_US": "https://github.com/THUDM/ChatGLM3"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_base",
            "label": {
              "zh_Hans": "API URL",
              "en_US": "API URL"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API URL",
              "en_US": "Enter your API URL"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "yi",
      "label": {
        "zh_Hans": "零一万物",
        "en_US": "01.AI"
      },
      "description": {
        "zh_Hans": "零一万物提供的模型，例如 yi-34b-chat 和 yi-vl-plus。",
        "en_US": "Models provided by 01.AI, such as yi-34b-chat and yi-vl-plus."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/yi/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/yi/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/yi/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/yi/icon_large/en_US"
      },
      "background": "#E9F1EC",
      "help": {
        "title": {
          "zh_Hans": "从零一万物获取 API Key",
          "en_US": "Get your API Key from 01.ai"
        },
        "url": {
          "zh_Hans": "https://platform.lingyiwanwu.com/apikeys",
          "en_US": "https://platform.lingyiwanwu.com/apikeys"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "endpoint_url",
            "label": {
              "zh_Hans": "自定义 API endpoint 地址",
              "en_US": "Custom API endpoint URL"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Base URL, e.g. https://api.lingyiwanwu.com/v1",
              "en_US": "Base URL, e.g. https://api.lingyiwanwu.com/v1"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "function_calling_type",
            "label": {
              "zh_Hans": "Function calling",
              "en_US": "Function calling"
            },
            "type": "select",
            "required": false,
            "default": "no_call",
            "options": [
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not Support"
                },
                "value": "no_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "支持",
                  "en_US": "Support"
                },
                "value": "function_call",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "openllm",
      "label": {
        "zh_Hans": "OpenLLM",
        "en_US": "OpenLLM"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/openllm/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/openllm/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/openllm/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/openllm/icon_large/en_US"
      },
      "background": "#F9FAFB",
      "help": {
        "title": {
          "zh_Hans": "如何部署 OpenLLM",
          "en_US": "How to deploy OpenLLM"
        },
        "url": {
          "zh_Hans": "https://github.com/bentoml/OpenLLM",
          "en_US": "https://github.com/bentoml/OpenLLM"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "server_url",
            "label": {
              "zh_Hans": "服务器URL",
              "en_US": "Server url"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入OpenLLM的服务器地址，如 http://192.168.1.100:3000",
              "en_US": "Enter the url of your OpenLLM, e.g. http://192.168.1.100:3000"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "localai",
      "label": {
        "zh_Hans": "LocalAI",
        "en_US": "LocalAI"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/localai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/localai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/localai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/localai/icon_large/en_US"
      },
      "background": "#F3F4F6",
      "help": {
        "title": {
          "zh_Hans": "如何部署 LocalAI",
          "en_US": "How to deploy LocalAI"
        },
        "url": {
          "zh_Hans": "https://github.com/go-skynet/LocalAI",
          "en_US": "https://github.com/go-skynet/LocalAI"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank",
        "speech2text"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "completion_type",
            "label": {
              "zh_Hans": "Completion type",
              "en_US": "Completion type"
            },
            "type": "select",
            "required": false,
            "default": "chat_completion",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话",
                  "en_US": "ChatCompletion"
                },
                "value": "chat_completion",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择对话类型",
              "en_US": "Select completion type"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "server_url",
            "label": {
              "zh_Hans": "服务器URL",
              "en_US": "Server url"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入LocalAI的服务器地址，如 http://192.168.1.100:8080",
              "en_US": "Enter the url of your LocalAI, e.g. http://192.168.1.100:8080"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "上下文大小",
              "en_US": "Context size"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "输入上下文大小",
              "en_US": "Enter context size"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "volcengine_maas",
      "label": {
        "zh_Hans": "Volcengine",
        "en_US": "Volcengine"
      },
      "description": {
        "zh_Hans": "火山方舟提供的模型，例如 Doubao-pro-4k、Doubao-pro-32k 和 Doubao-pro-128k。",
        "en_US": "Volcengine Ark models."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/volcengine_maas/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/volcengine_maas/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/volcengine_maas/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/volcengine_maas/icon_large/en_US"
      },
      "background": "#F9FAFB",
      "help": {
        "title": {
          "zh_Hans": "从火山引擎控制台获取您的 Access Key 和 Secret Access Key",
          "en_US": "Get your Access Key and Secret Access Key from Volcengine Console"
        },
        "url": {
          "zh_Hans": "https://console.volcengine.com/iam/keymanage/",
          "en_US": "https://console.volcengine.com/iam/keymanage/"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your Model Name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "auth_method",
            "label": {
              "zh_Hans": "鉴权方式",
              "en_US": "Authentication Method"
            },
            "type": "select",
            "required": true,
            "default": "aksk",
            "options": [
              {
                "label": {
                  "zh_Hans": "API Key",
                  "en_US": "API Key"
                },
                "value": "api_key",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "Access Key / Secret Access Key",
                  "en_US": "Access Key / Secret Access Key"
                },
                "value": "aksk",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择鉴权方式",
              "en_US": "Enter your Authentication Method"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "volc_access_key_id",
            "label": {
              "zh_Hans": "Access Key",
              "en_US": "Access Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "输入您的 Access Key",
              "en_US": "Enter your Access Key"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "auth_method",
                "value": "aksk"
              }
            ]
          },
          {
            "variable": "volc_secret_access_key",
            "label": {
              "zh_Hans": "Secret Access Key",
              "en_US": "Secret Access Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "输入您的 Secret Access Key",
              "en_US": "Enter your Secret Access Key"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "auth_method",
                "value": "aksk"
              }
            ]
          },
          {
            "variable": "volc_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "auth_method",
                "value": "api_key"
              }
            ]
          },
          {
            "variable": "volc_region",
            "label": {
              "zh_Hans": "火山引擎地域",
              "en_US": "Volcengine Region"
            },
            "type": "text-input",
            "required": true,
            "default": "cn-beijing",
            "options": null,
            "placeholder": {
              "zh_Hans": "输入火山引擎地域",
              "en_US": "Enter Volcengine Region"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "api_endpoint_host",
            "label": {
              "zh_Hans": "API Endpoint Host",
              "en_US": "API Endpoint Host"
            },
            "type": "text-input",
            "required": true,
            "default": "https://ark.cn-beijing.volces.com/api/v3",
            "options": null,
            "placeholder": {
              "zh_Hans": "输入 API Endpoint Host",
              "en_US": "Enter your API Endpoint Host"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "endpoint_id",
            "label": {
              "zh_Hans": "Endpoint ID",
              "en_US": "Endpoint ID"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "输入您的 Endpoint ID",
              "en_US": "Enter your Endpoint ID"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "base_model_name",
            "label": {
              "zh_Hans": "基础模型",
              "en_US": "Base Model"
            },
            "type": "select",
            "required": true,
            "default": null,
            "options": [
              {
                "label": {
                  "zh_Hans": "Doubao-vision-pro-32k",
                  "en_US": "Doubao-vision-pro-32k"
                },
                "value": "Doubao-vision-pro-32k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-vision-lite-32k",
                  "en_US": "Doubao-vision-lite-32k"
                },
                "value": "Doubao-vision-lite-32k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-pro-4k",
                  "en_US": "Doubao-pro-4k"
                },
                "value": "Doubao-pro-4k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-lite-4k",
                  "en_US": "Doubao-lite-4k"
                },
                "value": "Doubao-lite-4k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-pro-32k",
                  "en_US": "Doubao-pro-32k"
                },
                "value": "Doubao-pro-32k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-lite-32k",
                  "en_US": "Doubao-lite-32k"
                },
                "value": "Doubao-lite-32k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-pro-128k",
                  "en_US": "Doubao-pro-128k"
                },
                "value": "Doubao-pro-128k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-lite-128k",
                  "en_US": "Doubao-lite-128k"
                },
                "value": "Doubao-lite-128k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-pro-256k",
                  "en_US": "Doubao-pro-256k"
                },
                "value": "Doubao-pro-256k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Llama3-8B",
                  "en_US": "Llama3-8B"
                },
                "value": "Llama3-8B",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Llama3-70B",
                  "en_US": "Llama3-70B"
                },
                "value": "Llama3-70B",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Moonshot-v1-8k",
                  "en_US": "Moonshot-v1-8k"
                },
                "value": "Moonshot-v1-8k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Moonshot-v1-32k",
                  "en_US": "Moonshot-v1-32k"
                },
                "value": "Moonshot-v1-32k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Moonshot-v1-128k",
                  "en_US": "Moonshot-v1-128k"
                },
                "value": "Moonshot-v1-128k",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "GLM3-130B",
                  "en_US": "GLM3-130B"
                },
                "value": "GLM3-130B",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "GLM3-130B-Fin",
                  "en_US": "GLM3-130B-Fin"
                },
                "value": "GLM3-130B-Fin",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Mistral-7B",
                  "en_US": "Mistral-7B"
                },
                "value": "Mistral-7B",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "llm"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-embedding",
                  "en_US": "Doubao-embedding"
                },
                "value": "Doubao-embedding",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "text-embedding"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "Doubao-embedding-large",
                  "en_US": "Doubao-embedding-large"
                },
                "value": "Doubao-embedding-large",
                "show_on": [
                  {
                    "variable": "__model_type",
                    "value": "text-embedding"
                  }
                ]
              },
              {
                "label": {
                  "zh_Hans": "自定义",
                  "en_US": "Custom"
                },
                "value": "Custom",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "模型类型",
              "en_US": "Completion Mode"
            },
            "type": "select",
            "required": true,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择对话类型",
              "en_US": "Select Completion Mode"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              },
              {
                "variable": "base_model_name",
                "value": "Custom"
              }
            ]
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model Context Size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "输入您的模型上下文长度",
              "en_US": "Enter your Model Context Size"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "base_model_name",
                "value": "Custom"
              }
            ]
          },
          {
            "variable": "max_tokens",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper Bound for Max Tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "输入您的模型最大 token 上限",
              "en_US": "Enter your model Upper Bound for Max Tokens"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              },
              {
                "variable": "base_model_name",
                "value": "Custom"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "openai_api_compatible",
      "label": {
        "zh_Hans": "OpenAI-API-compatible",
        "en_US": "OpenAI-API-compatible"
      },
      "description": {
        "zh_Hans": "兼容 OpenAI API 的模型供应商，例如 LM Studio 。",
        "en_US": "Model providers compatible with OpenAI's API standard, such as LM Studio."
      },
      "icon_small": null,
      "icon_large": null,
      "background": null,
      "help": null,
      "supported_model_types": [
        "llm",
        "text-embedding",
        "speech2text",
        "rerank",
        "tts"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型全称",
            "en_US": "Enter full model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "endpoint_url",
            "label": {
              "zh_Hans": "API endpoint URL",
              "en_US": "API endpoint URL"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Base URL, e.g. https://api.openai.com/v1",
              "en_US": "Base URL, e.g. https://api.openai.com/v1"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "Completion mode",
              "en_US": "Completion mode"
            },
            "type": "select",
            "required": false,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择对话类型",
              "en_US": "Select completion mode"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "text-embedding"
              }
            ]
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "rerank"
              }
            ]
          },
          {
            "variable": "max_tokens_to_sample",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "function_calling_type",
            "label": {
              "zh_Hans": "Function calling",
              "en_US": "Function calling"
            },
            "type": "select",
            "required": false,
            "default": "no_call",
            "options": [
              {
                "label": {
                  "zh_Hans": "Function Call",
                  "en_US": "Function Call"
                },
                "value": "function_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "Tool Call",
                  "en_US": "Tool Call"
                },
                "value": "tool_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not Support"
                },
                "value": "no_call",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "stream_function_calling",
            "label": {
              "zh_Hans": "Stream function calling",
              "en_US": "Stream function calling"
            },
            "type": "select",
            "required": false,
            "default": "not_supported",
            "options": [
              {
                "label": {
                  "zh_Hans": "支持",
                  "en_US": "Support"
                },
                "value": "supported",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not Support"
                },
                "value": "not_supported",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "vision_support",
            "label": {
              "zh_Hans": "Vision 支持",
              "en_US": "Vision Support"
            },
            "type": "select",
            "required": false,
            "default": "no_support",
            "options": [
              {
                "label": {
                  "zh_Hans": "支持",
                  "en_US": "Support"
                },
                "value": "support",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not Support"
                },
                "value": "no_support",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "stream_mode_delimiter",
            "label": {
              "zh_Hans": "流模式返回结果的分隔符",
              "en_US": "Delimiter for streaming results"
            },
            "type": "text-input",
            "required": true,
            "default": "\\n\\n",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "voices",
            "label": {
              "zh_Hans": "可用声音（用英文逗号分隔）",
              "en_US": "Available Voices (comma-separated)"
            },
            "type": "text-input",
            "required": false,
            "default": "alloy",
            "options": null,
            "placeholder": {
              "zh_Hans": "alloy,echo,fable,onyx,nova,shimmer",
              "en_US": "alloy,echo,fable,onyx,nova,shimmer"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "tts"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "deepseek",
      "label": {
        "zh_Hans": "深度求索",
        "en_US": "deepseek"
      },
      "description": {
        "zh_Hans": "深度求索提供的模型，例如 deepseek-chat、deepseek-coder 。",
        "en_US": "Models provided by deepseek, such as deepseek-chat、deepseek-coder."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/deepseek/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/deepseek/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/deepseek/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/deepseek/icon_large/en_US"
      },
      "background": "#c0cdff",
      "help": {
        "title": {
          "zh_Hans": "从深度求索获取 API Key",
          "en_US": "Get your API Key from deepseek"
        },
        "url": {
          "zh_Hans": "https://platform.deepseek.com/api_keys",
          "en_US": "https://platform.deepseek.com/api_keys"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "endpoint_url",
            "label": {
              "zh_Hans": "自定义 API endpoint 地址",
              "en_US": "Custom API endpoint URL"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Base URL, e.g. https://api.deepseek.com/v1 or https://api.deepseek.com",
              "en_US": "Base URL, e.g. https://api.deepseek.com/v1 or https://api.deepseek.com"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "hunyuan",
      "label": {
        "zh_Hans": "腾讯混元",
        "en_US": "Hunyuan"
      },
      "description": {
        "zh_Hans": "腾讯混元提供的模型，例如 hunyuan-standard、 hunyuan-standard-256k, hunyuan-pro, hunyuan-role, hunyuan-large, hunyuan-large-role, hunyuan-turbo-latest, hunyuan-large-longcontext, hunyuan-turbo, hunyuan-vision, hunyuan-turbo-vision, hunyuan-functioncall 和 hunyuan-lite。",
        "en_US": "Models provided by Tencent Hunyuan, such as hunyuan-standard, hunyuan-standard-256k, hunyuan-pro, hunyuan-role, hunyuan-large, hunyuan-large-role, hunyuan-turbo-latest, hunyuan-large-longcontext, hunyuan-turbo, hunyuan-vision, hunyuan-turbo-vision, hunyuan-functioncall and hunyuan-lite."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/hunyuan/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/hunyuan/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/hunyuan/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/hunyuan/icon_large/en_US"
      },
      "background": "#F6F7F7",
      "help": {
        "title": {
          "zh_Hans": "从腾讯混元获取 API Key",
          "en_US": "Get your API Key from Tencent Hunyuan"
        },
        "url": {
          "zh_Hans": "https://console.cloud.tencent.com/cam/capi",
          "en_US": "https://console.cloud.tencent.com/cam/capi"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "secret_id",
            "label": {
              "zh_Hans": "Secret ID",
              "en_US": "Secret ID"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Secret ID",
              "en_US": "Enter your Secret ID"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "secret_key",
            "label": {
              "zh_Hans": "Secret Key",
              "en_US": "Secret Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Secret Key",
              "en_US": "Enter your Secret Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "siliconflow",
      "label": {
        "zh_Hans": "硅基流动",
        "en_US": "SiliconFlow"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/siliconflow/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/siliconflow/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/siliconflow/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/siliconflow/icon_large/en_US"
      },
      "background": "#ffecff",
      "help": {
        "title": {
          "zh_Hans": "从 SiliconFlow 获取 API Key",
          "en_US": "Get your API Key from SiliconFlow"
        },
        "url": {
          "zh_Hans": "https://cloud.siliconflow.cn/account/ak",
          "en_US": "https://cloud.siliconflow.cn/account/ak"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank",
        "speech2text",
        "tts"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "function_calling_type",
            "label": {
              "zh_Hans": "Function calling",
              "en_US": "Function calling"
            },
            "type": "select",
            "required": false,
            "default": "no_call",
            "options": [
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not Support"
                },
                "value": "no_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "支持",
                  "en_US": "Support"
                },
                "value": "function_call",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "perfxcloud",
      "label": {
        "zh_Hans": "PerfXCloud",
        "en_US": "PerfXCloud"
      },
      "description": {
        "zh_Hans": "PerfXCloud（澎峰科技）为开发者和企业量身打造的AI开发和部署平台，提供多种模型的的推理能力。",
        "en_US": "PerfXCloud (Pengfeng Technology) is an AI development and deployment platform tailored for developers and enterprises, providing reasoning capabilities for multiple models."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/perfxcloud/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/perfxcloud/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/perfxcloud/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/perfxcloud/icon_large/en_US"
      },
      "background": "#e3f0ff",
      "help": {
        "title": {
          "zh_Hans": "从 PerfXCloud 获取 API Key",
          "en_US": "Get your API Key from PerfXCloud"
        },
        "url": {
          "zh_Hans": "https://cloud.perfxlab.cn/panel/token",
          "en_US": "https://cloud.perfxlab.cn/panel/token"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "endpoint_url",
            "label": {
              "zh_Hans": "自定义 API endpoint 地址",
              "en_US": "Custom API endpoint URL"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Base URL, e.g. https://cloud.perfxlab.cn/v1",
              "en_US": "Base URL, e.g. https://cloud.perfxlab.cn/v1"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "zhinao",
      "label": {
        "zh_Hans": "360 智脑",
        "en_US": "360 AI"
      },
      "description": {
        "zh_Hans": "360 智脑提供的模型。",
        "en_US": "Models provided by 360 AI."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/zhinao/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/zhinao/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/zhinao/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/zhinao/icon_large/en_US"
      },
      "background": "#e3f0ff",
      "help": {
        "title": {
          "zh_Hans": "从360 智脑获取 API Key",
          "en_US": "Get your API Key from 360 AI."
        },
        "url": {
          "zh_Hans": "https://ai.360.com/platform/keys",
          "en_US": "https://ai.360.com/platform/keys"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "fireworks",
      "label": {
        "zh_Hans": "Fireworks AI",
        "en_US": "Fireworks AI"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/fireworks/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/fireworks/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/fireworks/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/fireworks/icon_large/en_US"
      },
      "background": "#FCFDFF",
      "help": {
        "title": {
          "zh_Hans": "从 Fireworks AI 获取 API Key",
          "en_US": "Get your API Key from Fireworks AI"
        },
        "url": {
          "zh_Hans": "https://fireworks.ai/account/api-keys",
          "en_US": "https://fireworks.ai/account/api-keys"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "fireworks_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型URL",
            "en_US": "Model URL"
          },
          "placeholder": {
            "zh_Hans": "输入模型URL",
            "en_US": "Enter your Model URL"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "model_label_zh_Hanns",
            "label": {
              "zh_Hans": "模型中文名称",
              "en_US": "The zh_Hans of Model"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型中文名称",
              "en_US": "Enter your zh_Hans of Model"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "model_label_en_US",
            "label": {
              "zh_Hans": "模型英文名称",
              "en_US": "The en_US of Model"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型英文名称",
              "en_US": "Enter your en_US of Model"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "fireworks_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "4096",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "function_calling_type",
            "label": {
              "zh_Hans": "Function calling",
              "en_US": "Function calling"
            },
            "type": "select",
            "required": false,
            "default": "no_call",
            "options": [
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not Support"
                },
                "value": "no_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "支持",
                  "en_US": "Support"
                },
                "value": "function_call",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "mixedbread",
      "label": {
        "zh_Hans": "MixedBread",
        "en_US": "MixedBread"
      },
      "description": {
        "zh_Hans": "Embedding and Rerank Model Supported",
        "en_US": "Embedding and Rerank Model Supported"
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/mixedbread/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/mixedbread/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/mixedbread/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/mixedbread/icon_large/en_US"
      },
      "background": "#EFFDFD",
      "help": {
        "title": {
          "zh_Hans": "从 MixedBread 获取 API Key",
          "en_US": "Get your API key from MixedBread AI"
        },
        "url": {
          "zh_Hans": "https://www.mixedbread.ai/",
          "en_US": "https://www.mixedbread.ai/"
        }
      },
      "supported_model_types": [
        "text-embedding",
        "rerank"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "nomic",
      "label": {
        "zh_Hans": "Nomic Atlas",
        "en_US": "Nomic Atlas"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/nomic/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/nomic/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/nomic/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/nomic/icon_large/en_US"
      },
      "background": "#EFF1FE",
      "help": {
        "title": {
          "zh_Hans": "从Nomic Atlas获取 API Key",
          "en_US": "Get your API key from Nomic Atlas"
        },
        "url": {
          "zh_Hans": "https://atlas.nomic.ai/data",
          "en_US": "https://atlas.nomic.ai/data"
        }
      },
      "supported_model_types": [
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "nomic_api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "voyage",
      "label": {
        "zh_Hans": "Voyage",
        "en_US": "Voyage"
      },
      "description": {
        "zh_Hans": "Embedding and Rerank Model Supported",
        "en_US": "Embedding and Rerank Model Supported"
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/voyage/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/voyage/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/voyage/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/voyage/icon_large/en_US"
      },
      "background": "#EFFDFD",
      "help": {
        "title": {
          "zh_Hans": "从 Voyage 获取 API Key",
          "en_US": "Get your API key from Voyage AI"
        },
        "url": {
          "zh_Hans": "https://dash.voyageai.com/",
          "en_US": "https://dash.voyageai.com/"
        }
      },
      "supported_model_types": [
        "text-embedding",
        "rerank"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "gitee_ai",
      "label": {
        "zh_Hans": "Gitee AI",
        "en_US": "Gitee AI"
      },
      "description": {
        "zh_Hans": "快速体验大模型，领先探索 AI 开源世界",
        "en_US": "快速体验大模型，领先探索 AI 开源世界"
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/gitee_ai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/gitee_ai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/gitee_ai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/gitee_ai/icon_large/en_US"
      },
      "background": null,
      "help": {
        "title": {
          "zh_Hans": "从 Gitee AI 获取 token",
          "en_US": "Get your token from Gitee AI"
        },
        "url": {
          "zh_Hans": "https://ai.gitee.com/dashboard/settings/tokens",
          "en_US": "https://ai.gitee.com/dashboard/settings/tokens"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank",
        "speech2text",
        "tts"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "novita",
      "label": {
        "zh_Hans": "novita.ai",
        "en_US": "novita.ai"
      },
      "description": {
        "zh_Hans": "适配多种海外应用场景的高性价比 LLM API",
        "en_US": "An LLM API that matches various application scenarios with high cost-effectiveness."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/novita/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/novita/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/novita/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/novita/icon_large/en_US"
      },
      "background": "#eadeff",
      "help": {
        "title": {
          "zh_Hans": "从 novita.ai 获取 API Key",
          "en_US": "Get your API key from novita.ai"
        },
        "url": {
          "zh_Hans": "https://novita.ai/settings#key-management?utm_source=dify&utm_medium=ch&utm_campaign=api",
          "en_US": "https://novita.ai/settings#key-management?utm_source=dify&utm_medium=ch&utm_campaign=api"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "huggingface_tei",
      "label": {
        "zh_Hans": "Text Embedding Inference",
        "en_US": "Text Embedding Inference"
      },
      "description": {
        "zh_Hans": "用于文本嵌入模型的超快速推理解决方案。",
        "en_US": "A blazing fast inference solution for text embeddings models."
      },
      "icon_small": null,
      "icon_large": null,
      "background": "#FFF8DC",
      "help": {
        "title": {
          "zh_Hans": "如何部署 Text Embedding Inference",
          "en_US": "How to deploy Text Embedding Inference"
        },
        "url": {
          "zh_Hans": "https://github.com/huggingface/text-embeddings-inference",
          "en_US": "https://github.com/huggingface/text-embeddings-inference"
        }
      },
      "supported_model_types": [
        "text-embedding",
        "rerank"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "server_url",
            "label": {
              "zh_Hans": "服务器URL",
              "en_US": "Server url"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入Text Embedding Inference的服务器地址，如 http://192.168.1.100:8080",
              "en_US": "Enter the url of your Text Embedding Inference, e.g. http://192.168.1.100:8080"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "gpustack",
      "label": {
        "zh_Hans": "GPUStack",
        "en_US": "GPUStack"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/gpustack/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/gpustack/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/gpustack/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/gpustack/icon_large/en_US"
      },
      "background": null,
      "help": null,
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank",
        "speech2text",
        "tts"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "endpoint_url",
            "label": {
              "zh_Hans": "服务器地址",
              "en_US": "Server URL"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "输入 GPUStack 的服务器地址，如 http://192.168.1.100",
              "en_US": "Enter the GPUStack server URL, e.g. http://192.168.1.100"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "Completion mode",
              "en_US": "Completion mode"
            },
            "type": "select",
            "required": false,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "补全",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "对话",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择补全类型",
              "en_US": "Select completion type"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "8192",
            "options": null,
            "placeholder": {
              "zh_Hans": "输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens_to_sample",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "8192",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "function_calling_type",
            "label": {
              "zh_Hans": "Function calling",
              "en_US": "Function calling"
            },
            "type": "select",
            "required": false,
            "default": "no_call",
            "options": [
              {
                "label": {
                  "zh_Hans": "Function Call",
                  "en_US": "Function Call"
                },
                "value": "function_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "Tool Call",
                  "en_US": "Tool Call"
                },
                "value": "tool_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not Support"
                },
                "value": "no_call",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "vision_support",
            "label": {
              "zh_Hans": "Vision 支持",
              "en_US": "Vision Support"
            },
            "type": "select",
            "required": false,
            "default": "no_support",
            "options": [
              {
                "label": {
                  "zh_Hans": "支持",
                  "en_US": "Support"
                },
                "value": "support",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not Support"
                },
                "value": "no_support",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "voices",
            "label": {
              "zh_Hans": "可用声音（用英文逗号分隔）",
              "en_US": "Available Voices (comma-separated)"
            },
            "type": "text-input",
            "required": false,
            "default": "Chinese Female",
            "options": null,
            "placeholder": {
              "zh_Hans": "Chinese Female, Chinese Male, Japanese Male, Cantonese Female, English Female, English Male, Korean Female",
              "en_US": "Chinese Female, Chinese Male, Japanese Male, Cantonese Female, English Female, English Male, Korean Female"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "tts"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "azure_ai_studio",
      "label": {
        "zh_Hans": "Azure AI Studio",
        "en_US": "Azure AI Studio"
      },
      "description": {
        "zh_Hans": "Azure AI Studio",
        "en_US": "Azure AI Studio"
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/azure_ai_studio/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/azure_ai_studio/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/azure_ai_studio/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/azure_ai_studio/icon_large/en_US"
      },
      "background": "#93c5fd",
      "help": {
        "title": {
          "zh_Hans": "如何在Azure AI Studio上的私有化部署的模型",
          "en_US": "How to deploy customized model on Azure AI Studio"
        },
        "url": {
          "zh_Hans": "https://learn.microsoft.com/zh-cn/azure/ai-studio/how-to/deploy-models",
          "en_US": "https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models"
        }
      },
      "supported_model_types": [
        "llm",
        "rerank"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "endpoint",
            "label": {
              "zh_Hans": "Azure AI Studio Endpoint",
              "en_US": "Azure AI Studio Endpoint"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "请输入你的Azure AI Studio推理端点",
              "en_US": "Enter your API Endpoint, eg: https://example.com"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Azure AI Studio API Key",
              "en_US": "Enter your Azure AI Studio API Key"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "jwt_token",
            "label": {
              "zh_Hans": "JWT令牌",
              "en_US": "JWT Token"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Azure AI Studio 推理 API Key",
              "en_US": "Enter your Azure AI Studio JWT Token"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "rerank"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "oci",
      "label": {
        "zh_Hans": "OCIGenerativeAI",
        "en_US": "OCIGenerativeAI"
      },
      "description": {
        "zh_Hans": "OCI 提供的模型，例如 Cohere Command R 和 Cohere Command R+。",
        "en_US": "Models provided by OCI, such as Cohere Command R and Cohere Command R+."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/oci/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/oci/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/oci/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/oci/icon_large/en_US"
      },
      "background": "#FFFFFF",
      "help": {
        "title": {
          "zh_Hans": "从 OCI 获取 API Key",
          "en_US": "Get your API Key from OCI"
        },
        "url": {
          "zh_Hans": "https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm",
          "en_US": "https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "oci_config_content",
            "label": {
              "zh_Hans": "oci api key config file's content",
              "en_US": "oci api key config file's content"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 oci api key config 文件的内容(base64.b64encode(\"user_ocid/fingerprint/tenancy_ocid/region/compartment_ocid\".encode('utf-8')) )",
              "en_US": "Enter your oci api key config file's content(base64.b64encode(\"user_ocid/fingerprint/tenancy_ocid/region/compartment_ocid\".encode('utf-8')) )"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "oci_key_content",
            "label": {
              "zh_Hans": "oci api key file's content",
              "en_US": "oci api key file's content"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 oci api key 文件的内容(base64.b64encode(\"pem file content\".encode('utf-8')))",
              "en_US": "Enter your oci api key file's content(base64.b64encode(\"pem file content\".encode('utf-8')))"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "fishaudio",
      "label": {
        "zh_Hans": "Fish Audio",
        "en_US": "Fish Audio"
      },
      "description": {
        "zh_Hans": "Fish Audio 提供的模型，目前仅支持 TTS。",
        "en_US": "Models provided by Fish Audio, currently only support TTS."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/fishaudio/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/fishaudio/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/fishaudio/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/fishaudio/icon_large/en_US"
      },
      "background": "#E5E7EB",
      "help": {
        "title": {
          "zh_Hans": "从 Fish Audio 获取你的 API Key",
          "en_US": "Get your API key from Fish Audio"
        },
        "url": {
          "zh_Hans": "https://fish.audio/go-api/",
          "en_US": "https://fish.audio/go-api/"
        }
      },
      "supported_model_types": [
        "tts"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "api_base",
            "label": {
              "zh_Hans": "API URL",
              "en_US": "API URL"
            },
            "type": "text-input",
            "required": false,
            "default": "https://api.fish.audio",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API URL",
              "en_US": "Enter your API URL"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "use_public_models",
            "label": {
              "zh_Hans": "Use Public Models",
              "en_US": "Use Public Models"
            },
            "type": "select",
            "required": false,
            "default": "false",
            "options": [
              {
                "label": {
                  "zh_Hans": "使用公共模型",
                  "en_US": "Allow Public Models"
                },
                "value": "true",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "仅使用私有模型",
                  "en_US": "Private Models Only"
                },
                "value": "false",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "切换以使用公共模型",
              "en_US": "Toggle to use public models"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "latency",
            "label": {
              "zh_Hans": "Latency",
              "en_US": "Latency"
            },
            "type": "select",
            "required": false,
            "default": "normal",
            "options": [
              {
                "label": {
                  "zh_Hans": "低延迟 (可能降低质量)",
                  "en_US": "Low (may affect quality)"
                },
                "value": "balanced",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "标准",
                  "en_US": "Normal"
                },
                "value": "normal",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "切换以调整延迟",
              "en_US": "Toggle to choice latency"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "x",
      "label": {
        "zh_Hans": "xAI",
        "en_US": "xAI"
      },
      "description": {
        "zh_Hans": "xAI is a company working on building artificial intelligence to accelerate human scientific discovery. We are guided by our mission to advance our collective understanding of the universe.",
        "en_US": "xAI is a company working on building artificial intelligence to accelerate human scientific discovery. We are guided by our mission to advance our collective understanding of the universe."
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/x/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/x/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/x/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/x/icon_large/en_US"
      },
      "background": null,
      "help": {
        "title": {
          "zh_Hans": "从 xAI 获取 token",
          "en_US": "Get your token from xAI"
        },
        "url": {
          "zh_Hans": "https://x.ai/api",
          "en_US": "https://x.ai/api"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "endpoint_url",
            "label": {
              "zh_Hans": "API Base",
              "en_US": "API Base"
            },
            "type": "text-input",
            "required": false,
            "default": "https://api.x.ai/v1",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Base",
              "en_US": "Enter your API Base"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "leptonai",
      "label": {
        "zh_Hans": "Lepton AI",
        "en_US": "Lepton AI"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/leptonai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/leptonai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/leptonai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/leptonai/icon_large/en_US"
      },
      "background": "#F5F5F4",
      "help": {
        "title": {
          "zh_Hans": "从 Lepton AI 获取 API Key",
          "en_US": "Get your API Key from Lepton AI"
        },
        "url": {
          "zh_Hans": "https://dashboard.lepton.ai",
          "en_US": "https://dashboard.lepton.ai"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": null,
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "sagemaker",
      "label": {
        "zh_Hans": "Sagemaker",
        "en_US": "Sagemaker"
      },
      "description": {
        "zh_Hans": "Sagemaker上的私有化部署的模型",
        "en_US": "Customized model on Sagemaker"
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/sagemaker/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/sagemaker/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/sagemaker/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/sagemaker/icon_large/en_US"
      },
      "background": "#ECE9E3",
      "help": {
        "title": {
          "zh_Hans": "如何在Sagemaker上的私有化部署的模型",
          "en_US": "How to deploy customized model on Sagemaker"
        },
        "url": {
          "zh_Hans": "https://github.com/aws-samples/dify-aws-tool/blob/main/README_ZH.md#%E5%A6%82%E4%BD%95%E9%83%A8%E7%BD%B2sagemaker%E6%8E%A8%E7%90%86%E7%AB%AF%E7%82%B9",
          "en_US": "https://github.com/aws-samples/dify-aws-tool/blob/main/README.md#how-to-deploy-sagemaker-endpoint"
        }
      },
      "supported_model_types": [
        "llm",
        "text-embedding",
        "rerank",
        "speech2text",
        "tts"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "Completion mode",
              "en_US": "Completion mode"
            },
            "type": "select",
            "required": false,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "Chat",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "选择对话类型",
              "en_US": "Select completion mode"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          },
          {
            "variable": "sagemaker_endpoint",
            "label": {
              "zh_Hans": "sagemaker endpoint",
              "en_US": "sagemaker endpoint"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "请输出你的Sagemaker推理端点",
              "en_US": "Enter your Sagemaker Inference endpoint"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "audio_s3_cache_bucket",
            "label": {
              "zh_Hans": "音频缓存桶(s3 bucket)",
              "en_US": "audio cache bucket(s3 bucket)"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "sagemaker-us-east-1-******207838",
              "en_US": "sagemaker-us-east-1-*******7838"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "speech2text"
              }
            ]
          },
          {
            "variable": "audio_model_type",
            "label": {
              "zh_Hans": "Audio model type",
              "en_US": "Audio model type"
            },
            "type": "select",
            "required": true,
            "default": null,
            "options": [
              {
                "label": {
                  "zh_Hans": "内置音色",
                  "en_US": "preset voice"
                },
                "value": "PresetVoice",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "克隆音色",
                  "en_US": "clone voice"
                },
                "value": "CloneVoice",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "跨语种克隆音色",
                  "en_US": "crosslingual clone voice"
                },
                "value": "CloneVoice_CrossLingual",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "文字指令音色",
                  "en_US": "Instruct voice"
                },
                "value": "InstructVoice",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "语音模型类型",
              "en_US": "Audio model type"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "tts"
              }
            ]
          },
          {
            "variable": "prompt_audio",
            "label": {
              "zh_Hans": "Mock Audio Source",
              "en_US": "Mock Audio Source"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "被模仿的音色音频",
              "en_US": "source audio to be mocked"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "tts"
              }
            ]
          },
          {
            "variable": "prompt_text",
            "label": {
              "zh_Hans": "Prompt Audio Text",
              "en_US": "Prompt Audio Text"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "模仿音色的对应文本",
              "en_US": "text for the mocked source audio"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "tts"
              }
            ]
          },
          {
            "variable": "instruct_text",
            "label": {
              "zh_Hans": "instruct text for speaker",
              "en_US": "instruct text for speaker"
            },
            "type": "text-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "tts"
              }
            ]
          },
          {
            "variable": "aws_access_key_id",
            "label": {
              "zh_Hans": "Access Key (如果未提供，凭证将从运行环境中获取。)",
              "en_US": "Access Key (If not provided, credentials are obtained from the running environment.)"
            },
            "type": "secret-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Access Key",
              "en_US": "Enter your Access Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "aws_secret_access_key",
            "label": {
              "zh_Hans": "Secret Access Key",
              "en_US": "Secret Access Key"
            },
            "type": "secret-input",
            "required": false,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 Secret Access Key",
              "en_US": "Enter your Secret Access Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "aws_region",
            "label": {
              "zh_Hans": "AWS 地区",
              "en_US": "AWS Region"
            },
            "type": "select",
            "required": false,
            "default": "us-east-1",
            "options": [
              {
                "label": {
                  "zh_Hans": "美国东部 (弗吉尼亚北部)",
                  "en_US": "US East (N. Virginia)"
                },
                "value": "us-east-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "美国西部 (俄勒冈州)",
                  "en_US": "US West (Oregon)"
                },
                "value": "us-west-2",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "亚太地区 (新加坡)",
                  "en_US": "Asia Pacific (Singapore)"
                },
                "value": "ap-southeast-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "亚太地区 (东京)",
                  "en_US": "Asia Pacific (Tokyo)"
                },
                "value": "ap-northeast-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "欧洲 (法兰克福)",
                  "en_US": "Europe (Frankfurt)"
                },
                "value": "eu-central-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "AWS GovCloud (US-West)",
                  "en_US": "AWS GovCloud (US-West)"
                },
                "value": "us-gov-west-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "亚太地区 (悉尼)",
                  "en_US": "Asia Pacific (Sydney)"
                },
                "value": "ap-southeast-2",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "中国北京 (cn-north-1)",
                  "en_US": "AWS Beijing (cn-north-1)"
                },
                "value": "cn-north-1",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "中国宁夏 (cn-northwest-1)",
                  "en_US": "AWS Ningxia (cn-northwest-1)"
                },
                "value": "cn-northwest-1",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "vessl_ai",
      "label": {
        "zh_Hans": "VESSL AI",
        "en_US": "VESSL AI"
      },
      "description": null,
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/vessl_ai/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/vessl_ai/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/vessl_ai/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/vessl_ai/icon_large/en_US"
      },
      "background": "#F1EFED",
      "help": {
        "title": {
          "zh_Hans": "How to deploy VESSL AI LLM Model Endpoint",
          "en_US": "How to deploy VESSL AI LLM Model Endpoint"
        },
        "url": {
          "zh_Hans": "https://docs.vessl.ai/guides/get-started/llama3-deployment",
          "en_US": "https://docs.vessl.ai/guides/get-started/llama3-deployment"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "customizable-model"
      ],
      "provider_credential_schema": null,
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "Model Name",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "Enter model name",
            "en_US": "Enter model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "endpoint_url",
            "label": {
              "zh_Hans": "Endpoint Url",
              "en_US": "Endpoint Url"
            },
            "type": "text-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Enter VESSL AI service endpoint url",
              "en_US": "Enter VESSL AI service endpoint url"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "Enter VESSL AI secret key",
              "en_US": "Enter VESSL AI secret key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "mode",
            "label": {
              "zh_Hans": "Completion Mode",
              "en_US": "Completion Mode"
            },
            "type": "select",
            "required": false,
            "default": "chat",
            "options": [
              {
                "label": {
                  "zh_Hans": "Completion",
                  "en_US": "Completion"
                },
                "value": "completion",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "Chat",
                  "en_US": "Chat"
                },
                "value": "chat",
                "show_on": []
              }
            ],
            "placeholder": {
              "zh_Hans": "Select completion mode",
              "en_US": "Select completion mode"
            },
            "max_length": 0,
            "show_on": [
              {
                "variable": "__model_type",
                "value": "llm"
              }
            ]
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    },
    {
      "provider": "stepfun",
      "label": {
        "zh_Hans": "阶跃星辰",
        "en_US": "Stepfun"
      },
      "description": {
        "zh_Hans": "阶跃星辰提供的模型，例如 step-1-8k、step-1-32k、step-1v-8k、step-1v-32k、step-1-128k 和 step-1-256k。",
        "en_US": "Models provided by stepfun, such as step-1-8k, step-1-32k、step-1v-8k、step-1v-32k, step-1-128k and step-1-256k"
      },
      "icon_small": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/stepfun/icon_small/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/stepfun/icon_small/en_US"
      },
      "icon_large": {
        "zh_Hans": "/console/api/workspaces/current/model-providers/stepfun/icon_large/zh_Hans",
        "en_US": "/console/api/workspaces/current/model-providers/stepfun/icon_large/en_US"
      },
      "background": "#FFFFFF",
      "help": {
        "title": {
          "zh_Hans": "从 stepfun 获取 API Key",
          "en_US": "Get your API Key from stepfun"
        },
        "url": {
          "zh_Hans": "https://platform.stepfun.com/interface-key",
          "en_US": "https://platform.stepfun.com/interface-key"
        }
      },
      "supported_model_types": [
        "llm"
      ],
      "configurate_methods": [
        "predefined-model",
        "customizable-model"
      ],
      "provider_credential_schema": {
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "model_credential_schema": {
        "model": {
          "label": {
            "zh_Hans": "模型名称",
            "en_US": "Model Name"
          },
          "placeholder": {
            "zh_Hans": "输入模型名称",
            "en_US": "Enter your model name"
          }
        },
        "credential_form_schemas": [
          {
            "variable": "api_key",
            "label": {
              "zh_Hans": "API Key",
              "en_US": "API Key"
            },
            "type": "secret-input",
            "required": true,
            "default": null,
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的 API Key",
              "en_US": "Enter your API Key"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "context_size",
            "label": {
              "zh_Hans": "模型上下文长度",
              "en_US": "Model context size"
            },
            "type": "text-input",
            "required": true,
            "default": "8192",
            "options": null,
            "placeholder": {
              "zh_Hans": "在此输入您的模型上下文长度",
              "en_US": "Enter your Model context size"
            },
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "max_tokens",
            "label": {
              "zh_Hans": "最大 token 上限",
              "en_US": "Upper bound for max tokens"
            },
            "type": "text-input",
            "required": true,
            "default": "8192",
            "options": null,
            "placeholder": null,
            "max_length": 0,
            "show_on": []
          },
          {
            "variable": "function_calling_type",
            "label": {
              "zh_Hans": "Function calling",
              "en_US": "Function calling"
            },
            "type": "select",
            "required": false,
            "default": "no_call",
            "options": [
              {
                "label": {
                  "zh_Hans": "不支持",
                  "en_US": "Not supported"
                },
                "value": "no_call",
                "show_on": []
              },
              {
                "label": {
                  "zh_Hans": "Tool Call",
                  "en_US": "Tool Call"
                },
                "value": "tool_call",
                "show_on": []
              }
            ],
            "placeholder": null,
            "max_length": 0,
            "show_on": []
          }
        ]
      },
      "preferred_provider_type": "custom",
      "custom_configuration": {
        "status": "no-configure"
      },
      "system_configuration": {
        "enabled": false,
        "current_quota_type": null,
        "quota_configurations": []
      }
    }
  ]
}
```

## Analysis
### Validation
- Validate setup
- Validate login
- Validate account initialization
### Action
- Get tenant id
- creates an instance of ModelProviderService
- retrieve the list of model providers
- encode the provider list as JSON.