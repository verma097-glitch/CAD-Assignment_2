num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 != 0:
    result = num1 % num2
    print("Remainder is:", result)
else:
    print("Cannot perform modulus with zero!")