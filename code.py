import random

response= str(input("press y to roll and n to exit : "))

if (response=="y"):
    no=random.randint(1,6)
    print(no)

if (response=="n"):
    print("Hope you enjoyed")

