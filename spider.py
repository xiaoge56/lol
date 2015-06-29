#coding:utf-8
import urllib2
from bs4 import BeautifulSoup

url0=r'http://lolbox.duowan.com/matchList.php?serverName=网通三&playerName=三纷绣气'
url=r'http://lolbox.duowan.com/matchList.php?serverName=网通三&playerName=三纷绣气&page=8#12290959436'
url2=r'http://lolbox.duowan.com/matchList/ajaxMatchDetail2.php?matchId=12290959436&serverName=%E7%BD%91%E9%80%9A%E4%B8%89&playerName=%E4%B8%89%E7%BA%B7%E7%BB%A3%E6%B0%94&favorate=0'
url3=r'http://lolbox.duowan.com/matchList.php?serverName=网通三&playerName=甩饼的阿三'

def http_header():
    send_headers = {  'Host':'lolbox.duowan.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36', 
                  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', \
                  'Connection':'keep-alive'} 
    req = urllib2.Request(url2,headers=send_headers)   
    return req

def battle_detail_parse(html):
    
    soup = BeautifulSoup(html)
    div_layer=soup('div','layer')
    
    if len(div_layer)>0:
        
        for every_player in div_layer:
            deal_with_bs_data(every_player)
            break
        
    else:
        print '详细战斗数据为空'

def find_match_id(html):
    '返回战斗场次的id'
    soup = BeautifulSoup(html)
    li=soup.find_all(r'li')
    match_id_list=[]
    for id in li:
        match_id_list.append(id['id'][3:])
    return match_id_list
def deal_with_bs_data(player_data):
    '从bs格式数据中取回需要的数据以及格式'

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
    div_layer('p').get_text()
     
    
    for m in data:
        print m
    return m
re=http_header()
html=urllib2.urlopen(re).read()
battle_detail_parse(html)
