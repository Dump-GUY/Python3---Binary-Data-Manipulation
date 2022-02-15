#decoder for sample RE 610 - "9.exe" - 5.day MD5hash:a5a5ed26f73d974ade21f9a215a124d5
import malduck
hexblob = "0000000000000000000000000000000043A33A07D1799713918917139171987381719803C1D11953897936C6799119F2334336967371B0378300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000043A33A07D1799713918917139171987381719803C1D11953897936C6799119F23343B696130BB7E20B9B380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000043A33A07D1799713918917139171987381719803C1D11953897936C6799119F23343BB374B233797710BB9070000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009052EE3EC980FD43"
hexblobbytes = bytes.fromhex(hexblob)
key= "CSOL" #key is rotating char after char
length = 408 #length of hexblob
decodedbytes = bytearray()
decodedbytes2 = bytearray()
for i in range(0,length,1):
    pomocna1 = ord(key[i%4])
    pomocna2 = hexblobbytes[i]
    pomocna3 = malduck.ror(hexblobbytes[i],ord(key[i%4]),8)
    decodedbytes+= int.to_bytes(pomocna3,1,byteorder="big",signed=False)

for i in decodedbytes:
    if i != 0:
        decodedbytes2 += int.to_bytes(i,1,byteorder="big",signed=False)
print(decodedbytes2)