def jumpgame2(arr, ind, jumps):
    n = len(arr)
    
    if ind >= n - 1:
        return jumps
    
    if arr[ind] == 0:
        return float('inf')
    
    mini = float('inf')
    
    for step in range(1, arr[ind] + 1):
        mini = min(mini, jumpgame2(arr, ind + step, jumps + 1))
    
    return mini
arr = [2, 3, 1, 1, 4]
print(jumpgame2(arr, 0, 0))
