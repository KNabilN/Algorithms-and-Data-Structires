#Using a Node structure in our Tree
class Node:
    def __init__(self, key, value, count):
        self.left = None
        self.right = None
        self.value = value
        self.key = key
        self.count = count

class BST:
    #Initialize our tree
    def __init__(self):
        self.root = None
    #Adding key, value node (Client method)
    def put(self, key, value):
        self. root = self._put(self.root, key, value)
    #Adding key, value node (Developer method)
    def _put(self, x, key, value):
        if x == None:
            return Node(key, value, 1)
        if key > x.key:
            x.right = self._put(x.right, key, value)
        elif key < x.key:
            x.left = self._put(x.left, key, value)
        else:
            x.value = value
        #The size of the subtree
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x

    def size(self, x):
        if x == None: return 0
        return x.count

    #Find a certain key, value
    def get(self, key):
        x = self.root
        while x != None:
            if key < x.key: x = x.left
            elif key > x.key: x = x.right
            else: return x.value
        #If doesn't exist return None
        return None

    #Find the maximum key behind a certain key (Client Method)
    def floor(self, key):
        x = self._floor(self.root, key)
        return x.value

    #Find the maximum key behind a certain key (Developer Method)
    def _floor(self, x, key):
        if x == None: return None

        if key < x.key: self._floor(x.left, key)

        t = self._floor(x.right, key)
        if t != None: return t
        return x

    #Find the minumum key above a certain key (Client Method)
    def ceil(self, key):
        x = self._ceil(self.root, key)
        return x.value

    #Find the minumum key above a certain key (Developer Method)
    def _ceil(self, x, key):
         if x == None: return None

         if key > x.key: self._ceil(x.right, key)

         t = self._ceil(x.left, key)
         if t != None: return t
         return x

    #find how many nodes are smaller than a certain node (Client Method)
    def rank(self, key):
        x = self._rank(self.root, key)
        return x

    #find how many nodes are smaller than a certain node (Developer Method)
    def _rank(self, x, key):
        if x == None: return 0

        if key < x.key: return self._rank(x.left, key)
        elif key > x.key: return 1 + self.size(x.left) + self._rank(x.right, key)
        else: return self.size(x.left)

    #Return All keys inorder
    def keys(self):
        q = []
        self.inorder(self.root, q)
        return q

    def inorder(self, x, q):
        if x == None: return
        self.inorder(x.left, q)
        q.append(x.key)
        self.inorder(x.right, q)

    def deleteMin(self):
        self.root = self._deleteMin(self.root)

    def _deleteMin(self, x):
        if x.left == None: return x.right
        x.left = self._deleteMin(x.left)
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, x, key):
        if x == None:
            print("{key} doesn't exist")
            return None

        if key < x.key: x.left = self._delete(x.left, key)
        elif key > x.key: x.right = self._delete(x.right, key)
        else:

            if x.left == None: return x.right
            if x.right == None: return x.left

            t = x
            x = self.minimum(t.right)
            x.right = self.deleteMin(t.right)
            x.left = t.left

        return x


    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x

#Create an instance of Binary Search Tree
bst = BST()
#Adding Values to it
bst.put("a", 2)
bst.put("A", 2)
bst.put("D", 1)
bst.put("B", 5)
bst.put("C", 5)
#Delete the minimum key
bst.deleteMin()
print(bst.keys())
#Delete a certain key
bst.delete('D')
print(bst.keys())
