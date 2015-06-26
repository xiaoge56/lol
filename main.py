#coding:utf-8
from collections import deque

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
    visited.append(start_user_point)
    sequence=deque()
    sequence.append(start_user_point)
    while len(sequence)!=0:
        pre_deal_user=sequence.popletf()

        neighbours=user_info_spider(pre_deal_user)

        if len(neighbours)>0:
            for neighbour in neighbours:
                if neighbour not in visited:
                    sequence.append(neighbour)
        else:
            'error,the return neighbour is None'
            return False
    return True
    
def main():
    start_user_point=init_choice()
    if breadth_frist_search(start_user_point):
        print 'Done'
    else:
        print "error!"
