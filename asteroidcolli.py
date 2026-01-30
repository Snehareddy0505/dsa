class Solution:
    def asteroidcollision(self, asteriod):
        stack = []
        for ast in asteriod:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()          # FIX 1
                    continue
                elif stack[-1] == -ast:
                    stack.pop()          # FIX 1
                break
            else:
                stack.append(ast)
        return stack                     # FIX 2

asteriod =list(map(int,input().split()))
sol = Solution()
print(sol.asteroidcollision(asteriod))
