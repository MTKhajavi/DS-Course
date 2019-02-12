
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root,data):
    if data > root.value:
        if root.right:
            insert(root.right, data)
        else:
            root.right = Node(data)
    if data < root.value:
        if root.left:
            insert(root.left, data)
        else:
            root.left = Node(data)

#inorder is an array which we want to store the inorder traversal in it.
def inordertraversal(root, inorder):
    if root:
        # First call on left child
        inordertraversal(root.left, inorder)

        # then print the data of node
        inorder.append(root.value)

        # now recur on right child
        inordertraversal(root.right, inorder)
