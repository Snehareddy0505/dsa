def shortest_job_first(arr):
    n = len(arr)
    
    # Step 1: Sort jobs by burst time
    arr.sort()
    
    t = 0          # current time
    wtTime = 0     # total waiting time
    
    # Step 2: Calculate waiting time
    for i in range(n):
        wtTime += t
        t += arr[i]
    
    # Step 3: Return average waiting time
    return wtTime / n
arr = [6, 8, 7, 3]
print(shortest_job_first(arr))
