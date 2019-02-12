
inf = 1000000000
#Sample Input
# n = 7
# arr = "7 2 3 13 5 17 11"
# q = 4
# inp = ["3 7", "2 5", ...]
def func(n, arr, q, inp):
    a = []  # main array
    node = []  # array of minimum elements(use segment tree structure)
    s = arr.split()
    ans = []
    for i in range(4 * n):
        node.append(0)
    for i in range(n):
        a.append(int(s[i]))
    make_tree(1, 0, n, node, a)
    for i in range(q):
        s = inp[i].split()
        p1 = int(s[0])
        p2 = int(s[1])
        ans += [get_min(1, 0, n, p1, p2, node)]

    return ans

def make_tree(ind, l, r, node, a):
    if (l == r - 1):
        node[ind] = a[l]
        return
    mid = (l + r) // 2
    make_tree(ind * 2, l, mid, node, a)
    make_tree(ind * 2 + 1, mid, r, node, a)
    node[ind] = min(node[ind * 2], node[ind * 2 + 1])


def get_min(ind, l, r, ql, qr, node):  # ql, qr determine segment of query
    if (qr <= l or r <= ql):
        return inf
    if (ql <= l and r <= qr):
        return node[ind]
    mid = (l + r) // 2
    return min(get_min(ind * 2, l, mid, ql, qr, node)
               , get_min(ind * 2 + 1, mid, r, ql, qr, node))

