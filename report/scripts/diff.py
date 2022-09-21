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

saving = 1

graphdirectory = "../graphs/"

# ---------- COMPUTATIONS ----------

t1 = 1
t2 = t1/2
e3s = np.linspace(-3*t1, 5*t1, 5)
Us = np.linspace(0.1, 10, 25)

fig, ax = plt.subplots(figsize=(5, 5))

for e3 in e3s:

	et = 0.5*(e3-t2-sqrt((t2-e3)**2 + 8*t1**2))
	diff = []

	for U in Us:

		H = np.array([[0, sqrt(2)*t1, 2*t2, 0],
					 [sqrt(2)*t1, t2+e3, sqrt(2)*t1, 2*t1],
					 [2*t2, sqrt(2)*t1, U, 0],
					 [0, 2*t1, 0, 2*e3+U]])

		eigs = np.linalg.eigvals(H)
		es = np.amin(eigs)

		diff.append(es - et)

		# ---------- PLOT ----------


	ax.plot(Us, diff, linestyle='-', label=rf"$\varepsilon_3 = {e3}$")

ax.plot(Us, np.zeros(len(Us)), color='k', linewidth=2)

ax.set_xlabel("$U$")
ax.set_ylabel(r"$\varepsilon_s - \varepsilon_t$")
ax.minorticks_on()
ax.grid(which='minor', linewidth=0.2)
ax.grid(which='major', linewidth=0.6)
ax.set_ylim(-0.5, 0.5)
ax.legend(loc='lower right')

plt.draw()

# # ---------- SAVING ----------

if saving:
	fig.savefig(graphdirectory + "diff")

plt.show()