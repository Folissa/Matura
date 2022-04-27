def pattern_in_text(text, pattern):
    pattern_not_found = True
    for i in range(len(text) - len(pattern) + 1):
        pattern_check = True
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                pattern_check = False
                break
        if pattern_check:
            print(f"Found pattern at index {i}.")
            pattern_not_found = False
    if pattern_not_found:
        print("Pattern not found.")


def main():
    text = input("Input a word: ")
    pattern = input("Input a pattern: ")
    pattern_in_text(text, pattern)


if __name__ == "__main__":
    main()
