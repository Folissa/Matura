#  Lomuto partition scheme
def partitioning_lomuto(number_list, lesser, greater):
    i = lesser - 1
    pivot = number_list[greater]
    for j in range(lesser, greater):
        if number_list[j] <= pivot:
            i += 1
            number_list[i], number_list[j] = number_list[j], number_list[i]
    number_list[i + 1], number_list[greater] = number_list[greater], number_list[i + 1]
    return i + 1


def quick_sort_lomuto(number_list, lesser, greater):
    if len(number_list) < 2:
        return number_list
    if lesser < greater:
        partitioning_index = partitioning_lomuto(number_list, lesser, greater)
        quick_sort_lomuto(number_list, lesser, partitioning_index - 1)
        quick_sort_lomuto(number_list, partitioning_index + 1, greater)


# Hoare partition scheme
def partitioning_hoare(number_list, low, high):
    i = low - 1
    j = high
    pivot = number_list[high]
    while True:
        while True:
            i += 1
            if i >= high or number_list[i] >= pivot:
                break
        while True:
            j -= 1
            if j < low or number_list[j] < pivot:
                break
        if i >= j:
            break
        number_list[i], number_list[j] = number_list[j], number_list[i]
    number_list[high], number_list[i] = number_list[i], number_list[high]
    return i


def quick_sort_hoare(number_list, low, high):
    if low < high:
        partitioning_index = partitioning_hoare(number_list, low, high)
        quick_sort_hoare(number_list, low, partitioning_index - 1)
        quick_sort_hoare(number_list, partitioning_index + 1, high)


def main():
    user_list = [23, 2, 0, 42, 23, 42, 2000, 1, 32]
    list_length = len(user_list)
    quick_sort_hoare(user_list, 0, list_length - 1)
    print("Sorted array is:")
    for i in range(list_length):
        print("%d" % user_list[i], end=" ")


if __name__ == "__main__":
    main()
