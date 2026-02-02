import math
def prime(num):
    cnt=0
    for i in range(1,int(math.sqrt(num))+1):
        if num%i==0:
            cnt+=1
            if num//i !=i:
                cnt+=1
        if cnt>2:
            break
    if cnt==2:
        print("yes")
    else:
        print("no")
    return cnt
num=35
print(prime(num))
