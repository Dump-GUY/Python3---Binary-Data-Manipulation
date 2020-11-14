#examples of some data type manipulation and conversion - basic

#strings
string1 = "This is string"
string2 = '''
example of
another
string
'''
string3 = "\x54\x68\x69\x73\x20\x69\x73\x20\x73\x74\x72\x69\x6e\x67"
string4 = chr(84) + chr(104) + chr(105) + chr(115) + chr(32) + chr(105) + chr(115) + chr(32) + chr(115) + chr(116) + chr(114) + chr(105) + chr(110) + chr(103)# from int to char --> string

#string to bytes/bytearray
bytes1 = string1.encode("utf-8")
bytes2 = string1.encode()#default utf-8
bytes3 = b"This is string" #bytes representation of string
bytes4 = bytes(string3, 'utf-8')
bytearray1 = bytearray(string1, 'utf-8')
bytes5 = bytes.fromhex("5468697320697320737472696e67")#from hexstring to bytes

#string from bytes/bytearray
hexstring5 =  (b'\x54\x68\x69\x73\x20\x69\x73\x20\x73\x74\x72\x69\x6e\x67').hex() # convert bytes to hexstring
hexstring5 = hex(11368) #converts from integer to hexstring with 0x prefix
string6 = bytes1.decode()
string7 = bytes1.decode("utf-8")
string8 = bytearray1.decode("utf-8")
string9 = bytearray1.decode()


#bytes - immutable and bytearrays - mutable
bytes6 = b"These are bytes"#bytes representation of string
bytearray2 = bytearray("This string becomes bytearray in utf-8","utf-8")
bytearray3 = bytearray(bytes6) #converting bytes to bytearray
bytes7 = bytes(bytearray2)#converting bytearray to bytes
bytes8 = b'\x54\x68\x69\x73\x20\x69\x73\x20\x73\x74\x72\x69\x6e\x67'
bytes9 = bytes([65, 66, 67])#from list of integers to bytes
bytearray4 = bytearray([65, 66, 67])#from list of integers to bytearray
bytes10 = (165000).to_bytes(4, byteorder='big', signed=True)#integer to 4bytes

#integers
a = 65
b = 0x41
c = ord("A")#from char to int
d = int.from_bytes(b'\x41\x41\x41\x41', byteorder='big', signed=True)#from bytes to integer
e = int.from_bytes([65, 65, 65], byteorder='little',signed=False)
f = int(65.22)#from float to integer
g = int("deadbeef", 16)#convert from hex string to int
h = int("0xff", 16)#convert from hex string to int


#some list routines
list_of_integers = [104,101,108,108,111]
list_of_chars = ['h','e','l','l','o']
list_of_strings = ['hello','hello','hello'] 

#converting list of integers to list of chars
list_of_chars2 = []
for i in list_of_integers:
    list_of_chars2 += chr(i) # possible list_of_chars2.append(chr(i))

#converting list of integers to bytes/bytearray
bytes11 = bytes(list_of_integers)
bytearray4 = bytearray(list_of_integers)

#converting list of chars to list of integers
list_of_integers2 = []
for c in list_of_chars:
    list_of_integers2.append(ord(c))
    
#converting list of chars to bytes/bytearray
bytes12 = bytes()
for c in list_of_chars:
    bytes12 += c.encode()

#converting list of chars to string
string10 = ""
for c in list_of_chars:
    string10 += c

string11 = ""
string11 = ("").join(list_of_chars)

#converting bytes to list of integers - each round 4 bytes converted to integer
list_of_integers3 = []
bytes13 = b"\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64\x2c\x20\x63\x6f\x76\x69\x64\x20\x73\x75\x63\x6b\x73"
for i in range(0,len(bytes13),4):
    list_of_integers3.append(int.from_bytes(bytes13[i:i+4], byteorder='big', signed=False))

#tuple example - something like read-only list of diferent types
My_tuple1 = ("hello", 126 , 33.25,b"\x41\x41")
My_tuple2 = (My_tuple1[0],My_tuple1[3])
bytes14 = My_tuple1[3]
string11,integer1,float1,bytes15 = My_tuple1

