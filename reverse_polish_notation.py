import operator
operators = {"+": operator.add,
             "-": operator.sub,
             "*": operator.mul,
             "/": operator.truediv}


def value_reverse_polish_notation(rpn_expression):
    stack = []
    for element in rpn_expression:
        if element not in operators:
            stack.append(element)
        else:
            b = stack[-1]
            a = stack[-2]
            stack = stack[0:-2]
            stack.append(operators.get(element)(int(a), int(b)))
    return stack[0]


def main():
    print("Input a reverse polish notation expression. Type 'end' to end the input.")
    user_expression = []
    while True:
        user_input = input()
        if user_input != "end":
            user_expression.append(user_input)
        else:
            break
    print(f"Value of the expression: {value_reverse_polish_notation(user_expression)}")


if __name__ == "__main__":
    main()
