###

# RansomFlag CTF Write-Up

## Overview
This repository contains the walkthrough of the **RansomFlag** CTF challenge. The goal of this challenge is to decrypt an encrypted flag using a provided script and given values. This document will guide you through the steps and logic behind solving the challenge.

## Challenge Description
In this challenge, we are tasked with decrypting a flag that has been encrypted using a combination of RSA-like encryption and the ChaCha20 cipher. The following data is provided:

- An encrypted flag in Base64 format.
- An RSA-like private key (d and n).
- A list of integers representing the encrypted message.
- A Base64-encoded nonce for ChaCha20.
- A hardcoded XOR key.

## Walkthrough
Below is the Python script used to decrypt the flag. Each step is explained in detail:

### Script
```python
import base64
from Crypto.Cipher import ChaCha20
from math import pow

# Given values from the challenge
encrypted_flag = "4HGJ/3Y6iekXR+FXdpdpa+ww4601QUtLGAzHO/8="
nonce_b64 = "nFE+9jfXTKM="
private_key_d = 56771
private_key_n = 57833
encrypted_message = [
    41179, 49562, 30232, 7343, 51179, 49562, 24766, 36190, 30119, 33040,
    22179, 44468, 15095, 22179, 3838, 28703, 32061, 17380, 34902, 51373,
    41673, 6824, 41673, 26412, 27116, 51179, 34646, 15095, 10590, 11075,
    1613, 20320, 31597, 51373, 20320, 44468, 23130, 47991, 11075, 15095,
    34928, 20768, 15095, 8054
]
xor_key = "0x1337"

# Function to decrypt RSA-like encrypted values
def rsa_decrypt(c, d, n):
    # Compute (c ** d) % n
    return (c ** d) % n

# Step 1: Decrypt the obfuscated key using RSA-like encryption
decrypted_obfuscated_key_b64 = ''.join(
    [chr(rsa_decrypt(c, private_key_d, private_key_n)) for c in encrypted_message]
)

# Decode Base64 to retrieve the obfuscated key
decrypted_obfuscated_key = base64.b64decode(decrypted_obfuscated_key_b64)

# Step 2: Recover the original key using XOR with "0x1337"
chacha_key = bytearray(decrypted_obfuscated_key[i] ^ ord(xor_key[i % len(xor_key)]) for i in range(len(decrypted_obfuscated_key)))

# Step 3: Decrypt the flag using ChaCha20 with the recovered key and nonce
nonce = base64.b64decode(nonce_b64)
cipher = ChaCha20.new(key=bytes(chacha_key), nonce=nonce)
decrypted_flag = cipher.decrypt(base64.b64decode(encrypted_flag)).decode('utf-8')

print(f"Recovered Flag: {decrypted_flag}")
```

### Explanation
1. **Decrypting the Obfuscated Key:**
   - The provided `encrypted_message` is decrypted using an RSA-like algorithm with the given private key `d` and modulus `n`.
   - The decrypted values are combined into a Base64-encoded string.

2. **Decoding the Base64 String:**
   - The Base64-encoded string is decoded to retrieve the obfuscated key.

3. **Recovering the Original Key:**
   - The original key is recovered by XORing each byte of the obfuscated key with the repeating characters of the string "0x1337".

4. **Decrypting the Flag:**
   - The ChaCha20 cipher is initialized using the recovered key and the decoded nonce.
   - The encrypted flag is decrypted using ChaCha20, resulting in the plaintext flag.

## Conclusion
By following the steps in the provided script, we successfully decrypted the flag for the **RansomFlag** CTF challenge. This challenge demonstrated concepts such as RSA-like encryption, XOR operations, Base64 encoding/decoding, and ChaCha20 decryption.

### Contact me: 

<a href="https://www.instagram.com/t2tt/" style="color: white; text-decoration: none;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg" alt="Instagram" width="30" />
</a>

