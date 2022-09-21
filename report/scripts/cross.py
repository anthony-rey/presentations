# ---------- PACKAGES ----------

import matplotlib.pyplot as plt
import numpy as np
from math import *

# ---------- ENVIRONMENT ----------

colors = [[0.8, 0, 0.5],[0, 0.5, 0.8],[0.8, 0.5, 0]]

plt.rcParams.update({
	'text.usetex': True,
	'font.family': 'serif',
	'font.size': 14,
	'legend.facecolor': colors[0],
	'legend.framealpha': 0.08,
	'legend.fontsize': 12,
	'savefig.dpi': 250,
	'savefig.bbox': 'tight',
	'savefig.format': 'png',
	})

# ---------- SETUP ----------

saving = 0

graphdirectory = "../graphs/"

# ---------- COMPUTATIONS ----------

t1 = 1
t2 = t1/2
e3s = np.linspace(-10*t1, 10*t1, 50)
Us = np.linspace(0.1, 100, 1000)

fig, ax = plt.subplots(figsize=(5, 5))

cross = np.zeros((1, len(e3s)))

for i in range(len(e3s)):

	et = 0.5*(e3s[i]-t2-sqrt((t2-e3s[i])**2 + 8*t1**2))
	diff = []

	for U in Us:

		H = np.array([[0, sqrt(2)*t1, 2*t2, 0],
					 [sqrt(2)*t1, t2+e3s[i], sqrt(2)*t1, 2*t1],
					 [2*t2, sqrt(2)*t1, U, 0],
					 [0, 2*t1, 0, 2*e3s[i]+U]])

		eigs = np.linalg.eigvals(H)
		es = np.amin(eigs)

		diff = es - et

		if diff>-0.01 and diff<0.01:
			cross[0][i] = U

		# ---------- PLOT ----------


ax.scatter(e3s, cross, marker='x', color=colors[0])

ax.set_xlabel(r"$\varepsilon_3$")
ax.set_ylabel(r"$U$")
ax.minorticks_on()
ax.grid(which='minor', linewidth=0.2)
ax.grid(which='major', linewidth=0.6)
# ax.legend(loc='lower right')

plt.draw()

# # ---------- SAVING ----------

if saving:
	fig.savefig(graphdirectory + "cross")

plt.show()