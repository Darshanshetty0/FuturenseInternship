from datetime import datetime

# Task 1: Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Task 2: Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.model}")

# Task 3: BankAccount class
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")
    
    def display_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

# Task 4: Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Task 5: Student class
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
    def print_details(self):
        print(f"Student: {self.name}, Grades: {self.grades}, Average: {self.average_grade()}")

# Task 6: Employee class
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
        print(f"New salary after {percentage}% raise is {self.salary}")

# Task 7: Library class
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title} by {book.author}")
    
    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]
        print(f"Removed book with title: {title}")
    
    def display_books(self):
        if self.books:
            print("Library Collection:")
            for book in self.books:
                print(f"{book.title} by {book.author}")
        else:
            print("Library is empty")

# Task 8: Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)
    
    def circumference(self):
        return 2 * 3.14159 * self.radius

# Task 9: Book class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def print_details(self):
        print(f"Book: {self.title} by {self.author}, published in {self.year}")
    
    def is_classic(self):
        current_year = datetime.now().year
        return current_year - self.year > 50

# Task 10: Shape and its subclasses
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

# You can now test these classes and their methods by creating instances and calling the methods

# Testing the Person class
print("Testing Person class:")
p = Person("Alice", 30)
p.introduce()
print("\n")

# Testing the Car class
print("Testing Car class:")
c = Car("Toyota", "Corolla", 2020)
c.display_info()
print("\n")

# Testing the BankAccount class
print("Testing BankAccount class:")
acc = BankAccount("12345678", 1000)
acc.display_balance()
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(1500)
print("\n")

# Testing the Rectangle class
print("Testing Rectangle class:")
rect = Rectangle(10, 5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")
print("\n")

# Testing the Student class
print("Testing Student class:")
s = Student("Bob", [85, 90, 78])
s.print_details()
print("\n")

# Testing the Employee class
print("Testing Employee class:")
e = Employee("Charlie", "Developer", 70000)
e.give_raise(10)
print("\n")

# Testing the Library class
print("Testing Library class:")
lib = Library()
b1 = Book("1984", "George Orwell", 1949)
b2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
lib.add_book(b1)
lib.add_book(b2)
lib.display_books()
lib.remove_book("1984")
lib.display_books()
print("\n")

# Testing the Circle class
print("Testing Circle class:")
circle = Circle(5)
print(f"Area: {circle.area()}")
print(f"Circumference: {circle.circumference()}")
print("\n")

# Testing the Book class
print("Testing Book class:")
book = Book("Pride and Prejudice", "Jane Austen", 1813)
book.print_details()
print(f"Is classic: {book.is_classic()}")
print("\n")

# Testing the Shape, Square, and Triangle classes
print("Testing Shape, Square, and Triangle classes:")
shape = Shape()
square = Square(4)
triangle = Triangle(3, 6)
print(f"Shape area: {shape.area()}")
print(f"Square area: {square.area()}")
print(f"Triangle area: {triangle.area()}")
print("\n")

