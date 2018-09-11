# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:19:18 2017

@author: ZHENGHAN ZHANG
"""

import numpy as np
import matplotlib.pyplot as plt

#read the file
fp=open('tips.csv','r')
header=fp.readline().strip().split(',')
    #read the csv, add the numbers and get the average bill&tip for each day    
dataBill={}
dataTip={}
m=0
for i in fp:
    line=i.strip().split(',')
    row={}
    for j in range(len(header)):
        key=header[j]
        value=line[j]
        row[key]=value
        if  row['day'] not in dataBill:
            dataBill[row['day']]=0
        else:
            dataBill[row['day']]+=float(row['total_bill'])
        if  row['day'] not in dataTip:
            dataTip[row['day']]=0
        else:
            dataTip[row['day']]+=float(row['tip'])
            m+=1
        for i in dataBill:    
            dataBill[i]=dataBill[i]/m
        for i in dataTip:  
            dataTip[i]=dataTip[i]/m
    fp.close()
#print(dataBill,dataTip)

#plot the chart
p1=plt.bar(np.arange(len(dataBill))-0.125, dataBill.values(),width=0.25,yerr=np.std(list(dataBill.values())))
p2=plt.bar(np.arange(len(dataTip))+0.125, dataTip.values(),width=0.25,yerr=np.std(list(dataTip.values())))

plt.ylabel('Amount')
plt.title('Bill and Tips by day')
plt.xticks(np.arange(len(dataBill)), dataBill.keys())
plt.yticks(np.arange(0, 10, 2))
plt.legend((p1,p2),('Bill','Tips'))