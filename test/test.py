from multiprocessing import Process,Queue
import os
import time


def f(q1,q2):

    q2.put([1,2,3])
    print 'aaabbbbb'    
    print 'q value {1} ,current process id:{0}'.format(os.getpid(),q1.get())
 
    print '\\\\'
if __name__ == '__main__':
    q1=Queue()
    q2=Queue()
    q1.put([1,2,3])
    m=[1,2,3]
    
    print 'q put in the main process pid:{0}'.format(os.getpid())
    p = Process(target=f, args=(q1,q2))
    
    p.start()
    print q1.qsize()
    p.join()
    help(q2.get)
