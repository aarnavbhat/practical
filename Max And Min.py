L1 = list(input("Enter a list :" ))
n = len(L1)
min_val = L1[0]
max_val = L1[0]

for i in range(n):
    if L1[i] > max_val:
        max_val = L1[i]
    if L1[i] < min_val:
        min_val = L1[i]

print("Largest element:", max_val)
print("Smallest element:", min_val)
