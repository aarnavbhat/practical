U1 = []
U2 = []


n = int(input("Enter number of elements: "))


a_c = 0
b_c = 0


for i in range(n):
    b_c = int(input(f"Enter element {i + 1}: "))
    a_c += b_c
    U2.append(a_c)
    U1.append(b_c)

print(U1)
print(U2)
