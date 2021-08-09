import json
import os

path='./info.json'
if os.path.isfile(path) and os.access(path,os.R_OK):
    with open("info.json","r") as t:
         j= json.load(t)
    data = j
else:
    data={}


print(len(data))

k=0
num=int(input("Enter number of times you want to search record:"))
for i in range(num):
    name=input("Enter your name:")
  
    for key,value in data.items():
       # print(key)
        #print(value)
        sum=0
        if key == name:
            #data[name].append((date,amount))
            for j in range(len(value)):
                #print(value[j][1])
                k=1
                sum=sum+value[j][1]
                print(value[j][0],value[j][1])
     
            print(sum)     
    

