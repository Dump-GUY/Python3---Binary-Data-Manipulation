#AES decrypt bytes and decode from base64
from Crypto.Cipher import AES
import codecs

with open('C:\\Users\\xxx\\Desktop\\ANALYZE\\Flare-On7_ALL_Writeup\\FLARE7_CTF\\5_-_TKApp\\Analyze\\Runtime.dll','rb') as enc_file:
    encrypted_bytes = enc_file.read()
#AES decrypt
key = '248e9d7323a1a3c5d5b3283dcb2b40211a14415b6dcd2a86181721fd74b4befd'
iv = '4e6f53616c744f665468654561727468'

cipher = AES.new(bytes.fromhex(key), AES.MODE_CBC, bytes.fromhex(iv))
decrypted_bytes = cipher.decrypt(encrypted_bytes)
#from base64
decoded_bytes = codecs.decode(decrypted_bytes, 'base64')

with open('C:\\Users\\xxx\\Desktop\\xxx.bin','wb') as file_decrypted:
    file_decrypted.write(decoded_bytes)

