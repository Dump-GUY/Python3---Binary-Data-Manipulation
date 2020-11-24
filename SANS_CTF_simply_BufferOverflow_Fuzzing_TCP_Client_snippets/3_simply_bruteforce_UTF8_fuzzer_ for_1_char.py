#simply bruteforce UTF-8 fuzzer for 1 char - with hitting the right char we get different output from server and we can continue with next char...
import socket

for i in range(0,256):
    host = "F05-target.allyourbases.co"
    port =  8035                
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = s.recv(1024)
    print('Received', repr(data))
    push_bytes = b"\xac\xcd\xfc"#these bytes we already know
    push_bytes += i.to_bytes(1, byteorder='big', signed=False)
    push_bytes += b"\x0a"
    print("Pushed char: ",push_bytes)

    s.sendall(push_bytes)
    data = s.recv(1024)
    print('Received', repr(data))
    s.close()
