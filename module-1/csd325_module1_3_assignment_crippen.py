# Name: Aurora Crippen
# Date: June 13, 2026
# Course: CSD 325-T301_2267_1 Advanced Python
# Assignment: Module 1.3 Assignment
# Description: Bottles On the Wall

#Countdown function - receives the number entered by the user
def countdown_bottles(bottles):

    #loop that continues as long as the number of bottles is greater than 0
    while bottles > 0:

        #variable named word to keep grammar correct for bottle / bottles
        word = "bottle" if bottles == 1 else "bottles"

        #prints first line of song
        print(f"{bottles} {word} of beer on the wall, {bottles} {word} of beer.")

        #checks whether the number in the second line of the song will be 1 for bottle
        if bottles - 1 == 1:
            next_word = "bottle"
        else:
            next_word = "bottles"

        #checks if there is more than one bottle remaining otherwise it'll print the last line
        if bottles > 1:
            print(f"Take one down and pass it around, {bottles - 1} {next_word} of beer on the wall.\n")
        else:
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")

        bottles -= 1

#main function
def main():

    #prompt user for how many bottles
    bottles = int(input("How many bottles of beer are on the wall? "))

    #input validation and pass the user input to the countdown function
    if bottles <= 0:
        print("Please enter a number greater than 0.")
    else:
        countdown_bottles(bottles)
        print("Time to buy more bottles of beer!")

#Checks whether this file is being run directly
if __name__ == "__main__":
    main()