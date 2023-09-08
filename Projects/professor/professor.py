import random


def main():
    counter = 10
    score = 0
    level = get_level()
    #generate_integer(level)
    while counter > 0:
        counter -= 1
        try:
            intx = generate_integer(level)
            inty = generate_integer(level)

            tries = 3
            while tries > 0:

                try:

                    x = int(input(f"{intx} + {inty} = "))
                    #intx + inty == x # reprompt 10 times

                    if intx + inty != x:
                        print("EEE")
                        tries -= 1
                    else:
                        score += 1
                        break

                except (ValueError):
                    print("EEE")
                    tries -= 1
                    pass

            if tries == 0:
                z = intx + inty
                print(f"{intx} + {inty} = {z}")
            #stop program if incorrect anwser or  cat is put in but keep repropting

        except (EOFError):
            break


    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in (1,2,3):
                pass
            else:
                return level
        except (ValueError):
            pass

def generate_integer(level):

    if level == 1:
        intz = random.randint(0,9)
    elif level == 2:
        intz = random.randint(10,99)
    elif level == 3:
        intz = random.randint(100,999)

    return intz

if __name__ == "__main__":
    main()