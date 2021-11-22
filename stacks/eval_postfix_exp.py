# Eg: 2 3 1 * + 9 -

def eval_post_fix_exp(exp):
    stack = []
    for i in exp.split():
        if i.isdigit():
            stack.append(int(i))
        else:
            # Found an operator pop the two elements of stack.
            try:
                val1 = stack.pop()
                val2 = stack.pop()
            except IndexError:
                raise ValueError("Invalid Input")
            val = 0
            if i == "*":
                val = val1 * val2
            elif i == "+":
                val = val1 + val2
            elif i == "-":
                val = val1 - val2
            elif i == "/":
                val = val1 / val2
            else:
                raise ValueError("Invalid Input")
            stack.append(val)
    if len(stack) != 1:
        raise ValueError("Invalid Input")
    return stack.pop()


print(eval_post_fix_exp("2 3 1 * + 9 -"))
