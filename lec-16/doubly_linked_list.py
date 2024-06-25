class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class double_linked_list:
    def __init__(self):
        self.head = None

    # Adding data elements
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    # Insert element
    def insert(self, PrevVal, NewVal):
        if self.head is None:
            print("Empty List")
            return
        Current = self.head
        while (Current.next is not None):
            if Current.data == PrevVal:
                NewNode = Node(NewVal)
                NewNode.next = Current.next
                NewNode.prev = Current
                Current.next = NewNode
                break
            Current = Current.next

    # append element at the end
    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while(last.next is not None):
            last=last.next
        last.next = NewNode
        NewNode.prev = last
        return
    
    # Print the Doubly Linked list
    def listprint(self, node):
        while (node is not None):
            print(node.data)
            last = node
            node = node.next

dllist = double_linked_list()
dllist.push(12)
dllist.push(8)
dllist.push(62)
dllist.listprint(dllist.head)
print()
dllist.insert(8, 30)
dllist.listprint(dllist.head)
print()
dllist.append(45)
dllist.listprint(dllist.head)
print()