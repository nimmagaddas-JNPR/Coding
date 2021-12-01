def find_string_anagrams(str, pattern):
    result_indexes = []
    if len(str) == 0 or len(pattern) == 0:
        return result_indexes

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
            result_indexes.append(start)

        if end >= len(p_map) - 1:
            if p_map[str[start]] == 0:
                matched_count -= 1
            p_map[str[start]] += 1
            start += 1
    return result_indexes


print(find_string_anagrams("abbcabc", "abc"))
print(find_string_anagrams("ppqp", "pq"))
