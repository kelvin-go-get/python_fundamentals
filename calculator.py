print("Choose an operation")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation= input()

if operation == "1":
  num1=int(input("Enter first number: "))
  num2=int(input("Enter second number: "))
  print("The sum is: ", num1+num2)
elif operation == "2":
  num1=int(input("Enter first number: "))
  num2=int(input("Enter second number: "))
  print("The difference is: ", num1-num2)
elif operation == "3":
  num1=int(input("Enter first number: "))
  num2=int(input("Enter second number: "))
  print("The product  is: ", num1*num2)
elif operation == "4":
  num1=int(input("Enter first number: "))
  num2=int(input("Enter second number: "))
  if num2==0:
    print("Error: Cannot divide by zero")
  else:
    print("The quotient is: ", num1/num2)
else:
  print("Invalid input")