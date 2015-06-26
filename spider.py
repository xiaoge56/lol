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
    req = urllib2.Request(url0,headers=send_headers)   
    return req

def battle_detail_parse(html):
    soup = BeautifulSoup(html)
    print soup.prettify()

def find_match_id(html):
    '返回战斗场次的id'
    soup = BeautifulSoup(html)
    li=soup.find_all(r'li')
    match_id_list=[]
    for id in li:
        match_id_list.append(id['id'][3:])
    return match_id_list

re=http_header()
html=urllib2.urlopen(re).read()
battle_detail_parse(html)
