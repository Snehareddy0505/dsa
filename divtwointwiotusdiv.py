def divide(dividend,divisor):
    sum=0
    cnt=0
    while sum+divisor<=dividend:
        cnt+=1
        sum+=divisor
    return cnt
dividend=22
divisor=3
print(divide(dividend,divisor))