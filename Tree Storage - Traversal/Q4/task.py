class Node:
    def __init__(self, name):
        self.city_name = name
        self.city1 = None
        self.city2 = None
        self.max_depth = 1
        self.answer = 0


def postorder_traversal(root, list):
    if root:
        if root.city1:
            postorder_traversal(root.city1, list)
        if root.city2:
            postorder_traversal(root.city2, list)
        if root.city1 and root.city2:
            root.max_depth = max(root.city1.max_depth, root.city2.max_depth) + 1
            root.answer = root.city1.max_depth + root.city2.max_depth + 1
        elif root.city1:
            root.max_depth = root.city1.max_depth + 1
            root.answer = root.city1.max_depth + 1
        elif root.city2:
            root.max_depth = root.city2.max_depth + 1
            root.answer = root.city2.max_depth + 1
        else:
            pass
        list.append(root.answer)
        return list


def solve(root):
    temp = postorder_traversal(root, [])
    return max(temp)
