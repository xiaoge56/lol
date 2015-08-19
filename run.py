#coding:utf-8
import io
from bfs import breadth_frist_search
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def main():
	
	init=io.MyInit()
	choice_start_user=init.start_user
	print choice_start_user
	breadth_frist_search(init)
	print 'end'
	
if __name__=='__main__':
        main()
