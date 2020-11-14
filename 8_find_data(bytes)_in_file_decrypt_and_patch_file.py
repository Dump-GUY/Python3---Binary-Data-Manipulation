# Hash of example sample: D087611929584DAA2B23E49F0F081EA8
#This snippet could be used to print or patch decrypted bytes of binary file

#example of decryption routine for mentioned sample (some xor + not routine)
def decrypt_data(encrypted_bytes):
    xor_key = b'f424'
    decrypted_bytes = b""
    for i in encrypted_bytes:  #be careful each byte is process through round as integer, dont want to process null bytes
        if i !=0:              #result of "not" operation "~" is signed int and must be converted to unsigned (& 0xff)
            decrypted_bytes += ((~((((i^xor_key[0])^xor_key[1])^xor_key[2])^xor_key[3])) & 0xff).to_bytes(1, byteorder='big', signed=False)
        else:
            decrypted_bytes += i.to_bytes(1, byteorder='big', signed=False)
    return decrypted_bytes


#open file in read mode and find location of interrest
with open ("C:\\Users\\DFIR_GUY\\Desktop\\ise32\\ise32_xxx.bin","rb") as bin_file:
    Original_file_bytes = bytearray(bin_file.read()) #must be mutable bytearray will be patching bytes

    bin_file.seek(0, 2)  # Seek the end - go to last byte (first argument offset, second argument in seek if 0 start seek from file start offset)
    num_bytes = bin_file.tell()  # Get the file size

    for i in range(num_bytes):          #will be searching whole file for byte pattern
        bin_file.seek(i)             #Now I am in the end of file so go back to the beginning of file binary_file.seek(0)
        eight_bytes = bin_file.read(8) #reading 8 bytes each round from current position in file seek

        #if found matched byte pattern
        if eight_bytes == b"\xc0\xce\xd9\xc5\xce\xc7\x98\x99":  # My byte pattern of interrest - the start of data in file to be decrypted 
            print("Found byte pattern at " + str(i) + " - " + hex(i))
            encrypted_data_size = 800 #how many bytes of interrest to be decrypted           
            bin_file.seek(i)   # Go back to beginning of encrypted data where pattern starts
            encrypted_data = bin_file.read(encrypted_data_size) #read our encrypted 800 bytes
            decrypted_data = decrypt_data(encrypted_data) # decrypt 800 encrypted bytes

            #printing original encrypted and modified decrypted bytes
            print("Original encrypted data size: %d" % len(encrypted_data))
            print("Original encrypted data:\n",encrypted_data)
            print("\nDecrypted data size: %d" % len(decrypted_data))
            print("Decrypted data:\n",decrypted_data)

            #patching original file with decrypted bytes to the same location in file (original encrypted data) save as patched file
            for k in range(i,i+encrypted_data_size,1):#replacing decrypted bytes in original_file_bytes
                Original_file_bytes[k] = decrypted_data[k-i]

            with open ("C:\\Users\\DFIR_GUY\\Desktop\\ise32\\patched_ise32_xxx.bin","wb") as bin_file_patched:
                bin_file_patched.write(Original_file_bytes)

            
