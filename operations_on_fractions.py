from euclidean_algorithm import optimized_euclidean_algorithm
from euclidean_algorithm import NWW

operations = {"+", "-", "*", "/"}


def reducing_fraction(numerator, denominator):
    nwd = optimized_euclidean_algorithm(numerator, denominator)
    numerator //= nwd
    denominator //= nwd
    return [numerator, denominator]


def operations_on_fractions(numerator_a, denominator_a, numerator_b, denominator_b, operation):
    if operation == "*" or operation == "/":
        if operation == "/":
            numerator_b, denominator_b = denominator_b, numerator_b
        fraction = reducing_fraction(numerator_a * numerator_b, denominator_a * denominator_b)
        return f"{fraction[0]} / {fraction[1]}"
    elif operation == "+" or operation == "-":
        nww_of_denominators = NWW(denominator_a, denominator_b)
        multiplier_a = nww_of_denominators // denominator_a
        multiplier_b = nww_of_denominators // denominator_b
        numerator_a *= multiplier_a
        numerator_b *= multiplier_b
        numerator_operations = {'+': numerator_a + numerator_b,
                                '-': numerator_a - numerator_b
                                }
        fraction = reducing_fraction(numerator_operations[operation], numerator_a * nww_of_denominators // numerator_a)
        return f"{fraction[0]} / {fraction[1]}"


def main():
    numerator_a = int(input("Numerator of first number: "))
    denominator_a = int(input("Denominator of first number: "))
    numerator_b = int(input("Numerator of second number: "))
    denominator_b = int(input("Denominator of second number: "))
    operation = input("Operation you want to perform (+, -, *, /): ")
    print(f"({numerator_a} / {denominator_a}) {operation} ({numerator_b} / {denominator_b}) = "
          f"{operations_on_fractions(numerator_a, denominator_a, numerator_b, denominator_b, operation)}")


if __name__ == "__main__":
    main()
