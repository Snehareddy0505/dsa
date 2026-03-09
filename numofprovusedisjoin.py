class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return

        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]


class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        ds = DisjointSet(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    ds.union(i, j)

        provinces = 0
        for i in range(n):
            if ds.find(i) == i:
                provinces += 1

        return provinces
isConnected = [
 [1,1,0],
 [1,1,0],
 [0,0,1]
]

s = Solution()
print(s.findCircleNum(isConnected)) 