from collections import deque
import zlib
blink='\n'
r=deque()
m=list('dwojaawdasdaaaaaaaaaaaaaaaa')
r.extend(m)

print r


with open('./test.txt','a+') as f:
    for i in r:
        f.write(i+blink)
f.close()
xx=[]

with open('./test.txt') as f:
    for line in f:
        xx.append(line.split()[0])
ttt=deque()
ttt.extend(xx)


