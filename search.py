import requests

def create_data(search_type, search): #Sends data to the functions that called it
    url_search = f"https://pokeapi.co/api/v2/{search_type}/{search}" #Link PokeAPI
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search}' not found") #Finish if nothing was found
        return "error"
    return requested.json()

#-------------------------------------------------------------
def data_verification(options): #Data verification
    while True:
        try:
            action = int(input("Action: "))
            if action not in options:
                raise ValueError
            return action

        except ValueError:
            print("Invalid action\n")

#-------------------------------------------------------------
def search_id_or_name(search): #Search Pokémon by name or ID
    data = create_data("pokemon", search)
    if data == "error":
        return

    print(f"\nID: {data["id"]}") #ID
    print(f"Pokémon: {data["name"]}") #Name

    type1 = data["types"][0]["type"]["name"]
    type2 = data["types"][-1]["type"]["name"]

    if type1 == type2: #Mono-type
        print(f"Type: {type1}")

    else: #Dual-type
        print(f"Type: {type1}")
        print(f"Type: {type2}")

    while True:
        print("\nSelect: \n1- See moves \n2- See abilities \n3- End search\n")
        action = data_verification([1, 2, 3])

        if action == 1: #Show moves
            print(f"\nMoves that {data["name"]} can learn:")
            for attack in data["moves"]:
                print(attack["move"]["name"])

        if action == 2: #Show hability
            print(f"\nAbilities that {data["name"]} can have:")
            for ability in data["abilities"]:
                print(ability["ability"]["name"])

        if action == 3: #End search
            print(f"\nEnding search on '{data["name"]}'")
            break

#-------------------------------------------------------------
def search_type(search): #Search specific type
    search = search.lower()
    data = create_data("type", search)
    if data == "error":
        return

    while True:
        print(f"\nSelect: \n1- See all {search} type pokémon \n2- See {search}:type pokémon")
        print(f"3- See {search} type moves \n4- See {search} type chart \n5- End search\n")
        action = data_verification([1, 2, 3, 4, 5])

        if action == 1: #See pokémon
            print(f"\n{search} type pokémon:")
            for pokemon in data["pokemon"]:
                print(pokemon["pokemon"]["name"])

        if action == 2: #Search with secondary type
            def pokemon_list():
                type_list = []
                for pokemon in data["pokemon"]:
                    type_list.append(pokemon["pokemon"]["name"])
                return type_list

            type1 = pokemon_list()

            search2 = input("\nType: ")
            data = create_data("type", search2)
            if data == "error":
                search_type(search)
                return
            
            type2 = pokemon_list()

            print(f"{search}:{search2} pokémon:")
            for a in type1:
                for b in type2:
                    if a == b:
                        print(b)
            
        if action == 3: #See moves
            for move in data["moves"]:
                print(move["name"])

        if action == 4: #See type chart
            def chart(text):
                list = []

                for type in data["damage_relations"][text]:
                    list.append(type["name"])
                return list

            print(f"2x damage from-to:\n{chart("double_damage_from")} -> {search} -> {chart("double_damage_to")}\n")
            print(f"1/2x damage from-to:\n{chart("half_damage_from")} -> {search} -> {chart("half_damage_to")}\n")
            print(f"0x damage from-to:\n{chart("no_damage_from")} -> {search} -> {chart("no_damage_to")}")

        if action == 5: #End search
            print(f"Ending search on '{search}'")
            break

#-------------------------------------------------------------
def search_move(search): #Search a move
    data = create_data("move", search)
    if data == "error":
        return
    
    #Data Verification

    #To Do
    pass

#-------------------------------------------------------------
def search_ability(search):  #Search ability
    search = src_msg = search.lower()
    search = search.replace(" ", "-")

    data = create_data("ability", search)
    if data == "error":
        return

    for ability in data["effect_entries"]:
        if ability["language"]["name"] == "en":
            print(f"\nEffect: \n{ability["effect"].replace("\n\n", "\n")}")
            print(f"\nShort version: \n{ability["short_effect"].replace("\n\n", "\n")}")

    while True:
        print("\nSelect: \n1- See Pokémon with this ability \n2- End search\n")
        action = data_verification([1, 2])

        if action == 1:
            print(f"\nPokémon with '{src_msg}' naturally:")
            for pokemon in data["pokemon"]:
                if pokemon["is_hidden"] == False:
                    print(f"{pokemon["pokemon"]["name"]}")
                
            print(f"\nPokémon with '{src_msg}' as a hidden ability:")
            for pokemon in data["pokemon"]:
                if pokemon["is_hidden"] == True:
                    print(f"{pokemon["pokemon"]["name"]}")

        if action == 2: #End search
            print(f"Ending search on '{src_msg}'")
            break