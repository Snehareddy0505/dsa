def fun(i,n):
    if i>n:
        return 
    print(i)
    fun(i+1,n)
n=int(input("enter n:"))
fun(1,n)