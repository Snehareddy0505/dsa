class MinStack:
    def __init__(self):
        self.st = []   # each element = (value, min_so_far)

    def push(self, val):
        if not self.st:
            self.st.append((val, val))
        else:
            current_min = min(val, self.st[-1][1])
            self.st.append((val, current_min))

    def pop(self):
        if self.st:
            self.st.pop()

    def top(self):
        return self.st[-1][0]

    def getMin(self):
        return self.st[-1][1]


# --------- MAIN (Run in VS Code) ----------
if __name__ == "__main__":
    s = MinStack()

    s.push(5)
    s.push(3)
    s.push(7)
    s.push(2)

    print("Top:", s.top())        # 2
    print("Min:", s.getMin())     # 2

    s.pop()
    print("Min after pop:", s.getMin())  # 3
