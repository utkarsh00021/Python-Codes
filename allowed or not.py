a=int(input("enter no of classes Held:"))
b=int(input("enter no of classes Attend:"))
c=b/a*100
if (c>=75):
    print("Allowed",c)
else:
    print("Not Allowed",c)
