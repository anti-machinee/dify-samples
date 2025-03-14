# VersionApi

## Argument
- current_version

## CURL
```bash
curl 'http://localhost/console/api/version?current_version=0.15.1' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,vi;q=0.8,en-AU;q=0.7' \
  -H 'Connection: keep-alive' \
  -b $'pga4_session=b6535706-ae8a-443e-bdfd-dca89424b322\u00211FLgJJKrucRIi/k85oqB7CGBV1TL51eyl1J0/zkrDJM=; PGADMIN_LANGUAGE=en' \
  -H 'Referer: http://localhost/app/f3f6d21f-a90d-4d55-8973-b81d56cebdcf/configuration' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDYxYTBkNTgtN2NhYy00MmUxLWI2ZWUtMGNkZjRiZWE4YTM2IiwiZXhwIjoxNzQxODU5ODQ4LCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.UVfyg2RieFl-7Z-lsmKkCUWS3Lw2-9ncBh5nIdewslQ' \
  -H 'content-type: application/json' \
  -H 'sec-ch-ua: "Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

## Payload
```bash
current_version: 0.15.1
```

## Response
```bash
{
    "version": "1.0.1",
    "release_date": "2025-03-11",
    "release_notes": "http://docs.dify.ai",
    "can_auto_update": true,
    "features": {
        "can_replace_logo": false,
        "model_load_balancing_enabled": false
    }
}
```

## Analysis
### Action
- It initializes a result dictionary with default values, including the current version and feature flags from dify_config
- If check_update_url is not set, it returns the default result.
- It sends a GET request to the check_update_url with the current_version as a parameter.
- Response Handling
    - It parses the JSON response content.
    - It calls _has_new_version to check if a new version is available.
    - If a new version is available, it updates the result with the new version details from the response.
### Raise errors
- Exception
    - If an exception occurs during the request to check_update_url, it logs a warning and returns the default result.

# _has_new_version
## Argument
- latest_version
- current_version
## Actions
- It compares the latest_version with the current_version to determine if a new version is available.
- It returns True if the latest_version is greater than the current_version, otherwise False.
## Response
- True or False
## Raise errors
- InvalidVersion
    - invalid version format
