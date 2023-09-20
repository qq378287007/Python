
import subprocess


def runCmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out.decode("gbk")

cmd = "ipconfig"
cmd = "ls"
cmd = "hello.exe"
cmd = "ping"

try:
    str = runCmd(cmd)
except:
    str = "error"
print(str)
