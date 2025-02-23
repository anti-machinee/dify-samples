# ToolManager

## 

## get_builtin_provider
### Arguments
#### provider
### Action
- :oad builtin provider from cache
### Response
- 
### Raise error
- ToolProviderNotFoundError

## get_builtin_tool
### Arguments
#### provider
#### tool_name
#### provider
### Action
- Get provider controller by provider name
- Get tool by tool name
### Response
- Builtin tool
### Raise error
- ToolNotFoundError

## get_tool_runtime
### Arguments
#### provider_type
#### provider_id
#### tool_name
#### tenant_id
#### invoke_from
#### tool_invoke_from
### Action
- There are 4 types of tools
    - builtin
    - api
    - workflow
    - app
        - Not supported (version 0.15.1)
- For builtin tools
    - Get builtin tool runtime
    - Get builtin provider controller
    - Check if the builtin tool need credentials
        - If not, the credentials is empty
    - Query builtin provider from database
        - Must have
    - Decrypt the credentials
        - Get builtin provider controller
        - Init the tool configuration manager
        - Decrypt the tool credentials
### Response
- Return tool runtime based on tool type
- Credentials are decrypted
### Raise error
- ToolProviderNotFoundError
- ValueError
- NotImplementedError

## get_agent_tool_runtime
### Arguments
#### tenant_id
#### app_id
#### agent_tool
#### invoke_from
### Action
- Get tool runtime
- Get parameters of tool runtime
- Iterate over tool parameters
    - 
### Response
### Raise error
- ValueError

## load_builtin_providers_cache
### Arguments
### Action
- 
### Response
- 
### Raise error
- 