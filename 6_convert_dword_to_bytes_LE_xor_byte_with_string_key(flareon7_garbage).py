#example of dexoring from Flareon7 challenge 2 Garbage - FLAG

string_key_bytes = b"nPTnaGLkIqdcQwvieFQKGcTGOTbfMjDNmvibfBDdFBhoPaBbtfQuuGWYomtqTFqvBSKdUMmciqKSGZaosWCSoZlcIlyQpOwkcAgw "
dword_list_in_decimal = [741548835,1231306510,67771914,436344355,604530244,745804082,255995178,224677950,387646557,84096534,134815796,237248867,1479808021,981018906,1482031104,84]
My_bytearray = bytearray()

#converting each dword/int little endian from list to bytearray
for i in dword_list_in_decimal:
    My_bytearray += i.to_bytes(4,"little",signed=False)

#xoring converted bytearray with string_key_bytes

for k in range(0,len(My_bytearray)):
    My_bytearray[k] = My_bytearray[k] ^ string_key_bytes[k] 

print(My_bytearray)