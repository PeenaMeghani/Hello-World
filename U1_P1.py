a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("\nBefore swapping : ")
print(f"Num1 : {a}  &  Num2 : {b}")               

a, b = b, a

print("\nAfter swapping : ")
print(f"Num1 : {a}  &  Num2 : {b}")