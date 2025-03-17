# AppService

## get_paginate_apps
### Arguments
- user_id
- tenant_id
- args
### Action
- Filters apps by tenant ID. Excludes universal apps, meaning only tenant-specific apps are included
- Add filter by app mode
- Add filter by who created -> careful because access control is not implemented
- Limits search string to 30 characters to prevent abuse
### Response
- 

## get_app
### Arguments
- app
### Action
- If app mode is agent chat, process agent tool steps. Otherwise returns directly
- Query model config from database
- Get agent mode
- Iterating over agent tools
    - Filter invalid tools
    - Convert tool data to an object
    - Init tool runtime
    - Init tool manager
    - Get decrypted parameters
    - Mask tool parameters
    - Override tool parameters with parameters
- Override agent mode of model config with agent mode that tool parameters are overridden
- Wrap app in modified class that store model config overridden
### Response
- App with parameters are overridden and masked
### Error handling
- Pass if error happens #TODO
### In get_agent_tool_runtime, it has runtime_parameters = encryption_manager.decrypt_tool_parameters(runtime_parameters). Why the for loop still calls manager.decrypt_tool_parameters
#### Different Contexts of Decryption
- get_agent_tool_runtime() decrypts runtime_parameters.
    - This means that only the parameters retrieved at runtime are decrypted at that stage.
    - However, this does not necessarily include parameters defined in agent_tool_entity.tool_parameters.
- manager.decrypt_tool_parameters(agent_tool_entity.tool_parameters) decrypts tool_parameters.
    - agent_tool_entity.tool_parameters could come from a static configuration rather than runtime.
    - These parameters may still be encrypted when retrieved from an external source.
- Since runtime_parameters and tool_parameters could come from different sources, the decryption step must be applied separately to each.
#### Ensuring All Parameters Are Decrypted
- Even though get_agent_tool_runtime() decrypts runtime_parameters, it does not modify agent_tool_entity.tool_parameters directly.
    - agent_tool_entity.tool_parameters might have come from:
        - A database
        - An API call
        - A configuration file
        - Another external system
- If these parameters were encrypted at rest, they must be decrypted before use.
- Thus, the second decryption call ensures that both runtime and static parameters are properly decrypted before being masked and used
#### Separation of Concerns
- get_agent_tool_runtime() is only responsible for retrieving and preparing the runtime tool.
- ToolParameterConfigurationManager.decrypt_tool_parameters() handles decryption at the tool configuration level.
- This separation ensures flexibility:
    - If agent_tool_entity.tool_parameters ever comes from a different encrypted source, it still gets decrypted properly.
    - If additional logic is needed in parameter decryption (e.g., different decryption methods per provider), manager.decrypt_tool_parameters() can handle it.
#### Masking Requires Decryption
- After decryption, the parameters are masked using:
- If manager.decrypt_tool_parameters() was skipped, mask_tool_parameters() might receive encrypted values, leading to incorrect masking.
- Thus, decryption before masking is essential.