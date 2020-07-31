import socket
import threading

ip = input("请输入ip地址")
port = int(input("请输入端口号"))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_set = set()
s.bind((ip, port))
s.listen(5)
print('人家在等你呀.....')


def tcplink(sock, addr):
    host1, port1 = addr
    print('[%s:%s] 来玩啦...' % addr)
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            print('Client say：' + data)
            senddata = "port " + str(port1) + ": " + data
            sock.send(senddata.encode())
        except:
            socket_set.remove(sock)
            print('[%s:%s] 欢迎再来玩呀!' % addr)
            break
        if data == 'exit' or not data:
            socket_set.remove(sock)
            sock.close()
            print('[%s:%s] 她走了!' % addr)
            break
        else:
            list1 = []
            for i in socket_set:
                if i != sock:
                    list1.append(i)
            for i in list1:
                i.send(data)


while True:
    sock, addr = s.accept()
    socket_set.add(sock)
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
