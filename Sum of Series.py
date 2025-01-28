def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

x = int(input("Enter a number: "))
n = int(input("Enter number of terms : "))

for i in range (n):
    sum += (x**i)/fact(i)

print(" Sum of series = ", sum)
