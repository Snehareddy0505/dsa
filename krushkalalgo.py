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


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])   # sort edges by weight
    ds = DisjointSet(n)

    mst_weight = 0
    mst_edges = []

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges


# Example Graph
n = 4
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

weight, mst = kruskal(n, edges)

print("Minimum Spanning Tree Weight:", weight)
print("Edges in MST:", mst) 