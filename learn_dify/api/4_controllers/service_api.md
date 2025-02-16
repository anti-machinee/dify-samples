# Note
- This endpoint is relative to the base URL. Read the [Controllers](learn_dify/api/4_controllers/4_controllers.md) for more details
- In the future, consider to use tools for API documentation (Swagger UI, ...)

# index
## IndexApi
### HTTP verb
- GET
### Relative URL
- /
### Analysis
- Return metadata about the API and server
### Questions
- Where it is used in FE?

# app
## AppParameterApi
### HTTP verb
- GET
### Relative URL
- /parameters
### Analysis
- Authorize before function call with [validate_app_token](#validate_app_token)
- Provide App model
- Get parameters of the app from feature_dict and user_input_form
    - If app mode is workflow
        - Get workflow from App model
            - Get features_dict from workflow
            - Get user_input_form from workflow
    - Else
        - Get app_model_config
        - Get features_dict from app_model_config
        - Get user_input_form from features_dict
- Set app parameters given features_dict and user_input_form with [get_parameters_from_feature_dict](helpers.md#get_parameters_from_feature_dict)
### Questions
- How App model is provided to this attribute?
- What workflow looks like?
- What app_model_config looks like?
- What features_dict looks like?
- What user_input_form looks like?
## AppMetaApi
### HTTP verb
- GET
### Relative URL
- /meta
### Analysis
### Questions
## AppInfoApi
### HTTP verb
- GET
### Relative URL
- /info
### Analysis
### Questions

# audio
## AudioApi
## TextApi

# completion
## CompletionApi
## CompletionStopApi
## ChatApi
## ChatStopApi

# conversation
## ConversationApi
## ConversationDetailApi
## ConversationRenameApi

# file
## FileApi

# message
## MessageListApi
## MessageFeedbackApi
## MessageSuggestedApi

# workflow
## WorkflowRunApi
## WorkflowRunDetailApi
## WorkflowTaskStopApi
## WorkflowAppLogApi

# dataset
## DatasetListApi
## DatasetApi

## DocumentAddByTextApi
## DocumentAddByFileApi
## DocumentUpdateByTextApi
## DocumentUpdateByFileApi
## DocumentDeleteApi
## DocumentListApi
## DocumentIndexingStatusApi

## HitTestingApi

## SegmentApi
## DatasetSegmentApi

## UploadFileApi

# Further analysis

# wrap
## validate_app_token

# References
