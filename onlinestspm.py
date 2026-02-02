class StockSpanner:
    def __init__(self):
        self.st = []        # stack stores (price, index)
        self.ind = -1

    def next(self, val: int) -> int:
        self.ind += 1

        # remove smaller or equal prices
        while self.st and self.st[-1][0] <= val:
            self.st.pop()

        if not self.st:
            ans = self.ind + 1
        else:
            ans = self.ind - self.st[-1][1]

        self.st.append((val, self.ind))
        return ans
s = StockSpanner()

prices = [100, 80, 60, 70, 60, 75, 85]
for p in prices:
    print(s.next(p), end=" ")
