import random

while True:
    try:
        level = int(input("Level:"))
        if level <= 0:
            pass
        else:
            break
    except (ValueError):
        pass

rando = random.randint(0,level)

while True:
    try:
        guess = int(input("Guess:"))

        if guess < rando:
            print("Too Small!")

        elif guess > rando:
            print("Too large!")

        elif guess == rando:
            print("Just right!")
            break
    except (EOFError):
        break
    except (ValueError):
        pass


