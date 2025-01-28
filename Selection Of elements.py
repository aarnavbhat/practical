list_01 = []
n = int(input("Enter number of elements: "))

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    list_01.append(element)

list_02 = []

for num in list_01:
    if num % 2 == 0:
        list_02.append(num)

print("Even numbers list:", list_02)
