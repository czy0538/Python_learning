import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1'), 5005)
while True:
    data, addr = s.recvfrom(1024)
    if not data:
        print('client has exited!')
        break
    print('receoved:', data, 'from', addr)
s.close()

