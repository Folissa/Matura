def function(x):
    return x * x + 2 * x + x


def rectangle_numerical_integration(a, b, n):
    side_x = (b - a) / n
    middle_of_side_x = a + (side_x / 2)
    area = 0
    for i in range(n):
        area += abs(function(middle_of_side_x))
        middle_of_side_x += side_x
    return area * side_x


def main():
    while True:
        a = int(input("Input beginning of a range [a,b]: "))
        b = int(input("Input the end of a range [a,b]: "))
        if a < b:
            break
        else:
            print("a must be greater than b")
    n = int(input("Input quantity of rectangles: "))
    print(f"The area is equal to {rectangle_numerical_integration(a, b, n)}.")


if __name__ == "__main__":
    main()
