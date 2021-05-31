# 2 question 
# percentage calculation

sub1 = int(input("Subject 1 Marks : "))
sub2 = int(input("Subject 2 Marks : "))
sub3 = int(input("Subject 3 Marks : "))


percent = ((sub1+sub2+sub3) / 300 )*100

print("Subject criteria : 33% in each subject is required.")
if(sub1 > 33 and sub2 > 33 and sub3 > 33):
    if(percent<40):
       print("The student has failed in the exam .")
    else:
       print(f"The student has passed the exam with a percentage of {percent}.")    
else:
    print("The student has failed .")