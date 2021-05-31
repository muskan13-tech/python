# grading system 
# question 6

marks = int(input("Enter the marks of the students . "))
if(marks in range(90,100)):
    print("Excellent.")
elif(marks in range(80,90)):
    print("A+") 
elif(marks in range(70,80)):
    print("B+") 
elif(marks in range(60,70)):
    print("C+")            
elif(marks in range(50,60)):
    print("D")      
else:
    print("F")    


# question 7.
post = ''' hari is good boy . he teaches very nicely.'''
if("harry" in post):
    print("Present")
else:
    print("Not Present")        