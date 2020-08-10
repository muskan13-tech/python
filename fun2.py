# name = input("your name : ")
# def lst_chr(name):
#     return name[-1]
# print(lst_chr(name))    

#odd even function 

# n=int(input("Enter any number :  "))
# def odd_even(n):
#     if n%2==0:
#         return " even  "
#     else :
#         return " odd "
# print(odd_even(n))            


# PYTHONIC WAY 
def is_even(num):      #parameter 
    return num%2==0

print(is_even(4))    #argument

#no parameter 
def blog():
    return "Muskan - blogspot "

print(blog())