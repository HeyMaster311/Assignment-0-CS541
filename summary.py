
import pandas as pd

data_csv=pd.read_csv('/Users/yifanliang/Documents/python/Assignment 0/us-states.csv')

dt=data_csv.sort_values(by=['fips'])
print(dt)
place=input('Please enter the state that you want to check out:')
dt1=dt.loc[dt['state']==place,:]
while dt1.empty:
    print('The state name is wrong. Please re-enter the correct state.')
    place=input('Please enter the state that you want to check out:')
    dt1=dt.loc[dt['state']==place,:]

dt2=dt1.sort_values(by=['date'])
print(dt2)
dt3=dt2['cases']

minimum=min(dt3)
maximum=max(dt3)
mean=sum(dt3)/len(dt3)
variance = sum([((x - mean) ** 2) for x in dt3]) / len(dt3)
std = variance ** 0.5
print('For the case data of'+place+', the maximum is: '+str(maximum)+'.\n The minimum is: '+ str(minimum)+
'.\n  The average is:'+ str(mean)+'.\n  The standard derivation is:' + str(std)+ '.')