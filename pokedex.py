from pokemon import id_or_name
from ability import search_ability

while True:
    print("\nSelect: \n1- Search by name or ID")
    print("2- Search hability \n3- Search by type \n4- Finish Program \n")
    options = [1, 2, 3, 4]

    try:
        e = 2 #test_mode --------------------------- #e = int(input("Action: "))
        if e not in options:
            raise ValueError

    except ValueError:
        print("\nInvalid action\n")
        continue

    if e == 1: #Search Pokémon by name or ID
        search = input("Name or ID: ")
        id_or_name(search)

    if e == 2: #Search specific ability
        search = input("Name of the ability: ").lower()
        search.replace(" ", "-")
        search_ability()

    if e == 3: #Search specific type
        pass

    if e == 4:
        print("Ending program...") #End
        break