def main():
    usertime = input("What time is it?")

    time = convert(usertime)
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18 <= time <= 19.0:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    inthrs = float(hours)
    intmin = float(minutes)

    return intmin / 60 + inthrs


if __name__ == "__main__":
    main()