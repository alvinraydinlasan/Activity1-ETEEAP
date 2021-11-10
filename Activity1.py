input("Student name: ")
prelim = int(input("Prelims: "))
midterm = int(input("Midterm: "))
semi = int(input("Semifinal: "))
final = int(input("Final: "))

total = (prelim+midterm+semi+final)/4

print("Average: ", total)

if total >= 75:
    print("Passed")
else:
    print("Failed")

if total>=99 and total<=100:
    print(total, " Your Grade is A")
elif total>=90 and total<=98:
    print(total, " Your Grade is B")
elif total>=80 and total<=89:
    print(total, " Your Grade is C")
elif total>=71 and total<=79:
    print(total, " Your Grade is D")
elif total>=61 and total<=70:
    print(total, " Your Grade is E")
elif total<=89:
    print(total, " Your Grade is F")