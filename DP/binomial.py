def factorial(n):
    fac = [1,1]

    for i in range(2, n):
        fac.append(i*fac[i-1])
    return fac[n-1]

def binomial(n, k):
    bin = factorial(n)//(factorial(k)*factorial(n-k))
    print(int(bin))

binomial(4, 2)