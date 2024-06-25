class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reset_head(self):
        if self.head is None:
            print("Linked list is empty.")
        else:
            self.head = self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Create a linked list
my_list = LinkedList()

# Add nodes to the list
my_list.add_node(10)
my_list.add_node(20)
my_list.add_node(30)
my_list.add_node(40)

# Reset the head
my_list.reset_head()

# Print the updated list
my_list.print_list()
