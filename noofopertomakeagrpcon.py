from collections import defaultdict

class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            stack = [node]
            while stack:
                curr = stack.pop()
                for nei in graph[curr]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

        components = 0

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1

        return components - 1
n = 4
connections = [[0,1],[0,2],[1,2]]

obj = Solution()
print(obj.makeConnected(n, connections))