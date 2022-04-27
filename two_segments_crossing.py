def segments_crossing(a, b, c, d, e, f, g, h):
    vector_ab = vector(a, b, c, d)
    vector_ac = vector(a, b, e, f)
    vector_ad = vector(a, b, g, h)

    vector_cd = vector(e, f, g, h)
    vector_ca = vector(e, f, a, b)
    vector_cb = vector(e, f, c, d)

    cross_product_ab_ac = cross_product(vector_ab, vector_ac)
    cross_product_ab_ad = cross_product(vector_ab, vector_ad)
    cross_product_cd_ca = cross_product(vector_cd, vector_ca)
    cross_product_cd_cb = cross_product(vector_cd, vector_cb)

    if cross_product_ab_ac * cross_product_ab_ad < 0 and cross_product_cd_ca * cross_product_cd_cb < 0:
        return True
    elif cross_product_ab_ac == 0 and check(a, b, c, d, e, f):
        return True
    elif cross_product_ab_ad == 0 and check(a, b, c, d, g, h):
        return True
    elif cross_product_cd_ca == 0 and check(e, f, g, h, a, b):
        return True
    elif cross_product_cd_cb == 0 and check(e, f, g, h, c, d):
        return True
    return False


def check(a, b, c, d, e, f):
    return min([a, c]) <= e <= max([a, c]) and min([b, d]) <= f <= max([b, d])


def cross_product(vector1, vector2):
    return vector1[0] * vector2[1] - vector1[1] * vector2[0]


def vector(a, b, c, d):
    return [c - a, d - b]


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
    print("D(g,h)")
    g = int(input("g = "))
    h = int(input("h = "))
    if segments_crossing(a, b, c, d, e, f, g, h):
        print("Segments cross.")
    else:
        print("Segments don't cross.")


if __name__ == "__main__":
    main()
