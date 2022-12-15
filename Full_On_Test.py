#Two number questions and five string questions.

print("As you play the game pay attention to the options given to you at the bottom.")
print("Also, if it says A.) as  an answer, simply answer as 'a'")
total = 0

print("A.) a Runner")
print("B.) a Swimmer")
print("C.) a Professional eating contest contendor")

test = input("Who is Michael Phelps")


if test == "a":
    print("You're incorrect.")

elif test == "b":
    print("Correct! You got the right answer!")
    total +=1

elif test == "c":
    print("You were very, very, VERY wrong.")

else:
    print("invalid response")

total = str(total)
print("Your total is " + total)

test2 = input("True or False, rubber ducks are orange ")

if test2 == "true":
    print("Incorrect. Only part of a rubber duck is orange.")

elif test2 == "false":
    print("Correct! only part of the duck is actually orange, but they're mostly yellow.")
    total = int(total)
    total +=1

elif test2 == "neither":
    print("You found the secret answer, yes it is neither if you would like to look at it that way.")

else:
    print("invalid response")

total = str(total)
print("Your total is " + total)

print("A.) The spy.")
print("B.) The engineer.")
print("C.) I don't know.")

test3 = input("What team fortress 2 character can become other players of the opposite team?")


if test3 == "a":
    print("Correct!")
    total = int(total)
    total += 1

elif test3 == "b":
    print("incorrect!")

elif test3 == "c":
    print("Okay, bad choice -1 points.")
    total = int(total)
    total -=1

else:
    print("invalid response")

total = str(total)
print("Your total is " + total)


print("A.) The Soldier")
print("B.) The Engineer")
print("C.) The Scout")
print("D.) The Heavy")
print("E.) All of the above")

test4 = input("Which character uses the shotgun?")


if test4 == "a":
    print("Correct, but there is a better answer.")

elif test4 == "b":
    print("Correct, but there is a better answer.")

elif test4 == "c":
    print("Correct, but there is a better answer.")

elif test4 == "d":
    print("Correct, but there is a better answer.")

elif test4 == "e":
    print("correct!")
    total = int(total)
    total += 1

else:
    print("invalid response")

total = str(total)
print("Your total is " + total)

test5 = input("Who is the biggest character in TF2 (use uncapitalized letters)")

if test5 == "heavy":
    print("Correct")
    total = int(total)

else:
    print("incorrect")

total = str(total)
print("Your total is " + total)

t5 = input("What is 5682 divided by 2")
t5 = int(t5)

if t5 == "2842":
    print("Correct!")
    total = int(total)
    total += 1

else:
    print("Incorrect")

total = str(total)
print("Your total is " + total)

t6 = input("What is 242^3")

if t6 == "14172488":
    print("Correct.")
    total = int(total)
    total += 1

else:
    print("incorrect")

total = str(total)
print("Your final score is " + total + "/7")

#//////////////////////////////////////////////////////////////////////////////////

q1 = total
q1 = float(q1)

q2 = 7
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
