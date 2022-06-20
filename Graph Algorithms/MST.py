class Edge:
    def __init__(self, s, e, w):
        self.w = w
        self.s = s
        self.e = e

    def other(self, v):
        if v == self.s:
            return self.e
        return self.s

    def either(self):
        return self.s

    def weight(self):
        return self.w

    def compareTo(self, that):
        return -1 if self.w < that.w else 1

    def __str__(self):
        return f"From {self.s} -> {self.e} Weight ==> {self.w}"

class EdgeWeightedGrapgh:
    def __init__(self, v):
        self.v = v
        self.e = []
        self.adj = []
        for _ in range(v):
            self.adj.append([])

    def addEdge(self, edge):
        s = edge.either()
        e = edge.other(s)
        self.adj[e].append(edge)
        self.adj[s].append(edge)
        self.e.append(edge)

    def getAdj(self, v):
        return self.adj[v]

    def edges(self):
        return self.e

class MiniQueue:
    def __init__(self, m):
        self.q = [None] * (m + 1)
        self.n = 1

    def add(self, val):
        self.q[self.n] = val
        self.swim(self.n)
        self.n += 1

    def swim(self, n):
        while n > 1 and self.less(n, n//2):
            self.swap(n//2, n)
            n//=2

    def swap(self, a, b):
        self.q[a], self.q[b] = self.q[b], self.q[a]

    def deleteMin(self):
        self.swap(1, self.n-1)
        minItem = self.q[self.n-1]
        self.q[self.n-1] = None
        self.n -= 1
        self.sink()
        return minItem

    def sink(self):
        key = 1
        while 2 * key <= self.n-1:
            key *= 2
            if key < self.n - 1 and self.less(key+1, key):
                key+=1

            if self.less(key, key//2):
                self.swap(key, key//2)

            else:
                break

    def less(self, a, b):
        return self.q[a].compareTo(self.q[b]) < 0

    def isEmpty(self):
        return self.n == 1

    def printAll(self):
        return self.q[1:self.n]

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

class Kruskal:
    def __init__(self, G):
        self.G = G
        v = self.G.v
        self.mst = []
        mpq = MiniQueue(len(self.G.edges()))

        for e in self.G.edges():
            mpq.add(e)

        uf = UnionFind(v)
        while not mpq.isEmpty() and len(self.mst) < v - 1:
            edge = mpq.deleteMin()
            s = edge.either()
            end = edge.other(s)
            if uf.connected(s, end): continue
            uf.union(s, end)
            self.mst.append(str(edge))

    def getMST(self):
        return self.mst

class PrimeLazy:
    def __init__(self, G):
        self.G = G
        self.mst = []
        v = self.G.v
        self.pq = MiniQueue(len(self.G.edges()))
        self.marked = [False]*v
        self.visit(G, 0)

        while not self.pq.isEmpty() and len(self.mst) < v-1:
            edge = self.pq.deleteMin()
            s = edge.either()
            end = edge.other(s)
            if self.marked[s] and self.marked[end]: continue
            self.mst.append(str(edge))
            if not self.marked[s]: self.visit(G, s)
            if not self.marked[end]: self.visit(G, end)

    def visit(self, G, v):
        self.marked[v] = True
        for edge in self.G.getAdj(v):
            if not self.marked[edge.other(v)]:
                self.pq.add(edge)

    def getMST(self):
        return self.mst

edges = [Edge(4,5,0.35),Edge(4,7,0.37),Edge(5,7,0.28),
Edge(0,7,0.16),Edge(1,5,0.32),Edge(0,4,0.38),Edge(2,3,0.17),
Edge(1,7,0.19),Edge(0,2,0.26), Edge(1,2,0.36), Edge(1,3,0.29),
Edge(2,7,0.34),Edge(6,2,0.4), Edge(3,6,0.52),Edge(6,0,0.58),
Edge(6,4,0.93)]

G = EdgeWeightedGrapgh(8)
for e in edges:
    G.addEdge(e)

print("Using Kruskal Algorithm")
kr = Kruskal(G)
print('\n'.join(kr.getMST()))
print()
print("Using Prime Algorithm")
pl = PrimeLazy(G)
print('\n'.join(pl.getMST()))
