# spam detecting 
sp1 = "make a lot of money"
sp2 = "buy now"
sp3 = "subscibe this"
sp4 =  "click this"

s = input("Enter the sentence : ")

if(sp1 in s):
    spam = True
elif(sp2 in s):
    spam = True
elif(sp3 in s):
    spam = True
elif(sp4 in s):
    spam = True
else:
    spam = False

if(spam == True):
    print("Spam is detected . Stay away !")                    
else:
    print("You'r system is Spam free. ")     