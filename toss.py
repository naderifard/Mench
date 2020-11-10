import random
from math import floor
def toss():
    tosslist=[]
    while True :
        x=floor(1+6*random.random())
        tosslist.append(x)
        if x!= 6:
            break
    return tosslist
for i in range(10):
    print(toss())
