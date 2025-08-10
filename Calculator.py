#Basic Calculator Program

#Get Input from user

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operation = input("enter an operation from the following (+, -, *, /): ")

#perfomr the calculation

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else: result = 'Error! Division by zero.'
else:
    result = 'Invalid operation!'

#Display the result

print(f"{num1} {operation}{num2} = {result}")