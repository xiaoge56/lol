#coding:utf-8
from collections import deque
class MyInit():
    def __init__(self):
        self.visited_user_disk=self.init_read_file('./dat/visited_user.dat')
        self.visited_MatchID_disk=self.init_read_file('./dat/visited_MatchID.dat')
        self.deque_user_disk=self.init_read_file('./dat/deque_user.dat')
        self.deque_MatchID_disk=self.init_read_file('./dat/deque_MatchID.dat')
        
        self.start_user=self.init_choice()
        
        self.__blink=r'\n'
    def init_dat(self):
        '主要是用来每次跑任务的时候，可以从上次中断的地方开始跑任务'
        
        #with open('./dat/visited_user.dat','r') as f:
        #   for line
        #   visited_user=f.read()
        # logging.info('/*-----------------------------------*/')
        # logging.info('/*--begin to init data--*/')
    
        # # init_read_file('./dat/visited_user.dat',self.visited_user_disk)
        # # init_read_file('./dat/visited_MatchID.dat',self.visited_MatchID_disk)
        # # init_read_file('./dat/deque_user.dat',self.deque_user_disk)
        # # init_read_file('./dat/deque_MatchID.dat',self.deque_MatchID_disk)
    
        # logging.info('initing user queue..')
        # logging.info('%d users have been done'% len(self.visited_user_disk))
        # logging.info('the current lengh of user_sequence is %d'% len(self.deque_user_disk))
        # logging.info ('%d matches have been recorded'% len(self.visited_MatchID_disk))
        # logging.info('the current lengh of deque_MatchID is %d'% len(self.deque_MatchID_disk))
        # logging.info('/*-----------------------------------*/')
    
    def write_next_init_file(self,path,content_list):
        '保存下次重新跑程序所需要的数据 '
         
        with open(path,'w') as f:
            for line in content_list:
                f.write(line+self.__blink)
    def init_read_file(self,path):
        '在新一轮任务开始前，读取本地的数据，这样可以从上次任务中断的地方开始跑任务'
        
        name=path.split(r'/')[-1]
        result=deque()
        with open(path) as f:
            for line in f:
                result.append(line.split()[0])
        if len(result)!=0:
            pass
            # logging.info('%s inited ok'%name)
        else:
            pass
            # logging.info('%s is None!!'%name)
        return result
    def save_detail_on_disk(self,detail_dat):
        '保存解析到的数据，以追加的形式写文件'
        
        try:
            with open('./dat/user.dat','a') as f:
                for line in detail_dat:
                    d='||'.join(line)
                    f.write(d+self.blink)
        except IOError,msg:
            print msg
            logging.DEBUG('./dat/user.dat can not open!')

    def init_choice(self):
        '初始化一个用户id,这次任务就从这个id开始爬取'
        
        if len(self.deque_user_disk)==0:
            user_point=r'三纷绣气'
            return user_point
        else:
            user_point=self.deque_user_disk.popleft()
            return user_point

def main():
    init=MyInit()
    print init.start_user
if __name__=='__main__':
    for x in range(100):
        main()