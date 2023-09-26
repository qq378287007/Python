import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 1111))
s.listen(8)
while True:
    conn, addr = s.accept()
    print(f"Remote Addr: {addr}")
    
    data = conn.recv(1024)
    if not data:
        print("Empty Data")
        continue
    
    str = data.decode('ascii')
    lines = str.split('\r\n')
    for line in lines:
        print(line)
            
    response_content = "hello world"
    response_headers = f"HTTP/1.1 200 OK\r\nContent-Length: {len(response_content)}\r\n\r\n"
    response = response_headers + response_content
    
    first_line = lines[0]
    if first_line == "GET /favicon.ico HTTP/1.1":
        conn.send("HTTP/1.1 300 error\r\nContent-Length: 5\r\n\r\nerror".encode("ascii"))
    else:
        conn.send(response.encode("ascii"))
    conn.close()
s.close()
