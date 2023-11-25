n=input("enter a string:")
count=0
for i in n:
    if i in "aeiouAEIOU":
        count+=1
print("number of vowels in the string is",count)
