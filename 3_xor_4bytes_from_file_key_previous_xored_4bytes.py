with open("C:\\Users\\xxx\\Downloads\\Python_scripts_byteOperations\\xxx.txt", "rb") as binary_file:
    # read text or bytes from the file
    data = binary_file.read()

xored_bytes = bytes()
pomocna = int()
for x in range(0,len(data),4):
    pomocna = int.from_bytes(data[x:x+4], byteorder='big', signed=False)
    if x == 0:
        xored_bytes += (pomocna^0x55667788).to_bytes(4, byteorder='big', signed=False) 
    else:
        pomocna2=int.from_bytes(xored_bytes[x-4:x], byteorder='big', signed=False)
        xored_bytes += (pomocna^pomocna2).to_bytes(4, byteorder='big', signed=False)
    

with open("C:\\Users\\xxx\\Downloads\\Python_scripts_byteOperations\\xxx4.txt", "wb") as binary_file2:
    # Write bytes to the file
    binary_file2.write(xored_bytes)