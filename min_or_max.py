def main():
    user_list = [0, 123, 12, 1, 43, 902, 12, 9000]
    print("Minimum:", minimum(user_list))
    print("Maximum:", maximum(user_list))


def minimum(number_list):
    minimum_number = number_list[0]
    for index in range(1, len(number_list)):
        if number_list[index] < minimum_number:
            minimum_number = number_list[index]
    return minimum_number


def maximum(number_list):
    maximum_number = number_list[0]
    for index in range(1, len(number_list)):
        if number_list[index] > maximum_number:
            maximum_number = number_list[index]
    return maximum_number


if __name__ == "__main__":
    main()
