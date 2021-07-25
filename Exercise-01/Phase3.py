
f = open("data.txt","w")
name = input("Enter name of customer:")
amount = int(input("Enter purchase amount:"))
date = input("Enter purchase date:")

f.write(name + "\n")
f.write(str(amount)+ "\n")
f.write(date + "\n")


f.close()
