#api decryption for sample:  MD5: d087611929584daa2b23e49f0f081ea8 
#ref:https://www.virustotal.com/gui/file/a41c908e8d7317062bd40401fad9e08433596dc8ecc0e27845ab35c651c63a18/details

import ida_bytes

#decryption of encrypted bytes
def decrypt_data(encrypted_bytes):
    xor_key = b'f424'
    decrypted_bytes = b""
    for i in encrypted_bytes:  #be careful each byte is process through round as integer, dont want to process null bytes
        if i !=0:              #result of "not" operation "~" is signed int and must be converted to unsigned (& 0xff)
            decrypted_bytes += ((~((((i^xor_key[0])^xor_key[1])^xor_key[2])^xor_key[3])) & 0xff).to_bytes(1, byteorder='big', signed=False)
        else:
            decrypted_bytes += i.to_bytes(1, byteorder='big', signed=False)
    return decrypted_bytes



start_address = 0x405068 #start address of encrypted bytes
end_address = 0x405388 #end address of encrypted bytes
size = end_address - start_address #size of encrypted bytes
original_bytes = ida_bytes.get_bytes(start_address,size) #getting all encrypted bytes
decrypted_bytes = decrypt_data(original_bytes)
ida_bytes.patch_bytes(start_address,decrypted_bytes) #patching original bytes with decrypted bytes

print("Bytes decrypted - start address: 0x%x" %(start_address))

