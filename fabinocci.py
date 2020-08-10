def is_fabnc(n):
    a=0
    b=1
    if n==0:
        print(a)
    elif n==1:
        print(b)
    else:
        print(a,b, end=" ")
        for n in range(n-2):
           c=a+b
           a=b
           b=c
           print(b,end=" ")

k = int(input("Enter the number : "))

is_fabnc(k)