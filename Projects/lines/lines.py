import sys

# Counts lines of a python program

if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguements")


if len(sys.argv) == 2:
  filename = sys.argv[1]
  if filename.endswith(".py"):
    try:
      with open(filename, "r") as file:
        lines = file.readlines()
      numlines = 0
      for line in lines:
        the_line = line.lstrip()
        if len(the_line) != 0 and (the_line.startswith("#") != True):
          numlines = numlines +1
    except (FileNotFoundError):
      sys.exit("File does not exist")
  else:
    sys.exit("Not a Python file")


