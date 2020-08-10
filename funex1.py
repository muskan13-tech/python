#TWO NUMBER COMPARE
# def compare(a,b):
#     if a>b :
#         return "greater is : "+ str(a)
#     return "greater is : " + str(b)

# a=int(input("Enter 1st number : "))
# b=int(input("Enter 2nd number : "))
# print(compare(a,b))


#COMPARE OF THREE NUMBERS 
def compare(a,b,c):
    if a>b and a>c:
        return str(a) + "  is Greatest"
    elif b>a and b>c:
        return str(b) + "  Is Greatest" 
    return str(c) + "  is Greatest "

a=int(input("1st number : "))           
b=int(input("2nd number : "))
c=int(input("3rd number : "))


print(compare(a,b,c))