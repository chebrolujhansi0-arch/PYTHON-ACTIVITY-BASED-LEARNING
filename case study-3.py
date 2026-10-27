salary = float(input("Enter basic salary: "))

hra = salary * 0.10
da = salary * 0.05
deduction = salary * 0.08
net_salary = salary + hra + da - deduction

print("HRA:", hra)
print("DA:", da)
print("Deduction:", deduction)
print("Net salary:", net_salary)