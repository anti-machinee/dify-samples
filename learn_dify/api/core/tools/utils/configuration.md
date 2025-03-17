# ToolParameterConfigurationManager

## init
### Arguments
- tenant_id
- tool_runtime
- provider_name
- provider_type
- identity_id

## _merge_parameters
### Action
- Ensures that tool parameters are updated with the latest runtime values while preserving any additional parameters that need to be included.
- Retrieve the tool parameters and runtime parameters
- Ensure modification does not affect the original parameters
- Iterate over the runtime parameters
    - If parameter in runtime parameters
        - Update the parameter in tool parameters with runtime parameter
    - If not found, append to current parameters
### Response
- Return the updated parameters

## decrypt_tool_parameters
### Arguments
- parameters
### Action
- Init parameter cache helper
- Get cached parameters
- Override current parameters
- Loop over current parameters
    - If parameter in current parameters
        - Decrypt the parameter
- Cache the decrypted parameters
### Response
- Decrypted parameters
