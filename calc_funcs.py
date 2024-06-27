"""
The main functions for my calculator project.
"""

def get_num(msg):
    """
    Returns a valid number chosen by the user.
    msg = message for user.
    """
    typing = True
    while typing:
        try:
            inp = int(input(msg))
        except:
            print("Please enter a number.")
        else:
            typing = False
            return inp


def two_nums():
    """
    Prompts the user for two numbers and returns them as a tuple.
    """
    num1 = get_num("Value 1: ")
    num2 = get_num("Value 2: ")
    return (num1, num2)


def add(n1, n2):
    """
    Adds two numbers.
    """
    return n1+n2


def subtract(n1, n2):
    """
    Subtracts two numbers.
    """
    return n1-n2


def multiply(n1, n2):
    """
    Multiplies two numbers.
    """
    return n1*n2


def divide(n1, n2):
    """
    Divides two numbers.
    """
    return n1/n2