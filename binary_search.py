from insertion_sort import insertion_sort


def binary_search(searched_array, searched_number):
    beginning_index = 0
    end_index = len(searched_array) - 1
    while beginning_index <= end_index:
        middle_of_array = (beginning_index + end_index) // 2
        if searched_array[middle_of_array] == searched_number:
            return f"Your number is on {middle_of_array} position."
        elif searched_array[middle_of_array] < searched_number:
            beginning_index = middle_of_array + 1
        else:
            end_index = middle_of_array - 1
    return "Your number doesn't exist in the array"


def main():
    user_list = []
    user_list_length = input("Input length of your list: ")
    for i in range(1, int(user_list_length) + 1):
        user_list.append(int(input(f"{i} number: ")))
    number = int(input("Input the number you are looking for in array: "))
    print(binary_search(insertion_sort(user_list), number))


if __name__ == "__main__":
    main()
