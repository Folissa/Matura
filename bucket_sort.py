from merge_sort import merge_sort
import math


def main():
    # user_list = [124, 12444, 12, 0, 12]
    # user_list = [0.4, 0.2, 0.5, 0.12, 0.99]
    # user_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    user_list = [324, 1231, 41, 135, 499, 899, 900]
    print(f"Sorted list: {bucket_sort(user_list)}")


def bucket_sort(list_to_sort):
    buckets = []
    slot_number = len(list_to_sort)
    bucket_range = math.ceil(max(list_to_sort) / slot_number)
    # create buckets
    for i in range(slot_number):
        buckets.append([])
    # put items from list to buckets
    for number in list_to_sort:
        bucket_index = math.floor(number / bucket_range)
        if bucket_index != slot_number:
            buckets[bucket_index].append(number)
        else:
            buckets[bucket_index - 1].append(number)
    # sort numbers in buckets
    for bucket_index in range(slot_number):
        merge_sort(buckets[bucket_index])
    # concatenate the result
    k = 0
    for bucket_index in range(slot_number):
        for number_index in range(len(buckets[bucket_index])):
            list_to_sort[k] = buckets[bucket_index][number_index]
            k += 1
    return list_to_sort


if __name__ == "__main__":
    main()
