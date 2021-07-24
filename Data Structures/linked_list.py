class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = Node(head)

    def pushTop(self, val):
        newNode = Node(val)
        current = self.head
        if not current.data:
            self.head = newNode
        else:
            while(current):
                if current.next == None:
                    break
                current = current.next
            current.next = newNode

    def showLinkedList(self):
        current = self.head
        print("***SINGLE LINKED LIST***")
        while(current):
            print(current.data, "==>", end=" ")
            current = current.next
        print()

    def findNodeByData(self, val):
        current, i = self.head, 0
        while(current):
            if current.data == val:
                print(current.data, "found at Node", i)
            i += 1
            current = current.next

if __name__ == "__main__":
    # ll1 = LinkedList()
    # n1, n2, n3 = Node(1), Node(2), Node(3)
    # ll1.head = n1
    # n1.next = n2
    # n2.next = n3
    # n4 = Node(4)
    # n5 = Node(50)
    # n3.next = n4
    # n4.next = n5
    # ll1.showLinkedList()
    # ll1.findNodeByData(50)
    # t1 = Node(100)
    # ll1.head = t1
    # t1.next = n1
    # ll1.showLinkedList()
    # ll1.pushTop(21)
    # ll1.showLinkedList()
    ll1 = LinkedList(head=1)
    ll1.pushTop(21)
    ll1.pushTop(16)
    ll1.pushTop(12)
    ll1.showLinkedList()