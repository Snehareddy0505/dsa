def powerexponent(x,n):
    ans=1
    for i in range(n):
        ans=ans*x
    return ans
print(powerexponent(2, 4))   # Output: 16
print(powerexponent(5, 3))   # Output: 125
