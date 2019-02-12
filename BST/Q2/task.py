def hasOnlyOneChild(pre, size):
    nextDiff = 0
    #next node in preorder - next next node
    lastDiff = 0
    #next node in preorder - last node in preorder.


    for i in range(size - 1):
        nextDiff = pre[i] - pre[i + 1]
        lastDiff = pre[i] - pre[size - 1]
        if nextDiff * lastDiff < 0:
            return False
    return True
