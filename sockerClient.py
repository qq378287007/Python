import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("127.0.0.1", 2080))
#s.connect(("192.168.234.129", 2080))
#s.connect(("172.17.0.3", 2080))
s.connect(("192.168.234.129", 2080))
while True:
    str = input("Send: ")
    if str == "exit":
        break
    s.send(str.encode("ascii"))
    data = s.recv(1024)
    str = data.decode('ascii')
    print("Receive: " + str)
s.close()
