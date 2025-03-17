# setup_required
- Check if password is initialized in self hosted environment by checking SELF_HOSTED and INIT_PASSWORD variables

# account_initialization_required
- Check if account is initialized by checking current_user.status

# get_app_model
- Wrap original function to perform validation
- Check app_id
- Query App model
- Validate app mode in DB and app mode in code
