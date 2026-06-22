# Name: Aurora Crippen
# GitHub Repository: https://github.com/AuroraC25/csd-325.git
# Date: June 21, 2026
# Course: CSD 325-T301_2267_1 Advanced Python
# Assignment: Module 2.2 Assignment
# Description: Documented Debugging and Flowchart

#Previous Course Assignment
#Course: CSD 205 Intro to Programming with Python
#Assignment: Module 11.2 Assignment
#Purpose: Demonstrate recursive and non-recursive methods
#for printing numbers from 1 through n.



def recursive_print(n, current=1):

    if current > n:
        return

    print(current)

    recursive_print(n, current + 1)


def non_recursive_print(n):

    for number in range(1, n + 1):
        print(number)


def main():

    # Input validation loop
    while True:
        try:
            n = int(input("Enter a positive integer greater than 0: "))

            if n <= 0:
                print("Error: Please enter a value greater than 0.\n")
            else:
                break

        except ValueError:
            print("Error: Please enter a valid integer.\n")

    print("\nRecursive Function")
    recursive_print(n)

    print("\nNon-Recursive Function")
    non_recursive_print(n)


if __name__ == "__main__":
    main()
