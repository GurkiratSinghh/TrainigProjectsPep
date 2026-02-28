class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    # 🔑 find path from root → target
    def find_path(self, root, target, path):
        if root is None:
            return False

        path.append(root)

        if root.name == target:
            return True

        if (self.find_path(root.left, target, path) or
            self.find_path(root.right, target, path)):
            return True

        path.pop()   # backtrack
        return False
