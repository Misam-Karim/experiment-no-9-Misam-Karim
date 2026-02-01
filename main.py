# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder: Misam Karim
# Date: 30/1/26

print("--- Factorial Finder ---\n")


# Write your code here
n = int(input("Enter Number: "))
fact = 1
if n<0:
    print(f"Factorial of {n} is Not Defined")
else:
    for i in range(1,n+1):
        fact *= i
    print(f"Factorial of {n} is {fact}")
