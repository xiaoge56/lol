import Queue
import threading
import urllib2
import time

hosts = ["http://hao123.com", "http://360.com", "http://baidu.com",
"http://ibm.com", "http://apple.com"]


class ThreadUrl(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		a=self.getname()


def main():
	print 'v'
	queue = Queue.Queue()
	for i in range(5):
		t = ThreadUrl(queue)
		# t.setDaemon(True)
		t.start()
    
	for host in hosts:
		queue.put(host)
	print 'a'
 	queue.join()
if __name__=='__main__':
	start = time.time()
	print start
	main()
	print "Elapsed Time: %s" % (time.time() - start)
