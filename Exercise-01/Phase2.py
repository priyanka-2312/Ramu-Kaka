print("Enter which operation would you like to perform?")
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

