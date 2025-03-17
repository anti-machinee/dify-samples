# Tenant

## Arguments
- `__tablename__` specifies the name of the table in the database.
- `__table_args__` defines additional table arguments, including a primary key constraint on the `id` column.
- `id`: A unique identifier for the tenant, generated using `uuid_generate_v4()`.
- `name`: The name of the tenant, which is a required field.
- `encrypt_public_key`: A text field for storing the tenant's encryption public key.
- `plan`: The subscription plan of the tenant, with a default value of 'basic'.
- `status`: The status of the tenant, with a default value of 'normal'.
- `custom_config`: A text field for storing custom configuration in JSON format.
- `created_at`: The timestamp when the tenant was created, with a default value of the current timestamp.
- `updated_at`: The timestamp when the tenant was last updated, with a default value of the current timestamp.

## get_accounts
### Actions
- This method returns a list of `Account` objects associated with the tenant by querying the `TenantAccountJoin` table.

## custom_config_dict
### Actions
- This property getter and setter allow accessing and modifying the `custom_config` field as a dictionary. The getter parses the JSON string into a dictionary, and the setter converts the dictionary back into a JSON string.
