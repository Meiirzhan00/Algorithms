import matplotlib.pyplot as plt


index = []
values = []
persentt = []

eng_alph = "abcdefghijklmnopqrstuvwxyz"
symbols = " .,/:;)(@#$%^&*+-"
c = 0
newstr = ""

with open("foo","r") as file:
    if file.mode == "r":
        message = file.read()
    for j in symbols:
            if j in message:
                s = message.split(f"{j}")
                for k in s:
                    newstr += k
                    lowerstr = newstr.lower()
                for i in eng_alph.lower():
                        if i in lowerstr:
                            c = lowerstr.count(i)
                            percent = (c * 100) / len(lowerstr)
                            with open("savedata", "a") as file:
                                index.append(i)
                                values.append(c)
                                persentt.append(percent)
                                file.write("\n")
                                file.write(f"{i} = {c} = {percent}%")

plt.xlabel('Әріптер')
plt.ylabel('Әріптер саны')
plt.bar(index,values)
plt.show()
