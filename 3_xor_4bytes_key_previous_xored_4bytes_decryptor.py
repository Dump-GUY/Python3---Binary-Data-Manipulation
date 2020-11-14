
data = b'\x01\x09\x1f\xe4\x64\x29\x75\x81\x44\x44\x00\xeb\x64\x37\x6b\x99\x1d\x43\x96\xb9\x69\x26\xee\xcd\x49\x07\xcf\xec'

xored_bytes = bytes()
pomocna = int()
for x in range(0,len(data),4):
    pomocna = int.from_bytes(data[x:x+4], byteorder='big', signed=False)
    if x == 0:
        xored_bytes += (pomocna^0x55667788).to_bytes(4, byteorder='big', signed=False) 
    else:
        pomocna2=int.from_bytes(data[x-4:x], byteorder='big', signed=False)
        xored_bytes += (pomocna^pomocna2).to_bytes(4, byteorder='big', signed=False)
    
print(xored_bytes.decode('latin1'))