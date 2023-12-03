days=int(input("enter the number of days:"))
year=days//360
weeks=days//7
remaining_days=days%7
print(f"{days} days is equal to {weeks} weeks,{year} year and {remaining_days} days.")
