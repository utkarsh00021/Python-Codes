seconds=int(input("Enter the number of seconds:"))
hours=seconds//3600
seconds=seconds%3600
minutes=seconds//60
print(f"{hours} hours, {minutes} minutes, and {seconds} seconds.")
