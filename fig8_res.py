import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps as cm
import load_obsdata as obs

# 1x2 grid of plots
fig, ax = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)
# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0, hspace=0)

ax[0].set_xlim(8.5, 12.5)
ax[0].set_ylim(-5.4, -0.6)

xlabel = r"$\log_{10} (M_* \,[M_{\odot}])$"
ylabel = r"$\log_{10} (dn/d\log_{10}M_* \,[{\rm cMpc}^{-3} {\rm dex}^{-1}])$"
ax[0].set_ylabel(ylabel)
ax[0].set_xlabel(xlabel)
ax[1].set_xlabel(xlabel)

# Panel 1: z = 2.2

d = obs.load_target_obsdata("SMF", "davidzon2017_z2.25")
ax[0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Davidzon+ 17 (z=2.25)")

d = obs.load_target_obsdata("SMF", "mcleod2021_z2")
ax[0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="McLeod+ 21 (z=2)")

ax[0].set_prop_cycle(None)

d = np.loadtxt("stellar_mass_function/SMF_z2_L25N512.dat")
ax[0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z2_L25N256.dat")
ax[0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z2_L25N128.dat")
ax[0].plot(d[:,0], d[:,1], ms=0)

ax[0].text(0.8, 0.7, "z=2.2", transform=ax[0].transAxes, fontsize=15)

ax[0].legend(loc="upper right", fontsize=10)

# Panel 4: z=0

d = obs.load_target_obsdata("SMF", "baldry2012_z0")
ax[1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Baldry+ 12 (z=0)")

d = obs.load_target_obsdata("SMF", "driver2022_z0")
ax[1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Driver+ 22 (z=0)")

ax[1].set_prop_cycle(None)

d = np.loadtxt("stellar_mass_function/SMF_z0_L25N512.dat")
ax[1].plot(d[:,0], d[:,1], ms=0, label="L25N512")

d = np.loadtxt("stellar_mass_function/SMF_z0_L25N256.dat")
ax[1].plot(d[:,0], d[:,1], ms=0, label="L25N256")

d = np.loadtxt("stellar_mass_function/SMF_z0_L25N128.dat")
ax[1].plot(d[:,0], d[:,1], ms=0, label="L25N128")

ax[1].text(0.8, 0.7, "z=0.1", transform=ax[1].transAxes, fontsize=15)

ax[1].legend(loc="lower left", fontsize=10)

plt.savefig("fig8_res.pdf", bbox_inches="tight", dpi=300)