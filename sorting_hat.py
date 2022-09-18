names = input()
flag = 0
while names != "Welcome!" and flag == 0:
    if len(names) < 5:
        print(f"{names} goes to Gryffindor.")
    elif len(names) == 5:
        print(f"{names} goes to Slytherin.")
    elif len(names) == 6:
        print(f"{names} goes to Ravenclaw.")
    elif len(names) > 6 and names != "Voldemort":
        print(f"{names} goes to Hufflepuff.")
    elif names == "Voldemort":
        print(f"You must not speak of that name!")
        flag = 1
        break
    names = input()
if flag == 0:
    print(f"Welcome to Hogwarts.")

