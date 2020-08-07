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

    def removeDuplicates(self, head):
        current = head

        while current.next:
            if current.data != current.next.data:
                current = current.next
            else:
                current.next = current.next.next
        return head


mylist = Solution()
sample = [1, 2, 2, 3, 3, 4]
head = None
for data in sample:
    head = mylist.insert(head, data)
mylist.display(head)
print()
head = mylist.removeDuplicates(head)
mylist.display(head)
