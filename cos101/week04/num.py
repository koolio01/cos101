# Display a multiplication table from 1 to 12.

print()

print("==============================")
print()
number = int(input("Enter a whole number: "))
for multiplier in range(1, 13):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")

print(f"MULTIPLICATION TABLE FOR {number}")
          


