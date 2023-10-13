import socket
from multiprocessing import Process

main_conns = []

def main_link():
    global main_conns
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 8888))
    sock.listen(10)
    while True:
        try:
            conn, addr = sock.accept()
            main_conns.append(conn)
            print("main_link connect from", addr)
            #print(f'ip: {addr[0]}, port: {str(addr[1])}')
            
            
            #ip, port = conn.getpeername()
            #print(f'ip: {ip}, port: {port}')
        except Exception as e:
            print(e)
            conn.close()
            main_conns.remove(conn)
        

def help_link():
    global main_conns
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 9999))
    sock.listen(10)
    while True:
        try:
            conn, addr = sock.accept()
            print("help_link connect from", addr)
            ip = addr[0]
            port = str(addr[1])
            ip_port = ' '.join([ip, port])
            
            for client in main_conns:
                client.send(ip_port.encode('utf-8'))
        except Exception as e:
            print(e)
            conn.close()    

if __name__ == '__main__':
    p = Process(target=help_link)
    p.daemon = True  # daemon True设置为守护即主死子死.
    p.start()
            
    main_link()