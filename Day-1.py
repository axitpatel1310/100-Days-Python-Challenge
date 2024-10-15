#Basic Calculator

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

def calculate():
    print("Select operation.")
    print("1). Add")
    print("2). Subtract")
    print("3). Multiply")
    print("4). Divide")
    
    choice = input("Enter your choice")
    
    if choice in ['1','2','3','4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f'The result is {add(num1,num2)}')
        
        if choice == '2':
            print(f'The result is {subtract(num1,num2)}')
        
        if choice == '3':
            print(f'The result is {multiply(num1,num2)}')
        
        if choice == '4':
            print(f'The result is {divide(num1,num2)}')
        
    else: 
        print('Invalid Option')
        
calculate()