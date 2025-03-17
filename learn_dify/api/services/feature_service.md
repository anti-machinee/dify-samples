# LicenseStatus
- Status of license
- Enum format

# LicenseModel
- Model for license

# FeatureModel
- Model for feature

# SystemFeatureModel
- Model for system feature

# FeatureService

## get_features
### Arguments
- tenant id
### Actions
- This initializes a new FeatureModel object with default values
- Calls a class method _fulfill_params_from_env to populate the features object with values from the environment configuration
- If billing is enabled and a tenant ID is provided, it calls another class method _fulfill_params_from_billing_api to populate the features object with billing-related information for the given tenant ID.
### Response
- Returns the populated FeatureModel object containing all the feature settings for the tenant

## get_system_features
### Actions
- Create SystemFeatureModel Instance
- Calls a class method _fulfill_system_params_from_env to populate the features object with values from the environment configuration
- If enterprise is enabled, it calls another class method _fulfill_params_from_enterprise to populates additional enterprise-specific parameters
### Response
- Returns the populated SystemFeatureModel instance accurately reflects the current system and enterprise configurations.

## _fulfill_system_params_from_env
### Arguments
- system_features
### Actions
- populates the system_features instance with various system parameters based on the environment configuration (dify_config)
- ensures that the SystemFeatureModel instance accurately reflects the current system settings, such as login methods, registration permissions, workspace creation permissions, and email setup status.
### Response

## _fulfill_params_from_env
### Arguments
- features
- tenant_id
### Actions
- sets the can_replace_logo attribute of the features object to the value of CAN_REPLACE_LOGO from the dify_config
- sets the model_load_balancing_enabled attribute of the features object to the value of MODEL_LB_ENABLED from the dify_config
- sets the dataset_operator_enabled attribute of the features object to the value of DATASET_OPERATOR_ENABLED from the dify_config
### Response
- updates the FeatureModel object with specific feature settings based on the environment configuration provided by dify_config

## _fulfill_params_from_billing_api
### Arguments
- features
- tenant_id
### Actions
- responsible for populating the FeatureModel object with billing-related information for a given tenant ID
- calls the BillingService.get_info method to retrieve billing information for the specified tenant ID
- Members: Updates size and limit if members key is present.
- Apps: Updates size and limit if apps key is present.
- Vector Space: Updates size and limit if vector_space key is present.
- Documents Upload Quota: Updates size and limit if documents_upload_quota key is present.
- Annotation Quota Limit: Updates size and limit if annotation_quota_limit key is present.
- Docs Processing: Updates docs_processing if docs_processing key is present.
- Can Replace Logo: Updates can_replace_logo if can_replace_logo key is present.
- Model Load Balancing Enabled: Updates model_load_balancing_enabled if model_load_balancing_enabled key is present.
### Response
- updates the FeatureModel object with various billing-related settings based on the information retrieved from the BillingService for the specified tenant ID

## _fulfill_params_from_enterprise
### Arguments
- features
### Actions
- calls EnterpriseService.get_info() to retrieve enterprise-specific configuration data, stored in the enterprise_info dictionary.
- The method checks for the presence of specific keys in the enterprise_info dictionary.
- If a key exists, it assigns the corresponding value to the appropriate attribute of the features object.
- If the license key exists in enterprise_info, it further checks for status and expired_at within the license dictionary. It assigns these values to the features.license attributes, converting the status to a LicenseStatus enum.
### Response
- ensures that the features object is populated with the latest enterprise-specific settings, which can include single sign-on (SSO) configurations, login methods, registration permissions, workspace creation permissions, and license details. This allows the system to adapt its behavior based on the enterprise's configuration.
