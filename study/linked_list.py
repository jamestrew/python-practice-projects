class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution():
    def insert(self, head, data):
        if head is None:
            return Node(data)
        else:
            head.next = self.insert(head.next, data)
        return head

    def display(self, head):
        current = head

        while current:
            print(current.data, end=' ')
            current = current.next


mylist = Solution()
sample = [2, 3, 4, 1]
head = None
for data in sample:
    head = mylist.insert(head, data)
mylist.display(head)
