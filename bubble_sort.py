def bubble_sort(list_to_sort):
    for i in range(0, len(list_to_sort) - 1):
        for j in range(0, len(list_to_sort) - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    return list_to_sort


def main():
    user_list = []
    print("Add numbers to your list (write 'stop' to end adding to your list).")
    while True:
        user_input = input("Add a number to your list: ")
        if user_input == "stop":
            break
        else:
            user_list.append(int(user_input))
    print("Your sorted list: ", bubble_sort(user_list))


if __name__ == "__main__":
    main()
