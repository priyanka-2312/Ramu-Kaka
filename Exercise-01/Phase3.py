
def store():
    f= open("MyFile.txt" ,"a+")
    Name=input("Enter the name of customer:")
    Amount=input("Enter the amount of purchased product:")
    Date=input("Enter the date of purchase:")

    newline="\n"
    f.write(Name)
    f.write(newline)
    f.write(Amount)
    f.write(newline)
    f.write(Date)
    f.write(newline)
             

    f.close()
store()
