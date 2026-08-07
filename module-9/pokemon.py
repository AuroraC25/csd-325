# Name: Aurora Crippen
# GitHub Repository: https://github.com/AuroraC25/csd-325.git
# Date: August 6, 2026
# Course: CSD 325-T301_2267_1 Advanced Python
# Assignment: Module 9.2 Assignment
# Description: PokeAPI 


import json
import requests


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


url = "https://pokeapi.co/api/v2/pokemon/mew"

response = requests.get(url)

print("Connection status:")
print(response.status_code)

print("\nFormatted Pokemon Data:")
jprint(response.json())