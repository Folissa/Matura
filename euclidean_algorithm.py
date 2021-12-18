def main():
    first_number = int(input("First number:"))
    second_number = int(input("Second number:"))
    print(f"NWD({first_number},{second_number}) = {optimized_euclidean_algorithm(first_number, second_number)}")
    print(f"NWW({first_number},{second_number}) = {NWW(first_number, second_number)}")


# for first_number and second_number being an integer
def euclidean_algorithm(first_number, second_number):
    # for second_number > 0
    if first_number == 0:
        return second_number
    # for first_number > 0
    elif second_number == 0:
        return first_number
    # for first_number > 0 and second_number > 0
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        else:
            second_number -= first_number
    return first_number


def optimized_euclidean_algorithm(first_number, second_number):
    while second_number != 0:
        temporary = second_number
        second_number = first_number % second_number
        first_number = temporary
    return first_number


def NWW(first_number, second_number):
    # if a != 0 and b !=0
    return first_number * second_number // euclidean_algorithm(first_number, second_number)


if __name__ == "__main__":
    main()
