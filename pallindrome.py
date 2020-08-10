def palindrm(word):
    if s==p:
        return True
    return False

s = input("Enter a word may be a pallindrome! : ") 
p = s[::-1] 

print(palindrm(s))