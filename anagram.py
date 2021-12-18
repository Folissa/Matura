# anagram to wyraz lub zdanie powstałe po przestawieniu liter innego wyrazu (zdania)

def main():
    first_word = input("Input first word: ")
    second_word = input("Input second word: ")
    print(anagram(first_word, second_word))


def anagram(first_word, second_word):
    chars = {}
    if len(first_word) != len(second_word):
        return False
    else:
        for i in first_word:
            if i not in chars:
                chars[i] = 1
            else:
                chars[i] += 1
        for i in second_word:
            if i in chars:
                chars[i] -= 1
        for i in chars:
            if chars[i] != 0:
                return False
        return True


if __name__ == "__main__":
    main()
