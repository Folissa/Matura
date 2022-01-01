def main():
    user_list = [3, 4, 2, 13, 491, 200, 1200]
    print(f"Minimum number in the list: {min_and_max(user_list)[0]}. "
          f"Maximum number in the list: {min_and_max(user_list)[1]}.")


def min_and_max(number_list):
    minimum = number_list[0]
    maximum = number_list[0]
    for index in range(1, len(number_list)):
        if number_list[index] > maximum:
            maximum = number_list[index]
        elif number_list[index] < minimum:
            minimum = number_list[index]
    return minimum, maximum


if __name__ == "__main__":
    main()

