# 1. Create a dictionary 'person' with keys '"name", "age", and "city"' and corresponding values '"John", 25, and "New York"'. Print the dictionary.
person = {"name": "John", "age": 25, "city": "New York"}
print("Person dictionary:", person)

# 2. Given the dictionary 'person = {"name": "Alice", "age": 30, "city": "London"}', add a new key-value pair '"profession": "Engineer"' using assignment and print the updated dictionary.
person = {"name": "Alice", "age": 30, "city": "London"}
person["profession"] = "Engineer"
print("Updated person dictionary:", person)

# 3. Create a dictionary 'student' with keys '"name", "grades", and "age"' and corresponding values '"Bob", [85, 90, 78], and 22'. Use the '.get()' method to print the value associated with the key "grades".
student = {"name": "Bob", "grades": [85, 90, 78], "age": 22}
grades = student.get("grades")
print("Grades:", grades)

# 4. Given the dictionary 'car = {"brand": "Toyota", "model": "Camry", "year": 2020}', update the value associated with the key "year" to '2021' using assignment and print the dictionary.
car = {"brand": "Toyota", "model": "Camry", "year": 2020}
car["year"] = 2021
print("Updated car dictionary:", car)

# 5. Create a dictionary 'inventory' with keys '"apples", "bananas", and "oranges"' and corresponding values '10, 5, and 8'. Use the '.keys()' method to print all the keys in the dictionary.
inventory = {"apples": 10, "bananas": 5, "oranges": 8}
keys = inventory.keys()
print("Inventory keys:", keys)

# 6. Given the dictionary 'inventory = {"apples": 10, "bananas": 5, "oranges": 8}', use the '.values()' method to print all the values in the dictionary.
values = inventory.values()
print("Inventory values:", values)

# 7. Create a dictionary 'book' with keys '"title", "author", and "year"' and corresponding values '"1984", "George Orwell", and 1949'. Use the '.items()' method to print all the key-value pairs in the dictionary.
book = {"title": "1984", "author": "George Orwell", "year": 1949}
items = book.items()
print("Book items:", items)

# 8. Given the dictionary 'person = {"name": "Charlie", "age": 28, "city": "San Francisco"}', remove the key-value pair with the key "age" using the '.pop()' method and print the updated dictionary.
person = {"name": "Charlie", "age": 28, "city": "San Francisco"}
person.pop("age")
print("Updated person dictionary after popping 'age':", person)

# 9. Create a dictionary 'employee' with keys '"name", "position", and "salary"' and corresponding values '"Diana", "Manager", and 75000'. Use the '.update()' method to change the "salary" to '80000' and add a new key-value pair '"department": "Sales"'. Print the updated dictionary.
employee = {"name": "Diana", "position": "Manager", "salary": 75000}
employee.update({"salary": 80000, "department": "Sales"})
print("Updated employee dictionary:", employee)

# 10. Given the dictionary 'movie = {"title": "Inception", "director": "Christopher Nolan", "year": 2010}', use the '.popitem()' method to remove the last inserted key-value pair and print the removed pair and the updated dictionary.
movie = {"title": "Inception", "director": "Christopher Nolan", "year": 2010}
removed_pair = movie.popitem()
print("Removed pair:", removed_pair)
print("Updated movie dictionary:", movie)
