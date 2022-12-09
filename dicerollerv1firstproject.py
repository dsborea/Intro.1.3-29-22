import random

min_val=1

max_val=6

roll_again= "yes"

while roll_again== "yes" or roll_again== "y":

    print("Dices rollinh...")

    print("YOur roll is...")

    print(random.randint(min_val, max_val))

    print(random.randint(min_val, max_val))

roll_again = input("Roll Dice Again?")

#would like to create an input option to use for all table top game dice size

#don't understand why it is just an endless loop despite it giving a result...maybe because its just left as randint rather than a result of the randmness?