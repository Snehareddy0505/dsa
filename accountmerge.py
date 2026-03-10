from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(list)
        email_to_name = {}

        # Build graph
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            
            for email in acc[1:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
                email_to_name[email] = name

        visited = set()
        result = []

        # DFS to collect connected emails
        def dfs(email, temp):
            visited.add(email)
            temp.append(email)

            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, temp)

        for email in graph:
            if email not in visited:
                temp = []
                dfs(email, temp)
                result.append([email_to_name[email]] + sorted(temp))

        return result
accounts = [
["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]
]

obj = Solution()
print(obj.accountsMerge(accounts))