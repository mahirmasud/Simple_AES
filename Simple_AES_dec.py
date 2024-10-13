from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

# Provided key and IV base
key_base = b'the_enc_key_is_'
iv_base = b'my_great_iv_is_'

# Provide ciphertext
enc = eval(input("Enter the input enc : "))

# Try all possible values for the random byte for both key and IV
for key_byte in range(256):
    for iv_byte in range(256):
        key = key_base + bytes([key_byte])
        iv = iv_base + bytes([iv_byte])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_msg = cipher.decrypt(enc)
        
        try:
            unpadded_msg = unpad(decrypted_msg, 16)
            
            print(f'decrypted_msg = {unpadded_msg.decode()}')
            break
        except ValueError:
            continue
    else:
        continue
    break