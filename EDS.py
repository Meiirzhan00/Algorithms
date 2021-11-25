import random
from sympy import *

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

x = random.randint(1,p-1)
y = (g**x)%p

print(f'Ашық кілт: (p, g, y) = {p, g, y}. Жабық кілт: x = {x}')

k = random.randint(1,p-1)
if gcd(p,k):
    k = k

m = int(input('Шифрлау керек санды енгіз: '))
a = (g**k)%p

# b = 0
# while True:
#     b += 1
#     if m == (x*a + k*b)%(p-1):
#         b = b
#         break

# print(hash('meiirzhan'))

r = (g**k)%p
s = (m - x*r)*(k**(-1))%(p-1)

print(f'Электронды цифрлық қолтаңба : {r, s}')

if ((y**r)*(r**s))%p == (g**m)%p:
    print('Қолтаңба дұрыс !')
