# 1. Declare an integer variable 'a' with the value 10 and a float variable 'b' with the value 3.14. Print their sum.
a = 10
b = 3.14
print("Sum of a and b:", a + b)

# 2. Assign the value 'True' to a variable 'is_valid' and the value 'False' to a variable 'is_empty'. Print both variables.
is_valid = True
is_empty = False
print("is_valid:", is_valid)
print("is_empty:", is_empty)

# 3. Create a complex number variable 'c' with the value '2 + 3j' and print its real and imaginary parts.
c = 2 + 3j
print("Real part of c:", c.real)
print("Imaginary part of c:", c.imag)

# 4. Declare a byte variable 'byte_data' with the value "b'hello'" and print its length.
byte_data = b'hello'
print("Length of byte_data:", len(byte_data))

# 5. Create a 'bytearray' variable 'byte_array' initialized with the byte sequence "b'\x01\x02\x03'". Modify the first byte to '0x04' and print the modified 'bytearray'.
byte_array = bytearray(b'\x01\x02\x03')
byte_array[0] = 0x04
print("Modified byte_array:", byte_array)

# 6. Convert the integer '255' to a binary string using the 'bin' function and print the result.
binary_string = bin(255)
print("Binary representation of 255:", binary_string)

# 7. Given two Boolean variables 'x = True' and 'y = False', print the result of the logical 'AND' operation between 'x' and 'y'.
x = True
y = False
print("Result of x AND y:", x and y)

# 8. Assign the result of '5 > 3' to a variable 'result' and print its type.
result = 5 > 3
print("Result of 5 > 3:", result)
print("Type of result:", type(result))

# 9. Create a float variable 'pi' with the value '3.141592653589793' and round it to 4 decimal places. Print the rounded value.
pi = 3.141592653589793
rounded_pi = round(pi, 4)
print("Rounded value of pi:", rounded_pi)

# 10. Assign the hexadecimal value '0x1A' to an integer variable 'hex_value' and print its decimal equivalent.
hex_value = 0x1A
print("Decimal equivalent of 0x1A:", hex_value)
