"""
This script reverses a string and swaps its case.

It is designed to take one or more command-line arguments, merge them
into a single string, reverse the string, swap the case of each 
character, and then print the result. If no arguments are provided, 
it prints a usage message.

Functions:
- reverse_and_swap_case(s): Reverses the string s and swaps its case.
- main(): Processes command-line arguments and invokes reverse_and_swap_case.

Usage:
To run the script, use the following command in the terminal:
$ python3 exec.py <string1> <string2> ...

Example:
$ python3 exec.py 'Hello World!' 
!DLROw OLLEh

$ python3 exec.py 'Hello' 'my Friend'
DNEIRf YM OLLEh
"""
import sys

def reverse_and_swap_case(s):
    """
    Reverse the input string using the slicing operator and swap 
    the case of each character.

    Parameters:
    s (str): The string to be reversed and case-swapped.

    Returns:
    The modified string with its characters reversed and case swapped.
    """
    return s[::-1].swapcase()

def main():
    """
    Main function to process command-line arguments.

    If arguments are provided, merges them into a single string,
    reverses the string, swaps the case, and prints the result.
    Otherwise, prints a usage message.
    """
    if len(sys.argv) > 1:
        combined_string = " ".join(sys.argv[1:])
        result = reverse_and_swap_case(combined_string)
        print(result)
    else:
        print("Usage: python3 exec.py <string1> <string2> ...")

if __name__ == "__main__":
    main()
