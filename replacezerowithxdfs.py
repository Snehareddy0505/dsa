def solve(board):
    if not board:
        return
    
    n = len(board)
    m = len(board[0])
    
    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != 'O':
            return
        
        board[r][c] = 'S'  # mark safe
        
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
    
    # Step 1: Traverse boundaries
    for i in range(n):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][m-1] == 'O':
            dfs(i, m-1)
    
    for j in range(m):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[n-1][j] == 'O':
            dfs(n-1, j)
    
    # Step 2: Convert remaining O -> X, S -> O
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'S':
                board[i][j] = 'O'
board = [
    ['X','X','X','X'],
    ['X','O','O','X'],
    ['X','X','O','X'],
    ['X','O','X','X']
]

solve(board)

print(board)