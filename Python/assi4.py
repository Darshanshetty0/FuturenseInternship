# 1. Create a tuple 'fruits' containing '("apple", "banana", "cherry")'. Access and print the second element of the tuple.
fruits = ("apple", "banana", "cherry")
print("Second element of fruits tuple:", fruits[1])

# 2. Given the tuple 'numbers = (1, 2, 3, 4, 5)', use slicing to print the subtuple '(2, 3, 4)'.
numbers = (1, 2, 3, 4, 5)
print("Subtuple (2, 3, 4):", numbers[1:4])

# 3. Create a tuple 'colors' with the elements '("red", "green", "blue")'. Use the '.index()' method to find the index of "green" and print the result.
colors = ("red", "green", "blue")
green_index = colors.index("green")
print("Index of 'green':", green_index)

# 4. Given the tuple 'values = (1, 2, 3, 1, 2, 1)', use the '.count()' method to count how many times 1 appears in the tuple and print the result.
values = (1, 2, 3, 1, 2, 1)
one_count = values.count(1)
print("Count of 1 in values tuple:", one_count)

# 5. Create a tuple 'person' containing '("John", 25, "Engineer")'. Unpack the tuple into three variables 'name', 'age', and 'profession', and print each variable.
person = ("John", 25, "Engineer")
name, age, profession = person
print("Name:", name)
print("Age:", age)
print("Profession:", profession)

# 6. Given the tuple 'numbers = (1, 2, 3, 4, 5)', convert it to a list, append the number 6, and then convert it back to a tuple. Print the final tuple.
numbers = (1, 2, 3, 4, 5)
numbers_list = list(numbers)
numbers_list.append(6)
numbers = tuple(numbers_list)
print("Updated numbers tuple:", numbers)

# 7. Create a tuple 'dimensions' containing '(1920, 1080)'. Use tuple unpacking to assign the values to variables 'width' and 'height', then print 'width' and 'height'.
dimensions = (1920, 1080)
width, height = dimensions
print("Width:", width)
print("Height:", height)

# 8. Given the tuple 'data = (10, 20, 30, 40, 50)', create a new tuple 'even_data' that contains only the even numbers from 'data' using a generator expression, and print 'even_data'.
data = (10, 20, 30, 40, 50)
even_data = tuple(num for num in data if num % 2 == 0)
print("Tuple of even numbers:", even_data)

# 9. Create a tuple 'letters' with the elements '('a', 'b', 'c', 'd')'. Convert the tuple to a string by joining the elements with a comma separator and print the resulting string.
letters = ('a', 'b', 'c', 'd')
letters_string = ','.join(letters)
print("Joined letters string:", letters_string)

# 10. Given the tuple 'records = ((1, "Alice"), (2, "Bob"), (3, "Charlie"))', iterate over the tuple and print each ID and name on a new line.
records = ((1, "Alice"), (2, "Bob"), (3, "Charlie"))
for record in records:
    print(f"ID: {record[0]}, Name: {record[1]}")
