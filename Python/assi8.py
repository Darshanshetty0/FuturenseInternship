# Task 1: Check if a number is even or odd
def check_even_odd():
    print("Even" if int(input("Enter an integer: ")) % 2 == 0 else "Odd")

# Task 2: Check if a year is a leap year
def check_leap_year():
    year = int(input("Enter a year: "))
    print("Leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a leap year")

# Task 3: Find the largest of three numbers
def find_largest():
    nums = [int(input(f"Enter integer {i+1}: ")) for i in range(3)]
    print("The largest number is:", max(nums))

# Task 4: Check if a string is a palindrome
def check_palindrome():
    s = input("Enter a string: ")
    print("Palindrome" if s == s[::-1] else "Not a palindrome")

# Task 5: Check if a number is positive, negative, or zero
def check_number():
    num = int(input("Enter an integer: "))
    print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")

# Task 6: Convert grade to letter grade
def convert_grade():
    grade = int(input("Enter a grade (0-100): "))
    print("A" if 90 <= grade <= 100 else "B" if 80 <= grade <= 89 else "C" if 70 <= grade <= 79 else "D" if 60 <= grade <= 69 else "F" if 0 <= grade <= 59 else "Invalid grade")

# Task 7: Determine age category
def determine_age_category():
    age = int(input("Enter your age: "))
    print("Child" if age < 13 else "Teenager" if age <= 19 else "Adult")

# Task 8: Check if two numbers are equal
def check_equality():
    print("Equal" if int(input("Enter first integer: ")) == int(input("Enter second integer: ")) else "Not equal")

# Task 9: Check if a number is positive and a multiple of 5
def check_positive_multiple_of_5():
    num = int(input("Enter an integer: "))
    print("Positive multiple of 5" if num > 0 and num % 5 == 0 else "Not a positive multiple of 5")

# Task 10: Determine the quadrant of a point
def determine_quadrant():
    x, y = int(input("Enter the x-coordinate: ")), int(input("Enter the y-coordinate: "))
    if x > 0 and y > 0:
        print("The point is in the first quadrant.")
    elif x < 0 and y > 0:
        print("The point is in the second quadrant.")
    elif x < 0 and y < 0:
        print("The point is in the third quadrant.")
    elif x > 0 and y < 0:
        print("The point is in the fourth quadrant.")
    elif x == 0 and y != 0:
        print("The point is on the y-axis.")
    elif y == 0 and x != 0:
        print("The point is on the x-axis.")
    else:
        print("The point is at the origin.")

if __name__ == "__main__":
    check_even_odd()
    check_leap_year()
    find_largest()
    check_palindrome()
    check_number()
    convert_grade()
    determine_age_category()
    check_equality()
    check_positive_multiple_of_5()
    determine_quadrant()
