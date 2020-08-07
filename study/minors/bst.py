class Node():
    def __init__(self, data):
        self.left = self.right = None
        self.data = data


class Solution():
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def getHeight(self, root):
        if root:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        else:
            return -1

    def levelOrder(self, root):
        lst = [root] if root else []

        while lst:
            node = lst.pop()
            print(node.data, end=' ')

            if node.left:
                lst.insert(0, node.left)
            if node.right:
                lst.insert(0, node.right)


sample = [3, 5, 4, 7, 2, 1]
myTree = Solution()
root = None
for i in sample:
    root = myTree.insert(root, i)

myTree.levelOrder(root)
