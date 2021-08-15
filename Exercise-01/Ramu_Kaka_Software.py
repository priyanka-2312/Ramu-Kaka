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


class Record:
    def __init__(self, message , name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date
        self.message = message


def welcome():
    message = "Welocome Mr. Ramu"
    print(message)

    

def multiple_operation():
    print("Enter which operation would you like to perform:")
    ch = input("Please select the desired operation +,-,*,/: ")
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    result = 0
    if ch == '+':
        result = num1 + num2
    elif ch == '-':
        result = num1 - num2
    elif ch == '*':
         result = num1 * num2
    elif ch == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Can't divide by Zero")

    print(num1, ch , num2, ":", result)



def insert_record():
    k=0
    num=int(input("Enter number of times you want to insert record:"))
    for i in range(num):
        name=input("Enter your name:")
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



def findCustomer_ShowTotal():
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
    
def show_details_with_pet_name():
    k=0
    num=int(input("Enter number of times you want to insert record:"))
    for i in range(num):
        name=input("Enter your name:")
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





def showTotalAmount_GreaterThan():
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





def RunProgram():

    print('----------------\n Welcome\n')
    while True:
        print ('----------------\nPlease choose from follow:')
        print ('1: Welcoming Ramu Kaka')
        print ('2: Multiple calculations')
        print ('3: Insert a Record')
        print('4: Search a customer and shows total owe amount')
        print('5: Show details with pet name')
        print('6: Show total amount greater than given amount')
        print('7: Exit')
        choice = int(input())

        if choice == 1:
            welcome()
        elif choice == 2:
            multiple_operation()
        elif choice == 3:
            insert_record()
        elif choice == 4:
            findCustomer_ShowTotal()
        elif choice == 5:
            show_details_with_pet_name()
        elif choice == 6:
            showTotalAmount_GreaterThan()
        elif choice == 7:
            break
        else:
            print('Wrong choice..')

RunProgram()
