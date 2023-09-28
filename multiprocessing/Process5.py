import time
from multiprocessing import Process

def foo():
    print(123)
    time.sleep(3)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

def main():
    p1 = Process(target=foo)
    p1.daemon = True
    p1.start()
    
    p2 = Process(target=bar)
    p2.start()
    
    time.sleep(1)
    print("main-------") 

if __name__ == '__main__':
    main()