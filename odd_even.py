input_tuple = tuple((int, input("Enter a tuple of numbers separated by spaces: ").split()))

odd_numbers = [num for num in input_tuple if num % 2 != 0]
even_numbers = [num for num in input_tuple if num % 2 == 0]

print("Odd numbers in the tuple:", odd_numbers)
print("Even numbers in the tuple:", even_numbers)