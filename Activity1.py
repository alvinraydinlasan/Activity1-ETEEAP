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