def powerexpo(x,n):
    ans=1
    while n>0:
        if n%2==1:
            ans=ans*x
            n-=1
        else:
            n=n//2
            x=x*x
    return ans
print(powerexpo(2,4))