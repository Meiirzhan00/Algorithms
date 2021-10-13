import math

n = int(input())
s = math.sqrt(n)
s = math.ceil(s)

for k in range(int(s)):
    x = s + k
    l = x**2 - n
    y = math.sqrt(l)
    if y%2 == 0:
        p = x + y
        q = x - y
        print(f"p = {int(p)}, q = {int(q)}")
        break
