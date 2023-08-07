vowels = "AEIOUaeiou"
input_string = input("Enter a string: ")
vowel_count = 0
vowels_found = []

for char in input_string:
    if char in vowels:
        vowel_count += 1
        vowels_found.append(char)

print("Vowels found:", vowels_found)
print("Total count of vowels:", vowel_count)