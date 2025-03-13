# WorkspaceService

## get_tenant_info
### Arguments
- tenant
### Action
- Check if Tenant Exists. If the tenant parameter is None, the method returns None.
- Initialize Tenant Info Dictionary
    - A dictionary tenant_info is created with basic information about the tenant, including id, name, plan, status, created_at, in_trail, trial_end_reason, and role.
- Retrieve User Role
    - The method queries the TenantAccountJoin table to find the role of the current user (current_user.id) within the tenant (tenant.id).
- If no matching record is found, an assertion error is raised.
- The user's role is added to the tenant_info dictionary.
- Check Feature Permission
    - The method checks if the tenant has the feature to replace the logo using the FeatureService.
- Custom Configurations
    - If the tenant can replace the logo and the user has the roles OWNER or ADMIN, additional custom configurations are added to the tenant_info dictionary.
    - This includes the URL for replacing the web app logo and a flag for removing the web app brand.
### Response
- The method returns the tenant_info dictionary containing all the gathered information.