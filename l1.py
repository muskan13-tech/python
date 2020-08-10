def square(n):                  #return a list value (n is a return list value )
    square_l=[]
    for i in n:
       square_l.append(i*i)
    return square_l


number=list(range(1,11))
print(square(number))        
    

