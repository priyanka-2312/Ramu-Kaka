import json
import os
from operator import itemgetter
path='./info.json'
if os.path.isfile(path) and os.access(path,os.R_OK):
    with open("info.json","r") as t:
         j= json.load(t)
    data = j
else:
    data={}


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1])
    return sub_li

def SortR(sub_li):
    return (sorted(sub_li, key = lambda x:x[1], reverse =True))
#print(data)
test=[]
sorted_list=[]
final_list=[]
k=0
num=len(data)
if 1==1:
#for i in range(num):
    for key,value in data.items():
      #  print(key)
       # print(value)
        sum=0
        test=value[0]
       # print(test)
        for j in range(len(test)):
              #  print('test--',test[j][1])
               sum=sum+int(test[j][1])
               
        if k == 0:
            k=1
            sorted_list=[[key,sum]]
            #print(sorted_list)
        else:
            sorted_list.append([key,sum]) 
            #print(sorted_list)    


          
            
    
    
#print(sorted_list)
no =int(input("Enter the amount:"))
k=0
for j in range(len(sorted_list)):
  
   if sorted_list[j][1] > no:
      #print(sorted_list[j][1])
      if k==0:
       final_list= [sorted_list[j][0],sorted_list[j][1]]
       k=1
      else:
          final_list.append([sorted_list[j][0],sorted_list[j][1]])

#print(Sort(sorted_list))
#print('Reverse sorted list:-',SortR(sorted_list))
print('final list greater than no.:-',final_list)
