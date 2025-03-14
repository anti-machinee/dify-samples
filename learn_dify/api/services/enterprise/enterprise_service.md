# EnterpriseService

## get_info
### Actions
- This class method sends a GET request to the /info endpoint of the enterprise API.
- It uses the EnterpriseRequest.send_request method to perform the HTTP request.
- The method returns the response from the API, which is expected to contain enterprise-specific information.
### Response
- Output of GET request

## get_app_web_sso_enabled
### Arguments
- app_code
### Actions
- This class method sends a GET request to the /app-sso-setting endpoint of the enterprise API, with a query parameter appCode set to the provided app_code.
- It uses the EnterpriseRequest.send_request method to perform the HTTP request.
- The method returns the response from the API, which is expected to contain information about whether web SSO (Single Sign-On) is enabled for the specified application.
### Response
- Output of GET request