#coding:utf-8
from collections import deque
import logging
import sys

blink='\n'
visited_MatchID=[]
visited_user=[]
deque_user=deque()
deque_MatchID=deque()

def init_choice():
    global deque_user
    user_point=deque_user.popleft()
    return user_point
def usr_info_spider(user_point):
    '''
    do spider and save the data
    '''
    return user_point.neighbours
def compute_undirect_graph(graph,user,neighbours):
    'construct a undirect graph of user_point info'
    if user not in graph.keys():
        if len(neighbours)!=0:
            for neighbour in neighbours:
                graph[user].add()
    else:
        for neighbour in neighbours:
                graph[user].add(neighbour)

    
def breadth_frist_search(start_user_point):
    'search the graph starting by one node using BFS'
    global visited_user
    global deque_MatchID
    global visited_MatchID
    global deque_user
    
    
    deque_user.append(start_user_point)

    logging.info('Starting.....')
    while len(deque_user)!=0:
        
        pre_deal_user=deque_user.popletf()
        visited_user.append(pre_deal_user)

        try:
            deque_MatchID=find_user_marchIDs(pre_deal_user)
        except HTTPError, e:
            write_next_init_file('./dat/deque_MatchID.dat',deque_MatchID)
            logging.DEBUG('The server couldn\'t fulfill the request...deque_MatchID saved!')
            print 'The server couldn\'t fulfill the request.'  
            print 'Error code: ', e.code
            
        except URLError, e:
            #log
            print 'We failed to reach a server.'  
            print 'Reason: ', e.reason
        
        for match in deque_MatchID:
            find_users,detail_dat=find_mathID_detail(match)
            save_detail_on_disk(detail_dat)
            
            for user in find_users:
                if user not in visited_user:
                    user_sequence.append(user)
            
    return True
def save_detail_on_disk(detail_dat):
    global blink
    try:
        with open('./dat/user.dat','a') as f:
            for line in detail_dat:
                f.write(line+blink)
    except IOError,msg:
        print msg
        logging.DEBUG('./dat/user.dat can not open!')
        
def init_read_file(path,result):
    'reading the last time record when continue to do work'

    
    name=path.split(r'/')[-1]
    
    with open(path) as f:
        for line in f:
            result.append(line.split()[0])
    if len(result)!=0:
        logging.info('%s inited ok'%name)
    else:
        logging.info('%s is None!!'%name)
        
def write_next_init_file(path,content_list):
    'write next time init info '
    
    global blink

    
    with open(path,'a+') as f:
        for line in content_list:
            f.write(line+blink)
    #log
def init_dat():
    'init history dat:visited_user,deque_user,visited_MatchID,deque_MatchID'

    global visited_user
    global visited_MatchID
    global deque_user
    global deque_MatchID
    
    #with open('./dat/visited_user.dat','r') as f:
     #   for line
     #   visited_user=f.read()
    logging.info('/*----begin to init data----*/')

    init_read_file('./dat/visited_user.dat',visited_user)
    init_read_file('./dat/visited_MatchID.dat',visited_MatchID)
    init_read_file('./dat/deque_user.dat',deque_user)
    init_read_file('./dat/deque_MatchID.dat',deque_MatchID)

    logging.info('initing user queue..')
    logging.info('%d users have been done'% len(visited_user))
    logging.info('the current lengh of user_sequence is %d'% len(deque_user))
    logging.info ('%d matches have been recorded'% len(visited_MatchID))
    logging.info('the current lengh of deque_MatchID is %d'% len(deque_MatchID))
    logging.info('/*-----------------------------------*/')
def main():

    
    logging.basicConfig(
    filename='mylog.log',
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S'
    )
    
    init_dat()
    logging.info('init_dat ok... ')
    
    start_user_point=init_choice()
    
    logging.info('start_user_point get value:%s'%(start_user_point))
    logging.info('begin to crawl data ... ')
    
    if breadth_frist_search(start_user_point):
        logging.info('Done')
    else:
        logging.info("error!")
    

if __name__=='__main__':
    main()
