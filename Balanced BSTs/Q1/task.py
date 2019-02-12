class Node:
    def __init__(self):
        self.value = None
        self.children = [None, None]

    def is_nill(self):
        return self.value is None

    def insert(self, value):
        if self.is_nill():
            self.value = value
            self.children = [Node(), Node()]
            return 0
        else:
            dir_to_go = 0 if value < self.value else 1
            depth = self.children[dir_to_go].insert(value)
            return depth + 1

def func(li):
    tree = Node()
    depths = [tree.insert(num) for num in li]
    return depths

