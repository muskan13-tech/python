# prime number 


a = int(input("Enter a number ."))
result = True
for i in range(2,a):
    if(a%i == 0):
        result = False
        break


if result:
    print("Number is  prime")
else:
    print("Number is not prime ")    
