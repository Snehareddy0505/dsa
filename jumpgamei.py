def jumpgame(arr):
    maxind=0
    n=len(arr)
    for i in range(n):
        if i>maxind:
            return False
        maxind=max(maxind,i+arr[i])
    return True
arr=[2,3,2,1,0]
print(jumpgame(arr))