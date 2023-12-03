limit=int(input("enter a number:"))
sum_of_even=0
for num in range (1,limit+1):
    if num%2==0:
        sum_of_even+=num
print(sum_of_even)
