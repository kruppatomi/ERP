""" Common module
implement commonly used functions here
"""

import random
import data_manager
import ui


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """
    import random

    printer = []
    for i in range(2):
        lowercase = random.choice("abcdefghijklmnopqrstuvwxyz")
        for j in lowercase:
            printer.append(j)

        uppercase = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for j in uppercase:
            printer.append(j)

        numbers = random.choice("0123456789")
        for j in numbers:
            printer.append(j)

        characters = random.choice("[!@#$%^&*()?]")
        for j in characters:
            printer.append(j)

    random.shuffle(printer)

    generated = str(''.join(printer))
    
    return generated

