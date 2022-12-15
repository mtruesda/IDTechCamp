q1 = input("How many questions did you answer?")
q1 = float(q1)

q2 = input("How many did you get correct?")
q2 = float(q2)

score = q2/q1
score = score*10

#grade = int(grade) allows us to use numbers but grade = float(grade) allows storation of numbers

if score >= 90:
    print("Your grade is an A.")

elif 90 > score >=80:
    print("Your grade is a B.")

elif 80 > score >= 70:
    print("Your grade is a C.")

elif 70 > score >= 60:
    print("Your grade is a D.")

else:
    print("You failed.")
