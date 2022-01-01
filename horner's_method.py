def main():
    user_degree_of_polynomial = int(input("Input a degree of polynomial: "))
    user_coefficients = []
    for power in range(user_degree_of_polynomial + 1):
        user_coefficients.append(int(input(f"Input coefficient standing next to {power} power: ")))
    user_polynomial = ""
    for power in range(user_degree_of_polynomial, -1, -1):
        if power == 0:
            user_polynomial += f"{user_coefficients[power]} * x^{str(power)}"
        else:
            user_polynomial += f"{user_coefficients[power]} * x^{str(power)} + "
    user_x_value = int(input("Input the value of x: "))
    user_coefficients.reverse()
    value_of_polynomial = horner_recursive(user_x_value, user_coefficients, user_degree_of_polynomial)
    print(f"Your polynomial: {user_polynomial}.\n"
          f"It's value: {value_of_polynomial}.")


def horner_recursive(x_value, coefficients, degree_of_polynomial):
    if degree_of_polynomial == 0:
        return coefficients[0]
    else:
        return x_value * horner_recursive(x_value, coefficients, degree_of_polynomial - 1)\
               + coefficients[degree_of_polynomial]


def horner(x_value, coefficients, degree_of_polynomial):
    result = coefficients[0]
    for i in range(1, degree_of_polynomial + 1):
        result = result * x_value + coefficients[i]
    return result


if __name__ == "__main__":
    main()
