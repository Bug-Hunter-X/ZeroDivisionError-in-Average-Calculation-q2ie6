def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

#Example
my_list = [10, 20, 30, 40, 50]
avg = calculate_average(my_list)
print(f"The average is: {avg}")

my_empty_list = []
avg_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {avg_empty}")

# Example with ZeroDivisionError
my_list_zero = []

#This will raise an exception
# avg_zero = calculate_average(my_list_zero) 
# print(f"The average is: {avg_zero}")