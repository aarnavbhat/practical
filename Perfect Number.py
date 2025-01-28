num = int(input("Enter a number : "))
sum = 0

for i in range (1, num+1):
    if num % i == 0:
        sum += i

if sum == 2*num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
