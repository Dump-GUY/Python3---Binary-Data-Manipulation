from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto.Random import get_random_bytes

key = b'Password123'
#nonce = get_random_bytes(16)
tempkey = SHA.new(key).digest()
cipher = ARC4.new(tempkey)
msg = cipher.encrypt(b'This is my supersecret RC4 encrypted text!')

print('RC4 encrypted message:', msg.hex())


message = '20de1207fb5b4458d38778f19f36864732514bb02cf49b09bcc1d88af91885ca6a950925c41fb3a2dca1'
key = b'Password123'
#nonce = get_random_bytes(16)
tempkey = SHA.new(key).digest()
cipher = ARC4.new(tempkey)
msg = cipher.decrypt(bytes.fromhex(message))

print('RC4 decrypted message:',msg.decode('utf-8'))

