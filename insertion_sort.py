def insertion_sort(list_to_sort):
    for element_index in range(1, len(list_to_sort)):
        element = list_to_sort[element_index]
        insertion_index = element_index
        while insertion_index > 0 and list_to_sort[insertion_index - 1] > element:
            list_to_sort[insertion_index] = list_to_sort[insertion_index - 1]
            insertion_index -= 1
        list_to_sort[insertion_index] = element
    return list_to_sort


def main():
    user_list = []
    user_list_length = input("Input length of your list: ")
    for i in range(1, int(user_list_length) + 1):
        user_list.append(int(input(f"{i} number: ")))
    print(f"Your list before: {user_list}, and after: {insertion_sort(user_list)}.")


if __name__ == "__main__":
    main()
