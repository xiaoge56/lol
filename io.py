#coding:utf-8
def init_dat():
    '主要是用来每次跑任务的时候，可以从上次中断的地方开始跑任务'

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
    
def write_next_init_file(path,content_list):
    '保存下次重新跑程序所需要的数据 '
    
    global blink

    
    with open(path,'w') as f:
        for line in content_list:
            f.write(line+blink)
def init_read_file(path,result):
    '在新一轮任务开始前，读取本地的数据，这样可以从上次任务中断的地方开始跑任务'

    name=path.split(r'/')[-1]
    #print path
    with open(path) as f:
        for line in f:
            result.append(line.split()[0])
    if len(result)!=0:
        logging.info('%s inited ok'%name)
    else:
        logging.info('%s is None!!'%name)
        
def save_detail_on_disk(detail_dat):
    '保存解析到的数据，以追加的形式写文件'
    global blink
    try:
        with open('./dat/user.dat','a') as f:
            for line in detail_dat:
                d='||'.join(line)
                f.write(d+blink)
    except IOError,msg:
        print msg
        logging.DEBUG('./dat/user.dat can not open!')

def init_choice():
    '初始化一个用户id,这次任务就从这个id开始爬取'
    global deque_user_disk
    if len(deque_user_disk)==0:
        user_point=r'三纷绣气'
        return user_point
    else:
        user_point=deque_user_disk.popleft()
        return user_point