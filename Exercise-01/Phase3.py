
import json
import os

path='./info.json'
if os.path.isfile(path) and os.access(path,os.R_OK):
    with open("info.json","r") as t:
         j= json.load(t)
    data = j
else:
    data={}




k=0
num=int(input("Enter number of times you want to insert record:"))
for i in range(num):
    name=input("Enter you name:")
    amount=int(input("Enter the amount:"))
    date=input("Enter the date:")
    for key,value in data.items():
        print(key)
        print(value)
        
        if key == name:
            data[name].append([date,amount])
            k=1
                
    if k == 0:
        date_amount = [[date,amount]]
        data[name]=date_amount
            
    
    

print(json.dumps(data))    
with open("info.json", "w") as f:
   p=json.dump(data, f)



