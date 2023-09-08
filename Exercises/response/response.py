import validators
import sys

def main():
    is_valid = validate(input("What is your email address? "))

    if is_valid:
        print("Valid")
    else:
        print("Invalid")

def validate(s):
    is_valid = validators.email(s)
    return is_valid == True


if __name__ == "__main__":
    main()