# greatest fuction question 1

def greatest(a,b,c):
    if a>b:
        if a>c:
            return f"{a} is greatest ."
        return f"{c} is greatest ."
    elif b>a:
        if b>c:
            return f"{b} is greatest ."
        else:
            return f"{c} is greatest ."            


a = int(input("Number 1 : "))
b = int(input("Number 2 : "))     
c = int(input("Number 3 : "))            

print(greatest(a,b,c))