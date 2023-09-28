import os, time
import random
from multiprocessing import Lock, Process

def work(lock):
    lock.acquire()
    print(f'{os.getpid()} start')
    time.sleep(random.randrange(3, 7))
    print(f'{os.getpid()} end')
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(33):
        p = Process(target=work, args=(lock, ))
        p.start()