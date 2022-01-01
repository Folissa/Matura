def main():
    user_quantity_of_numbers = int(input("How much fib numbers you want to print out?: "))
    fibonacci(user_quantity_of_numbers)


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


if __name__ == "__main__":
    main()
