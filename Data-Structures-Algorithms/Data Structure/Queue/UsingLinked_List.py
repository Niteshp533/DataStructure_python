class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, value):
        new_node = Node(value )
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.front == None:
                return 'Empty Queue!'
        else:
            self.front = self.front.next
        
    def traverse(self):
        
        curr = self.front
        while curr != None:
            print(curr.data, end =" ")
            curr= curr.next
            
    def is_empty(self):
        return self.front == None
     
    def size(self):
        curr = self.front
        count = 0
        while curr != None:
            count += 1
            curr= curr.next
        return count
    
    def front_ele(self):
        if self.front == None:
                return 'Empty Queue!'
        else:
            return self.front.data
    
    def rear_ele(self):
        if self.front == None:
                return 'Empty Queue!'
        else:
            return self.rear.data
        