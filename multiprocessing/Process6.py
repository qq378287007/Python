import os, time
import random
from multiprocessing import Process

def work():
    print(f'{os.getpid()} start')
    time.sleep(random.randrange(3, 7))
    print(f'{os.getpid()} end')

if __name__ == '__main__':
    for i in range(33):
        p = Process(target=work)
        p.start()