#here will give only row number so that we have to print the entire row
#def generateRow(row,col):
 #   n=row-1
    # r=col-1 
  # ans=1
   # for i in range(r):
    #    ans=ans*(n-i)
     #   ans=ans//(i+1)
    #print(ans,end=" ")
#row=int(input())
#for col  in range(1,row+1):
 #   generateRow(row,col)
   
#optimal approach
row=int(input())
ans=1
print(ans,end=" ")
for col in range(1,row):
    ans=ans*(row-col)
    ans=ans//col
    print(ans,end=" ")
