#coding:utf-8
import log
from collections import deque
def breadth_frist_search(myobject):
    'search the graph starting by one node using BFS'
    global visited_user_disk
    # global deque_MatchID_disk
    global visited_MatchID_disk
    global deque_user_disk
    
    start_user_point=myobject.start_user
    
    
    
    
    visited_MatchID=myobject.visited_MatchID_disk
    deque_user=myobject.deque_user_disk#上次未完成工作进度,默认从头开始
    visited_user=myobject.visited_user_disk
    deque_MatchID=deque()
    
    start_user_point=myobject.start_user
    deque_user.append(start_user_point)
    
    logging.info('Starting.....')
    n=0
    while len(deque_user)!=0:
        
        current_user_node=deque_user.popleft()
        print 'current_user_node:{name},{times}'.format(name=current_user_node,times=n)
        if current_user_node not in visited_user:
            visited_user.append(current_user_node)
        else:
            print 'some bug!,this words should not be shown!'
            print n
            break
        
        try:
            get_deque_MatchID=find_user_matchIDs(current_user_node)#找到一个user的所有marchIds
            #返回的是一个包含字典的列表，字典中key是matchId，value是本次Id的模式
            if len(get_deque_MatchID)<1:
                '如果返回的数据为空,也就是数据过少'
                logging.info('the data of current user (%s) is small ,so drop it and continue '%(current_user_node))
                continue
        except urllib2.HTTPError,e:
            write_next_init_file('./dat/deque_MatchID.dat',deque_MatchID)
            logging.DEBUG('The server couldn\'t fulfill the request...deque_MatchID saved!')
            print 'The server couldn\'t fulfill the request.'  
            print 'Error code: ', e.code
        except urllib2.URLError, e:
            #log
            print 'We failed to reach a server.'  
            print 'Reason: ', e.reason
        #返回当前用户的matchID
        deque_MatchID.extend(get_deque_MatchID)
        # print '%s 有%s条记录'%(current_user_node,len(get_deque_MatchID))
        # count=0
        # print '已经记录过这些id:',visited_MatchID
        for match in deque_MatchID:#处理当前用户的所有marchid数据
            if match not in visited_MatchID:
                
                find_users,detail_dat=find_mathID_detail(match,current_user_node,myobject)#在函数返回之前，已经更新了统计数据
                if len(detail_dat)!=0:
                    visited_MatchID.append(match)
                    save_detail_on_disk(detail_dat)
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
        # print '%s 有%s条记录'%(current_user_node,len(get_deque_MatchID)+count)
        if n%10==0:
            write_next_init_file('./dat/deque_user.dat',deque_user)
            #write_next_init_file('./dat/deque_MatchID.dat',deque_MatchID)
            write_next_init_file('./dat/visited_MatchID.dat',visited_MatchID)
            write_next_init_file('./dat/visited_user.dat',visited_user)
            logging.info('new deque_user,deque_MatchID,visited_user,visited_MatchID have been recorded')
        n+=1
        if n>1:
            break
        
    return True