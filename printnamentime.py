def fun(i, n):
    if i > n:
        return
    print("sneha")
    fun(i + 1, n)

n = int(input("Enter n: "))
fun(1, n)
