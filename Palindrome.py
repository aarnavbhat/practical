data1 = input("Enter a string: ")
data2 = ""

for i in range(len(data1) - 1, -1, -1):
    data2 += data1[i]

if data2 == data1:
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")
