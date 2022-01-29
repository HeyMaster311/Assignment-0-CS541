
import math as m
def judge(x):
    a= int(m.sqrt(x))
    for i in range(2,a+1) :
        if x%i==0:
            return 0
    return x
    

x = int(input())
for j in range(1,x):
    if judge(x)!=0:
        if judge(x-2)!=0:
            print("Current maximal prime twins are", x, x-2)
            break
        else:
            x=x-1
    else:
        x=x-1


