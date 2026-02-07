def minplatform(arr,dep):
    j=0
    c=0
    res=0
    n=len(arr)
    arr.sort()
    dep.sort()
    for i in range(n):
        while j<n and dep[j]<arr[i]:
            c-=1
            j+=1
        c+=1
        res=max(res,c)
    return res
