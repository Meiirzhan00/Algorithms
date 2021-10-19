
# import time
# import math
#
# start_time = time.time()
#
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
#
# end = time.time() - start_time
# print(f"{end} seconds")
#
#
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
# end = time.time() - start_time
# print(f"{end} seconds")


# import time
# start_time = time.time()
#
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
# end = time.time() - start_time
# print(f"{end} seconds")


# import time
# import matplotlib.pyplot as plt
#
# start_time = time.time()
#
# index = []
# values = []
# persentt = []
#
# eng_alph = "abcdefghijklmnopqrstuvwxyz"
# symbols = " .,/:;)(@#$%^&*+-"
# c = 0
# newstr = ""
#
# with open("foo","r") as file:
#     if file.mode == "r":
#         message = file.read()
#     for j in symbols:
#             if j in message:
#                 s = message.split(f"{j}")
#                 for k in s:
#                     newstr += k
#                     lowerstr = newstr.lower()
#                 for i in eng_alph.lower():
#                         if i in lowerstr:
#                             c = lowerstr.count(i)
#                             percent = (c * 100) / len(lowerstr)
#                             with open("savedata", "a") as file:
#                                 index.append(i)
#                                 values.append(c)
#                                 persentt.append(percent)
#                                 file.write("\n")
#                                 file.write(f"{i} = {c} = {percent}%")
#
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.bar(index,values)
# plt.show()
