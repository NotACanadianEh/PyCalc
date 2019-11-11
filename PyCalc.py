#This is a basic addition and subtraction calculator for now

#Creates basic functions for addition and subtraction

#Addition
def add(x, y):
    return x + y

#Subtraction
def subtract(x, y):
    return x - y

print ("Select addition or subtraction")
print ("1 Addition")
print ("2 Subtraction")

#Uses 1 or 2 
choice = input("Select addition or subtraction, 1 or 2 ")
number1 = float(input("Choose first number "))
number2 = float(input ("Choose second number "))

if choice == '1':
    print (number1,"+",number2,"=", add(number1,number2))

elif choice == '2':
    print (number1,"-",number2,"=", subtract(number1,number2))
else:
    print ("You dun fucked up A-Aron")

