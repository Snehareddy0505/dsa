arr = list(map(int, input("enter the elements:").replace(',','').split()))
mpp = {}
for num in arr:
    mpp[num] = mpp.get(num, 0) + 1
q = int(input("enter number of queries:"))
for _ in range(q):
    number = int(input("enter number to checkvfrequency:"))
    print(mpp.get(number, 0))
 