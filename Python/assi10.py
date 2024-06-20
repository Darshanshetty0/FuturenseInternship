# Task 1: Print numbers from 1 to 10 using a while loop
def print_numbers():
    i = 1
    while i <= 10:
        print(i)
        i += 1

# Task 2: Calculate the sum of all even numbers between 1 and 50 using a while loop
def sum_even_numbers():
    i = 1
    total = 0
    while i <= 50:
        if i % 2 == 0:
            total += i
        i += 1
    print("Sum of all even numbers between 1 and 50 is:", total)

# Task 3: Ask the user to enter a number and keep asking until a negative number is entered
def ask_until_negative():
    while True:
        number = int(input("Enter a number: "))
        if number < 0:
            print("Negative number entered")
            break

# Task 4: Print Fibonacci sequence up to a certain number of terms specified by the user
def fibonacci_sequence():
    terms = int(input("Enter the number of terms: "))
    a, b = 0, 1
    count = 0
    while count < terms:
        print(a)
        nth = a + b
        a = b
        b = nth
        count += 1

# Task 5: Ask for the password until the correct password "Python123" is entered
def check_password():
    while True:
        password = input("Enter the password: ")
        if password == "Python123":
            print("Access Granted")
            break

# Task 6: Print the factorial of a number using a while loop
def factorial():
    num = int(input("Enter a number to calculate its factorial: "))
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    print(f"The factorial of {num} is {factorial}")

# Task 7: Find the greatest common divisor (GCD) of two numbers input by the user
def gcd():
    def compute_gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = compute_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {result}")

# Task 8: Reverse a list of numbers using a while loop
def reverse_list():
    input_list = input("Enter a list of numbers separated by spaces: ").split()
    num_list = [int(x) for x in input_list]
    reversed_list = []
    i = len(num_list) - 1
    while i >= 0:
        reversed_list.append(num_list[i])
        i -= 1
    print("Reversed list:", reversed_list)

if __name__ == "__main__":
    print("Task 1:")
    print_numbers()
    
    print("\nTask 2:")
    sum_even_numbers()
    
    print("\nTask 3:")
    ask_until_negative()
    
    print("\nTask 4:")
    fibonacci_sequence()
    
    print("\nTask 5:")
    check_password()
    
    print("\nTask 6:")
    factorial()
    
    print("\nTask 7:")
    gcd()
    
    print("\nTask 8:")
    reverse_list()
