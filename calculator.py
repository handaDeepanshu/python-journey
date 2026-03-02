def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if(b == 0):
        return "Error: Cannot divide by 0"
    return a/b


op = input("Enter operator")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if op == "+":
    print(add(a,b))
elif op == "-":
    print(sub(a,b))
elif op == "*":
    print(mul(a,b))
else:
    print(div(a,b))