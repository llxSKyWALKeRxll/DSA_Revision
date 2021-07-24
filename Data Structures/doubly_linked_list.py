class Node:
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.prev, self.next = None, None

class DoublyLinkedList:
    def __init__(self, head=None) -> None:
        self.head = Node(head)

    def pushTop(self, val):
        newNode = Node(val)
        current = self.head
        if not current.data:
            self.head = newNode
        else:
            while current:
                if current.next == None:
                    break
                current = current.next
            current.next = newNode
            newNode.prev = current

    def showLinkedList(self):
        current = self.head
        print("***DOUBLY LINKED LIST***")
        while(current):
            print(current.data, "<==>", end=" ")
            current = current.next
        print()

    def showLinkedListReverse(self):
        current = self.head
        while(current):
            if not current.next:
                break
            current = current.next
        print("***DOUBLY LINKED LIST (REVERSE)***")
        while(current):
            print(current.data, "<==>", end=" ")
            current = current.prev
        print()


if __name__ == "__main__":
    DLL1 = DoublyLinkedList(head=1)
    DLL1.pushTop(21)
    DLL1.pushTop(16)
    DLL1.pushTop(33)
    DLL1.showLinkedList()
    DLL1.showLinkedListReverse()