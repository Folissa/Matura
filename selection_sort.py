def main():
    user_list = [2, 1, 13, 41, 265, 43, 82, 63, 23, 100, 30, 10, 31, 4]
    print(f"Your list before sorting: {user_list}\n"
          f"Your list after sorting: {selection_sort(user_list)}")


def selection_sort(number_list):
    list_length = len(number_list)
    for i in range(list_length - 1):
        minimum_index = i
        for j in range(i + 1, list_length):
            if number_list[j] < number_list[minimum_index]:
                minimum_index = j
        if minimum_index != i:
            number_list[i], number_list[minimum_index] = number_list[minimum_index], number_list[i]
    return number_list


if __name__ == "__main__":
    main()
