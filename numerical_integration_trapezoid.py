def function(x):
    return x * x + 2 * x + x


def trapezoid_numerical_integration(a, b, n):
    h = (b - a) / n
    area = 0
    for i in range(1, n + 1):
        first_base = abs(function(a + h * (i - 1)))
        second_base = abs(function(a + h * i))
        area += first_base + second_base
    return area * h / 2


def main():
    while True:
        a = int(input("Input beginning of a range [a,b]: "))
        b = int(input("Input the end of a range [a,b]: "))
        if a < b:
            break
        else:
            print("a must be greater than b")
    n = int(input("Input quantity of trapezoids: "))
    print(f"The area is equal to {trapezoid_numerical_integration(a, b, n)}.")


if __name__ == "__main__":
    main()
