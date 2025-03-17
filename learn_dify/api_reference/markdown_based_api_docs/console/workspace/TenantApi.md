# TenantApi

## CURL
```bash
curl 'http://localhost/console/api/workspaces/current?' \
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
    "id": "b2baab04-c6e4-4b78-9c8a-67cd62cc3aef",
    "name": "admin's Workspace",
    "plan": "basic",
    "status": "normal",
    "created_at": 1740303411,
    "role": "owner",
    "in_trial": null,
    "trial_end_reason": null,
    "custom_config": null
}
```

## Analysis
### Validation
- Validate setup
- Validate login
- Validate account initialization
### Serialization
- Serialize the return value into tenant fields
### Action
- Get current tenant
- Validate archive tenant
  - Swith to first tenant
  - Raise authorisation error
- Use workspace service to get tenant info
### Raise error
- Raise authorisation
  - When tenant status is archive but there are no join tenants