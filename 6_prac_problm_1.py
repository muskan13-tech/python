# 1 question 
# pending

a=int(input())
b=int(input())
c=int(input())
d=int(input())

if a>b:
    if a>c:
        if a>d:
            print(f"{a} is greter .")
        else:
            print(f"{d} is greater .")
elif b>a:
    if b>c:
        if b>d:
           print(f"{b} is greater .") 
        else:
          print(f"{d} is greater .")
elif c>a:
    if c>b:
        if c>d:
           print(f"{b} is greater .") 
        else:
          print(f"{d} is greater .")          

