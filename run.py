#coding:utf-8
import io
from bfs import breadth_frist_search
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def main():
	
	init=io.MyInit()
	breadth_frist_search(init)
	print init.count_dat
	
if __name__=='__main__':
        main()
# http://www.55bl.com/thread-646-1-1.html
# http://bayes.wustl.edu/etj/prob/book.pdf