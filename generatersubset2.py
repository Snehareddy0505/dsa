def generatesubarray(arr):
    n=len(arr)
    total_set=(1<<n)
    ans=[]
    for val in range(total_set):
        subset=[]
        for i in range(n):
            if(val&(1<<i)):
                subset.append(arr[i])
         
        ans.append(subset)
    return ans
    
arr=list(map(int,input().split()))
print(generatesubarray(arr))