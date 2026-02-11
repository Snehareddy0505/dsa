# they willgive row and column so we need to find the element in that place
row=int(input())
col=int(input())
n=row-1
r=col-1
ans=1
for i in range(r): # is for iterating only r times only
    ans=ans*(n-i) #numerators  ex:10-0=10
    ans=ans//(i+1)#denominators ex:0+1=1
print(ans)
