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
visited_MatchID_disk=[]
visited_user_disk=[]
deque_user_disk=deque()
deque_MatchID_disk=deque()

def init_choice():
    global deque_user_disk
    if len(deque_user_disk)==0:
        user_point=r'三纷绣气'
        return user_point
    else:
        user_point=deque_user_disk.popleft()
        return user_point

def compute_undirect_graph(graph,user,neighbours):
    'construct a undirect graph of user_point info'
    if user not in graph.keys():
        if len(neighbours)!=0:
            for neighbour in neighbours:
                graph[user].add()
    else:
        for neighbour in neighbours:
                graph[user].add(neighbour)
def find_user_matchIDs(username):
    'search the target user latest 3page martch id'
    matchid=[]
    serverName=r'网通三'
    playerName=username
    

    matchId_by_name_url=r'http://lolbox.duowan.com/matchList.php?serverName=%s&playerName=%s'%(serverName,urllib.quote(playerName))
    re=spider.http_header(matchId_by_name_url)
    html=urllib2.urlopen(re).read()
    soup_html=spider.BeautifulSoup(html,"html.parser")
    page_nnnumber=int(spider.get_page_limit(soup_html))
    t=spider.find_match_id(soup_html)
    matchid.extend(t)#page_nnnumber默认从0开始，记录数据，避免后续重复查询
    # print '第%s页有%s条数据,当前一共%s数据'%(1,len(t),len(matchid))
    
    if page_nnnumber<=2:
        logging.DEBUG('%s 用户数据过少，不予统计'%(username))
        return []
    
    else:
        for n_page in range(1,4):
            matchId_by_name_url=r'http://lolbox.duowan.com/matchList.php?serverName=%s&playerName=%s&page=%s'%(serverName,playerName,str(n_page+1))
            re=spider.http_header(matchId_by_name_url)
            html=urllib2.urlopen(re).read()
            soup_html=spider.BeautifulSoup(html,"html.parser")
            temp=spider.find_match_id(soup_html)
            
            matchid.extend(temp)
            # print '第%s页有%s条数据,当前一共%s数据'%(n_page+1,len(temp),len(matchid))
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
    if len(detail_dat)!=0:
         for item in detail_dat:
             find_users.append(item[0])
    else:
        return find_users,detail_dat
    return find_users,detail_dat
    
def breadth_frist_search(start_user_point):
    'search the graph starting by one node using BFS'
    global visited_user_disk
    # global deque_MatchID_disk
    global visited_MatchID_disk
    global deque_user_disk
    
    visited_MatchID=visited_MatchID_disk
    deque_user=deque_user_disk#上次未完成工作进度,默认从头开始
    visited_user=visited_user_disk
    deque_MatchID=deque()
    
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
                
                find_users,detail_dat=find_mathID_detail(match,current_user_node)
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
        # if n>10:
            # break
        
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
    'reading the last time record when continue to work'

    
    name=path.split(r'/')[-1]
    #print path
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

    global visited_user_disk
    global visited_MatchID_disk
    global deque_user_disk
    global deque_MatchID_disk
    
    #with open('./dat/visited_user.dat','r') as f:
     #   for line
     #   visited_user=f.read()
    logging.info('/*-----------------------------------*/')
    logging.info('/*--begin to init data--*/')

    init_read_file('./dat/visited_user.dat',visited_user_disk)
    init_read_file('./dat/visited_MatchID.dat',visited_MatchID_disk)
    init_read_file('./dat/deque_user.dat',deque_user_disk)
    init_read_file('./dat/deque_MatchID.dat',deque_MatchID_disk)

    logging.info('initing user queue..')
    logging.info('%d users have been done'% len(visited_user_disk))
    logging.info('the current lengh of user_sequence is %d'% len(deque_user_disk))
    logging.info ('%d matches have been recorded'% len(visited_MatchID_disk))
    logging.info('the current lengh of deque_MatchID is %d'% len(deque_MatchID_disk))
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
