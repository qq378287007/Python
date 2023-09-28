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
    p1 = Run('anne')
    p2 = Run('alex')
    p3 = Run('ab')
    p4 = Run('hey')
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('main end')
