# Tool

## Base class
- This is base class of
    - ApiTool
    - BuiltinTool
    - WorkflowTool

## Runtime
### instance variable in __init__
- Unique for each tool
### class variables
- All instances of the same tool share the same class variables

## fork_tool_runtime
### Arguments
- runtime
### Action
- Create a duplicate of the attributes with model_copy
- Make a shallow copy
### Response
- An instance of Tool class

## get_runtime_parameters
### Action
- Get class attributes
- Can be overridden in subclasses

## get_all_runtime_parameters
### Action
- retrieves and merges runtime parameters for a tool
- ensures that user-defined parameters override existing ones, or are added if they don’t exist
### Response
- parameters overridden
### If parameters and user_parameters are identical
- user_parameters = self.get_runtime_parameters()
    - The get_runtime_parameters method simply returns self.parameters or an empty list.
    - However, this method could be overridden in a subclass to return a modified version of self.parameters.
    - This means user_parameters could differ from parameters if get_runtime_parameters is customized.
- By default, parameters and user_parameters are the same.
- They only differ if get_runtime_parameters is overridden to modify or extend the list dynamically.
- The method allows for flexibility by letting developers customize runtime parameters without modifying the original self.parameters.