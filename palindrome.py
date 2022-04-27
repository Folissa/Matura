# palindrome is a string which is identical reversed to the original
def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def is_palindrome_list(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


def main():
    user_string = input("Input a string: ")
    print(is_palindrome_list(user_string))


if __name__ == "__main__":
    main()
