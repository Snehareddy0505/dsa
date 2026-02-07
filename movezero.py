def movezero(arr):
    ind=0
    for i in range(len(arr)):
        if arr[i]!=0:
           arr[ind]=arr[i]
           ind+=1
    for i in range(ind,len(arr)):
        arr[i]=0
arr=[0,1,0,3,12]
movezero(arr)
print(arr)
 