def miniflipbit(start,goal):
    ans=start^goal
    cnt=0
    for i in range(31):
        if(ans&(1<<i)):
            cnt+=1
    return cnt
print(miniflipbit(10,7))