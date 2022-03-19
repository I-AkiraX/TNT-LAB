marks=[92,72,83,65]
marks[0]+=5
marks[1]+=5
tot=0
for i in range(0,4):
    tot+=marks[i]
avg = tot/4
if avg>=91 and avg<=100:
    print("Your Grade is O")
elif avg>=81 and avg<91:
    print("Your Grade is E")
elif avg>=71 and avg<81:
    print("Your Grade is A")
elif avg>=61 and avg<71:
    print("Your Grade is B")
elif avg>=51 and avg<61:
    print("Your Grade is C")
elif avg>=41 and avg<51:
    print("Your Grade is D")
elif avg>=33 and avg<41:
    print("Your Grade is E")
elif avg>=21 and avg<33:
    print("Your Grade is F")
elif avg>=0 and avg<21:
    print("Your Grade is G")
else:
    print("Invalid Input!")
