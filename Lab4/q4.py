sg, sb = 0, 0

for i in range(3):
    sg += int(input(f'Girls in {i+1} grp: '))
for i in range(5):
    sb += int(input(f'Boys in {i+1} grp: '))
print("Total number of girls = ",sg)
print("Total number of boys = ",sb)
print("Total number of students = ",sg+sb)
