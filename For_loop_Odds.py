upperlimit = input("Give me an upper limit")
upperlimit = int(upperlimit)

lowerlimit = input("Give me a lower limit")
lowerlimit = int(lowerlimit)

totalvariable = 0

for x in range(lowerlimit,upperlimit+1):
    totalvariable += x

print(totalvariable)

