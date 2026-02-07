def maximummeetings(start,end):
    n=len(start)
    meetings=[]
    for i in range(n):
        meetings.append((end[i],start[i]))
    meetings.sort()
    le=-1
    c=0
    for e,s in meetings:
        if s>le:
            c+=1
            le=e
    return c