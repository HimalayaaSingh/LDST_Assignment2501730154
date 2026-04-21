# -------- Dynamic Array --------
class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize()
        self.arr[self.size] = x
        self.size += 1
        print(f"Appended {x} | Size: {self.size}, Capacity: {self.capacity}")

    def _resize(self):
        print(f"Resizing from {self.capacity} to {self.capacity * 2}")
        new_arr = [None] * (self.capacity * 2)
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity *= 2

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return None
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        print(f"Popped {val} | Size: {self.size}")
        return val

    def __str__(self):
        return str([self.arr[i] for i in range(self.size)])


# -------- Singly Linked List --------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_by_value(self, x):
        temp = self.head
        prev = None
        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next
        print("Value not found")

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)


# -------- Doubly Linked List --------
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = DoublyNode(x)
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next
        print("Target not found")

    def delete_at_position(self, pos):
        if not self.head:
            return

        temp = self.head
        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            temp = temp.next
            if not temp:
                return

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)


# -------- Stack --------
class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            print("Stack Underflow")
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.data if self.head else None


# -------- Queue --------
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            print("Queue Underflow")
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        return self.head.data if self.head else None


# -------- Parentheses Checker --------
def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in pairs:
            if stack.pop() != pairs[ch]:
                return False

    return stack.head is None


# -------- Main Execution --------
if __name__ == "__main__":
    print("--- Dynamic Array ---")
    arr = DynamicArray(2)
    for i in range(10):
        arr.append(i)
    print(arr)
    arr.pop()
    arr.pop()
    arr.pop()
    print(arr)

    print("\n--- Singly Linked List ---")
    sll = SinglyLinkedList()
    sll.insert_at_beginning(1)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(3)
    sll.traverse()
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    sll.traverse()
    sll.delete_by_value(2)
    sll.traverse()

    print("\n--- Doubly Linked List ---")
    dll = DoublyLinkedList()
    dll.head = DoublyNode(1)
    dll.head.next = DoublyNode(2)
    dll.head.next.prev = dll.head
    dll.insert_after(1, 3)
    dll.traverse()
    dll.delete_at_position(1)
    dll.traverse()

    print("\n--- Stack ---")
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.pop(), st.peek())

    print("\n--- Queue ---")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue(), q.front())

    print("\n--- Parentheses Checker ---")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", "Balanced" if is_balanced(t) else "Not Balanced")