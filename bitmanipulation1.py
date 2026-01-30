#n=int(input())
#i=int(input())
#checkithbit
#print(n&(1<<i))
#print((n>>i)&i)
#setithbit
#print(n&~(1<<i))
#toggleithbith
#print(n^(1<<i))
#checkifnumispowerof2
#if n > 0 and (n & (n - 1)) == 0:
 #   print("power of 2")
###else:
  #  print("not power of 2")
#countthenumofsetbit
def countsetbit(n):
    cnt = 0
    while n:
        n &= n - 1
        cnt += 1
    return cnt
print(countsetbit(13))  
