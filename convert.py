# Author: Matt Karenbauer

from collections import deque


def hex_calc(value):
    """
    Calculates hexadecimal value of user-entered base-10 integer.

    As long as the remainder of the user-entered base-10 value and
    modulo 16 does not equal 0, the function stores the remainder 
    in a queue and uses a dictionary to assign remainders 10-15.
    Outputs the queue representation of the hex value at the end.

    Parameters: the user-entered base-10 integer

    Returns: None
    """
    hex_dict = {  # Dictionary for hex values over 9
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    hex_stack = deque()  # Queue to hold hexidecimal representation

    while value > 0:
        remainder = value % 16
        if remainder > 9:
            remainder = hex_dict[remainder]
            hex_stack.append(remainder)
        else:
            hex_stack.append(remainder)
        value = value // 16

    print("Hexadecimal Value: ", end="")
    while hex_stack:
        print(hex_stack.pop(), end="")


def binary_calc(value):
    """
    Calculates binary value of user-entered base-10 integer.

    As long as the remainder of the user-entered base-10 value and
    modulo 2 does not equal 0, the function stores the remainder 
    in a queue. Outputs the queue representation of the binary value 
    at the end.

    Parameters: the user-entered base-10 integer

    Returns: None
    """
    binary_stack = deque()  # Queue to hold binary representation

    while value > 0:
        remainder = value % 2
        binary_stack.append(remainder)  # Add binary digit to queue
        value = value // 2

    print("Binary Value: ", end="")
    while binary_stack:
        print(binary_stack.pop(), end="")


def setup():
    """
    Starting point for the program.

    Asks user for a base-10, positive decimal integer and calls the 
    binary_calc and hex_calc functions for computation. The program will
    loop, asking the user for a new number as long as they do not enter 
    the string "quit".

    Parameters: None

    Returns: None
    """
    value = input("Enter a positive decimal integer (\"quit\" to stop): ")

    while value.lower() != "quit":
        binary_calc(int(value))  # Calls converter function on inputted value
        print("\n")
        hex_calc(int(value))  # Calls converter function on inputted value
        value = input(
            "\nEnter a positive decimal integer (\"quit\" to stop): ")


setup()
