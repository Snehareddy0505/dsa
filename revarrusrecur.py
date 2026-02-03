def revarr(l, r):
    if l >= r:
        return
    a[l], a[r] = a[r], a[l]
    revarr(l + 1, r - 1)

n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter elements: ").split()))

revarr(0, n - 1)

print("Reversed array:", a)
