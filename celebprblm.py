def celebrityproblem(mat):
    n = len(mat)
    top = 0
    down = n - 1

    # Step 1: Find a possible celebrity
    while top < down:
        if mat[top][down] == 1:
            # top knows down → top can't be celebrity
            top += 1
        else:
            # top does not know down → down can't be celebrity
            down -= 1

    candidate = top

    # Step 2: Verify the candidate
    for i in range(n):
        if i != candidate:
            # candidate should not know i
            # everyone should know candidate
            if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                return -1   # no celebrity

    return candidate
mat = [
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]

print(celebrityproblem(mat))  # Output: 2
