# simple-calculator.py
#Program to make a simple calculator:

#function to add two numbers:
def add(a, b):
    return a + b
    
#function to subtract two numbers:
def subtract(a, b):
    return a - b

#function to multiply two numbers:
def multiply(a, b):
    return a * b
    
#function to divide two numbers:
def divide(a, b):
    return a / b

print("select operation")
print("1.Add")
print("2.Subtract")
print("3.multiply")
print("4.divide")

#check if choice is one of the four option
while True:
    choice = input("Enter your choice(1/2/3/4):")
    
   #taking input from the user:
    if choice in ('1','2','3','4'):
        num1= float(input("Enter fisrt number:"))
        num2= float(input("Enter second number:"))
        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))
    
        elif choice =='3':
            print(num1, "*", num2,"=",multiply(num1, num2))
       
        elif choice =='4':
            print(num1, "/", num2,"=", divide(num1, num2))
            
    else:
        print("Invalid Input")
