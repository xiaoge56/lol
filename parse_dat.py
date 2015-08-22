#coding:utf-8
import urllib
import urllib2
import read_lol_dat
def find_mathID_detail(match_id,user_id,my_object):
    '根据提供的match_id，返回的数据为两个对象，一个是用户列表，一个是这次战斗中的用户战斗数据'
    
    serverName=r'网通三'
    playerName=user_id
    
    # test='{0},{1},{2}'.format(match_id,urllib.quote(str(serverName)),urllib.quote(str(playerName)))
    # print test
    battle_url=r'http://lolbox.duowan.com/matchList/ajaxMatchDetail2.php?matchId={0}&serverName={1}&playerName={2}&favorate=0'.format(match_id,urllib.quote(str(serverName)),urllib.quote(str(playerName)))
    
    find_users=[]
    re=read_lol_dat.http_header(battle_url)
    html=urllib2.urlopen(re).read()
    
    soup_html=read_lol_dat.BeautifulSoup(html,"html.parser")
    
    detail_dat=battle_detail_parse(soup_html,my_object)
    
    
    if len(detail_dat)!=0:
         for item in detail_dat:
             find_users.append(item[0])
             #更新数据时候，同时更新统计数据
             if my_object.global_users_dat_count.has_key(item[0]):
                 if my_object.global_users_dat_count[item[0]]>20:
                      break
                 else:
                     my_object.global_users_dat_count[item[0]]+=1
             else:
                  my_object.global_users_dat_count[item[0]]=1             
    else:
        return find_users,detail_dat
    return find_users,detail_dat
    
    
def find_match_id(soup_html):
    '''返回战斗场次的id
    返回一个字典，key是match_id，value是这次id的模式，比如匹配赛|大乱斗|排位赛
    '''

    keyword=[u'匹配赛',u'排位赛']
    match_id_set={}
    return_set={}
    #soup = BeautifulSoup(html)
    li=soup_html.find_all(r'li')
    typegame=soup_html.find_all(r'span','game')
    typelist=[]
    for ty in typegame:
        typelist.append(ty.get_text())    
    match_id_list=[]
    for ids in li:
        match_id_list.append(ids['id'][3:])
    for x,y in zip(match_id_list,typelist):
        match_id_set[x]=y
    for key in match_id_set:
        if match_id_set[key] in keyword:
            return_set[key]=match_id_set[key]
    # print  return_set       
    return return_set

def battle_detail_parse(soup_html,my_object):
    '返回一个列表，包含每场战斗中玩家的详细数据'
    
    div_layer=soup_html('div','layer')
    retDataList=[]
    if len(div_layer)>0:
        
        for every_player in div_layer:
            userdat=deal_with_bs_data(every_player)
            #更新統計結果
            if my_object.global_users_dat_count.has_key(userdat[0]):
                if my_object.global_users_dat_count[userdat[0]]>20:
                     break
                else:
                    my_object.global_users_dat_count[userdat[0]]+=1
            else:
                 my_object.global_users_dat_count[userdat[0]]=1
            print '當前用戶{0}的統計：{1}'.format(userdat[0],my_object.global_users_dat_count[userdat[0]])
            retDataList.append(userdat)
        return retDataList
    else:
        print '详细战斗数据为空'
        return retDataList

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
    
    return data
    
def get_page_limit(soup_html):
    '''
    对于每一个用户来说，这个函数应该只能被调用一次。返回用户战斗记录的页面长度
    
    '''
    page_num=soup_html('span','page-num')
    return page_num[0].get_text(strip=True,separator=u'|')[-2:]

def find_user_matchIDs(username):
    'search the target user latest 3page martch id'
    matchid=[]
    serverName=r'网通三'
    playerName=username
    

    matchId_by_name_url=r'http://lolbox.duowan.com/matchList.php?serverName={0}&playerName={1}'.format(serverName,urllib.quote(str(playerName)))
    
    # matchId_by_name_url=r'http://lolbox.duowan.com/matchList.php?serverName=%E7%BD%91%E9%80%9A%E4%B8%89&playerName=%E4%B8%89%E7%BA%B7%E7%BB%A3%E6%B0%94'
    re=read_lol_dat.http_header(matchId_by_name_url)
    html=urllib2.urlopen(re).read()
    
    soup_html=read_lol_dat.BeautifulSoup(html,"html.parser")
    page_nnnumber=int(get_page_limit(soup_html))
    
    t=find_match_id(soup_html)

    matchid.extend(t)#page_nnnumber默认从0开始，记录数据，避免后续重复查询
    # print '第%s页有%s条数据,当前一共%s数据'%(1,len(t),len(matchid))
    
    if page_nnnumber<=2:
        logging.DEBUG('%s 用户数据过少，不予统计'%(username))
        return []
    
    else:
        for n_page in range(1,4):
            matchId_by_name_url=r'http://lolbox.duowan.com/matchList.php?serverName=%s&playerName=%s&page=%s'%(serverName,playerName,str(n_page+1))
            re=read_lol_dat.http_header(matchId_by_name_url)
            html=urllib2.urlopen(re).read()
            soup_html=read_lol_dat.BeautifulSoup(html,"html.parser")
            temp=find_match_id(soup_html)
            
            matchid.extend(temp)
            # print '第%s页有%s条数据,当前一共%s数据'%(n_page+1,len(temp),len(matchid))
            if len(matchid)>15:
                break
    
    return matchid