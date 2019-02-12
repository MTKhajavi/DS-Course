from heapq import heappush,heappop

# Sample Input:
# n = 10
# arr1 = "0 0 0 0 1 0 1 0 1"  0 is for a course, 1 is for a prof.
# arr2 = "5 10 17 6 2 1 3 2 4" course units or h_index of the prof.

def maxVahed(n, arr1, arr2):
    heap = []
    heapSize = 0
    arr1 = list(map(int, arr1.split()))
    arr2 = list(map(int, arr2.split()))

    for i in range(n-1):
        if(arr1[i] == 0):
            heappush(heap,arr2[i])
            heapSize += 1
        else:
            while(heapSize >= arr2[i]):
                heapSize -= 1
                heappop(heap)

    return sum(heap)
