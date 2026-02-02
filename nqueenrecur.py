def solveNQueens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    ans = []

    def isSafe(row, col):
        # check same column
        for i in range(row):
            if board[i][col] == "Q":
                return False

        # check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def nqueen(row):
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for col in range(n):
            if isSafe(row, col):
                board[row][col] = "Q"
                nqueen(row + 1)
                board[row][col] = "."   # backtrack

    nqueen(0)
    return ans
result = solveNQueens(4)
print(result)
