def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    sum = 0
    while (p **2 <= n):
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            sum+=p

    return sum

print(SieveOfEratosthenes(2000000))