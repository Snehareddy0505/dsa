def job_sequencing(job_id, profit, deadline):
    n = len(job_id)

    # Create jobs as (profit, deadline, id)
    jobs = []
    for i in range(n):
        jobs.append((profit[i], deadline[i], job_id[i]))

    # Step 1: Sort jobs by profit (descending)
    jobs.sort(reverse=True, key=lambda x: x[0])

    # Step 2: Find maximum deadline
    max_deadline = max(deadline)

    # Step 3: Slot array to store job ids
    slot = [-1] * (max_deadline + 1)

    total_profit = 0
    count_jobs = 0

    # Step 4: Schedule jobs
    for p, d, jid in jobs:
        for t in range(d, 0, -1):
            if slot[t] == -1:
                slot[t] = jid
                total_profit += p
                count_jobs += 1
                break

    return count_jobs, total_profit
job_id   = [1, 2, 3, 4]
profit   = [20, 10, 40, 30]
deadline = [1, 1, 2, 2]

print(job_sequencing(job_id, profit, deadline))
