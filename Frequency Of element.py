J = list(input("Enter List :"))

U1, U2 = [], []

alpha = 0

for i in J:
    if i not in U1:
        alpha = J.count(i)
        U1.append(i)
        U2.append(alpha)



print("Element \t \t \t frequency")

for i in range(len(J)):
    print(U1[i], " \t\t\t", U2[i])
