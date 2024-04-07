num1=10
num2=15

def add():
    add=num1+num2
    print(add)

def sub():
    sub=num1-num2
    print(sub)

def mul():
    mul=num1*num2
    print(mul)


operation = input("Enter the operation ('add', 'sub', 'mul', or 'end' to exit): ")
while operation != "end":
    if operation == "add":
        add()
    elif operation == "sub":
        sub()
    else:
        mul()
    operation = input("Enter the operation ('add', 'sub', 'mul', or 'end' to exit): ")