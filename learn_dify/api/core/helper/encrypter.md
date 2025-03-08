# decrypt_token
## Arguments
- tenant_id
- token
## Action
- decodes a Base64-encoded token
- Decrypt the decoded value
## What is overall functionalty?
- Decrypts a Base64-encoded encrypted token using RSA or AES (hybrid encryption).
- Retrieves RSA private keys securely, leveraging Redis caching.
- Uses hybrid encryption for optimized security and performance.
- Ensures decrypted values are returned safely without exposing secrets unnecessarily.