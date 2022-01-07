#  perfect number is a natural number that is equal to the sum of its positive divisors excluding the number itself
from math import sqrt


def main():
    for user_number in range(1, 10000):
        perfect_numbers(user_number)


def perfect_numbers(number):
    sum_of_proper_divisors = 1
    for divisor in range(2, int(sqrt(number)) + 1):
        if number % divisor == 0:
            sum_of_proper_divisors += divisor + number / divisor
    if number == sqrt(number) * sqrt(number):
        sum_of_proper_divisors -= sqrt(number)
    if sum_of_proper_divisors == number:
        print(number)


if __name__ == "__main__":
    main()
