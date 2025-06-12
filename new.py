import requests

baseUrl = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(name):
    url = f"{baseUrl}/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Pokémon not found.")

name = input("Enter the name of the Pokémon: ")
pokemon= get_pokemon(name)

if pokemon:
    print(f"name: {pokemon['name']}")
    print(f"height: {pokemon['height']}")
    print(f"weight: {pokemon['weight']}")
    print("Abilities:")