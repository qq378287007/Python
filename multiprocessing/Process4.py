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
    
    p = Run('anne')
    p.daemon = True
    p.start()
    
    time.sleep(random.randrange(1, 5))
    print('main end')
