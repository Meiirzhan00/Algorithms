import math
import matplotlib.pyplot as plt
import time

index = ["Ферма","Полард","Пробные деление"]
values = []

start_time_po = time.time()

n = int(input("Ферма | Санды енгіз: "))
s = math.sqrt(n)
s = math.ceil(s)

for k in range(int(s)):
    x = s + k
    l = x**2 - n
    y = math.sqrt(l)
    if y%2 == 0:
        p = x + y
        q = x - y
        break

r=time.time()
end_po = time.time() - start_time_po
print(f"Ферма: {math.ceil(end_po)} секунд")
values.append(end_po)


start_time_ph = time.time()
n = int(input("Полард | Санды енгіз: "))
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

end_ph = time.time() - start_time_ph
print(f"Полард: {math.ceil(end_ph)} секунд")
values.append(end_ph)



import time
start_time_pr = time.time()


x=int(input('Пробные деление | Санды енгіз: '))
Ans = []
d = 2
while d <= x:
    if x % d == 0:
        Ans.append(d)
        x //= d
    else:
        d += 1
q=1
my_dict={}
for item in range(1000):
    if item in Ans:
      my_dict[item]=Ans.count(item)
      q*=(item**(Ans.count(item)-1))*(item-1)

end_pr = time.time() - start_time_pr
print(f"Пробные деление: {math.ceil(end_pr)} секунд")
values.append(end_pr)

plt.xlabel('Theories')
plt.ylabel('Time to second')
plt.bar(index,values)
plt.show()

# def san():
#   x=int(input('Санды енгіз : '))
#   Ans = []
#   d = 2
#   while d <= x:
#       if x % d == 0:
#         Ans.append(d)
#         x //= d
#       else:
#           d += 1
#   q=1
#   my_dict={}
#   for item in range(1000):
#     if item in Ans:
#       my_dict[item]=Ans.count(item)
#       q*=(item**(Ans.count(item)-1))*(item-1)
#   print("Жәй сандарға жіктелген : ", Ans)
#   print("Дәрежесі бойынша жіктелген: ", my_dict)
#
# san()

# import time
# import math

# n = int(input())
# s = math.sqrt(n)
# s = math.ceil(s)
#
# for k in range(int(s)):
#     x = s + k
#     l = x**2 - n
#     y = math.sqrt(l)
#     if y%2 == 0:
#         p = x + y
#         q = x - y
#         print(f"p = {int(p)}, q = {int(q)}")
#         break

# import time
# import math
# n = int(input())
# for b in range(2,n+1):
#     f = 1
#     while b > 1:
#         f *= b
#         b -= 1
#
#     A = 2**f%n
#     i = A - 1
#
#     p = math.gcd(n, i)
#
#     if p != 1:
#         q = n / p
#         break
#
# print(f"q = {int(q)}, p = {p}")

n, m, s = 3, 3, 0
a = [[i+j for j in range(m)] for i in range(n)]
for i in range(n):
    s += sum(a[i])
print(s)

a = [0, 1, 2, 3]
for a[0] in a:
    print(a[0])


a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
t = 0
for row in a:
    for elem in row:
        t += elem % 5
print(t)


