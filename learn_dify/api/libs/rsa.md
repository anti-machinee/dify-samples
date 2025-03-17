# get_decrypt_decoding
## Arguments
- tenant_id
## Action
- Get the Redis cache. If key not found, load fromt private key file
- Cache the key in Redis for 120 seconds to reduce file reads
- Converts the private key into an RSA cipher
## Response
- RSA key and cipher RSA

# decrypt_token_with_decoding
## Arguments
- encrypted_text
- rsa_key
- cipher_rsa
## Action
- Handle 2 types of encrypted text
    - Hybrid Encryption
        - The encrypted text starts with prefix_hybrid, meaning it was encrypted using AES for performance and RSA for key security.
        - Extracts:
            - enc_aes_key → AES key (encrypted using RSA)
            - nonce → Used for AES encryption
            - tag → Used for integrity check
            - ciphertext → The actual encrypted data
        - Steps to decrypt:
            - RSA decrypts enc_aes_key to get the AES key.
            - AES decrypts the ciphertext using the decrypted AES key.
    - Pure RSA Encryption
        - If there is no hybrid prefix, it simply decrypts using RSA.

# decrypt
## Arguments
- encrypted_text
- tenant_id
## Action
- Retrieve RSA key
- Decrypt the encrypted text
