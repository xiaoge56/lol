#coding:utf-8
import logging
from collections import deque
import urllib2
import parse_dat
def breadth_frist_search(myobject):
    'search the graph starting by one node using BFS'
    
    # start_user_point=myobject.start_user
    
    
     
    print myobject.current_user
    visited_MatchID=myobject.visited_MatchID_disk
    deque_user=myobject.deque_user_disk#上次未完成工作进度,默认从头开始
    visited_user=myobject.visited_user_disk
    deque_MatchID=deque()
    
    start_user_point=myobject.start_user
    deque_user.append(start_user_point)
    
    # print 'visited_MatchID:',visited_MatchID
    # print 'visited_user:',visited_user
    # print 'deque_user:',deque_user
    
    logging.info('Starting.....')
    n=0
    while len(deque_user)!=0:
        
        myobject.current_user=deque_user.popleft()
        # print 'myobject.current_user:{name},{times}'.format(name=myobject.current_user,times=n)
        if myobject.current_user not in visited_user:
            visited_user.append(myobject.current_user)
            
        else:
            print 'some bug!,this words should not be shown!'
            print n
            break
        
        try:
            get_deque_MatchID=parse_dat.find_user_matchIDs(myobject.current_user)#找到一个user的所有marchIds
            #返回的是一个包含字典的列表，字典中key是matchId，value是本次Id的模式
            if len(get_deque_MatchID)<1:
                '如果返回的数据为空,也就是数据过少'
                logging.info('the data of current user (%s) is small ,so drop it and continue '%(myobject.current_user))
                continue
        except urllib2.HTTPError,e:
            myobject.write_next_init_file('./dat/deque_MatchID.dat',deque_MatchID)
            logging.DEBUG('The server couldn\'t fulfill the request...deque_MatchID saved!')
            print 'The server couldn\'t fulfill the request.'  
            print 'Error code: ', e.code
        except urllib2.URLError, e:
            #log
            print 'We failed to reach a server.'  
            print 'Reason: ', e.reason
        #返回当前用户的matchID
        
        deque_MatchID.extend(get_deque_MatchID)
        # print '%s 有%s条记录'%(myobject.current_user,len(get_deque_MatchID))
        # count=0
        # print '已经记录过这些id:',visited_MatchID
        for match in deque_MatchID:#处理当前用户的所有marchid数据
            if match not in visited_MatchID:
                
                find_users,detail_dat=parse_dat.find_mathID_detail(match,myobject.current_user,myobject)#在函数返回之前，已经更新了统计数据
                
                if len(detail_dat)!=0:
                    visited_MatchID.append(match)
                    myobject.save_detail_on_disk(detail_dat)
                else:
                    break
                for user in find_users:
                    
                    if user not in visited_user and user not in deque_user:
                        #出现问题，会有重复的user_id出现在deque_user中，原因是，vistied_user由于每次只添加一个，更新速度慢
                        deque_user.append(user)
            # else:
                # count+=1
                # print '已经记录过了1次,当前的matchid是:',match
                # print 'deque_user:',deque_user
        # print '%s 有%s条记录'%(myobject.current_user,len(get_deque_MatchID)+count)
        
        
        break
        myobject.write_next_init_file('./dat/deque_user.dat',deque_user)
        #write_next_init_file('./dat/deque_MatchID.dat',deque_MatchID)
        myobject.write_next_init_file('./dat/visited_MatchID.dat',visited_MatchID)
        myobject.write_next_init_file('./dat/visited_user.dat',visited_user)
        logging.info('new deque_user,deque_MatchID,visited_user,visited_MatchID have been recorded')

        
    return True