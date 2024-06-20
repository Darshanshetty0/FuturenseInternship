# 1. Create a set 'fruits' containing '{"apple", "banana", "cherry"}'. Add "orange" to the set using the '.add()' method and print the set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print("Updated fruits set:", fruits)

# 2. Given the set 'numbers = {1, 2, 3, 4, 5}', remove the element '3' using the '.remove()' method and print the set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("Updated numbers set after removing 3:", numbers)

# 3. Create two sets 'set1 = {1, 2, 3, 4}' and 'set2 = {3, 4, 5, 6}'. Use the '.union()' method to get the union of the two sets and print the result.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# 4. Given the sets 'setA = {1, 2, 3}' and 'setB = {2, 3, 4}', use the '.intersection()' method to find the intersection of the two sets and print the result.
setA = {1, 2, 3}
setB = {2, 3, 4}
intersection_set = setA.intersection(setB)
print("Intersection of setA and setB:", intersection_set)

# 5. Create a set 'colors' with the elements '{"red", "green", "blue"}'. Use the '.discard()' method to remove "green" from the set and print the set.
colors = {"red", "green", "blue"}
colors.discard("green")
print("Updated colors set after discarding 'green':", colors)

# 6. Given the sets 'setA = {1, 2, 3}' and 'setB = {3, 4, 5}', use the '.difference()' method to find the difference of 'setA' and 'setB' and print the result.
setA = {1, 2, 3}
setB = {3, 4, 5}
difference_set = setA.difference(setB)
print("Difference of setA and setB (setA - setB):", difference_set)

# 7. Create a set 'numbers' containing '{1, 2, 3, 4, 5}'. Use the '.pop()' method to remove and print an arbitrary element from the set. Then print the updated set.
numbers = {1, 2, 3, 4, 5}
popped_element = numbers.pop()
print("Popped element:", popped_element)
print("Updated numbers set after popping an element:", numbers)

# 8. Given the sets 'set1 = {1, 2, 3}' and 'set2 = {2, 3, 4}', use the '.symmetric_difference()' method to find the symmetric difference of the two sets and print the result.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# 9. Create a set 'numbers' with the elements '{1, 2, 3, 4, 5}'. Check if '3' is in the set using the 'in' keyword and print the result.
numbers = {1, 2, 3, 4, 5}
is_three_in_set = 3 in numbers
print("Is 3 in numbers set?", is_three_in_set)

# 10. Given the sets 'setA = {1, 2, 3, 4}' and 'setB = {3, 4}', use the '.issubset()' method to check if 'setB' is a subset of 'setA' and print the result.
setA = {1, 2, 3, 4}
setB = {3, 4}
is_setB_subset_of_setA = setB.issubset(setA)
print("Is setB a subset of setA?", is_setB_subset_of_setA)
