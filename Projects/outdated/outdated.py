months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        user_input = input("Date:")
        split_dash = user_input.split("/")
        split_space = user_input.replace(",","").split(" ")
        if len(split_dash) == 3:
            month, day, year = split_dash
            digit_day = int(day)
            digit_month = int(month)
            digit_year = int(year)
            if digit_day <= 31 & digit_month <= 12:
                print(f"{digit_year:02}-{digit_month:02}-{digit_day:02}")
                break
        elif len(split_space) == 3:
            if "," not in user_input:
                pass
            else:
                month, day, year = split_space
                digit_day = int(day)
                digit_month = int(months.index(month)) + 1
                digit_year = int(year)
                if digit_day <= 31 & digit_month <= 12:
                    print(f"{digit_year:02}-{digit_month:02}-{digit_day:02}")
                    break
        else:
            pass

    except (EOFError, ValueError):
        pass

