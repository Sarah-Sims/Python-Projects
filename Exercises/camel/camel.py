'''
Outputs user entered
text in camelCase
'''

user = input("camelCase:")

for c in user:
    if c.islower():
        print(c, end="")
    else:
        print("_" + c.lower(), end="")
print()
