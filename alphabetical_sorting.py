def quicksort_alphabetical(lst):
    if not lst:
        return []
    return quicksort_alphabetical([x for x in lst[1:] if x < lst[0]]) + [lst[0]] + \
        quicksort_alphabetical([x for x in lst[1:] if x >= lst[0]])


def main():
    my_list = ['Jack', 'Sam', 'Jay', 'Mark', 'Baron']
    print(quicksort_alphabetical(my_list))


if __name__ == "__main__":
    main()
