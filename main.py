#coding:utf-8
from collections import deque
import logging
import sys

blink='\n'
visited_MatchID=[]
visited_user=[]
deque_user=None
deque_MatchID=None

def init_choice():

    
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
    #visited=[]
    
    user_sequence=deque() #init queue
    matchIDs_sequence=deque()
    user_sequence.append(start_user_point)

    logging.info('Started')
    while len(user_sequence)!=0:
        
        pre_deal_user=sequence.popletf()
        visited_user.append(pre_deal_user)

        try:
            matchIds=find_user_marchIDs(pre_deal_user)
        except HTTPError, e:
            with open('./dat/MatchID.dat','a') as f:
                f.write(matchIds+blink)
            #log
            print 'The server couldn\'t fulfill the request.'  
            print 'Error code: ', e.code
            
        except URLError, e:
            #log
            print 'We failed to reach a server.'  
            print 'Reason: ', e.reason
        
        for match in matchIDs_sequence:
            find_users,detail_dat=find_mathID_detail(match)
            save_detail_on_disk(detail_dat)

            for user in find_users:
                if user not in visited:
                    user_sequence.append(user)

    return True
def init_read_file(path,result):
    'reading the last time record when continue to do work'

    
    name=path.split(r'/')[-1]
    
    with open('./test.txt') as f:
        for line in f:
            result.append(line.split()[0])
    if len(result)!=0:
        logging.info('%s inited ok'%name)
    else:
        logging.info('%s is None!!'%name)
        
def init_write_file(path,content_list):
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
    init_read_file('./dat/visited_user.dat',visited_user)
    
   # with open('./dat/MatchId.dat','r') as f:
    #    visited_MatchID=f.read()
    init_read_file('./dat/MatchId.dat',visited_MatchID)
    
    #with open('./dat/deque_user.dat','r') as f:
     #   deque_user=f.read()
    init_read_file('./dat/deque_user.dat',deque_user)
    
    with open('./dat/deque_MatchID.dat','r') as f:
        deque_MatchID=f.read()
    init_read_file('./dat/deque_MatchID.dat',deque_MatchID)

    logging.info('initing user queue..')
    
    logging.info('%d users have been done'% len(visited))
    logging.info('the current lengh of user_sequence'% len(deque_user))
    
    logging.info ('%d matches have been record'% len(visited_MatchID))
    logging.info('the current lengh of deque_MatchID is %d'% len(deque_MatchID))                                                        
def main():
    abc=[]
    init_read_file('test.txt',abc)
    '''
    logging.basicConfig(filename='mylog.log', level=logging.INFO)
    
    init_dat()
    logging.info('init_dat ok... ')
    
    start_user_point=init_choice()

    logging.info('start_user_point get value:%s'%(start_user_point))
    logging.info('begin to crawl data ... ')
    
    if breadth_frist_search(start_user_point):
        logging.info('Done')
    else:
        logging.info("error!")
    '''
abc=[]
logging.basicConfig(filename='mylog.log', level=logging.INFO)
init_read_file('test.txt',abc)
