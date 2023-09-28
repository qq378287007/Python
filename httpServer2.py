import socket
import subprocess

'''
cmd = "ipconfig"
cmd = "ls"
cmd = "hello.exe"
cmd = "ping"
netstat -an
tasklist
'''
def runCmd(cmd):
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        str = out.decode("gbk")
    except:
        str = "error"
    return str

def handle_conn(conn: socket.socket):
    '''
    data = b''
    while True:
        recv_data = conn.recv(1024)
        if not recv_data:
            break
        data += recv_data
    '''
    data = conn.recv(1024 * 2)
    #data = request.decode("gbk") #str.encode("utf-8")
    ascii = data.decode('ascii') #解码
    str = ascii.split('\r\n')
    #print("receive:\n")
    for line in str:
        print(line)
    conn.send("HTTP/1.1 200 OK\r\bServer: python\r\n\r\nreceive".encode("ascii"))
    '''
    request_start_line = str[0]
    #print(f"request_start_line:\n\t{request_start_line}\n")
    tmp = request_start_line.split(' ')
    cmd = tmp[1]
    cmd = cmd[1:]
    #print(f"cmd:\n\t{cmd}\n")

    response_start_line = "HTTP/1.1 200 OK\r\b"
    response_headers = "Server: python\r\nName: mali\r\n"
    if cmd == "favicon.ico":
        response_text = ""
    else:
        response_text = runCmd(cmd)

    response = response_start_line + response_headers + "\r\n" + response_text
    data = bytes(response, "gbk")
    #print(f"send:\n{data}\n")
    conn.send(data) #bytes.decode("gbk")
    '''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口复用
s.bind(("127.0.0.1", 8080))  # 绑定端口
s.listen(5)  # 等待客户端连接

while True:
    conn, addr = s.accept()
    #print(f"{conn} : {addr}\n")
    handle_conn(conn)
    conn.close()

#curl http://127.0.0.1:8080/ping
#curl http://127.0.0.1:8080/ipconfig