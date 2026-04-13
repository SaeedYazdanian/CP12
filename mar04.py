import random
target = random.randint(1, 100)
running = True
while running == True:
    user = int(input("Enter your guess: "))
    if user < target:
        print("go higher")
    if user > target:
        print("go lower")
    if user == target:
        print("you won!")
        running = False

#count how many choices the user made to get it right
#ask the user for game level:
    #easy: 1-10
    #medium: 1-100
    #hard: 1-1000


