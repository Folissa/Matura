from prime_numbers import is_prime
from math import sqrt


def main():
    user_number = int(input("Input a number: "))
    print(prime_factorization(user_number))


def prime_factorization(number):
    if is_prime(number):
        list_of_factors = [1, number]
    else:
        list_of_factors = []
        i = 2
        while number > 1 and i <= sqrt(number):
            while number % i == 0:
                list_of_factors.append(i)
                number //= i
            i += 1
        if number > 1:
            list_of_factors.append(number)
    return list_of_factors


if __name__ == "__main__":
    main()
