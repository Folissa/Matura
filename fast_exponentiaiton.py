from numeral_systems import decimal_to_other_system


def fast_exponentiation(base, exponent):
    result = 1
    exponent = int(decimal_to_other_system(exponent, 2))
    while exponent > 0:
        if exponent % 10 == 1:
            result *= base
        base *= base
        exponent //= 10
    return result


def main():
    base = int(input("Please input a base: "))
    exponent = int(input("Please input an exponent: "))
    print(f"{base}^{exponent} = {fast_exponentiation(base, exponent)}")


if __name__ == "__main__":
    main()
