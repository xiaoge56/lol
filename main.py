#coding:utf-8
from collections import deque
import logging
import sys
import spider
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

blink='\n'
visited_MatchID=[]
visited_user=[]
deque_user=deque()
deque_MatchID=deque()

def init_choice():
    global deque_user
    if len(deque_user)==0:
        user_point=r'三纷绣气'
        return user_point
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
def find_user_marchIDs(username):
    'search the target user latest 3page martch id'
    matchid=[]
    serverName=r'网通三'
    playerName=username
    

    matchId_by_name_url=r'http://lolbox.duowan.com/matchList.php?serverName=%s&playerName=%s'%(serverName,urllib.quote(playerName))
    re=spider.http_header(matchId_by_name_url)
    html=urllib2.urlopen(re).read()
    soup_html=spider.BeautifulSoup(html,"html.parser")
    page_nnnumber=int(spider.get_page_limit(soup_html))
    
    matchid.extend(spider.find_match_id(soup_html))#避免重复查询
    
    if page_nnnumber<=2:
        logging.DEBUG('%s 用户数据过少，不予统计'%(username))
        return []
    
    else:
        for n_page in range(1,4):
            matchId_by_name_url=r'http://lolbox.duowan.com/matchList.php?serverName=%s&playerName=%s&page=%s'%(serverName,playerName,str(n_page))
            re=spider.http_header(matchId_by_name_url)
            html=urllib2.urlopen(re).read()
            soup_html=spider.BeautifulSoup(html,"html.parser")
            matchid.extend(spider.find_match_id(soup_html))
            if len(matchid)>15:
                break
    return matchid
def find_mathID_detail(matchId,user_id):
    'retrun find_users and detail_dat,the input match is the match id'
    serverName=r'网通三'
    playerName=user_id
    battle_url=r'http://lolbox.duowan.com/matchList/ajaxMatchDetail2.php?matchId=%s&serverName=%s&playerName=%s&favorate=0'%(matchId,urllib.quote(serverName),urllib.quote(playerName))
    find_users=[]
    re=spider.http_header(battle_url)
    html=urllib2.urlopen(re).read()
    soup_html=BeautifulSoup(html,"html.parser")
    detail_dat=spider.battle_detail_parse(soup_html)
    for item in detail_dat:
        find_users.append(item[0])

    return find_users,detail_dat
    
def breadth_frist_search(start_user_point):
    'search the graph starting by one node using BFS'
    global visited_user
    global deque_MatchID
    global visited_MatchID
    global deque_user
    
    
    deque_user.append(start_user_point)

    logging.info('Starting.....')
    while len(deque_user)!=0:
        
        pre_deal_user=deque_user.popleft()
        visited_user.append(pre_deal_user)

        try:
            get_deque_MatchID=find_user_marchIDs(pre_deal_user)
             
        except urllib2.HTTPError,e:
            write_next_init_file('./dat/deque_MatchID.dat',deque_MatchID)
            logging.DEBUG('The server couldn\'t fulfill the request...deque_MatchID saved!')
            print 'The server couldn\'t fulfill the request.'  
            print 'Error code: ', e.code
            
        except urllib2.URLError, e:
            #log
            print 'We failed to reach a server.'  
            print 'Reason: ', e.reason
        deque_MatchID.extend(get_deque_MatchID)
        
        for match in deque_MatchID:
            find_users,detail_dat=find_mathID_detail(match,pre_deal_user)
            visited_MatchID.append(match)
            save_detail_on_disk(detail_dat)
            
            for user in find_users:
                if user not in visited_user:
                    deque_user.append(user)
        write_next_init_file('./dat/deque_user.dat',deque_user)
        write_next_init_file('./dat/deque_MatchID.dat',deque_MatchID)
        write_next_init_file('./dat/visited_MatchID.dat',visited_MatchID)
        write_next_init_file('./dat/visited_user.dat',visited_user)
        logging.info('new deque_user,deque_MatchID,visited_user,visited_MatchID have been recorded')
        
    return True
def save_detail_on_disk(detail_dat):
    global blink
    try:
        with open('./dat/user.dat','a') as f:
            for line in detail_dat:
                d='||'.join(line)
                f.write(d+blink)
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

    
    with open(path,'w') as f:
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
    logging.info('/*-----------------------------------*/')
    logging.info('/*--begin to init data--*/')

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
   
#matchid=find_user_marchIDs(r'三纷绣气')
#for ids in matchid:
#    find_mathID_detail(ids,r'三纷绣气')
    
if __name__=='__main__':
    
    main()
