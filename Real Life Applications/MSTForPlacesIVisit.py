class Edge:
    #The main structure to represent destinations
    def __init__(self, side, otherside, weight):
        #weight is the distance in KM
        self.side = side
        self.otherside = otherside
        self.weight = weight

    def either(self):
        return self.side

    def other(self, vertex):
        if vertex == self.side:
            return self.otherside
        return self.side

    def getWeight(self):
        return self.weight

    def __str__(self):
        return f"{self.side} -> {self.otherside}"

    def __lt__(self, that):
        return self.weight < that.weight

class EdgeWeightedGrapgh:
    #To represent the map bet places
    def __init__(self, v):
        self.v = v
        self.adj = []
        self.edges = []
        for _ in range(v):
            self.adj.append([])

    def addEdge(self, edge):
        st = edge.either()
        en = edge.other(st)
        self.adj[st].append(edge)
        self.adj[en].append(edge)
        self.edges.append(edge)

    def getEdges(self):
        return self.edges

    def getAdj(self, v):
        return self.adj[v]

class UF:
    #Union Find Algorithm to use with Kruksal Algo
    def __init__(self, v):
        self.root = [i for i in range(v)]
        self.rank = [1] * v

    def checkRank(self, x, y):
        return 1 if self.rank[x] > self.rank[y] else -1

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] == self.rank[rootY]:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            elif self.checkRank(rootX, rootY) > 1:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def connected(self, st, en):
        return self.find(st) == self.find(en)

import heapq
class Kruksal:
    def __init__(self, G):
        heap = G.getEdges()
        heapq.heapify(heap)
        uf = UF(G.v)
        self.mst = []

        while heap and len(self.mst) < G.v - 1:
            minEdge = heapq.heappop(heap)
            st = minEdge.either()
            en = minEdge.other(st)
            if uf.connected(st, en): continue
            self.mst.append(minEdge)
            uf.union(st, en)

    def getMST(self):
        return self.mst

class PrimeLazy:
    def __init__(self, G):
        self.G = G
        self.heap = []
        self.mst = []
        self.marked = [0]*self.G.v
        self.visit(0)

        while self.heap and len(self.mst) < G.v - 1:
            edge = heapq.heappop(self.heap)
            st = edge.either()
            en = edge.other(st)
            if self.marked[st] and self.marked[en]: continue
            self.mst.append(edge)
            if not self.marked[st]: self.visit(st)
            if not self.marked[en]: self.visit(en)

    def getMST(self):
        return self.mst

    def visit(self, vertex):
        self.marked[vertex] = 1
        for edge in self.G.getAdj(vertex):
            en = edge.other(vertex)
            if not self.marked[en]:
                heapq.heappush(self.heap, edge)

mp = {
0: "Home",
1:"7ab3a",
2:"Korne4",
3:"Mohsem",
4:"GYM"
}
edges = [Edge(0,1,1.7), Edge(0,2,5.3),Edge(0,3,0.27), Edge(0,4,1.2),
Edge(1,2,3.9), Edge(1,3,1.6), Edge(1,4,1.8), Edge(2,3,5.1), Edge(2,4,4.1), Edge(3,4,1)]

G = EdgeWeightedGrapgh(5)
for e in edges:
    G.addEdge(e)

print("Using Kruskal Algorithm")
kr = Kruksal(G)
w = 0
for edge in kr.getMST():
    st = edge.either()
    end = edge.other(st)
    w += edge.getWeight()
    print(f"From {mp[st]} -> {mp[end]}")
w*=2
print(f"This Takes {w} KM")
print()
print("Using prime Algorithm")
pl = PrimeLazy(G)
w = 0
for edge in pl.getMST():
    st = edge.either()
    end = edge.other(st)
    w += edge.getWeight()
    print(f"From {mp[st]} -> {mp[end]}")
w*=2
print(f"This Takes {w} KM")
