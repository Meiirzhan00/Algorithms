import math

n = int(input())

for b in range(2,n+1):
    f = 1
    while b > 1:
        f *= b
        b -= 1

    A = 2**f%n
    i = A - 1

    p = math.gcd(n, i)

    if p != 1:
        q = n / p
        break

print(f"q = {int(q)}, p = {p}")
