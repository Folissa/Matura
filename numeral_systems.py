import math
import time

hexadecimal = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
               "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
subscript = {"2": "₂", "4": "₄", "8": "₈", "10": "₁₀", "16": "₁₆"}


def main():
    while True:
        action = input("Please choose an action you want to perform:\n"
                       "(1) Convert the decimal number to a different numeral system (2, 4, 8, or 16).\n"
                       "(2) Convert the number (2, 4, 8, or 16 base) to decimal.\n"
                       "(3) Convert the binary number to a different numeral system (4, 8, or 16).\n"
                       "(4) Convert the number (4, 8, or 16 base) to binary.\n"
                       "> ")
        if action == "1":
            number = input("Please input the number you want to convert: ")
            numeral_system = input("What system do you want to use?: ")
            print(f"{decimal_to_other_system(int(number), numeral_system)}{subscript.get(numeral_system)}")
            break
        elif action == "2":
            number = input("Please input the number you want to convert: ")
            numeral_system = input("What is the numeral system of this number?: ")
            print(f"{other_system_to_decimal(number, numeral_system)}₁₀")
            break
        elif action == "3":
            number = input("Please input the number you want to convert: ")
            numeral_system = input("What system do you want to use?: ")
            print(
                f"{bin_to_others(number, numeral_system)}{subscript.get(numeral_system)}")
            break
        elif action == "4":
            number = input("Please input the number you want to convert: ")
            numeral_system = input("What is the numeral system of this number?: ")
            print(
                f"{others_to_bin(number, numeral_system)}₂")
            break
        else:
            print("There is no such option.")
            time.sleep(1.5)


def strip_from_zero(number_to_strip):
    i = 0
    while True:
        if number_to_strip[i] == "0":
            number_to_strip = number_to_strip[i+1:]
        else:
            break
        i += 1
    return number_to_strip


def decimal_to_other_system(decimal_number, other_system_base):
    hexadecimal_strings = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    number_in_new_system = ""
    if other_system_base == "16":
        while decimal_number != 0:
            number_in_new_system = hexadecimal_strings[(decimal_number % 16)] + number_in_new_system
            decimal_number //= 16
    else:
        while decimal_number != 0:
            number_in_new_system = str(decimal_number % int(other_system_base)) + number_in_new_system
            decimal_number //= int(other_system_base)
    return number_in_new_system


def other_system_to_decimal(number_in_other_system, numeral_system_base):
    list_of_digits = []
    decimal_number = 0
    for i in (str(number_in_other_system)):
        list_of_digits.append(i)
    if numeral_system_base == "16":
        #  First solution:
        """
        list_of_digits.reverse()
        for i in range(len(str(number_in_other_system))):
            decimal_number += hexadecimal.get(list_of_digits[i]) * int(numeral_system_base) ** i
        """
        #  Second solution:
        for i in range(len(str(number_in_other_system)) - 1, -1, -1):
            decimal_number += hexadecimal.get(list_of_digits[len(str(number_in_other_system)) - 1 - i]) \
                              * int(numeral_system_base) ** i
    else:
        #  First solution:
        """
        list_of_digits.reverse()
        for i in range(len(str(number_in_other_system))):
            decimal_number += int(list_of_digits[i]) * numeral_system_base ** i
        """
        #  Second solution:
        for i in range(len(str(number_in_other_system)) - 1, -1, -1):
            decimal_number += int(list_of_digits[len(str(number_in_other_system)) - 1 - i])\
                              * int(numeral_system_base) ** i
    return decimal_number


def bin_to_others(binary_number, numeral_system_base):
    hexadecimal_str = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
                       10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
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
            new_number = new_number + hexadecimal_str.get(new_digit)
        else:
            for j in range(len(i)):
                new_digit += 2 ** j * int(i[j])
            new_number = new_number + str(new_digit)
    return new_number


def others_to_bin(number_in_other_system, numeral_system_base):
    grouped_digits = []
    numeral_base_grouping_number = int(math.log2(int(numeral_system_base)))
    for i in range(len(number_in_other_system)):
        grouped_digits.append([])
        if numeral_system_base == "16":
            for bin_digit in decimal_to_other_system(hexadecimal.get(number_in_other_system[i]), 2):
                grouped_digits[i].append(str(bin_digit))
        else:
            for bin_digit in decimal_to_other_system(int(number_in_other_system[i]), 2):
                grouped_digits[i].append(str(bin_digit))
        while len(grouped_digits[i]) % numeral_base_grouping_number != 0:
            grouped_digits[i].reverse()
            grouped_digits[i].append("0")
            grouped_digits[i].reverse()
    new_number = ""
    for i in range(len(grouped_digits)):
        for j in range(len(grouped_digits[i])):
            new_number += grouped_digits[i][j]
    return new_number


if __name__ == "__main__":
    main()
