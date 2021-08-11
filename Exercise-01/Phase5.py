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
    pet_name=input("Enter pet name:")
    amount=int(input("Enter the amount:"))
    date=input("Enter the date:")
    for key,value in data.items():
        print(key)
        print(value)
        sum=0
        
        if key == name:
            
            data[name].append((date,amount))
            for j in range(len(value)):
                print(value[j][1])
                k=1
                sum=sum+value[j][1]
     
            print(sum)
            data[key]=(value,pet_name)
    if k == 0:
        date_amount = [(date,amount)]
        
        data[name]=(date_amount,pet_name)
        k=1
   
    

print(json.dumps(data))    
with open("info.json", "w") as f:
   p=json.dump(data, f)



