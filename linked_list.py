class Node:
    def __init__(self,data):
        self.data = data
        self.next= None

class Linkedlist:
    def __init__(self):
        print("initializin linked list with none")
        self.head = None
    def insertAtBegin(self, data):
        new_node = Node(data)
        print("created new node with data as ",data)
        if self.head is None:
            self.head = new_node
            print("pointed head to the new node as there are no nodes")
            return
        else:
            new_node.next = self.head
            self.head = new_node
            print("pointed head to the new node and made it to be the first node")

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

ll=Linkedlist()
ll.insertAtBegin(5)
ll.printLL()
ll.insertAtBegin(6)
ll.printLL()
