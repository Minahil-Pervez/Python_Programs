# Write a Python program to do arithmetical operations addition and division

#Addition
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2
print(f"Sum: {num1} + {num2} = {sum_result}")

#Division
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor number for division: "))
if num4 == 0:
       print("Error: Division by zero is not possible")
else:
       div_result = num3 / num4
print(f"Division: {num3} / {num4} = {div_result}")

