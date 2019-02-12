import heapq


def find_difference(arr, n, m):
    max = 0; min = 0

    min_heap = heapq.heapify(arr)
    temp = arr.copy()
    for i in range(len(temp)):
        temp[i] = -1*temp[i]
    max_heap = heapq.heapify(temp)
    for i in range(m):
        max += heapq.heappop(list(max_heap))
        min += heapq.heappop(min_heap)

    return - max - min
