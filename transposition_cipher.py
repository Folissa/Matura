# transposition two adjacent digits
def transposition_adjacent(string):
    string_length = len(string)
    string_list = []
    for char in string:
        string_list.append(char)
    for index in range(0, string_length - 1, 2):
        temporary = string_list[index]
        string_list[index] = string_list[index + 1]
        string_list[index + 1] = temporary
    new_string = ""
    for char in string_list:
        new_string += char
    return new_string


def transposition_consonants(string):
    string_length = len(string)
    string_list = []
    is_first = 1
    first_value = ""
    first_index = None
    for char in string:
        string_list.append(char)
    for index in range(string_length):
        if is_a_consonant(string_list[index]):
            if is_first:
                first_index = index
                first_value = string_list[index]
                is_first = 0
            else:
                temporary = string_list[index]
                string_list[index] = first_value
                first_value = temporary
    if not is_first:
        string_list[first_index] = first_value
    new_string = ""
    for char in string_list:
        new_string += char
    return new_string


def transposition_consonants_decipher(string):
    string_length = len(string)
    string_list = []
    is_first = 1
    first_value = ""
    first_index = None
    for char in string:
        string_list.append(char)
    for index in range(string_length - 1, -1, -1):
        if is_a_consonant(string_list[index]):
            if is_first:
                first_index = index
                first_value = string_list[index]
                is_first = 0
            else:
                temporary = string_list[index]
                string_list[index] = first_value
                first_value = temporary
    if not is_first:
        string_list[first_index] = first_value
    new_string = ""
    for char in string_list:
        new_string += char
    return new_string


def is_a_consonant(char):
    vowels = {"a", "e",  "i", "o", "u", "y"}
    if char in vowels:
        return 0
    else:
        return 1


def main():
    user_string = input("Input a string to cipher: ")
    ciphering_metod = input("How would you like to cipher your string?:\n"
                            "(1) Transposition adjacent,\n"
                            "(2) Transposition consonants.\n"
                            "> ")
    if ciphering_metod == "1":
        ciphered = transposition_adjacent(user_string)
        print(f"Your string before: {user_string}, and after ciphering: {ciphered}.")
        print(f"Deciphering: {transposition_adjacent(ciphered)}.")
    elif ciphering_metod == "2":
        ciphered = transposition_consonants(user_string)
        print(f"Your string before: {user_string}, and after ciphering: {ciphered}.")
        print(f"Deciphering: {transposition_consonants_decipher(ciphered)}.")


if __name__ == "__main__":
    main()
