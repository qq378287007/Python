import time, random
from multiprocessing import Process

class Run(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print(f'{self.name} start')
        time.sleep(random.randrange(1, 5))
        print(f'{self.name} end')

if __name__ == "__main__":        
    print('main start')
    
    '''
    p1 = Run('anne')
    p2 = Run('alex')
    p3 = Run('ab')
    p4 = Run('hey')
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join() #等待p1进程停止
    p4.join()
    p3.join()
    p2.join()
    '''
    ps = []
    for name in ['anne', 'alex', 'ab', 'hey']:
        ps.append(Run(name))
    for p in ps:
        p.start()
    for p in ps:
        p.join()
        
    print('main end')
