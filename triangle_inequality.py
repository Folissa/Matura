def triangle_inequality(a, b, c):
    return b + c > a > 0 and a + b > c > 0 and a + c > b > 0


def main():
    first_side = int(input("Input the length of first side of the triangle: "))
    second_side = int(input("Input the length of second side of the triangle: "))
    third_side = int(input("Input the length of third side of the triangle: "))
    if triangle_inequality(first_side, second_side, third_side):
        print("You can make a triangle.")
    else:
        print("You can't make a triangle.")


if __name__ == "__main__":
    main()
