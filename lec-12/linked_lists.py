class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    def Inbetween(self,middle_val,newdata):
        if self.headval is None:
            print("The mentioned node is absent")
            return
        current_node= self.headval
        while current_node.dataval:
            # print(f"--> {self.headval.dataval}")
            if current_node.dataval == middle_val:
                NewNode = Node(newdata)
                NewNode.nextval = current_node.nextval
                current_node.nextval = NewNode
                break
            current_node = current_node.nextval
        # NewNode = Node(newdata)
        # NewNode.nextval = middle_node.nextval
        # middle_node.nextval = NewNode

    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = NewNode

    def reset_head(self):
        pass

    # Function to remove node
    def RemoveNode(self, Removekey):
        HeadVal = self.headval
            
        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return

        prev.nextval = HeadVal.nextval
        HeadVal = None
    



list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

# Add new node "Sun" before "Mon"
list.AtBegining("Sun")

# Add new node "Thu" at the end
list.AtEnd("Thu")

# Add new node "Sat" at the end
list.AtEnd("Sat")

# Add new node "Fri" in between "Thu" and "Sat"
list.Inbetween("Thu","Fri")

# Reset head to the frist node
# list.reset_head()

# Remove "Mon" from the list
list.RemoveNode("Mon")

# print(list.headval.dataval)
list.listprint()
