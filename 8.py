def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y


def divide(x,y):
    if y==0:
        return "Error! Division by zero"
    return x/y


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice 1/2/3/4: ")
num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))



if(choice =='1'):
    print("Sum is : ",add(num1,num2))
    
elif(choice =='2'):
    print("subtract is : ",subtract(num1,num2))
elif(choice =='3'):
    print("multiply is : ",multiply(num1,num2))
elif(choice =='4'):
    print("divide is : ",divide(num1,num2))
else:
    print("INVALID INPUT")
