# AccountProfileApi

## CURL
```bash
curl 'http://localhost/console/api/account/profile' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9,vi;q=0.8,en-AU;q=0.7' \
  -H 'Connection: keep-alive' \
  -b $'pga4_session=b6535706-ae8a-443e-bdfd-dca89424b322\u00211FLgJJKrucRIi/k85oqB7CGBV1TL51eyl1J0/zkrDJM=; PGADMIN_LANGUAGE=en' \
  -H 'Referer: http://localhost/app/f3f6d21f-a90d-4d55-8973-b81d56cebdcf/configuration' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDYxYTBkNTgtN2NhYy00MmUxLWI2ZWUtMGNkZjRiZWE4YTM2IiwiZXhwIjoxNzQxNzQ5OTE0LCJpc3MiOiJTRUxGX0hPU1RFRCIsInN1YiI6IkNvbnNvbGUgQVBJIFBhc3Nwb3J0In0.NGQCK4RUK84xO_1mV9I-sSfYESarPDh-nhIG5X3N-Fc' \
  -H 'content-type: application/json' \
  -H 'sec-ch-ua: "Chromium";v="134", "Not:A-Brand";v="24", "Microsoft Edge";v="134"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"'
```

## Response
```bash
{
    "id": "061a0d58-7cac-42e1-b6ee-0cdf4bea8a36",
    "name": "admin",
    "avatar": null,
    "email": "admin@gmail.com",
    "is_password_set": true,
    "interface_language": "en-US",
    "interface_theme": "light",
    "timezone": "America/New_York",
    "last_login_at": 1741048929,
    "last_login_ip": "172.18.0.1",
    "created_at": 1740303410
}
```

## Analysis
### Validation
- Validate setup
- Validate loginl
- Validate enterprise license 
### Serialization
- Serialize the return value into account fields
### Action
- Return current user (Flask login object)