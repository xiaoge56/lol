#coding:utf-8
def find_mathID_detail(match_id,user_id,my_object):
    '根据提供的match_id，返回的数据为两个对象，一个是用户列表，一个是这次战斗中的用户战斗数据'
    
    serverName=r'网通三'
    playerName=user_id
    battle_url=r'http://lolbox.duowan.com/matchList/ajaxMatchDetail2.php?match_id=%s&serverName=%s&playerName=%s&favorate=0'%(match_id,urllib.quote(serverName),urllib.quote(playerName))
    find_users=[]
    re=spider.http_header(battle_url)
    html=urllib2.urlopen(re).read()
    soup_html=BeautifulSoup(html,"html.parser")
    detail_dat=spider.battle_detail_parse(soup_html)
    
    
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

def battle_detail_parse(soup_html):
    '返回一个列表，包含每场战斗中玩家的详细数据'
     
    div_layer=soup_html('div','layer')
    retDataList=[]
    if len(div_layer)>0:
        
        for every_player in div_layer:
            userdat=deal_with_bs_data(every_player)
            print userdat,' |delete'
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