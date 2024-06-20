import re
from math import gcd

# Task 1: Check if a string is a valid hexadecimal number
def check_hexadecimal():
    hex_num = input("Enter a hexadecimal number: ")
    if re.fullmatch(r"[0-9a-fA-F]+", hex_num):
        print("Valid hexadecimal")
    else:
        print("Invalid hexadecimal")

# Task 2: Check if three integers can form a valid triangle
def check_triangle():
    sides = [int(input(f"Enter side {i+1}: ")) for i in range(3)]
    if sum(sides) - max(sides) > max(sides):
        print("Valid triangle")
    else:
        print("Invalid triangle")

# Task 3: Check if a string is a valid email address
def check_email():
    email = input("Enter an email address: ")
    if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        print("Valid email")
    else:
        print("Invalid email")

# Task 4: Check if four integers can form a valid rectangle
def check_rectangle():
    sides = [int(input(f"Enter side {i+1}: ")) for i in range(4)]
    if sides[0] == sides[2] and sides[1] == sides[3]:
        print("Valid rectangle")
    else:
        print("Invalid rectangle")

# Task 5: Check if a list of integers is sorted in ascending order
def check_sorted():
    nums = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
    if nums == sorted(nums):
        print("Sorted")
    else:
        print("Not sorted")

# Task 6: Print the age group based on user's age
def age_group():
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Child")
    elif 13 <= age <= 17:
        print("Teenager")
    elif 18 <= age <= 35:
        print("Young Adult")
    elif 36 <= age <= 60:
        print("Adult")
    else:
        print("Senior")

# Task 7: Round a floating-point number to the nearest integer
def round_number():
    num = float(input("Enter a floating-point number: "))
    print(round(num))

# Task 8: Check if two integers are coprime
def check_coprime():
    a, b = int(input("Enter first integer: ")), int(input("Enter second integer: "))
    if gcd(a, b) == 1:
        print("Coprime")
    else:
        print("Not coprime")

# Task 9: Check if a string is a valid binary number
def check_binary():
    binary_num = input("Enter a binary number: ")
    if re.fullmatch(r"[01]+", binary_num):
        print("Valid binary")
    else:
        print("Invalid binary")

# Task 10: Determine the type of triangle based on side lengths
def triangle_type():
    sides = [int(input(f"Enter side {i+1}: ")) for i in range(3)]
    if len(set(sides)) == 1:
        print("Equilateral")
    elif len(set(sides)) == 2:
        print("Isosceles")
    else:
        print("Scalene")


if __name__ == "__main__":
    check_hexadecimal()
    check_triangle()
    check_email()
    check_rectangle()
    check_sorted()
    age_group()
    round_number()
    check_coprime()
    check_binary()
    triangle_type()
