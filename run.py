#coding:utf-8
import io
from bfs import breadth_frist_search
def main():
	init=io.MyInit()
	choice_start_user=init.start_user
	breadth_frist_search(init)
	
	print choice_start_user
if __name__=='__main__':
	main()