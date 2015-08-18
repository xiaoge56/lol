#coding:utf-8
import io
from bfs import breadth_frist_search
def main():
	print 'a'
	init=io.MyInit()
	choice_start_user=init.start_user
	breadth_frist_search(init)
	
	
if __name__=='__main__':
        main()
