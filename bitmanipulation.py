n=int(input())
i=int(input())
def checithbit(n):
     if(n&(1<<i)!=0):
          print("set")
     else:
          print("not set")