# Find the largest number among the three input numbers

num1 = 10
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)



# Find the smallest number among the five input numbers
# Input five numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
num5 = float(input("Enter the fifth number: "))

# Find the smallest number
smallest = min(num1, num2, num3, num4, num5)

# Print the result
print(f"The smallest number among {num1}, {num2}, {num3}, {num4}, and {num5} is {smallest}")