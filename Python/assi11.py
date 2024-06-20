# Task 1: Print only the odd numbers from 1 to 50 using a 'for' loop
print("Odd numbers from 1 to 50:")
for i in range(1, 51):
    if i % 2 != 0:
        print(i)

print("\n")

# Task 2: Calculate the sum of all numbers in a list using a 'for' loop
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print("Sum of all numbers in the list:", sum_of_numbers)

print("\n")

# Task 3: Print each character of a string on a new line using a 'for' loop
string = "hello"
print("Characters of the string 'hello' on a new line:")
for char in string:
    print(char)

print("\n")

# Task 4: Print each word and its length from a list of words using a 'for' loop
words = ["abc", "aghd"]
print("Words and their lengths:")
for word in words:
    print(word, len(word))

print("\n")

# Task 5: Print "even" or "odd" for each number in a list using a 'for' loop
numbers = [1, 2, 3, 4]
print("Even or odd for each number in the list:")
for num in numbers:
    if num % 2 == 0:
        print(num, "even")
    else:
        print(num, "odd")

print("\n")

# Task 6: Generate a list of squares of numbers from 1 to 20 using a 'for' loop
squares = []
for i in range(1, 21):
    squares.append(i**2)
print("Squares of numbers from 1 to 20:", squares)

print("\n")

# Task 7: Print all prime numbers between 1 and 100 using a 'for' loop
print("Prime numbers between 1 and 100:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
