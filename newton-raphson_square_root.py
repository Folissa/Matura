def Newton_Raphson(area, epsilon):
    a = 1
    b = area
    while abs(a - b) >= epsilon:
        a = (a + b) / 2
        b = area / a
    return (a + b) / 2


def main():
    epsilon = 0.100000
    root_number = int(input("Input a numbert to calculate square root of: "))
    print(f"Square root of {root_number} is {Newton_Raphson(root_number, epsilon)}.")


if __name__ == "__main__":
    main()
