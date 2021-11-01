from math import *
def kitay():
    m1, m2, m3 = [int(i) for i in input().split()]
    c1, c2, c3 = [int(j) for j in input().split()]
    if gcd(m1,m2)==1 and gcd(m1,m3)==1 and gcd(m2,m3)==1:
        if c1 < m1 and c2 < m2 and c3 < m3:
            print(f"x = {c1}(mod{m1})\n"
                  f"x = {c2}(mod{m2})\n"
                  f"x = {c3}(mod{m3})")

            M = m1 * m2 * m3
            print(f"M = {M}")
            M1 = M//m1
            M2 = M//m2
            M3 = M//m3

            print(f"M1 = {M1}, M2 = {M2}, M3 = {M3}")

            for y1 in range(1,m1):
                if M1 * y1 % m1 == 1:
                    y1 = y1
                    print(f"y1 = {y1}")
            for n in range(1,m2):
                if M2 * n % m2 == 1:
                    y2 = n
                    print(f"y2 = {y2}")
            for k in range(1,m3):
                if M3 * k % m3 == 1:
                    y3 = k

            x0 = M1 * y1 * c1 + M2 * y2 * c2 + M3 * y3 * c3
            print(f"{M1}*{y1}*{c1} + {M2}*{y2}*{c2} + {M3}*{y3}*{c3}")
            print(f"x0 = {x0}")
            print(f"x = {x0%M}")
t = kitay()

def y():
    for y1 in range(1, t.m1):
        if t.M1 * y1 % t.m1 == 1:
            y1 = y1
