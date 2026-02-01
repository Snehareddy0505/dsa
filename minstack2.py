class MinStack:
    def __init__(self):
        self.st = []
        self.mini = None

    def push(self, val):
        if not self.st:
            self.st.append(val)
            self.mini = val
        elif val < self.mini:
            # store encoded value
            self.st.append(2 * val - self.mini)
            self.mini = val
        else:
            self.st.append(val)

    def pop(self):
        if not self.st:
            return

        x = self.st.pop()
        if x < self.mini:
            # restore previous minimum
            self.mini = 2 * self.mini - x

    def top(self):
        if not self.st:
            return None

        x = self.st[-1]
        if x < self.mini:
            return self.mini
        return x

    def getMin(self):
        return self.mini
s = MinStack()
s.push(5)
s.push(3)
s.push(7)
s.push(2)

print("Top:", s.top())      # 2
print("Min:", s.getMin())   # 2

s.pop()
print("Top:", s.top())      # 7
print("Min:", s.getMin())   # 3
