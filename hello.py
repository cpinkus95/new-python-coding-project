print("hello world")
print("here is my calculator")

num1 = float(input("Enter first number:"))
op = input("Enter operation:")
num2 = float(input("Enter second number:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")


#these are for testing
#This was a pain in the ass to figure out.
#I think im finally getting it a little