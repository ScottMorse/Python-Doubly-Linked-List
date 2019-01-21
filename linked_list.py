class Node:

    def __init__(self,data,prev_node,next_node):
        if (type(prev_node) is not Node and prev_node != None) or (
            type(next_node) is not Node and next_node != None):
            raise ValueError("prev_node and next_node must both be Nodes or None")
        self.data = data
        self._prev_node = prev_node
        self._next_node = next_node

    @property
    def prev_node(self):
        return self._prev_node
    
    @property
    def next_node(self):
        return self._next_node
    
    @prev_node.setter
    def prev_node(self,new_node):
        if type(new_node) is not Node and new_node != None:
            raise ValueError("prev_node must be a Node or None")
        self._prev_node = new_node

    @next_node.setter
    def next_node(self,new_node):
        if type(new_node) is not Node and new_node != None:
            raise ValueError("next_node must be a Node or None")
        self._next_node = new_node

    def __repr__(self):
        return f"<Node data:{self.data}>"
    
class DLL:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail
    
    @head.setter
    def head(self,new_node):
        if type(new_node) is not Node and new_node != None:
            raise ValueError("next_node must be a Node or None")
        self._head = new_node

    @tail.setter
    def tail(self,new_node):
        if type(new_node) is not Node and new_node != None:
            raise ValueError("next_node must be a Node or None")
        self._tail = new_node
    
    def push(self,data):
        prev_head = self.head
        self.head = Node(data,None,prev_head)
        if self.tail == None:
            self.tail = self.head
        else:
            self.head.next_node.prev_node = self.head
        self._size += 1
    
    def pop(self):
        if self.head == None:
            raise IndexError("List contains nothing to pop")
        prev_head = self.head
        self._size -= 1
        if self._size == 0:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next_node
            self.head.prev_node = None
        return prev_head.data

    def enqueue(self,data):
        prev_tail = self.tail
        self.tail = Node(data,prev_tail,None)
        if self.head == None:
            self.head = self.tail
        else:
            self.tail.prev_node.next_node = self.tail
        self._size += 1

    def dequeue(self):
        if not self.tail:
            raise IndexError("Nothing to dequeue in list.")
        prev_tail = self.tail
        self._size -= 1
        if self._size == 0:
            self.tail = None
            self.head = None
        else:
            self.tail = prev_tail.prev_node
            self.tail.next_node = None
        return prev_tail.data

    def _traverse(self,index,current_node,from_head):
        if index == 0:
            return current_node.data
        else:
            return self._traverse(index - 1,current_node.next_node if from_head else current_node.prev_node,from_head)
    
    def get(self,index):
        if type(index) is not int:
            raise ValueError("Index must be an integer")
        if index < 0:
            index += self._size
        if index > self._size - 1:
            raise IndexError("Index out of list bounds")
        if index < self._size // 2:
            return self._traverse(index,self.head,True)
        else:
            return self._traverse(self._size - index - 1,self.tail,False)
    
    def getAll(self):
        if self.head == None:
            return []
        nodes = [self.head]
        i = self._size
        current_node = self.head
        while i > 1:
            if current_node.next_node:
                current_node = current_node.next_node
                nodes.append(current_node)
            i -= 1
        return nodes

    def __repr__(self):
        return ", ".join([str(node.data) for node in self.getAll()])

if __name__ == "__main__":

    dll = DLL()
    
    dll.enqueue(1)
    dll.enqueue(2)
    dll.enqueue(3)
    dll.push(0)
    dll.push(1)

    dll.pop()

    dll.enqueue(4)

    dll.dequeue()

    print(dll)