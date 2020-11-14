with open("C:\\Users\\xxx\\Downloads\\xxx.txt", "rb") as binary_file:
    # read text or bytes from the file
    data = binary_file.read()

File_bytes = data
xored_bytes = bytes()
for x in File_bytes:
   xored_bytes += (x^0x55).to_bytes(1, byteorder='big', signed=False) 

with open("C:\\Users\\xxx\\Downloads\\xxx2.txt", "wb") as binary_file2:
    # Write bytes to the file
    binary_file2.write(xored_bytes)
