number = float(input("Enter a number less than 25:"))
print(number)
if number > 25:
    print("Error")
else:
    while number <= 25:
        print(f"Inside the loop, my varible is {number}")