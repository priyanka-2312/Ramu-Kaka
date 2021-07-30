import pickle
filename = 'records.txt'

class Record:
    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date

def getData():
    try:
        infile = open(filename, 'rb')
        data = pickle.load(infile)
        infile.close()
        return data
    except:
        return []

def setData(data):
    outfile = open(filename, 'wb')
    pickle.dump(data, outfile)
    outfile.close()


def showAllRecords():
    records = getData()
    for i in range (len(records)):
        print(records[i].name, records[i].amount, records[i].date)

def insertRecord():
     records = getData()
     name = input('Enter the name: ')
     amount = float(input('Enter the amount: '))
     date = input('Enter date in DD-MM-YYYY format: ')
     record = Record(name.strip(), amount, date)
     records.append(record)
     setData(records)
     print('Record inserted successfully')

def findRecords(records, name):
    result = []
    for i in range (len(records)):
        if (records[i].name.lower() == name.strip().lower()):
            result.append(records[i])
    
    return result


def deleteRecord():
    name = input('Enter the name: ')
    records = getData()
    result = findRecords(records, name)

    for i in range (len(result)): 
        records.remove(result[i]) 
    
    if len(result) > 0:
        print('Record deleted successfully')
        setData(records)
    else:
        print('No such record found')


def searchRecord():
    name = input('Enter the name: ')
    records = getData()
    result = findRecords(records, name)

    result.sort(key=lambda x: x.amount, reverse=True)
    total = 0
    for i in range (len(result)):
        total = total + result[i].amount

    if len(result) > 0:
        print('Total owed: ', total)
        for i in range (len(result)):
            print(result[i].amount, result[i].date)
    else:
        print('No such record found')
    

def RunProgram():

    print('----------------\n Welcome\n')
    while True:
        print ('----------------\nPlease choose from follow:')
        print ('1: Show all Records')
        print('2: Insert a Record')
        print('3: Delete a Record')
        print('4: Search a Record')
        print('5: Exit')
        choice = int(input())

        if choice == 1:
            showAllRecords()
        elif choice == 2:
            insertRecord()
        elif choice == 3:
            deleteRecord()
        elif choice == 4:
            searchRecord()
        elif choice == 5:
            break
        else:
            print('Wrong choice..')

RunProgram()
        
        
        



