# Input : Q = [10, 20, 30, 40, 50, 60,
#             70, 80, 90, 100]
#         k = 5
# Output : Q = [50, 40, 30, 20, 10, 60,
#              70, 80, 90, 100]
from queue import Queue


def reverse_first_k_elements(arr, k):
    if k <= 0:
        return arr
    que = Queue()
    for i in arr:
        que.put(i)
    if que.empty() is True or que.qsize() < k:
        return que
    stack = []
    temp = []
    for i in range(k):
        stack.append(que.get())
    for j in range(len(stack)):
        que.put(stack.pop())
    print(que)
    for k in range(que.qsize() - k):
        temp.append(que.get())
    for r in range(len(temp)):
        que.put(temp[r])
    return list(que.queue)


print(reverse_first_k_elements([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 5))
