# prime number is a natural number greater than 1 and it only has two factors (1 and itself)
import math


def main():
    for j in range(10):
        if is_prime(j):
            print(j)


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
