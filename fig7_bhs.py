import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps as cm
import load_obsdata as obs

# 3x2 grid of plots
fig, ax = plt.subplots(3, 2, figsize=(8, 12), sharex=True, sharey=False)
# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0, hspace=0)

ax[0,0].set_xlim(8.5, 12.5)

xlabel = r"$\log_{10} (M_* \,[M_{\odot}])$"
ax[2,0].set_xlabel(xlabel)
ax[2,1].set_xlabel(xlabel)

def shift(i):
    ndata = 3
    diffmax = 0.025
    mid = (ndata-1)/2
    return (i-mid)/mid*diffmax

# First row: black hole mass vs stellar mass --------------------------------
ax[0,0].set_ylim(3.9, 10.5)
ax[0,1].set_ylim(3.9, 10.5)
ylabel = r"$\log_{10} (M_{\rm BH} \,[M_{\odot}])$"
ax[0,0].set_ylabel(ylabel)
ax[0,1].set_yticklabels([])

# Panel 1: z = 2.2
d = np.loadtxt("mstar_mbh_relation/BH_Habouzit21.txt")
ax[0,0].plot(d[:,0], d[:,1], label="Habouzit+ 21", color="black", ms=0, ls="-")

# reset color cycle
ax[0,0].set_prop_cycle(None)

d = np.loadtxt("mstar_mbh_relation/BH_z2_Fiducial.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="Fiducial")

d = np.loadtxt("mstar_mbh_relation/BH_z2_LowCvisc.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="LowCvisc")

d = np.loadtxt("mstar_mbh_relation/BH_z2_LowCviscLowMseed.dat")
d = d[d[:,4] > 2]
ax[0,0].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="LowCviscLowMseed")

ax[0,0].text(0.8, 0.1, "z=2.2", transform=ax[0,0].transAxes, fontsize=15)

ax[0,0].text(0.85, 0.8, "A", transform=ax[0,0].transAxes, fontsize=25)

ax[0,0].legend(loc="upper left", fontsize=10)

# Panel 2: z = 0.1

d = np.loadtxt("mstar_mbh_relation/BH_Habouzit21.txt")
ax[0,1].plot(d[:,0], d[:,1], label="Habouzit+ 21", color="black", ms=0, ls="-")

d = np.loadtxt("mstar_mbh_relation/BH_McConnell_z0.txt")
ax[0,1].plot(d[:,0], d[:,1], label="McConnell & Ma 13", c="black", marker="d", ls=" ", ms=1)

d = np.loadtxt("mstar_mbh_relation/BH_EAGLE_z0.txt")
ax[0,1].plot(d[:,0], d[:,1], label="EAGLE", c="gray", ls="--", ms=0)

# reset color cycle
ax[0,1].set_prop_cycle(None)

d = np.loadtxt("mstar_mbh_relation/BH_z0_Fiducial.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z0_LowCvisc.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_mbh_relation/BH_z0_LowCviscLowMseed.dat")
d = d[d[:,4] > 2]
ax[0,1].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

ax[0,1].text(0.8, 0.1, "z=0.1", transform=ax[0,1].transAxes, fontsize=15)
ax[0,1].text(0.85, 0.8, "B", transform=ax[0,1].transAxes, fontsize=25)

ax[0,1].legend(loc="upper left", fontsize=10)


# second row: stellar mass function ----------------------------------------------
ax[1,0].set_ylim(-5.5,-0.5)
ax[1,1].set_ylim(-5.5,-0.5)
ylabel = r"$\log_{10} (dn/d\log_{10}M_* \,[{\rm cMpc}^{-3} {\rm dex}^{-1}])$"
ax[1,0].set_ylabel(ylabel)
ax[1,1].set_yticklabels([])
# Panel 3: z=2.2

d = obs.load_target_obsdata("SMF", "davidzon2017_z2.25")
ax[1,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Davidzon+ 17 (z=2.25)")

d = obs.load_target_obsdata("SMF", "mcleod2021_z2")
ax[1,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="McLeod+ 21 (z=2)")

# reset color cycle
ax[1,0].set_prop_cycle(None)

d = np.loadtxt("stellar_mass_function/SMF_z2_Fiducial.dat")
ax[1,0].plot(d[:,0], d[:,1], ms=0, label="Fiducial")

d = np.loadtxt("stellar_mass_function/SMF_z2_LowCvisc.dat")
ax[1,0].plot(d[:,0], d[:,1], ms=0, label="LowCvisc")

d = np.loadtxt("stellar_mass_function/SMF_z2_LowCviscLowMseed.dat")
ax[1,0].plot(d[:,0], d[:,1], ms=0, label="LowCviscLowMseed")

ax[1,0].text(0.8, 0.1, "z=2.2", transform=ax[1,0].transAxes, fontsize=15)
ax[1,0].text(0.85, 0.8, "C", transform=ax[1,0].transAxes, fontsize=25)

ax[1,0].legend(loc="lower left", fontsize=10)

# Panel 4: z=0

d = obs.load_target_obsdata("SMF", "baldry2012_z0")
ax[1,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Baldry+ 12 (z=0)")

d = obs.load_target_obsdata("SMF", "driver2022_z0")
ax[1,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Driver+ 22 (z=0)")

d = np.loadtxt("stellar_mass_function/SMF_EAGLE_z0.txt")
ax[1,1].plot(d[:,0], d[:,1], ms=0, label="EAGLE (Schaye +15)", c="k", ls="--")

# reset color cycle
ax[1,1].set_prop_cycle(None)

d = np.loadtxt("stellar_mass_function/SMF_z0_Fiducial.dat")
ax[1,1].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z0_LowCvisc.dat")
ax[1,1].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z0_LowCviscLowMseed.dat")
ax[1,1].plot(d[:,0], d[:,1], ms=0)


ax[1,1].text(0.8, 0.1, "z=0.1", transform=ax[1,1].transAxes, fontsize=15)
ax[1,1].text(0.85, 0.8, "D", transform=ax[1,1].transAxes, fontsize=25)

ax[1,1].legend(loc="lower left", fontsize=10)

# third row: SFR vs stellar mass ----------------------------------------------

# Panel 5: z=2.2
ax[2,0].set_ylim(-1.4, 2.6)
ax[2,1].set_ylim(-1.4, 2.6)
ylabel = r"$\log_{10} ({\rm SFR}\,[M_\odot {\rm yr}^{-1}])$"
ax[2,0].set_ylabel(ylabel)
ax[2,1].set_yticklabels([])


d = obs.load_target_obsdata("SFMS", "karim2011_z2.25")
ax[2,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Karim+ 11 (z=2.25)")

d = obs.load_target_obsdata("SFMS", "tomczak2016_z2.25")
ax[2,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Tomczak+ 16 (z=2.25)")

ax[2,0].set_prop_cycle(None)

d = np.loadtxt("mstar_sfr_relation/SFMS_z2_Fiducial.dat")
d = d[d[:,4] > 2]
ax[2,0].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z2_LowCvisc.dat")
d = d[d[:,4] > 2]
ax[2,0].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

d = np.loadtxt("mstar_sfr_relation/SFMS_z2_LowCviscLowMseed.dat")
d = d[d[:,4] > 2]
ax[2,0].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0)

ax[2,0].text(0.8, 0.1, "z=2.2", transform=ax[2,0].transAxes, fontsize=15)
ax[2,0].text(0.85, 0.8, "E", transform=ax[2,0].transAxes, fontsize=25)
ax[2,0].legend(loc="upper left", fontsize=10)

# Panel 6: z=0

d = obs.load_target_obsdata("SFMS", "karim2011_z0.3")
ax[2,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Karim+ 11 (z=0.3)")

d = obs.load_target_obsdata("SFMS", "whitaker2012_z0.25")
ax[2,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Whitaker+ 12 (z=0-0.5)")

ax[2,1].set_prop_cycle(None)

d = np.loadtxt("mstar_sfr_relation/SFMS_z0_Fiducial.dat")
d = d[d[:,4] > 2]
ax[2,1].errorbar(d[:,0]+shift(0), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="Fiducial")

d = np.loadtxt("mstar_sfr_relation/SFMS_z0_LowCvisc.dat")
d = d[d[:,4] > 2]
ax[2,1].errorbar(d[:,0]+shift(1), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="LowCvisc")

d = np.loadtxt("mstar_sfr_relation/SFMS_z0_LowCviscLowMseed.dat")
d = d[d[:,4] > 2]
ax[2,1].errorbar(d[:,0]+shift(2), d[:,1], yerr=(d[:,1]-d[:,2], d[:,3]-d[:,1]),  capsize=2, ms=0, label="LowCviscLowMseed")

ax[2,1].text(0.8, 0.1, "z=0.1", transform=ax[2,1].transAxes, fontsize=15)
ax[2,1].text(0.85, 0.8, "F", transform=ax[2,1].transAxes, fontsize=25)
ax[2,1].legend(loc="upper left", fontsize=10)

plt.savefig("fig7_bhs.pdf", bbox_inches="tight", dpi=300)