import socket
import subprocess

'''
cmd = "ipconfig"
cmd = "ls"
cmd = "hello.exe"
cmd = "ping"
'''
def runCmd(cmd):
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        str = out.decode("gbk")
    except:
        str = "error"
    return str

def handle_client(client: socket.socket):
    request = client.recv(1024)
    data = request.decode("gbk") #str.encode("utf-8")
    print(f"receive:\n{data}\n")
    str = data.split('\r\n')
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
    client.send(data) #bytes.decode("gbk")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口复用
s.bind(("127.0.0.1", 8080))  # 绑定端口
s.listen(5)  # 等待客户端连接

while True:
    client, addr = s.accept()
    #print(f"{client} : {addr}\n")
    handle_client(client)
    client.close()

#curl http://127.0.0.1:8080/ping
#curl http://127.0.0.1:8080/ipconfig


