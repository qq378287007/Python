import time, random
from multiprocessing import Process

def run(name):
    print(f'{name} start')
    time.sleep(random.randrange(1, 5))
    print(f'{name} end')

if __name__ == "__main__":        
    print('main start')

    #必须加,号 
    p1 = Process(target=run, args=('anne', )) 
    p2 = Process(target=run, args=('alice', ))
    p3 = Process(target=run, args=('biantai', ))
    p4 = Process(target=run, args=('haha', ))
    
    #start会自动调用run
    p4.start()
    p1.start()
    p2.start()
    p3.start()
    

    print('main end')
