class A():
    def __init__(self,a,count=[]):
        self.s=a
        self.count=count
        self.count.append(self.s)
m=A('a')
print m.s,m.count
n=A('b')
print n.s,n.count
