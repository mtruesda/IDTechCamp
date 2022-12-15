class Myrons_Pet:
       def __init__(self,My_petname,his_size):
            self.name = My_petname
            self.weight = his_size
       def eat(self,food_eaten):
            self.weight -= food_eaten
            print("You eat " + str(food_eaten) + " of " + self.name + " and he is now " + str(self.weight) + " lbs.")

Magic_Cow = Myrons_Pet("Bessie the Magic Cow",5000)

while True:

    print(Magic_Cow.name + " is my pet." + " She is right now, " + str(Magic_Cow.weight) + " much")
    f1 = input("Select a number and that will be how many pounds you will eat.")
    try :
        f1 = int(f1)
    except TypeError :
        print("Not an int.")
        continuefm

    f1 = int(f1)
    if f1*10 >= Magic_Cow.weight :
        f1 *= 10
    else :
        print("You ate too much, Bessie the Magic Cow is dead.")
        Magic_Cow = Myrons_Pet("Bessie the Magic Cow",5000)
        continue

    Magic_Cow.eat(f1)

    Magic_Cow.weight += 100

    print("Bessie gained 100 from magic. She is now " + str(Magic_Cow.weight))
