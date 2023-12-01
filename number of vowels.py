n=input("Enter a String")
count=0
for i in n:
    if i in "AEIOUaeiou":
        count+=1
print(count)
