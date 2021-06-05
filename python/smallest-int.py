"""
*********************************************************
*                                                       *
* Project Name: Smallest Integer                        *
* Author: github.com/kirigaine                          *
* Description: A simple program to search an array for  *
*   the smallest positive integer not in the array      *
* Requirements: None                                    *
*                                                       *
*********************************************************
"""

def main():

    array_a = [1,2,4,5,7,2,6]
    print(f"Smallest Integer Missing: {smallest_in_array(array_a)}")

def smallest_in_array(my_array):
    dict_a = {}
    smallest_int = 1

    if len(my_array) == 0:
        return 1

    for value in my_array:
        if value in dict_a:
            dict_a.update({value:(dict_a[value])+1})
        else:
            dict_a.update({value: 1})

    for i in range(1,max(my_array)+2):
        if i not in dict_a:
            smallest_int = i
            return smallest_int



main()