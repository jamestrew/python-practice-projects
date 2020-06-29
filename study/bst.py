sample = [3, 5, 2, 1, 4, 6, 7]


class Node():
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class Solution():
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root


myTree = Solution()
root = None
for i in sample:
    root = myTree.insert(root, i)
    print(i, root)
