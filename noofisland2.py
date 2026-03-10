class Solution:
    def numIslands2(self, m, n, positions):
        parent = {}
        rank = {}
        count = 0
        result = []

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal count
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                count -= 1

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r, c in positions:
            node = r * n + c

            if node in parent:
                result.append(count)
                continue

            parent[node] = node
            rank[node] = 0
            count += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                neighbor = nr * n + nc

                if 0 <= nr < m and 0 <= nc < n and neighbor in parent:
                    union(node, neighbor)

            result.append(count)

        return result
m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[2,1]]

obj = Solution()
print(obj.numIslands2(m, n, positions)) 