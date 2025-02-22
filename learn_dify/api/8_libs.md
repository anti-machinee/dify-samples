# login_required
- Check authorization header
- Validate token with the api admin key
- Get workspace id
- Find owner of workspace
- Login with admin user
- Skip login check bases on request method and environment variable
- Ensure user is logged in otherwise redirect to unauthorized hanlder
- Handle sync/async Flask version