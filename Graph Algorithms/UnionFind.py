class UnionFind:
    def __init__(self, N):
        self.root = [i for i in range(N)]
        self.rank = [1] * N

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootB != rootA:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootB] = rootA
                self.rank[rootA] += 1

    def find(self, a):
        if self.root[a] == a:
            return a
        self.root[a] = self.find(self.root[a])
        return self.root[a]

    def connected(self, a, b):
        return self.find(a) == self.find(b)

uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
