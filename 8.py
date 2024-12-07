def add(x,y): return x+y
def subtract(x,y):return x-y
def multiply(x,y):return x*y
def divide(x,y):
    if y==0:
        return "Error! Division by zero"
    return x/y

print("Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = input("Enter choice 1/2/3/4: ")
num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))
operations = {'1':add , '2':subtract, '3':multiply,'4':divide}
if choice in operations:
    print("Result is : ",operations[choice](num1,num2))
else:
    print("INVALID INPUT")
