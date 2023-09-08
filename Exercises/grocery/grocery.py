myitems = {}


while True:
    try:
        mylist = input().upper()

        if mylist not in myitems:
            myitems[mylist] = 1
        else:
                myitems[mylist] = myitems[mylist] +1

    except (EOFError):
        break

for x in sorted(myitems):
    print(myitems[x], x)

