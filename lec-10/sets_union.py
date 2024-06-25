DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA | DaysB

print(AllDays)
print()

AllDays = DaysA & DaysB

print(AllDays)
print()

AllDays = DaysA - DaysB

print(AllDays)
print()

DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)
