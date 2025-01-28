n = int(input(" Enter limit: "))
a = 0
b= 1
c = a + b

if c <=n :
    print(a)
    print(b)
    while c <= n:
        print(c)
        a=b
        b=c
        c=a+b
elif b <= n:
    print(a)
    print(b)
elif a <= n:
    print(a)
else
    print("Error")
