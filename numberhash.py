n = int(input("enter number of elements:"))
arr = list(map(int, input("enter elements").split()))
hash_table = [0] * 13

for num in arr:
    if 0 <= num < 13:
        hash_table[num] += 1
    else:
        print(f"{num} is out of range")

q = int(input("enter number of queries:"))
for _ in range(q):
    number = int(input("enter query number:"))
    if 0 <= number < 13:
        print(hash_table[number])
    else:
        print("Out of range")

