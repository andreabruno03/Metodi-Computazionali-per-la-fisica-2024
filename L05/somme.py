def somma(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def somma_sqrt(n):
    sum_sqrt = 0
    for i in range(n+1):
        sum_sqrt = sum_sqrt + pow(i, 0.5)
    return sum_sqrt

def sommaprod(n):
    sum = 0
    prod = 1
    for i in range(n+1):
        sum += i
    for i in range(1, n):
        prod = prod * (i+1)
        print(prod)
        print(i)
    return sum, prod

def sommatoria(n, alpha=1):
    sum = 0
    for i in range(n+1):
        sum = sum + i**alpha
    return sum
