import os
from socket import *
from multiprocessing import Process


def talk(conn):
    while 1:
        try:
            from_client_msg = conn.recv(1024)
            if not from_client_msg:
                break
            str = from_client_msg.decode('utf-8')
            print("进程<%s>来自客户端的消息:%s" %(os.getpid(), str))
            conn.send(str.upper().encode('utf-8'))
        except:
            conn.close()
            break

if __name__ == '__main__':
    server = socket()
    ip_port = ("127.0.0.1", 8001)
    server.bind(ip_port)
    server.listen(5)
    while True:
        try:
            conn, addr = server.accept()
            p = Process(target=talk, args=(conn,))
            p.daemon = True  # daemon True设置为守护即主死子死.
            p.start()
        except Exception as e:
            print(e)
            server.close()