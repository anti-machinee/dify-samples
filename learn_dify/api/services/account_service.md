# TenantService

## get_join_tenants
### Arguments
- Current user
### Action
- Query tables (Tenant, TenantAccountJoin) to get join tenants
### Response
- Account join tenants

## switch_tenant
### Arguments
- current user
- tenant_id
### Action
- Require tenant id is provided
- Query the TenantAccountJoin table to find a record where the account_id matches the given account's ID, the tenant_id matches the provided tenant ID, and the tenant's status is NORMAL.
- Require TenantAccountJoin exists
- Update all TenantAccountJoin records for the given account to set current to False where the tenant_id does not match the provided tenant ID.
- Set the current status of the matching TenantAccountJoin record to True
- Update the current_tenant_id of the account to the provided tenant ID
- Commit the changes to the database
### Response
- No value is returned
### Raise error
- ValueError
    - tenant id must be provided
- AccountNotLinkTenantError
    - Tenant not found
    - Account is not a member of the tenant
### Question
#### Why need to switchi Tenant:
- When the current tenant's status is ARCHIVE, it indicates that the tenant is no longer active or accessible.
- To ensure the user can continue to work within an active tenant, the method attempts to switch the user to another tenant they have joined.

## has_roles
### Arguments
- tenant
- roles
### Actions
- checks if all elements in the roles list are instances of TenantAccountJoinRole
- queries the TenantAccountJoin table to check if there is any record where the tenant_id matches the ID of the provided tenant. The role is in the list of roles provided (converted to their value attribute).
### Response
- True/False if find in the database
### Raise error
- ValueError
    - When roles must be TenantAccountJoinRole instances
