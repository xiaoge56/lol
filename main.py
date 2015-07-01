#coding:utf-8
from collections import deque
import logging

def init_choice():
    user_point="user id or user name"
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
    visited=[]
    
    user_sequence=deque() #init queue
    matchIDs_sequence=deque()
    user_sequence.append(start_user_point)

    logging.info('Started')
    while len(user_sequence)!=0:
        
        pre_deal_user=sequence.popletf()
        visited.append(pre_deal_user)

        try:
            matchIds=find_user_marchIDs(pre_deal_user)
        except HTTPError, e:
            print 'The server couldn\'t fulfill the request.'  
            print 'Error code: ', e.code
            
        except URLError, e:  
            print 'We failed to reach a server.'  
            print 'Reason: ', e.reason
        
        for match in matchIDs_sequence:
            find_users,detail_dat=find_mathID_detail(match)
            save_detail_on_disk(detail_dat)

            for user in find_users:
                if user not in visited:
                    user_sequence.append(user)

    return True
def init_queue():
    logging.info('initing queue')
    logging.info('the current lengh of user_sequence is '%s len(user_sequence))
    logging.info('%s users have been done'% len(visited))
    logging.info('the current lengh of user_sequence'% len(visited))
    pass
def main():
    logging.basicConfig(filename='mylog.log', level=logging.INFO)
    
    start_user_point=init_choice()

    logging.info('choice a user in the queue ')
    if breadth_frist_search(start_user_point):
        print 'Done'
    else:
        print "error!"
