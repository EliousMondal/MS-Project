import re
import matplotlib.pyplot as plt

PES_file = open("PES_2001.txt")
data = []
for line in PES_file:
    r = re.findall("^[0-9].+\S",line)
    if len(r)>0:
        data.append(r[0])
R = []
E = []
for r in data:
    d = r.split()
    R.append(float(d[0]))
    E.append(float(d[1]))

plt.figure()
plt.xlabel("R(au) ----->")
plt.ylabel("E(au) ----->")
plt.title("PES for H2")
plt.plot(R,E)
plt.show()
