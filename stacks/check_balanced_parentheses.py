# Input: exp = “[()]{}{[()()]()}”
# Output: Balanced
#
# Input: exp = “[(])”
# Output: Not Balanced
def is_pair(a, b):
    if a == '[' and b == ']':
        return True
    elif a == '(' and b == ')':
        return True
    elif a == '{' and b == '}':
        return True
    else:
        return False


def check_balanced_parentheses(exp):
    if len(exp) == 0:
        return exp
    stack = []
    for i in exp:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if is_pair(stack[-1], i):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


print(check_balanced_parentheses("[()]{}{[()()]()}"))
print(check_balanced_parentheses("[(])"))
