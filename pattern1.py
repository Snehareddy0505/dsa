#n=int(input("enter n:"))
#for i in range(n):
 #   for j in range(n):
 #       print("*",end="")
  #  print()
n=int(input())
# for i in range(n):
   # for j in range(i):
   #     print("*",end="")
    #print()

#pattern3
#for i in range(1,n+1):
 #   for j in range(1,i+1):
  #      print(j,end="")
   # print()
   #pattern4
#for i in range(1,n+1):
 #   for j in range(1,i+1):
  #      print(i,end="")
   # print()
   #pattern5
#for i in range(1,n+1):
 #   for j in range(0,n-i+1):
  #      print("*",end="")
   # print()
    #pattern 6
#for i in range(1,n+1):

 # print()
 #pattern7 \
#for i in range(0,n+1):
  #  for j in range(0,n-i-1):
   #     print(" ",end="")
   ## for  j in range(0,2*i+1):
      #  print("*",end="")
#    for j in range(0,n-i-1):
   ##     print(" ",end="")
  #  print()
#pattern 8
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(0,2*i-1):
          print("*",end="")
    print()