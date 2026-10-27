participants = int(input("Enter number of participants: "))
fee = float(input("Enter fee per participant: "))
expenses = float(input("Enter total expenses: "))

income = participants * fee
balance = income - expenses

print("Total income:", income)
print("Total expenses:", expenses)
print("Balance:", balance)

if balance >= 0:
    print("Event is within budget")
else:
    print("Event has a loss")