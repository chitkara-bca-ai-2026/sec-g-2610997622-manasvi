print("=" * 45)
print("        SCHOOL RESULT PROCESSING")
print("=" * 45)

name = input("Enter Student Name : ")
roll = input("Enter Roll Number : ")

marks = []
failed = False

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))

    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()

    marks.append(mark)

    if mark < 40:
        failed = True

total = sum(marks)
percentage = (total / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:
    result = "PASS"

    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"
    else:
        grade = "E"
        remarks = "Pass"

print("\n" + "=" * 45)
print("             STUDENT REPORT CARD")
print("=" * 45)
print("Student Name :", name)
print("Roll Number  :", roll)
print("-" * 45)
print(f"Total Marks  : {total} / 500.0")
print(f"Percentage   : {percentage:.2f}%")
print("Result       :", result)
print("Grade        :", grade)
print("Remarks      :", remarks)
print("=" * 45)