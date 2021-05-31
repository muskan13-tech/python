# question 4
def addRecrsv(n):
    if n <= 1:
        return n
    return n + addRecrsv(n-1)  
# question 6
def convertInch(inch):
    c = inch*2.54
    return c 

m = int(input("Sum of the series is of :  "))
print(addRecrsv(m))

i = int(input("Inches : "))
print(convertInch(i))
