import socket
from multiprocessing import Process

def main_link():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect(('127.0.0.1', 8888))
        bs = sock.recv(1024)
        
    except Exception as e:
        print(e)
        sock.close()

def help_link():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect(('127.0.0.1', 9999))
        bs = sock.recv(1024)
        
    except Exception as e:
        print(e)
        sock.close()

if __name__ == '__main__':
    #p = Process(target=help_link)
    #p.daemon = True  # daemon True设置为守护即主死子死.
    #p.start()
    
    main_link()