class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoubleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_back(self, node:Node):
        if self.tail == None:
            self.tail = node
            self.head = node
        else :
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size += 1

    def push_front(self, node:Node):
        if self.head == None:
            self.head = node
            self.tail = node
        else :
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

        self.size += 1

    def push_index(self, node:Node, index):
        if index <= 0:
            self.push_first(node)
        elif index >= self.size :
            self.push_back(node)
        else:
            tmp_node = self.head
            node_idx = 1
            while node_idx < index:
                tmp_node = node.next
                node_idx += 1

            node.next = tmp_node.next
            tmp_node.next.prev = node
            node.prev = tmp_node
            tmp_node.next = node

        self.size += 1

    def peek_front(self):
        return self.head

    def peek_back(self):
        return self.tail

    def peek_index(self, index):
        if index > self.size-1 :
            return None

        if index < 0 :
            return None

        tmp_node = self.head
        node_idx = 0
        while node_idx != index :
            node_idx += 1
            tmp_node = tmp_node.next

        return tmp_node

    def pop_front(self):
        if self.size == 0:
            return None
        
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        
        self.size -= 1

        return node

    def pop_back(self):
        if self.size == 0:
            return None

        node = self.tail
        self.tail = self.tail.prev
        self.tail.next = None

        self.size -= 1

        return node

    def pop_index(self, index):
        if self.size == 0:
            return None

        if index <= 0:
            return self.pop_front()

        elif index >= self.szie :
            return self.pop_back()

        else :
            node = self.head
            node_idx = 0
            while node_idx != index :
                node_idx += 1
                node = node.next

            node.prev.next = node.next
            node.next.prev = node.prev

            self.size -= 1

            return node

    def reverse(self):
        if self.size == 0 :
            return

        node = self.tail

        self.tail, self.head = self.head, self.tail

        while node != None:
            node.prev, node.next = node.next, node.prev
            print(node.prev)
            print(node.next)
            node = node.next


    def print_forward(self):
        node = self.head

        while node != None :
            print(node.data)
            node = node.next

    def print_backward(self):
        node = self.tail

        while node != None:
            print(node.data)
            node = node.prev

    def remove_somenode(self, node:Node):
        next_node = node.next
        node.data = next_node.data
        node.next = next_node.next

        next_node.next.prev = node

dlist = DoubleList()


n1 = Node(3)
n2 = Node(5)
n3 = Node(4)

dlist.push_back(n1)
dlist.push_front(n2)
dlist.push_index(n3, 1)

dlist.print_forward()
print("==========")

dlist.reverse()
dlist.print_forward()

#print(dlist.peek_index(0).data)
