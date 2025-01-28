input_string = input("Enter a string: ")

lowercase_count = 0
uppercase_count = 0
digit_count = 0
other_count = 0

for char in input_string:
    if char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        other_count += 1

print("There are", lowercase_count, "lowercase letters,")
print(uppercase_count, "uppercase letters,")
print(digit_count, "digits, and")
print(other_count, "other characters.")
