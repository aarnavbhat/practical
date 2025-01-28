

num = int(input("enter a number" ))

n = num
dig = 0
sum = 0


while n > 0:
    n = int(n/10)
    dig += 1
n = num
while n > 0:
    sum += (n % 10)**dig
    n = int(n/10)

if sum == num:
    print("Armstrong Number")
else:
    print(" Not an armstrong number")


    
