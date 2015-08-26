from multiprocessing import Process, Queue,Lock,Pool
import time
import random
import os


def produce_number(l,q):
    
    # l.acquire()
    pid=os.getpid()
    while True:
        str_value='pid:{0} ,produce a random number:{1}'.format(pid,random.randint(1,100))
        q.put(str_value)
        time.sleep(2)
    # l.release()
def aaaa(l,q):
    print 'aaaa' 
def main():
    l=Lock()
    dat = Queue()
    pool=Pool(processes=2)
    # pool.apply_async(produce_number, [l,dat])
    p1 = Process(target=produce_number, args=(l,dat,))
    p2 = Process(target=produce_number, args=(l,dat,))
    p3 = Process(target=produce_number, args=(l,dat,))
    p4 = Process(target=produce_number, args=(l,dat,))
    p5 = Process(target=produce_number, args=(l,dat,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    # p1.join()
    # p1.join()
    # p1.join()
    # p1.join()
    while True:
        
        if dat.empty():
            pass
        else:
            print dat.get()
    p1.join()
    p1.join()
    p1.join()
    p1.join()
if __name__ == '__main__':
    main()
