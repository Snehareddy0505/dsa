def fun(i):
    if i >= n // 2:
        return
    a[i], a[n - i - 1] = a[n - i - 1], a[i]
    fun(i + 1)

a = list(map(int, input("Enter array elements: ").split()))
n = len(a)
fun(0)

print("Reversed array:", a)
