# SystemFeatureApi

## Argument

## CURL
```bash
curl 'http://localhost/console/api/system-features' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,vi;q=0.8,en-AU;q=0.7' \
  -H 'Connection: keep-alive' \
  -b $'pga4_session=b6535706-ae8a-443e-bdfd-dca89424b322\u00211FLgJJKrucRIi/k85oqB7CGBV1TL51eyl1J0/zkrDJM=; PGADMIN_LANGUAGE=en' \
  -H 'Referer: http://localhost/app/f3f6d21f-a90d-4d55-8973-b81d56cebdcf/configuration' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDYxYTBkNTgtN2NhYy00MmUxLWI2ZWUtMGNkZjRiZWE4YTM2IiwiZXhwIjoxNzQxODU1NDgyLCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.oiNX1CNaNNtredSMakEi4Kjr3u8zBjjAeUDB_CTMAHs' \
  -H 'content-type: application/json' \
  -H 'sec-ch-ua: "Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

## Response
```bash
{
    "sso_enforced_for_signin": false,
    "sso_enforced_for_signin_protocol": "",
    "sso_enforced_for_web": false,
    "sso_enforced_for_web_protocol": "",
    "enable_web_sso_switch_component": false,
    "enable_email_code_login": false,
    "enable_email_password_login": true,
    "enable_social_oauth_login": false,
    "is_allow_register": false,
    "is_allow_create_workspace": false,
    "is_email_setup": true,
    "license": {
        "status": "none",
        "expired_at": ""
    }
}
```

## Analysis
### Action
- Get system features
