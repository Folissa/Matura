def prime_factorization(number):
    list_of_factors = []
    i = 2
    while i * i <= number:
        while number % i == 0:
            list_of_factors.append(i)
            number //= i
        i += 1
    if number > 1:
        list_of_factors.append(number)
    return list_of_factors


def main():
    for user_number in range(2, 100):
        print(prime_factorization(user_number))


if __name__ == "__main__":
    main()
