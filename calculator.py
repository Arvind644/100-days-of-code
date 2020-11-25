# a simple calculator in python

num1 = float(input("Enter first number :")
num2 = float(input("Enter second number :")
op   = input("enter operator :")

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "*":
  print(num1 * num2)
elif op == "/":
  print(num1 / num2)
else :
  print("Invalid Operator")
