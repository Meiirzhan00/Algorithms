# import matplotlib.pyplot as plt
#
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
# plt.xlabel('Әріптер')
# plt.ylabel('Әріптер саны')
# plt.bar(index,values)
# plt.show()

from tkinter import *
from tkinter import scrolledtext


def analysis():
    enc_txt = txt.get()
    lbl.configure(text=enc_txt)


window = Tk()
window.title("Жиілікті талдау")
window.geometry('1200x700')
lbl = Label(window)
lbl.grid(column=1)
txt = scrolledtext.ScrolledText(window, width=118, height=15)
txt.grid(column=0, row=0)
btn = Button(window, text = "Есептеу",width=25,height=5, command=analysis)
btn.grid(column=1,row=0)
window.mainloop()
