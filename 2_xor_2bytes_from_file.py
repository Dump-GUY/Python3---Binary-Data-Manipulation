with open("C:\\Users\\xxx\\Downloads\\xxx.txt", "rb") as binary_file:
    # read text or bytes from the file
    data = binary_file.read()

xored_bytes = bytes()
pomocna = int()
for x in range(0,len(data),2):
    pomocna = int.from_bytes(data[x:x+2], byteorder='big', signed=False)
    xored_bytes += (pomocna^0x5566).to_bytes(2, byteorder='big', signed=False) 
    

with open("C:\\Users\\xxx\\Downloads\\xxx3.txt", "wb") as binary_file2:
    # Write bytes to the file
    binary_file2.write(xored_bytes)