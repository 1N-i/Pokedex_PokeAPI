import requests

def id_or_name(search):
    url_busca = f"https://pokeapi.co/api/v2/pokemon/{search}"  # Link PokeAPI
    requested = requests.get(url_busca)
    if requested.status_code == 404:
        print(f"Error: '{search}' not found")  # Finish if nothing was found
        return

    data = requested.json()
    print(f"\nPokémon: {data["name"]}")

    type1 = data["types"][0]["type"]["name"]
    type2 = data["types"][-1]["type"]["name"]

    if type1 == type2:
        print(f"Type: {type1}")

    else:
        print(f"Type: {type1}")
        print(f"Type: {type2}")

    print(f"ID: {data["id"]}")