# Name: Aurora Crippen
# GitHub Repository: https://github.com/AuroraC25/csd-325.git
# Date: August 6, 2026
# Course: CSD 325-T301_2267_1 Advanced Python
# Assignment: Module 9.2 Assignment
# Description: Astronaut API Tutorial

import json
import requests

#Convert the astronaut data into readable JSON text
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

print("Connection status:")
print(response.status_code)

print("\nFormatted astronaut data:")
jprint(response.json())


