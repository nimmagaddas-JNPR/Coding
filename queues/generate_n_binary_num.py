# input: 7
# output: [1,10,11,100,101,110,111]
from queue import Queue


def generate_n_binary_num(k):
    if k <= 0:
        return k
    que = Queue()
    res_arr = []
    que.put("1")
    while que.empty() is False and len(res_arr) <= k:
        val = que.get()
        que.put(val + "0")
        que.put(val + "1")
        res_arr.append(val)
    return res_arr


print(generate_n_binary_num(7))
print(generate_n_binary_num(16))


