# Input : Q = [10, 20, 30, 40, 50, 60,
#             70, 80, 90, 100]
#         k = 5
# Output : Q = [50, 40, 30, 20, 10, 60,
#              70, 80, 90, 100]
# Input : Q = [10, 20, 30, 40, 50, 60,
#             70, 80, 90, 100]
#         k = 4
# Output : Q = [40, 30, 20, 10, 50, 60,
#              70, 80, 90, 100]

def rev_first_k_elem(arr, k):
    i = 0
    j = k - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


print(rev_first_k_elem([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 5))
print(rev_first_k_elem([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 4))