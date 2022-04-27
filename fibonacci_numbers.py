def fibonacci(quantity_of_numbers):
    i = 0
    x = 0
    y = 1
    while i != quantity_of_numbers:
        print(x)
        z = x + y
        x = y
        y = z
        i += 1


def recursive_fibonacci(number):
    if number < 3:
        return 1
    return recursive_fibonacci(number - 2) + recursive_fibonacci(number - 1)


def main():
    user_quantity_of_numbers = int(input("How much fib numbers you want to print out?: "))
    fibonacci(user_quantity_of_numbers)


if __name__ == "__main__":
    main()
