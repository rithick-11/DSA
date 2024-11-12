class Node:
    def __init__(self, data):
        self.data = data
        self.pt = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = Node(data)
            print("yess")
        else:
            cur = self.head
            while(cur.pt is not None):
                cur = cur.pt
            cur.pt = newNode
            print("yess")

            
    def print(self):
        cur = self.head
        while(cur.pt != None):
            print(cur.data)
            cur = cur.pt
        else:
            print("printed successfully")

    
List_1 = LinkedList()
List_1.add(1)
List_1.add(2)
List_1.add(3)
List_1.add(4)
List_1.print()
