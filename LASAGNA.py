#class - template for we can create an object that has variables.

class MyPet:
    def __init__(self,pet_name,pet_weight):
        #init means initialize
        self.name = pet_name
        self.weight = pet_weight
    def feed(self,food,food_weight):
        self.weight += food_weight
        print(self.name + " just ate " + food + " and now weighs " + str(self.weight) + " lbs.")


#self is referring to the object being worked on. self is the object currentl being referred to.

orange_cat = MyPet("Garfield",200)

print(orange_cat.name + " is my pet")

orange_cat.feed("Lasagna",5)

