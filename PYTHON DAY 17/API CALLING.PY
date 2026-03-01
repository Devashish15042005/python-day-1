import requests

url = "https://pokeapi.co/api/v2/pokemon/charizard"
def pokemon():
    response = requests.get(url)
    print(response)
