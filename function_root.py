# for continuous functions having one root
def function(x):
    return x * (x * (x - 3) + 2) - 4


def function_root(a, b, epsilon):
    if function(a) == 0:
        return a
    elif function(b) == 0:
        return b
    while abs(b - a) > epsilon:
        middle = (a + b) / 2
        if function(middle) == 0:
            return middle
        if function(a) * function(middle) < 0:
            b = middle
        else:
            a = middle
    return (a + b) / 2


def main():
    epsilon = 0.0000000000001
    while True:
        a = int(input("Input beginning of a range [a,b]: "))
        b = int(input("Input the end of a range [a,b]: "))
        if a < b:
            break
        else:
            print("a must be greater than b")
    print(f"The root of a function: {function_root(a, b, epsilon)}")


if __name__ == "__main__":
    main()
