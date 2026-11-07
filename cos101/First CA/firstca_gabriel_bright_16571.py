# This program displays a basic multiplication table

number = int(input("Enter a number (1-13), or 0 to exit: "))

if number == 0:
    print("Exiting program")
    exit()

elif number == 1:
    print("number must be greater than 1.")

elif number < 1 or number > 13:
    print("Enter a number between 1 and 13.")

else:
    print(f"Multiplication Table of {number}")

    for table in range(1, 13):
        print(f"{number} x {table} = {number * table}")
