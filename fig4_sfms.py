import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps as cm
import load_obsdata as obs

# 2x2 grid of plots
fig, ax = plt.subplots(2, 2, figsize=(8, 8), sharex=True, sharey=True)
# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0, hspace=0)

ax[0,0].set_xlim(8.5, 12.5)
ax[0,0].set_ylim(-1.4, 2.6)

xlabel = r"$\log_{10} (M_* \,[M_{\odot}])$"
ylabel = r"$\log_{10} (\mathrm{SFR} \,[M_{\odot} {\rm yr}^{-1}])$"
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
d = obs.load_target_obsdata("SFMS", "salmon2015_z6")
ax[0,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Salmon+ 15 (z=6)")

d = obs.load_target_obsdata("SFMS", "nakajima2023_z7")
ax[0,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Nakajima+ 23 (z=4-10)")

ax[0,0].set_prop_cycle(None)

d = np.loadtxt("mstar_sfr_relation/SFMS_z6_Fiducial.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="Fiducial")

d = np.loadtxt("mstar_sfr_relation/SFMS_z6_SNonly.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="SNonly")

d = np.loadtxt("mstar_sfr_relation/SFMS_z6_NoSNGalWind.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="NoSNGalWind")


d = np.loadtxt("mstar_sfr_relation/SFMS_z6_AGNonly.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(3), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="AGNonly")


d = np.loadtxt("mstar_sfr_relation/SFMS_z6_NoZdepSN.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(4), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="NoZdepSN")


d = np.loadtxt("mstar_sfr_relation/SFMS_z6_NoFB.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(5), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="NoFB")


ax[0,0].text(0.1, 0.9, "z=6", transform=ax[0,0].transAxes, fontsize=15)

ax[0,0].legend(loc="lower right", fontsize=10)

# Panel 2: z = 2.2

d = obs.load_target_obsdata("SFMS", "karim2011_z2.25")
ax[0,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Karim+ 11 (z=2.25)")

d = obs.load_target_obsdata("SFMS", "tomczak2016_z2.25")
ax[0,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Tomczak+ 16 (z=2.25)")

ax[0,1].set_prop_cycle(None)

d = np.loadtxt("mstar_sfr_relation/SFMS_z2_Fiducial.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z2_SNonly.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z2_NoSNGalWind.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z2_AGNonly.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(3), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z2_NoZdepSN.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(4), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z2_NoFB.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(5), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

ax[0,1].text(0.1, 0.9, "z=2.2", transform=ax[0,1].transAxes, fontsize=15)

ax[0,1].legend(loc="lower right", fontsize=10)

# Panel 3: z=1

d = obs.load_target_obsdata("SFMS", "karim2011_z0.9")
ax[1,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Karim+ 11 (z=0.9)")

d = obs.load_target_obsdata("SFMS", "karim2011_z1.1")
ax[1,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Karim+ 11 (z=1.1)")

d = obs.load_target_obsdata("SFMS", "tomczak2016_z0.875")
ax[1,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Tomczak+ 16 (z=0.875)")

d = obs.load_target_obsdata("SFMS", "tomczak2016_z1.125")
ax[1,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Tomczak+ 16 (z=1.125)")

ax[1,0].set_prop_cycle(None)

d = np.loadtxt("mstar_sfr_relation/SFMS_z1_Fiducial.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z1_SNonly.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z1_NoSNGalWind.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z1_AGNonly.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(3), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z1_NoZdepSN.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(4), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z1_NoFB.dat")
d = d[d[:,4] > 2]
ax[1,0].errorbar(d[:,0]+shift(5), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

ax[1,0].text(0.1, 0.9, "z=1", transform=ax[1,0].transAxes, fontsize=15)

ax[1,0].legend(loc="lower right", fontsize=10)

# Panel 4: z=0

d = obs.load_target_obsdata("SFMS", "karim2011_z0.3")
ax[1,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Karim+ 11 (z=0.3)")

d = obs.load_target_obsdata("SFMS", "whitaker2012_z0.25")
ax[1,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Whitaker+ 12 (z=0-0.5)")

ax[1,1].set_prop_cycle(None)

d = np.loadtxt("mstar_sfr_relation/SFMS_z0_Fiducial.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z0_SNonly.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z0_NoSNGalWind.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z0_AGNonly.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(3), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z0_NoZdepSN.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(4), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z0_NoFB.dat")
d = d[d[:,4] > 2]
ax[1,1].errorbar(d[:,0]+shift(5), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

ax[1,1].text(0.1, 0.9, "z=0.1", transform=ax[1,1].transAxes, fontsize=15)

ax[1,1].legend(loc="lower right", fontsize=10)

plt.savefig("fig4_sfms.pdf", bbox_inches="tight", dpi=300)