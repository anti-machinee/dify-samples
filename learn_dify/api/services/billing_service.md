# BillingService

## Class attributes
- base_url
- secret_key
- Get from environment variables

## get_info
### Arguments
- tenant_id
### Actions
- Creates a dictionary params containing the tenant_id as a key-value pair. This dictionary will be used as query parameters for the HTTP request.
- The _send_request method sends the HTTP GET request to the billing API and returns the response
### Response
- Returns the billing_info obtained from the _send_request method.

## _send_request
### Arguments
- method
- endpoint
- json
- endpoint
### Actions
- responsible for sending HTTP requests to the billing AP
- creates a dictionary headers containing the Content-Type and Billing-Api-Secret-Key. The Billing-Api-Secret-Key is retrieved from the class attribute secret_ke
- constructs the full URL for the API request by concatenating the base_url class attribute with the provided endpoint
- sends the HTTP request using the httpx.request method with the specified method, url, json, params, and headers
### Response
- returns the JSON content of the response
### Raise errors
- the request method is GET and the response status code is not 200 OK, this block raises a ValueError indicating that the billing information could not be retrieved