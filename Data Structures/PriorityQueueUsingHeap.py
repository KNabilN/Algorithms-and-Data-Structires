class PriorityQueue:
    def __init__(self, M):
        self.N = 0
        self.pq = [None] * (M+1)
        self.M = M

    def insert(self, item):
        if self.N < self.M + 1:
            self.N += 1
            self.pq[self.N] = item
            self.swim(self.N)

    def deleteMax(self):
        if not self.is_empty():
            self.exchange(self.N, 1)
            maxItem = self.pq[self.N]
            self.pq[self.N] = None
            self.N -= 1
            self.sink(1)
            return maxItem
        return "Empty"

    def is_empty(self):
        return self.N == 0

    def swim(self, i):
        while i > 1 and self.less(i // 2, i):
            self.exchange(i, i // 2)
            i //= 2

    def sink(self, key):
        while 2 * key <= self.N:
            j = 2 * key
            if j < self.N and self.less(j, j + 1): j+=1
            if not self.less(key, j): break
            self.exchange(key, j)
            key = j

    def exchange(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def less(self, i, j):
        try:
            return self.pq[i].compareTo(self.pq[j]) > 0
        except:
            return self.pq[i] < self.pq[j]

    def show(self):
        return self.pq

pq = PriorityQueue(11)
pq.insert(6)
pq.insert(2)
pq.insert(5)
pq.insert(0)
pq.insert(8)
pq.insert(1)
pq.insert(3)
pq.insert(9)
pq.insert(8)
pq.insert(10)

print(pq.show())
