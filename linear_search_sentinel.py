def main():
    user_list = []
    while True:
        user_list_element = int(input("Input a number to a list: "))
        if user_list_element != -1:
            user_list.append(user_list_element)
        elif user_list_element == -1:
            user_list.append(user_list_element)
            break
    user_element = int(input("Input searched number: "))
    print(linear_search_sentinel(user_list, user_element))


def linear_search_sentinel(searched_list, searched_element):
    for element_index in range(len(searched_list)):
        if searched_list[element_index] == searched_element:
            return f"Your element is on {element_index} index."
        elif searched_list[element_index] == -1:
            break
    return "Searched number is not in a list."


if __name__ == "__main__":
    main()
