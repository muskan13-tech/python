def default(name1,name2,age=55):         #default parameter 
    return (f"the info is : {name1 , name2 , age}")
    


n1=input("First name : ")
n2=input("Last name : ")
#a1=int(input("age : "))

print(default(n1,n2))