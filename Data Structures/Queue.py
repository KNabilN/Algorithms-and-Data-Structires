class Node:
    def __init__(self):
        self.next = None
        self.content = ""

class Queue:
    def __init__(self, content):
        self.head = Node()
        self.tail = self.head
        self.head.content = content

    def enqueue(self, content):
        oldTail = self.tail
        self.tail = Node()
        self.tail.content = content
        oldTail.next = self.tail

    def dequeue(self):
        if self.is_empty():
            return "Empty Queue!"
        wantedValue = self.head.content
        self.head = self.head.next
        return wantedValue

    def is_empty(self):
        return not self.head

MyQueue = Queue('Karim')
MyQueue.enqueue('Nabil')

print(MyQueue.dequeue())
print(MyQueue.dequeue())
print(MyQueue.dequeue())
