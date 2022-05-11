#Creating Stack data structure using LinkedList

class Node:
    #Node structure for LinkedList
    def __init__(self):
        self.nextNode = None
        self.content = ""

class Stack:

    def __init__(self, item):
        #Initializing Stack
        self.base = Node()
        self.base.content = item

    def push(self, content):
        #Adding new item for the stack
        oldBase = self.base
        self.base = Node()
        self.base.content = content
        self.base.nextNode = oldBase

    def pop(self):
        #Getting the last added item to the stack and removing it
        if self.is_empty():
            return "It Is Empty"
        wantedValue = self.base.content
        self.base = self.base.nextNode
        return wantedValue

    def is_empty(self):
        #Checking if the stack is empty
        return not self.base


MyStack = Stack("Karim")
MyStack.push('Nabil')
print(MyStack.pop())
print(MyStack.pop())
print(MyStack.pop())
