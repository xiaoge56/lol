#code:utf-8


def http_header(url):
    '构造http请求协议，伪造浏览器操作'
    send_headers = {  'Host':'lolbox.duowan.com',
                  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36', 
                  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', \
                  'Connection':'keep-alive'} 
    req = urllib2.Request(url,headers=send_headers)   
    return req

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