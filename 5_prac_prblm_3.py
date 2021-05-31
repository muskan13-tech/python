# 1 question hindi english dictionary
oxford_dict ={"home":"Ghar",
               "Anger":"Gussa",
               "Happy":"Khushi",
               "Smile":"Muskan",
               "Night":"Raat",
               "Day":"Din"}
# print(oxford_dict)
print("Options are :", oxford_dict.keys())
a = input("Enter a valid word for knowing the meaning : ")

print("Meaning is : ",oxford_dict.get(a))

