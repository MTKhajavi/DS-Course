class HeapNode:
    def __init__(self, data, row,):
        self.data = data
        self.row = row


def heapfiy_min(heap, i, size):

    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        min_ele = i
        if left < size and heap[min_ele].data > heap[left].data:
            min_ele = left
        if right < size and heap[min_ele].data > heap[right].data:
            min_ele = right

        if min_ele == i:
            break
        else:
            heap[i], heap[min_ele] = heap[min_ele], heap[i]
        i = min_ele

def merge_k_sorted_arrays(matrix, k, n):
    row = k
    col = n
    bubble = [0] * row
    heap = [None] * row
    ans = [None] * (row * col)
    n = row * col
    for i in range(0, row):
        heap[i] = HeapNode(matrix[i][0], i)
    for i in range(row - 1, -1, -1):
        heapfiy_min(heap, i, row)
    for i in range(0, n):
        ans[i] = heap[0].data
        # print "ans::iter", ans
        mat_row = heap[0].row
        if bubble[mat_row] >= col - 1:
            heap[0] = heap[row - 1]
            row = row - 1
        else:
            bubble[mat_row] += 1
            mat_col = bubble[mat_row]
            heap[0] = HeapNode(matrix[mat_row][mat_col], mat_row)
        heapfiy_min(heap, 0, row)
    return ans
