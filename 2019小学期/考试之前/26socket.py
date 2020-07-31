import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',5005))
while True:
    data,addr=s.recvfrom(1024)
    if not data:
        print("error")
        break
    print(data,addr)
s.close()

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port=5050
host="127.0.0.1"
while True:
    msg=input()
    if not msg:
        break
    s.sendto(msg.encode("utf-8"),(host,port))
s.close()