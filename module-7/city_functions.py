# Name: Aurora Crippen
# GitHub Repository: https://github.com/AuroraC25/csd-325.git
# Date: July 21, 2026
# Course: CSD 325-T301_2267_1 Advanced Python
# Assignment: Module 7.2 Assignment
# Description: Unit Testing

def city_country(city, country, population=None, language=None):
    #Return a city, country, optional population, and optional 
    #language formatted as a single string
    location = f"{city.title()}, {country.title()}"
    
    if population:
        location += f" - population {population}"

    if language:
        location += f", {language.title()}"
    
    return location

if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("omaha", "united states", "488797"))
    print(city_country("tokyo", "japan", "37000000", "japanese"))
