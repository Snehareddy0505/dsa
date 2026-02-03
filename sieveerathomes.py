def sieveoferathomes(n):
    prime = [1] * (n + 1)   # create array
    prime[0] = prime[1] = 0

    for i in range(2, int(n**0.5) + 1):
        if prime[i] == 1:
            for j in range(i * i, n + 1, i):
                prime[j] = 0

    for i in range(2, n + 1):
        if prime[i] == 1:
            print(i)
sieveoferathomes(20)

