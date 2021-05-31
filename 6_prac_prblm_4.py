# length check.
# question 4.
name = input("Enter a user name . ")
if len(name)>=10:
    print("limit exceeded . RETYPE ! ")
else:
    print("Correct.")    

# length check question 5 in list.

nameList = ['Muskan','Ritu','priya','megha','sweety','beauty','sweta']
n = input("Enter a name of your cousins : ")
if(n in nameList):
    print("You have the full list . ")
else:
    print("Someone is missing . ")    
