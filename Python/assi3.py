# 1. Create a list 'fruits' containing ["apple", "banana", "cherry"]. Add "orange" to the end of the list using the .append() method and print the list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Updated fruits list:", fruits)

# 2. Given the list 'numbers = [1, 2, 3, 4, 5]', insert the number '10' at index '2' using the '.insert()' method and print the list.
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 10)
print("Updated numbers list:", numbers)

# 3. Create a list 'colors' containing ["red", "green", "blue", "green"]. Remove the first occurrence of "green" using the '.remove()' method and print the list.
colors = ["red", "green", "blue", "green"]
colors.remove("green")
print("Updated colors list:", colors)

# 4. Given the list 'names = ["Alice", "Bob", "Charlie", "Bob"]', use the '.count()' method to count how many times "Bob" appears in the list and print the result.
names = ["Alice", "Bob", "Charlie", "Bob"]
bob_count = names.count("Bob")
print("Count of 'Bob':", bob_count)

# 5. Create a list 'numbers' with the values '[5, 2, 9, 1, 5, 6]'. Use the '.sort()' method to sort the list in ascending order and print the sorted list.
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print("Sorted numbers list:", numbers)

# 6. Given the list 'numbers = [1, 2, 3, 4, 5]', use the '.pop()' method to remove and print the last element of the list. Then, print the updated list.
numbers = [1, 2, 3, 4, 5]
last_element = numbers.pop()
print("Removed last element:", last_element)
print("Updated numbers list:", numbers)

# 7. Create a list 'items' containing ["pen", "pencil", "eraser"]. Use the '.index()' method to find the index of "pencil" and print the result.
items = ["pen", "pencil", "eraser"]
pencil_index = items.index("pencil")
print("Index of 'pencil':", pencil_index)

# 8. Given the list 'letters = ["a", "b", "c"]', use the '.extend()' method to add the elements of another list '["d", "e", "f"]' to letters and print the updated list.
letters = ["a", "b", "c"]
letters.extend(["d", "e", "f"])
print("Updated letters list:", letters)

# 9. Create a list 'values' with the elements '[10, 20, 30, 40, 50]'. Use slicing to print the sublist '[20, 30, 40]'.
values = [10, 20, 30, 40, 50]
sublist = values[1:4]
print("Sublist [20, 30, 40]:", sublist)

# 10. Given the list 'numbers = [1, 2, 3, 4, 5]', use list comprehension to create a new list 'squares' containing the squares of each number in numbers and print squares.
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print("List of squares:", squares)
