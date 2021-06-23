#Python3 snippet - Encrypting/Decrypting AES256 ECB with PKCS7 Padding
#rfc2898derivekey-HMACSHA1 for AES Key derivation

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA1
import malduck

Password = malduck.base64.decode('UGFzc3dvcmQ=')
Salt = malduck.unhex("0102030405060708")

#rfc2898derivekey-HMACSHA1,10 iterations, 32B length (IV not used in AES ECB mode)
def Derive_key(Password, Salt):
    derive_bytes = PBKDF2(Password, Salt, 32, count=10, hmac_hash_module=SHA1)
    return(derive_bytes)


def decrypt_AES(Aes_key, Encrypted_data):
    decrypted_data = malduck.crypto.aes.ecb.decrypt(Aes_key, Encrypted_data)
    return (malduck.unpad.pkcs7(decrypted_data))    #return pkcs7 unpad decrypted data

def encrypt_AES(Aes_key, data):
    data_padded = malduck.pad.pkcs7(data,32)    #padding pkcs7
    return (malduck.crypto.aes.ecb.encrypt(Aes_key, data_padded))

Aes_key = Derive_key(Password,Salt)

Test_data = b'This is Test !!!1234'
Encrypted_Data = encrypt_AES(Aes_key, Test_data)
Decrypted_Data = decrypt_AES(Aes_key, Encrypted_Data)

print("AES KEY: "+ Aes_key.hex())
print("Test DATA:",Test_data)
print("Encrypted Data: " + Encrypted_Data.hex())
print("Decrypted Data:",Decrypted_Data)



