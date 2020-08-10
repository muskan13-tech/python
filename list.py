# number=[1,2,3,4,5,6,7,8,9,10]
# print(number)

# word=["Muskan" , "Riytu","yash","mohit","rishu","harsh"]
# print(word)
# mixed=[1,2,3,4,5,"muskan","ritu","rishu",1.2,33.33]
# print(mixed[-1::-1])

#PROPERTIES OF LISTS

#APPEND METHOD 
fruit=["mango","apple","grapes","gauva"]
fruit.append("pineapple")
print(fruit)

#INSERT METHOD 
fruit.insert(3,"cheery")
print(fruit)

#CONCATENATE METHOD 
f1=["muskan","ritu","rishu","mohit"]
f2=fruit+f1
print(f2)

#EXTEND METHOD 
fruit.extend(f1)
print(fruit)

#LIST IN LIST 
fruit.append(f1)
print(fruit)

#POP METHOD
f1.pop()
print(f1)

#DELETE OPERATOR 
del f2[5]
print(f2)

#remove METHOD
f2.remove('ritu')
print(f2)