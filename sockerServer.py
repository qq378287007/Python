import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 2080))
s.listen(8)
while True:
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        str = data.decode('ascii')
        print("Receive: " + str)
        conn.send(str.encode("ascii"))
    conn.close()
s.close()
