def fun(i):
    if i < 1:
        return
    print(i)
    fun(i - 1)

n = int(input("enter n: "))
fun(n)
