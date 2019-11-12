#This is a basic addition and subtraction calculator for now
#Added multiplication and division oopsie need to add exit or restart

#Creates basic functions for addition and subtraction

#Addition
def add(x, y):
    return x + y
#Subtraction
def subtract(x, y):
    return x - y
#Division
def division(x, y):
    return x / y
#Multiplication
def multiplication(x, y):
    return x * y

#Begins usable part
print ("Select 1, 2, 3, 4")
print ("1 Addition")
print ("2 Subtraction")
print ("3 Division")
print ("4 Multiplication")
#Uses 1 or 2 
choice = input("Select one, 1,2,3,4 ")
number1 = float(input("Choose first number "))
number2 = float(input ("Choose second number "))

if choice == '1':
    print (number1,"+",number2,"=", add(number1,number2))
elif choice == '2':
    print (number1,"-",number2,"=", subtract(number1,number2))
elif choice == '3':
    print (number1,"/",number2,"=", division(number1,number2))
elif choice == '4':
    print (number1,"*",number2,"=", multiplication(number1,number2))
else:
    print ("You dun fucked up A-Aron")