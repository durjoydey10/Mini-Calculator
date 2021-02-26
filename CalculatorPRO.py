def add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b    


print("Selecet an operator: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


while True:
    choice=input("Enter choice(1/2/3/4): ") 

    if choice in ('1', '2', '3', '4'):
        num1 =float(input("Enter 1st Num: "))
        num2 =float(input("Enter 2nd Num: "))
        
        if choice == '1':
            print(num1,"+", num2, "=", add(num1,num2))
        elif choice == '2':
            print(num1,"-", num2, "=", Subtract(num1,num2))
        elif choice == '3':
            print(num1,"*", num2, "=", multiply(num1,num2))
        elif choice == '4':
            print(num1,"/", num2, "=", divide(num1,num2))
        
        break
    else:
        print("Null")    
    
    
    


