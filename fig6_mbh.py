import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps as cm
import load_obsdata as obs

# 2x2 grid of plots
fig, ax = plt.subplots(2, 2, figsize=(8, 8), sharex=True, sharey=True)
# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0, hspace=0)

ax[0,0].set_xlim(8.5, 12.5)
ax[0,0].set_ylim(4.9, 11.9)

xlabel = r"$\log_{10} (M_* \,[M_{\odot}])$"
ylabel = r"$\log_{10} (M_{\rm BH} \,[M_{\odot}])$"
ax[0,0].set_ylabel(ylabel)
ax[1,0].set_ylabel(ylabel)
ax[1,0].set_xlabel(xlabel)
ax[1,1].set_xlabel(xlabel)


def shift(i):
    ndata = 6
    diffmax = 0.05
    mid = (ndata-1)/2
    return (i-mid)/mid*diffmax

# Panel 1: z = 6
d = np.loadtxt("mstar_mbh_relation/BH_Habouzit21.txt")
ax[0,0].plot(d[:,0], d[:,1], label="Habouzit+ 21", color="black", ms=0, ls="-")

# reset color cycle
ax[0,0].set_prop_cycle(None)

d = np.loadtxt("mstar_mbh_relation/BH_z6_Fiducial.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="Fiducial")

d = np.loadtxt("mstar_mbh_relation/BH_z6_SNonly.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=0, elinewidth=0, ms=4, ls=" ", label="SNonly")


d = np.loadtxt("mstar_mbh_relation/BH_z6_NoSNGalWind.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="NoSNGalWind")


d = np.loadtxt("mstar_mbh_relation/BH_z6_AGNonly.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(3), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="AGNonly")


d = np.loadtxt("mstar_mbh_relation/BH_z6_NoZdepSN.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(4), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="NoZdepSN")


d = np.loadtxt("mstar_mbh_relation/BH_z6_NoFB.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(5), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=0, elinewidth=0, ms=4, ls=" ", label="NoFB")


ax[0,0].text(0.8, 0.1, "z=6", transform=ax[0,0].transAxes, fontsize=15)

ax[0,0].legend(loc="upper left", fontsize=10)

# Panel 2: z = 2.2

d = np.loadtxt("mstar_mbh_relation/BH_Habouzit21.txt")
ax[0,1].plot(d[:,0], d[:,1], label="Habouzit+ 21", color="black", ms=0, ls="-")

# reset color cycle
ax[0,1].set_prop_cycle(None)

d = np.loadtxt("mstar_mbh_relation/BH_z2_Fiducial.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z2_SNonly.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=0, elinewidth=0, ms=4, ls=" ")

d = np.loadtxt("mstar_mbh_relation/BH_z2_NoSNGalWind.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z2_AGNonly.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(3), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z2_NoZdepSN.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(4), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z2_NoFB.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(5), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=0, elinewidth=0, ms=4, ls=" ")

ax[0,1].text(0.8, 0.1, "z=2.2", transform=ax[0,1].transAxes, fontsize=15)

ax[0,1].legend(loc="upper left", fontsize=10)

# Panel 3: z=1

d = np.loadtxt("mstar_mbh_relation/BH_Habouzit21.txt")
ax[1,0].plot(d[:,0], d[:,1], label="Habouzit+ 21", color="black", ms=0, ls="-")

# reset color cycle
ax[1,0].set_prop_cycle(None)

d = np.loadtxt("mstar_mbh_relation/BH_z1_Fiducial.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z1_SNonly.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=0, elinewidth=0, ms=4, ls=" ")

d = np.loadtxt("mstar_mbh_relation/BH_z1_NoSNGalWind.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z1_AGNonly.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(3), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z1_NoZdepSN.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(4), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z1_NoFB.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(5), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=0, elinewidth=0, ms=4, ls=" ")

ax[1,0].text(0.8, 0.1, "z=1", transform=ax[1,0].transAxes, fontsize=15)

ax[1,0].legend(loc="upper left", fontsize=10)

# Panel 4: z=0

d = np.loadtxt("mstar_mbh_relation/BH_Habouzit21.txt")
ax[1,1].plot(d[:,0], d[:,1], label="Habouzit+ 21", color="black", ms=0, ls="-")

d = np.loadtxt("mstar_mbh_relation/BH_McConnell_z0.txt")
ax[1,1].plot(d[:,0], d[:,1], label="McConnell & Ma 13", c="black", marker="d", ls=" ", ms=1)

d = np.loadtxt("mstar_mbh_relation/BH_EAGLE_z0.txt")
ax[1,1].plot(d[:,0], d[:,1], label="EAGLE", c="gray", ls="--", ms=0)

# reset color cycle
ax[1,1].set_prop_cycle(None)

d = np.loadtxt("mstar_mbh_relation/BH_z0_Fiducial.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z0_SNonly.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=0, elinewidth=0, ms=4, ls=" ")

d = np.loadtxt("mstar_mbh_relation/BH_z0_NoSNGalWind.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z0_AGNonly.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(3), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z0_NoZdepSN.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(4), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z0_NoFB.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(5), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=0, elinewidth=0, ms=4, ls=" ")

ax[1,1].text(0.8, 0.1, "z=0.1", transform=ax[1,1].transAxes, fontsize=15)

ax[1,1].legend(loc="upper left", fontsize=10)

plt.savefig("fig6_mbh.pdf", bbox_inches="tight", dpi=300)