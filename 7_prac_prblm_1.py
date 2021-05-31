# question 1 , table 
a = int(input("Enter a number for the table : "))
# for i in range(1,11):
i = 1
while i<=10:    #3 question
    print(f"{a} * {i} = {a*i}")
    i= i+1

# question 2 
l1 = ['Harry','Shubham','Sagar','Muskan','Ritu']
for i in l1:
    if i.startswith("S" or "s"):
        print(f"Good Morning {i}")