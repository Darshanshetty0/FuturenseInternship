# Task 1: Squaring Even Numbers in a List
def square_even_numbers(input_list):
    squared_list = [x**2 for x in input_list]
    return squared_list

# Task 2: Reversing Strings in a Tuple
def reverse_strings(input_tuple):
    reversed_tuple = tuple(s[::-1] for s in input_tuple)
    return reversed_tuple

# Task 3: Calculating Average Grades for Students
def calculate_average_grades(grades_dict):
    average_grades_dict = {student: sum(grades) / len(grades) for student, grades in grades_dict.items()}
    return average_grades_dict

# Task 4: Separating Even and Odd Numbers from a List
def separate_even_odd_numbers(input_list):
    even_numbers = [x for x in input_list if x % 2 == 0]
    odd_numbers = [x for x in input_list if x % 2 != 0]
    return (even_numbers, odd_numbers)

# Task 5: Sorting a Set in Descending Order
def sort_set_descending(input_set):
    sorted_list = sorted(input_set, reverse=True)
    return sorted_list

if __name__ == "__main__":
    # Task 1
    list1 = [1, 2, 3, 4]
    squared_list = square_even_numbers(list1)
    print("Squared list:", squared_list)

    # Task 2
    tuple1 = ('hello', 'hi')
    reversed_tuple = reverse_strings(tuple1)
    print("Reversed tuple:", reversed_tuple)

    # Task 3
    grades_dict = {
        "student1": [80, 70, 75],
        "student2": [90, 85, 88]
    }
    average_grades_dict = calculate_average_grades(grades_dict)
    print("Average grades dictionary:", average_grades_dict)

    # Task 4
    list2 = [1, 2, 3, 4, 5, 6]
    result_tuple = separate_even_odd_numbers(list2)
    print("Resulting tuple (Even, Odd):", result_tuple)

    # Task 5
    set1 = {1, 4, 2, 3, 6, 8, 7, 9}
    sorted_list = sort_set_descending(set1)
    print("Sorted list:", sorted_list)
