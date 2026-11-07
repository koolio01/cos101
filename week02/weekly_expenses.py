#This program calculates the weekly expenses of a student


#input
student_name = input("Enter student's full name: ")
daily_transport = float(input("Enter your daily transport: "))
daily_feeding = float(input("Enter your daily feeding: "))
days_on_campus  = int(input("Enter numbers of days on campus: "))
other_expenses = float(input("Enter other expenses: "))

#process
transport_total = daily_transport * days_on_campus
feeding_total = daily_feeding * days_on_campus
weekly_total = transport_total + feeding_total + other_expenses
print()

#output
print("WEEKLY SUMMARY")
print("=======================================")
print(f"student: {student_name}")
print(f"Daily transport cost: NGN {transport_total:,.2f}")
print(f"Feeding total: NGN {daily_feeding:,.2f}")
print(f"Other expenses: NGN {other_expenses:,.2f}")
print(f"Weekly total: NGN {weekly_total:,.2f}")

               
