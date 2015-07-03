#coding:utf-8
import urllib2
import json
from collections import deque 
from bs4 import BeautifulSoup
lolskill={
"http://img.lolbox.duowan.com/spells/1_24x24.jpg":1,
"http://img.lolbox.duowan.com/spells/2_24x24.jpg":2,
"http://img.lolbox.duowan.com/spells/3_24x24.jpg":3,
"http://img.lolbox.duowan.com/spells/4_24x24.jpg":4,
"http://img.lolbox.duowan.com/spells/5_24x24.jpg":5,
"http://img.lolbox.duowan.com/spells/6_24x24.jpg":6,
"http://img.lolbox.duowan.com/spells/7_24x24.jpg":7,
"http://img.lolbox.duowan.com/spells/8_24x24.jpg":8,
"http://img.lolbox.duowan.com/spells/9_24x24.jpg":9,
"http://img.lolbox.duowan.com/spells/10_24x24.jpg":10,
"http://img.lolbox.duowan.com/spells/11_24x24.jpg":11,
"http://img.lolbox.duowan.com/spells/12_24x24.jpg":12,
"http://img.lolbox.duowan.com/spells/13_24x24.jpg":13,
"http://img.lolbox.duowan.com/spells/14_24x24.jpg":14,
"http://img.lolbox.duowan.com/spells/15_24x24.jpg":15,
"http://img.lolbox.duowan.com/spells/16_24x24.jpg":16,
"http://img.lolbox.duowan.com/spells/17_24x24.jpg":17,
"http://img.lolbox.duowan.com/spells/18_24x24.jpg":18,
"http://img.lolbox.duowan.com/spells/19_24x24.jpg":19,
"http://img.lolbox.duowan.com/spells/20_24x24.jpg":20,
"http://img.lolbox.duowan.com/spells/21_24x24.jpg":21,
}


def http_header(url):
    send_headers = {  'Host':'lolbox.duowan.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36', 
                  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', \
                  'Connection':'keep-alive'} 
    req = urllib2.Request(url,headers=send_headers)   
    return req

def battle_detail_parse(html):
    '返回一个列表，包含每场战斗中玩家的详细数据'
    soup = BeautifulSoup(html)
    div_layer=soup('div','layer')
    retDataList=[]
    if len(div_layer)>0:
        
        for every_player in div_layer:
            retDataList.append(deal_with_bs_data(every_player))
            
        return retDataList
    else:
        print '详细战斗数据为空'

def find_match_id(html):
    '''返回战斗场次的id
    返回一个字典，key是matchId，value是这次Id的模式，比如匹配赛|大乱斗|排位赛
    '''
    match_id_set={}
    soup = BeautifulSoup(html)
    li=soup.find_all(r'li')
    match_id_list=[]
    for id in li:
        match_id_list.append(id['id'][3:])
    return match_id_list
def deal_with_bs_data(player_data):
    '''从bs格式数据中取回需要的数据以及格式
        
    '''

    data=[]
    div_layer = player_data
    
    username = div_layer(r'p','tip-user-name')[0].get_text(strip=True)
    pick_hero = div_layer('span','tip-tip-user-name2')[0].get_text(strip=True)
    
    more_detail = div_layer(r'table','mod-tips-data')

    data.append(username)
    data.append(pick_hero)
    for table in more_detail:
        temp=table.get_text(strip=True,separator=u'|')
    l=temp.split('|')
    data.extend(l[1::2])
    
    damage=[]
    for p in player_data('p'):
        damage.append(p.get_text(strip=True,separator=u'|'))
    for x in damage[4:]:
        data.append(x.split('|')[1])
    
    print data
def get_page_limit(html):
    '''
    对于每一个用户来说，这个函数应该只能被调用一次。返回用户战斗记录的页面长度
    
    '''
    
    return page_number
matchId_by_name_url=r'http://lolbox.duowan.com/matchList.php?serverName=网通三&playerName=三纷绣气'
page_url=r'http://lolbox.duowan.com/matchList.php?serverName=网通三&playerName=三纷绣气&page=8'
battle_url=r'http://lolbox.duowan.com/matchList/ajaxMatchDetail2.php?matchId=12290959436&serverName=%E7%BD%91%E9%80%9A%E4%B8%89&playerName=%E4%B8%89%E7%BA%B7%E7%BB%A3%E6%B0%94&favorate=0'

martch_id_deque=deque()
visited_deque=deque()

url=matchId_by_name_url
re=http_header(url)
html=urllib2.urlopen(re).read()
f=open('test','w')
f.write(html)
f.close()

#print find_match_id(html)
#battle_detail_parse(html)
