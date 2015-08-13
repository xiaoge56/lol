import traceback  
import sys
# a=0
# b=1
# def call1(a,b):
# 	print 'call1'
# 	return divison(a,b)
# def divison(a,b):
# 	return a/b
# try:	
# 	s=call1(b,a)
# 	print s
# except Exception, err:
# 	print '----'
# 	print traceback.format_exc()
#     #or
# 	print sys.exc_info()[0]
# 	print '----'
# 	traceback.print_last()



def f():
	a=100
	c='x'
	1/0

try:
    f()
except:
	print 'wdasd'
	exc_type,exc_value,tb = sys.exc_info()
	print tb
	if tb is not None:
		prev=tb
		curr=tb.tb_next
		while curr is not None:
			prev=curr
			curr=curr.tb_next
			print prev.tb_frame.f_locals
    # if tb is not None:
	#    prev = tb
    #    curr = tb.tb_next
    #    while curr is not None:
    #         prev = curr
    #         curr = curr.tb_next
    #    print prev.tb_frame.f_locals