def point_on_segment(a, b, c, d, e, f):
    determinant = a * d + c * f + e * b - c * b - a * f - e * d
    if determinant != 0:
        print("Point doesn't belong to the segment AB, nor to the line.")
    elif check(a, b, c, d, e, f):
        print("Point does belong to the segment AB.")
    else:
        print("Point doesn't belong to the segment AB, but belongs to the line.")


def check(a, b, c, d, e, f):
    return min([a, c]) <= e <= max([a, c]) and min([b, d]) <= f <= max([b, d])


def main():
    print("A(a,b)")
    a = int(input("a = "))
    b = int(input("b = "))
    print("B(c,d)")
    c = int(input("c = "))
    d = int(input("d = "))
    print("C(e,f)")
    e = int(input("e = "))
    f = int(input("f = "))
    point_on_segment(a, b, c, d, e, f)


if __name__ == "__main__":
    main()
