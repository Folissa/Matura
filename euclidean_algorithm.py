# for first_number and second_number being an integer
def euclidean_algorithm(first_number, second_number):
    # for second_number > 0
    if first_number == 0:
        return second_number
    # for first_number > 0
    elif second_number == 0:
        return first_number
    # for first_number > 0 and second_number > 0
    while first_number != second_number:
        if first_number > second_number:
            first_number -= second_number
        else:
            second_number -= first_number
    return first_number


def optimized_euclidean_algorithm(first_number, second_number):
    while second_number != 0:
        temporary = second_number
        second_number = first_number % second_number
        first_number = temporary
    return first_number


def NWW(first_number, second_number):
    # if a != 0 and b !=0
    return first_number * second_number // euclidean_algorithm(first_number, second_number)


a = 4
b = 10

print(f"NWD({a},{b}) = {optimized_euclidean_algorithm(a, b)}")
print(f"NWW({a},{b}) = {NWW(a, b)}")
