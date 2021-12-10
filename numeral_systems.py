import math
import time


def decimal_to_other_system(decimal_number, other_system_base):
    number_in_new_system = ""
    while decimal_number != 0:
        number_in_new_system = str(decimal_number % other_system_base) + number_in_new_system
        decimal_number //= other_system_base
    return number_in_new_system


def decimal_to_hexadecimal(decimal_number):
    hexadecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    number_in_new_system = ""
    while decimal_number != 0:
        number_in_new_system = hexadecimal[(decimal_number % 16)] + number_in_new_system
        decimal_number //= 16
    return number_in_new_system


def other_system_to_decimal(number_in_other_system, numeral_system_base):
    list_of_digits = []
    decimal_number = 0
    for i in (str(number_in_other_system)):
        list_of_digits.append(i)
    #  First solution:
    """
    list_of_digits.reverse()
    for i in range(len(str(number_in_other_system))):
        decimal_number += int(list_of_digits[i]) * numeral_system_base ** i
    """
    #  Second solution:
    for i in range(len(str(number_in_other_system)) - 1, -1, -1):
        decimal_number += int(list_of_digits[len(str(number_in_other_system)) - 1 - i]) * int(numeral_system_base) ** i
    return decimal_number


def hexadecimal_to_decimal(number_in_other_system, numeral_system_base):
    hexadecimal = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11,
                   "C": 12, "D": 13, "E": 14, "F": 15}
    list_of_digits = []
    decimal_number = 0
    for i in (str(number_in_other_system)):
        list_of_digits.append(i)
    """
    #  First solution:
    list_of_digits.reverse()
    for i in range(len(str(number_in_other_system))):
        decimal_number += hexadecimal.get(list_of_digits[i]) * int(numeral_system_base) ** i
    """
    #  Second solution:
    for i in range(len(str(number_in_other_system)) - 1, -1, -1):
        decimal_number += hexadecimal.get(list_of_digits[len(str(number_in_other_system)) - 1 - i])\
                          * int(numeral_system_base) ** i
    return decimal_number


def bin_to_others(binary_number, numeral_system_base):
    hexadecimal = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B",
                   12: "C", 13: "D", 14: "E", 15: "F"}
    numeral_base_grouping_number = int(math.log2(int(numeral_system_base)))
    grouped_digits = []
    grouped_digits_list = []
    new_number = ''
    while len(binary_number) % numeral_base_grouping_number != 0:
        binary_number = '0' + binary_number
    while binary_number != '':
        for i in range(numeral_base_grouping_number):
            grouped_digits.append(binary_number[i])
        grouped_digits_list.append(grouped_digits)
        grouped_digits = []
        binary_number = binary_number[numeral_base_grouping_number:]
    for i in grouped_digits_list:
        i.reverse()
        new_digit = 0
        if numeral_system_base == "16":
            for j in range(len(i)):
                new_digit += 2 ** j * int(i[j])
            new_number = new_number + hexadecimal.get(new_digit)
        else:
            for j in range(len(i)):
                new_digit += 2 ** j * int(i[j])
            new_number = new_number + str(new_digit)
    return new_number


# TODO: Make conversion from others to BIN.


while True:
    action = input("Please choose an action you want to perform:\n"
                   "(1) Convert a decimal to a number in a different numeral system.\n"
                   "(2) Convert a number in different numeral system to a decimal.\n"
                   "(3) Convert a binary number to other system (4, 8, 16).\n"
                   "> ")
    if action == "1":
        number = input("Please input an integer, decimal number you want to convert: ")
        numeral_system = input("What system do you want to use (2, 4, 8, 10, 16)?: ")
        if numeral_system == "16":
            print(f"Number {number} in {numeral_system} base system is {decimal_to_hexadecimal(int(number))}.")
            break
        else:
            print(f"Number {number} in {numeral_system} base system is"
                  f" {decimal_to_other_system(int(number), int(numeral_system))}.")
            break
    elif action == "2":
        number = input("Please input a number you want to convert to a decimal (System base: 2, 4, 8, 10, 16): ")
        numeral_system = input("What is the numeral system of this number?: ")
        if numeral_system == "16":
            print(f"Number {number} in {numeral_system} base system is"
                  f" {hexadecimal_to_decimal(number, int(numeral_system))} as decimal.")
            break
        else:
            print(f"Number {number} in {numeral_system} base system is"
                  f" {other_system_to_decimal(number, int(numeral_system))} as decimal.")
            break
    elif action == "3":
        number = input("Please input a binary number you want to convert to the other system: ")
        numeral_system = input("What system do you want to use in a new number?: ")
        print(f"Binary number {number} in new system ({numeral_system}) is {bin_to_others(number, numeral_system)}.")
        break
    else:
        print("There is no such option.")
        time.sleep(1.5)