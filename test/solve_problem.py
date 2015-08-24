#coding:utf-8

def find_max_path(p1,p2):
	m,n=0,0
	M=[[0 for x in range(10)] for y in range(10)]
	print M
	for x in range(10):
		M[0,x]=1 
		M[x,0]=1 
	print M
	M[0,0]=0
	for x in range(1,10):
		for y in range(1,10):
			M[x,y]=M[x-1,y]+M[x,y-1]
	return M[p1,p2]

print find_max_path(3,4)		