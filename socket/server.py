import socket   
 
s = socket.socket()  
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 12345  
s.bind((host, port)) 
#s.bind(('localhost',6999))

s.listen(5) 

while True:
    conn, addr = s.accept()  
    print(f'accepted {conn} from {addr}')
    print(f'peername: {conn.getpeername()}')
    conn.send('欢迎访问菜鸟教程！'.encode('utf-8'))
    conn.close() 

s.close()
    