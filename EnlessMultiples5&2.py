#loop

while (1==1):

    odd = input("Give us a number")
    i = int(odd)
    if i < 100:
        print("invalid number")
        continue
    while i > 0:
        i -= 1
        if i % 8 == 0:
            print(i)
        if i % 3 == 0:
            print(i)
        else:
            continue










