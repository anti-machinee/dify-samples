# get_app_model

## Description
- This is a decorator used to wrap a view function in a web application
- It retrieves an application model from the database given app_id and do some validations before allowing the view function to proceed

## Argumment
### view
- A function that this decorator wraps
- If not provided, it returns a decorator
### mode
- An app mode or list of app modes

## Action
### decorator
- Wrap the actual view function passed to the decorator
### decorated_view
- Executed when the view is called
- Use @wraps(view_func) to preserve the original function metadata
- Require app_id
- Query database to retrieve app model
- Get app mode
- Validate against provided mode
- Pass app model to the view function

## Response
- Injects app_model into kwargs before calling the original view_func.

## Raise errors
- ValueError for missing app_id
- AppNotFoundError
    - cannot query app model in database.app mode is channel
    - app mode is channel
    - app mode in database is not in the provided mode
