a = int(input("Enter the first number:"))
op = input("Input the operation:")
b = int(input("Enter the second number:"))
result = None
if op == "+":
    result = a+b
elif op == "/":
    result = a/b
elif op == "-":
    result = a-b
elif op == "*":
    result = a*b
print("Result: {:.2f}".format(result))
