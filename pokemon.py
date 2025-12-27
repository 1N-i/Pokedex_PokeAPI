import requests

def id_or_name(search):
    url_search = f"https://pokeapi.co/api/v2/pokemon/{search}" #Link PokeAPI
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search}' not found") #Finish if nothing was found
        return
    
    data = requested.json()

    print(f"\nID: {data["id"]}") #ID
    print(f"Pokémon: {data["name"]}") #Name

    type1 = data["types"][0]["type"]["name"]
    type2 = data["types"][-1]["type"]["name"]

    if type1 == type2: #Mono-type
        print(f"Type: {type1}")

    else: #Dual-type
        print(f"Type: {type1}")
        print(f"Type: {type2}")

    #To do: Show generation origin

    while True: #New menu
        print("\nSelect: \n1- See moves \n2- See abilities \n3- End search")
        a = int(input("\nAction: "))

        if a == 1: #Show moves
            print(f"Moves that {data["name"]} can learn:")
            for attack in data["moves"]:
                print(attack["move"]["name"])

        if a == 2: #Show hability
            print(f"Abilities that {data["name"]} can have:")
            for ability in data["abilities"]:
                print(ability["ability"]["name"])

        if a == 3: #End search
            print(f"Ending search on '{data["name"]}'")
            break