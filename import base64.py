import base64
from Crypto.Cipher import ChaCha20
from math import pow

# القيم المعطاة من السؤال
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

# دالة لفك تشفير النصوص باستخدام RSA-like
def rsa_decrypt(c, d, n):
    # حساب القيم باستخدام (c ** d) % n بدلاً من دالة pow في Python 2.x
    return (c ** d) % n

# الخطوة 1: فك تشفير الرسالة المشفرة باستخدام المفتاح الخاص
decrypted_obfuscated_key_b64 = ''.join(
    [chr(rsa_decrypt(c, private_key_d, private_key_n)) for c in encrypted_message]
)

# فك تشفير Base64 للحصول على المفتاح المشوش
decrypted_obfuscated_key = base64.b64decode(decrypted_obfuscated_key_b64)

# الخطوة 2: استرجاع المفتاح الأصلي عن طريق XOR مع "0x1337"
chacha_key = bytearray(decrypted_obfuscated_key[i] ^ ord(xor_key[i % len(xor_key)]) for i in range(len(decrypted_obfuscated_key)))

# الخطوة 3: فك تشفير العلم باستخدام ChaCha20 مع المفتاح المسترجع والـ Nonce
nonce = base64.b64decode(nonce_b64)
cipher = ChaCha20.new(key=bytes(chacha_key), nonce=nonce)
decrypted_flag = cipher.decrypt(base64.b64decode(encrypted_flag)).decode('utf-8')

print(f"العلم المسترجع: {decrypted_flag}")
