

#Sample Input
# n = "0 0 1 0 1 0 1 1 1 0"
# q = 8
# inp = ["s 3 7", "g 4", ...]
def func(n, q, inp):
    node = []  # array of minimum elements(use segment tree structure)
    ans = []
    n = n.split()
    for i in range(4 * len(n)):
        node.append(0)
    for i in range(len(n)):
        if (int(n[i]) == 1):
            set_value(1, 0, len(n), i, i + 1, node)
    for i in range(q):
        s = inp[i].split()
        if (len(s) == 2):
            p1 = int(s[1])
            ans += [get_value(p1, 1, 0, len(n), node)]
        else:
            p1 = int(s[1])
            p2 = int(s[2])
            set_value(1, 0, len(n), p1, p2, node)

    return ans



def set_value(ind, l, r, ql, qr, node):
    if (ql <= l and r <= qr):
        node[ind] = 1 - node[ind]
        return
    if (l != r - 1):
        mid = (l + r) // 2
        set_value(2 * ind, l, mid, ql, qr, node)
        set_value(2 * ind + 1, mid, r, ql, qr, node)


def get_value(qind, ind, l, r, node):
    if (l <= qind and qind < r):
        if (l == r - 1):
            return node[ind]
        mid = (l + r) // 2
        return (node[ind] + get_value(qind, 2 * ind, l, mid, node) + get_value(qind, 2 * ind + 1, mid, r, node)) % 2
    return 0


