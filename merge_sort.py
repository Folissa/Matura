def merge(first_list, second_list):
    first_length = len(first_list)
    second_length = len(second_list)
    first_index = 0
    second_index = 0
    new_list = []
    while first_index <= first_length - 1 and second_index <= second_length - 1:
        if first_list[first_index] < second_list[second_index]:
            new_list.append(first_list[first_index])
            first_index += 1
        else:
            new_list.append(second_list[second_index])
            second_index += 1
    for remaining_index in range(first_index, first_length):
        new_list.append(first_list[remaining_index])
    for remaining_index in range(second_index, second_length):
        new_list.append(second_list[remaining_index])
    return new_list


def merge_sort(list_to_sort):
    if len(list_to_sort) > 1:
        mid = len(list_to_sort) // 2
        left_list = list_to_sort[:mid]
        right_list = list_to_sort[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list_to_sort[k] = left_list[i]
                i += 1
            else:
                list_to_sort[k] = right_list[j]
                j += 1
            k += 1
        while i < len(left_list):
            list_to_sort[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            list_to_sort[k] = right_list[j]
            j += 1
            k += 1


def main():
    # if two lists are sorted we can merge them with merge()
    user_first_list = [3, 5, 23, 62, 100, 300]
    user_second_list = [1, 4, 5, 24, 299, 2900, 5000]
    print(merge(user_first_list, user_second_list))
    # sorting one, not sorted list
    user_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    merge_sort(user_list)
    print(user_list)


if __name__ == "__main__":
    main()
