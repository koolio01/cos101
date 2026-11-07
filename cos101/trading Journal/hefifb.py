# This code multiplies number from 1 to 12

number = int(input("Enter your number(whole): "))

print()
print(f"MULTIPLICATION FOR {number}")
print("==================================")

for multiplier in range(1, 13):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")



