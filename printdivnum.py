class Solution:
    def printdivofnum(self, num):
        arr = []
        for i in range(1, num + 1):
            if num % i == 0:
                arr.append(i)
        return arr

num = 15
sol = Solution()
print(sol.printdivofnum(num))
