# Name: Aurora Crippen
# GitHub Repository: https://github.com/AuroraC25/csd-325.git
# Date: July 4, 2026
# Course: CSD 325-T301_2267_1 Advanced Python
# Assignment: Module 4.2 Assignment
# Description: Sitka Weather High/Low Temperatures
# Changes Made:
# Added a menu for Highs, Lows, and Exit.
# Added a loop so the user can keep choosing options.
# Added low temperature graph in blue.
# Added an exit message.
# Added functions to organize the program.

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt



# Load the weather data from the CSV file and store
# the dates, high temperatures, and low temperatures.
def load_weather_data():
    """Read dates, high temperatures, and low temperatures from the CSV file."""
    filename = 'sitka_weather_2018_simple.csv'

    #Create empty lists to store the weather information
    dates, highs, lows = [], [], []

    #Open the CSV file and read its contents
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Read each weather record from the file
        for row in reader:
            #Convert the date string into a datetime object
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            
            #Read the high and low temperatures
            high = int(row[5])
            low = int(row[6])

            #Store the weather information in the appropriate lists
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows



# Create and display a graph of either the high or
# low temperatures based on the user's selection.
def plot_temperatures(dates, temperatures, temp_type, color):
    """Create a temperature graph."""
    
    #Create the graph
    fig, ax = plt.subplots()
    
    #Plot the selected temperatures using the correct color
    ax.plot(dates, temperatures, c=color)

    #Format the graph title and labels
    plt.title(f"Daily {temp_type} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    #Display the graph
    plt.show()



# Display the menu options for the user.
def display_menu():
    """Display the menu choices."""
    print("\nSitka Weather Menu")
    print("Type High to view high temperatures.")
    print("Type Low to view low temperatures.")
    print("Type Exit to quit the program.")



# Control the overall flow of the program by loading
# the weather data, displaying the menu, processing
# user selections, and exiting when requested.
def main():
    """Run the Sitka weather menu program."""
    
    #Load all weather data before displaying the menu
    dates, highs, lows = load_weather_data()

    #Continue displaying the menu until the user chooses Exit
    while True:
        display_menu()
        
        #Read the user's menu selection
        choice = input("\nPlease enter your choice (High, Low, or Exit): ").strip().lower()

        #Display the high temperature graph
        if choice == "high":
            plot_temperatures(dates, highs, "high", "red")

        #Display the low temperature graph
        elif choice == "low":
            plot_temperatures(dates, lows, "low", "blue")

        #Exit the program
        elif choice == "exit":
            print("\nThank you for using the Sitka weather program. Goodbye!")
            sys.exit()

        #Data validation
        else:
            print("Invalid choice. Please enter High, Low, or Exit.")

#Start the program
if __name__ == "__main__":
    main()