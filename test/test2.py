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

def c():
	m=1
	s=2
	f()
def f():
	a=100
	c='x'
	1/0

try:
    c()
except:
	

	tb = sys.exc_traceback
	
	# print traceback.print_tb(tb_last)
	while tb.tb_next:
		tb=tb.tb_next
	for key in tb.tb_frame.f_locals:
		print 'the value of variable {0} is {1} '.format(key,tb.tb_frame.f_locals[key])

	# print exc_type,exc_value
	# print traceback.tb_lineno(tb)
	# print '|'
	# help(sys.exc_info())
	# # print help(tb)
	# # if tb is not None:
	# # 	prev=tb
	# # 	curr=tb.tb_next
	# # 	while curr is not None:
	# # 		prev=curr
	# # 		curr=curr.tb_next
	# # 		print prev.tb_frame.f_locals
    # # if tb is not None:
	#    prev = tb
    #    curr = tb.tb_next
    #    while curr is not None:
    #         prev = curr
    #         curr = curr.tb_next
    #    print prev.tb_frame.f_locals