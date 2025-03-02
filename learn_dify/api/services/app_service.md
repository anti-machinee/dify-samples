# AppService

## get_app
### Description
- Form information about the app
- If app mode is agent chat, update tools
### Argument
- app
### Action
- If app mode is agent chat, process additional steps. Otherwise returns directly
- Query model config from database
- Get agent mode
- Iterating over agent tools
    - Filter invalid tools
    - Convert tool data to an object
    - Init tool runtime
    - Init tool manager
    - Get decrypted parameters
    - Override tool parameters with parameters
    - Override agent mode of model config with agent mode that tool parameters are overridden
    - Wrap app in modified class that store model config overridden
### Response
### Raise error
### Error handling
- Pass if error happens -> TODO