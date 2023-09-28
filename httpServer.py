import socket
import gzip
import urllib.parse
import subprocess

def gzip_file(file_name):
    with open(file_name, 'rb') as file:
        bs = file.read()
        value = gzip.compress(bs)
        return value
    
def one_space(cmd: str):
    str_list = cmd.split(' ')
    str_list = [x for x in str_list if x]
    return ' '.join(str_list)

def runCmd(cmd):
    try:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        str = out.decode("gbk")
    except:
        str = "error"
    return str

def deal_first_line(line: str):
    print(f"line: {line}")
    if line == "GET /favicon.ico HTTP/1.1":
        value = gzip_file('favicon.ico')
        str = f"HTTP/1.1 200 OK\r\nAccept-Ranges: bytes\r\nContent-Encoding: gzip\r\nContent-Length: len(value)\r\nContent-Type: image/x-icon\r\n\r\n"
        return str.encode("ascii") + value
    else:
        str = line.split(' ')
        cmd = str[1]
        cmd = cmd[1:]
        cmd = urllib.parse.unquote(cmd)
        cmd = one_space(cmd)
        print(f"cmd: {cmd}")

        str = f"HTTP/1.1 200 OK\r\n\r\n"
        out = runCmd(cmd)
        return (str+out).encode("gbk")

def handle_conn(conn: socket.socket):
    data = conn.recv(1024)
    ascii = data.decode('ascii')
    str = ascii.split('\r\n')
    #for line in str:
    #    print(line)

    line = str[0]
    bs = deal_first_line(line)
    conn.send(bs)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 8080))
s.listen(5)

while True:
    conn, addr = s.accept()
    handle_conn(conn)
    conn.close()

# http://127.0.0.1:8080

