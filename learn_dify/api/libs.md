# login_required
- Check authorization header
- Validate token with the api admin key
- Get workspace id
- Find owner of workspace
- Login with admin user
- Skip login check bases on request method and environment variable
- Ensure user is logged in otherwise redirect to unauthorized hanlder
- Handle sync/async Flask version

# compact_generate_response
- If response of LLM generator is dict, return as JSON formatted string
- If response of LLM generator is not dict
    - Define a nested function to yield all values from response
    - Use flask.stream_with_context to stream response in a chunked manner
- Consider mimetype