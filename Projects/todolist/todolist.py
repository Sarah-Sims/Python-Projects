import sys

def main():
    # WHat are you trying to put into the list
    print_list()
    add_list(input("Add to list:"))

    remove_item = input("Remove From list:")
    if remove_item.lower() == "no":
        sys.exit()
    remove_list(remove_item)

def add_list(item):
    #creating the list
    todo_list = []

    #Opening the file and writing into the txt
    with open("todo_list.txt", "r+") as file:
        for todo in file:
            todo_list.append(todo.rstrip())
        if item not in todo_list:
            file.write(f"{item}\n")

def print_list():
    #print text file to the terminal
    with open("todo_list.txt", "r+") as file:
        for line in file:
            print(line.rstrip())


def remove_list(x):
  #removed from the to do list
    #pass through the index of the to do

    with open("todo_list.txt", "r") as file:
        lines = file.readlines()
    with open("todo_list.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != x:
                file.write(line)



if __name__ == "__main__":
    main()