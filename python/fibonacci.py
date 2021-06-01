import re


def main():

    while True:
        # Prompt user, exit program if "-1"
        x = userPrompt()
        if x == -1:
            break

        if x is not None:
            first = 0
            second = 1
            print("------------------------------------------------------------")
            for i in range(0,x):
                if i==0:
                    current_sum = 0
                elif i==1:
                    current_sum = 1
                else:
                    current_sum = first + second

                print(f"{current_sum} ",end='')

                first = second
                second = current_sum
            print("\n------------------------------------------------------------\n")

def userPrompt():
    # Prompt user for nth number to print up to
    temp_nth = ""
    regex_passed = None
    # Accept only integers and negative one
    while not regex_passed:
        temp_nth = input("How many digits of the Fibonacci Sequence would you like (-1 to quit): ")
        regex_passed = re.search("^(([0-9]*)|(-1))$", temp_nth)
        if not regex_passed:
            print("Invalid integer. Please try again entering an integer.\n")
    return int(temp_nth)

main()
