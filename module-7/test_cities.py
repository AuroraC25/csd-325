# Name: Aurora Crippen
# GitHub Repository: https://github.com/AuroraC25/csd-325.git
# Date: July 21, 2026
# Course: CSD 325-T301_2267_1 Advanced Python
# Assignment: Module 7.2 Assignment
# Description: Tests for city_functions.py

import unittest

from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    #Tests for the city_country() function.

    def test_city_country(self):
        #Does a city and country such as Santiago, Chile work?
        formatted_location = city_country("santiago", "chile")
        self.assertEqual(formatted_location, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()



