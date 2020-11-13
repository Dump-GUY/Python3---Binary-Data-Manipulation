#shitty xor encrypt example
super_secret = b"This is my super secret pass!!" #bytes representation of string
Xor_key = b"XO"

encrypted_supersecret = bytes()

for i in range(0,len(super_secret),2):#2 bytes of supe_secret processed each round
    integer_from_bytes2_fromSS_LE = int.from_bytes(super_secret[i:i+2], byteorder='little', signed=False)#2 bytes coverted to int little endian
    xored_integer_value = integer_from_bytes2_fromSS_LE ^ int.from_bytes(Xor_key, byteorder='big', signed=False)
    xored_integer_value_shifted = xored_integer_value << 1 #shifting
    encrypted_supersecret += (xored_integer_value_shifted).to_bytes(2, byteorder='big', signed=False)

print(encrypted_supersecret)
print(encrypted_supersecret.hex())


#shitty xor decrypt example (must be in reverse order)
encrypted_hexstring = "6036564c62def078424456de5074545456de76547a7af076727e5678f2dc"
encrypted_hexstring_to_bytes = bytes.fromhex(encrypted_hexstring)
Xor_key = b"XO"
decrypted_supersecret = bytes()
for i in range(0,len(encrypted_hexstring_to_bytes),2):
    integer_from_encrypted_hexstring_to_bytes2 = int.from_bytes(encrypted_hexstring_to_bytes[i:i+2], byteorder='big', signed=False)#2 bytes coverted to int big endian
    integer_value_shifted = integer_from_encrypted_hexstring_to_bytes2 >> 1 #shifting
    dexored_integer_value_shifted = integer_value_shifted ^ int.from_bytes(Xor_key, byteorder='big', signed=False)
    decrypted_supersecret += (dexored_integer_value_shifted).to_bytes(2, byteorder='little', signed=False)

print(decrypted_supersecret)