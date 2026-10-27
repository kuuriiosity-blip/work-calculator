hours = input("How many hours did you work? ")
hours = float(hours)

rate = input("What is your hourly rate in CZK? ")
rate = float(rate)

payment = hours * rate
print("Payment:", payment, "CZK")

expenses = input("How much did you spend in CZK? ")
expenses = float(expenses)

remaining = payment - expenses
print("Remaining money:", remaining, "CZK")

if remaining < 0:
    print("Your expenses are higher than your payment.")
else:
    print("Your expenses are covered.")