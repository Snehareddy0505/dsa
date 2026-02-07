def secmin(arr):
    if len(arr)<2 :
        return
    min1=max1=arr[0]
    for num in arr:
        if num<min1:
            min1=num
        if num>max1:
            max1=num
    min2=float('inf')
    max2=float('-inf')
    for num in arr:
        if min1<num<min2:
            min2=num
        if max1>num>max2:
            max2=num
    if min1==max1:
        print("all same")
    if min2==float("inf"):
        print("no 2nd min")
    else:
        print(min2)
    if max2==float('-inf'):
        print("no 2nd max")
    else:
        print(max2)
arr=[1,2,3,4,5,6]
secmin(arr) 