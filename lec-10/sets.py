Days = set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Months = {"Jan","Feb","Mar"}
Dates = {21,22,27}

print(Days)
print(Months)
print(Dates)

Days.add("Sun")

for day in Days:
    print(day)

print()

Days.discard("Sun")

for day in Days:
    print(day)