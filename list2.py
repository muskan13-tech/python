def list1(rev):
    lst2=[]
    for i in range(len(rev)):
        poped_item = rev.pop()
        lst2.append(poped_item)
    return lst2

number=list(range(1,11))
print(list1(number))

def list3(rev1):
    lst3=[]
    for i in range(len(rev1)):
        lst3.append(rev1[i][::-1])
    return lst3

name=["muskan","ritu","xyz"] 
print(list3(name))       