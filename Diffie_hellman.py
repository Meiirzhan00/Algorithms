import random
from sympy import *

a = int(input('a санын енгіз: '))
b = int(input('b санын енгіз: '))

while True:
    p = random.randint(1, 100)
    if isprime(p):
        p = p
        break

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots[0]

g = primRoots(p)


A = (g**a)%p
B = (g**b)%p

K = (B**a)%p

print(f'Жабық кілт мәні. K = {K}')

if (B**a)%p == (A**b)%p:
  print('Жабық кілт ДҰРЫС')
