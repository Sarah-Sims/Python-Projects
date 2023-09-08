from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) <= 2:
    sys.exit("Invalid usage")
if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font" or sys.argv[2] not in fonts :
        sys.exit("Invalid usage")


user_input = input("Input:")

# No font entered, use a random font
if len(sys.argv) == 1:

    rando_font = random.choice(fonts)
    figlet.setFont(font = rando_font)
    print(figlet.renderText(user_input))

# User entered font
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in fonts:
            figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(user_input))



