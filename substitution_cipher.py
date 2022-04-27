def caesar_cipher(string, key):
    new_string = ""
    for char in string:
        if 65 <= ord(char) <= 90:
            new_string += chr((ord(char) - 65 + key) % 26 + 65)
        elif 97 <= ord(char) <= 122:
            new_string += chr((ord(char) - 97 + key) % 26 + 97)
    return new_string


def caesar_decipher(string, key):
    new_string = ""
    for char in string:
        if 65 <= ord(char) <= 90:  # or use "if char.isupper():"
            new_string += chr((ord(char) - 65 - key) % 26 + 65)
        elif 97 <= ord(char) <= 122:  # or use "elif not char.isupper():"
            new_string += chr((ord(char) - 97 - key) % 26 + 97)
    return new_string


def main():
    user_string = input("Input a string to cipher: ")
    user_key = int(input("Input a key to cipher with: "))
    print("Your string:", user_string)
    string_ciphered = caesar_cipher(user_string, user_key)
    print("String ciphered:", string_ciphered)
    print("String deciphered:", caesar_decipher(string_ciphered, user_key))


if __name__ == "__main__":
    main()
