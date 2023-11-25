n=int(input(" enter the number: "))
Utkarsh=True
for i in range(2,n):
    if(n%i==0):
        print("not a prime no.")
        Utkarsh=False
        break
if(Utkarsh==True):
    print("prime no.")
