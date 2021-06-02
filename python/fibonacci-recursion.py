"""
*********************************************************
*                                                       *
* Project Name: Recursive Fibonacci Sequence            *
* Author: github.com/kirigaine                          *
* Description: A simple program to put in how many      *
*   numbers of the Fibonacci Sequence you would like.   *
* Requirements: Python Standard Library (re)            *
*                                                       *
*********************************************************
"""

import re

def main():

    while True:
        # Prompt user, exit program if "-1"
        x = userPrompt()
        if x == -1:
            break
        print("------------------------------------------------------------")
        print(str(fibbonachi(x)))
        print("------------------------------------------------------------\n") 


def userPrompt():
    # Prompt user for nth number to print up to
    temp_nth = ""
    regex_passed = None
    # Accept only integers and negative one
    while not regex_passed:
        temp_nth = input("How many digits of the Fibonacci Sequence would you like (-1 to quit): ")
        regex_passed = re.search("^(([0-9]*)|(-1))$", temp_nth)
        if not regex_passed:
            print("Invalid integer. Please try again entering a positive integer (or -1 to quit).\n")
    return int(temp_nth)

def fibbonachi(x):
    # fibonacci(x) == fibonacci(x-1) + fibonacci(x-2)
    # ...
    # fibonacci(4) = fibonacci(3) + fibonacci(2)
    # fibonacci(3) = fibonacci(2) + fibonacci(1)
    # fibonacci(2) = 1
    # fibonacci(1) = 0
    if x is not None:
        if x==0:
            # If you request none, you get none!
            return None
        elif x==1:
            return 0
        elif x==2:
            return 1
        else:
            # print(f"{x-1} {x-2}")
            return(fibbonachi(x-1) + fibbonachi(x-2))


main()