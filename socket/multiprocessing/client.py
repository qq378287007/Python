from socket import *

client = socket()
ip_port = ("127.0.0.1", 8001)
client.connect(ip_port)

while 1:
    inp = input(">>:").strip()
    if not inp: 
        continue
    if inp.upper() == "Q": 
        break
    
    client.send(inp.encode('utf-8'))
    from_server_msg = client.recv(1024)
    print("来自服务端的消息:", from_server_msg.decode('utf-8'))
    
client.close()