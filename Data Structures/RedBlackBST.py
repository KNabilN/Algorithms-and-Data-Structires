class Node:
    def __init__(self, key, value, color):
        self.right = None
        self.left = None
        self.key = key
        self.value = value
        self.color = color

class RedBlackBST:


    def __init__(self):
        self.root = None
        self.RED = True
        self.BLACK = False

    def get(self, key):
        x = self.root
        while x != None:
            if key < x.key: x = x.left
            elif key > x.key: x = x.right
            else:
                return x.value
        return None

    def isRed(self, x):
        if x == None:
            return self.BLACK
        return x.color == self.RED

    def rotateLeft(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = self.RED
        return x

    def rotateRight(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = self.RED
        return x

    def flipColors(self, x):
        x.color = self.RED
        x.right.color = self.BLACK
        x.left.color = self.BLACK

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, x, key, value):
        if x == None: return Node(key, value, self.RED)

        if key < x.key: x.left = self._insert(x.left, key, value)
        elif key > x.key: x.right = self._insert(x.right, key, value)
        else:
            x.value = value

        if self.isRed(x.right) and not self.isRed(x.left): x = self.rotateLeft(x)
        if self.isRed(x.left) and self.isRed(x.left.left): x = self.rotateRight(x)
        if self.isRed(x.right) and self.isRed(x.left): self.flipColors(x)

        return x

    def keysInOrder(self):
        q = []
        self.inorder(self.root, q)
        return q

    def inorder(self, x, q):
        if x == None: return
        self.inorder(x.left, q)
        q.append(x.key)
        self.inorder(x.right, q)

    def getRoot(self):
        if self.root != None:
            return(self.root.key)
        return "Empty Tree"


tree = RedBlackBST()

tree.insert("A", 1)
tree.insert("B", 2)
tree.insert("C", 3)

print(tree.keysInOrder())
