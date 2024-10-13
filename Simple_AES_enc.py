from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from os import urandom
import hashlib

key = b'the_enc_key_is_'
iv = b'my_great_iv_is_'
key += urandom(1)
iv += urandom(1)

cipher = AES.new(key, AES.MODE_CBC, iv)
msg = input("Enter the message : ").encode()
hashs = hashlib.sha256(msg).hexdigest()

msg1 = pad(msg, 16)
enc = cipher.encrypt(msg1)

print(f'enc = {enc}') # bytes object
print(f'hash = {hashs}') # str object
