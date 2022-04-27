def change_to_other_base(number, base):
    new_number = ""
    while number > 0:
        digit = str(number % base)
        new_number = digit + new_number
        number = number // base
    return new_number


def narcistic_numbers(number, base):
    end_sum = 0
    changed_number = change_to_other_base(number, base)
    for digit in changed_number:
        end_sum += int(digit) ** len(changed_number)
    if end_sum == number:
        return True
    else:
        return False


def main():
    for i in range(10000):
        if narcistic_numbers(i, 10):
            print(i)


if __name__ == "__main__":
    main()
