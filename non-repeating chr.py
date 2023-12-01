st=input()
Utkarsh=True
for i in st:
    if st.count(i)==1:
        print(i)
        Utkarsh=False
        break
if Utkarsh==True:
    print("None")
