class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self,dataval):
        # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False
    
    def removefromq(self):
        # Pop method to remove element
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")
    
    def size(self):
        return len(self.queue)
    

TheQueu = Queue()
TheQueu.addtoq("Mon")
TheQueu.addtoq("Tue")
TheQueu.addtoq("Wed")
print(TheQueu.removefromq())
print(TheQueu.removefromq())