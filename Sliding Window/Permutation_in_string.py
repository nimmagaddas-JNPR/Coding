def find_permutation(str, pattern):
    if len(str) == 0 or len(pattern) == 0:
        return -1
    p_map = {}
    for p in pattern:
        if p not in p_map:
            p_map[p] = 0
        p_map[p] += 1

    start, matched_count = 0, 0
    for end in range(len(str)):
        if str[end] in p_map:
            p_map[str[end]] -= 1
            if p_map[str[end]] == 0:
                matched_count += 1
            if matched_count == len(p_map):
                return True
        if end >= len(pattern) - 1:
            if str[start] in p_map:
                if p_map[str[start]] == 0:
                    matched_count -= 1
                p_map[str[start]] += 1
            start += 1

    return False


# print(find_permutation("oidbcaf", "abc"))
# print(find_permutation("odicf", "dc"))
print(find_permutation("bcdxabcdy", "bcdyabcdx"))
