lst=[(),(),('',),(),(3,1,4,2),([]),()]
for i in range(lst.count(())):
    lst.remove(())
print(lst)
