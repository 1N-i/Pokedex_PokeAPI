from search import search_id_or_name, search_type, search_move, search_ability

while True:
    print("\nSelect: \n1- Search by name or ID")
    print("2- Search by type \n3- Search move \n4- Search hability \n5- Finish Program")
    options = [1, 2, 3, 4, 5]

    try: #Data verification
        e = int(input("Action: "))
        if e not in options:
            raise ValueError

    except ValueError:
        print("Invalid action")
        continue

    if e == 1: #Search Pokémon by name or ID
        search1 = input("\nName or ID: ")
        search_id_or_name(search1)
        
    if e == 2: #Search specific type
        search2 = input("\nType: ")
        search_type(search2)
        
    if e == 3: #Search move
        search3 = input("\nMove: ")
        search_move(search3)

    if e == 4: #Search specific ability
        search4 = input("\nAbility name: ")
        search_ability(search4)
        
    if e == 5:
        print("Ending program...") #End
        break