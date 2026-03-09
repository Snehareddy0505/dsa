class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    # Find with Path Compression
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    # Union by Rank
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


# Example Usage
n = 7
ds = DisjointSet(n)

ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 5)

print(ds.find(3))  
print(ds.find(5))  

ds.union(3, 5)

print(ds.find(6))  