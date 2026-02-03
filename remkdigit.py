class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        while k > 0 and stack:
            stack.pop()
            k -= 1

        res = ''.join(stack)
        res = res.lstrip('0')

        return res if res else "0"


if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())   # FIXED

    sol = Solution()
    print(sol.removeKdigits(s, k))
