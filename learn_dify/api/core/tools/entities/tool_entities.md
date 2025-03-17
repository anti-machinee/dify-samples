# ToolIdentity

# ToolParameter

## ToolParameterType
### as_normal_type
### cast_value
#### Arguments
- value
#### Action
- Ensure input value is correctly cast based on its expected type
- Use match case syntax to check the type of self
- Raise if value is invalid
- Handle
    - String
    - Boolean
    - Number
    - File path
#### Response
- Casted value
#### Raise error
- ValueError if tool parameter type is invalid

## ToolParameterForm

# ToolDescription