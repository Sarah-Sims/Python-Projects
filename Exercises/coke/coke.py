'''
Tallys coins entered until amount_due
is less than zero, then calculates change.
'''

amount_due = 50

good_coins = [ 1, 5, 10, 25, 50]

while amount_due > 0:
    insert_coin = int(input("Insert Coin:"))

    if insert_coin in good_coins:
        amount_due = amount_due - insert_coin

    if amount_due > 0:
        print("Amount Due:", amount_due)

change_owed = abs(amount_due)
print("Change Owed:", change_owed)

