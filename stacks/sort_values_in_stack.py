# Input : [34, 3, 31, 98, 92, 23]
# Output : [3, 23, 31, 34, 92, 98]
# Create a temporary stack say tmpStack.
# While input stack is NOT empty do this:
# Pop an element from input stack call it temp
# while temporary stack is NOT empty and top of temporary stack is greater than temp,
# pop from temporary stack and push it to the input stack
# push temp in temporary stack
# The sorted numbers are in tmpStack
# Time Complexity: O(n2)
def sort_values_in_stack(o_stack):
    new_stack = []
    if len(o_stack) == 0:
        return o_stack
    while len(o_stack) > 0:
        temp = o_stack.pop()
        if len(new_stack) == 0 or new_stack[-1] < temp:
            new_stack.append(temp)
        else:
            while len(new_stack) > 0 and new_stack[-1] > temp:
                r = new_stack.pop()
                o_stack.append(r)
            new_stack.append(temp)
    return new_stack


print(sort_values_in_stack([34, 3, 31, 98, 92, 23]))
