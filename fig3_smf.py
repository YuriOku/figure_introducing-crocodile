import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps as cm
import load_obsdata as obs

# 2x2 grid of plots
fig, ax = plt.subplots(2, 2, figsize=(8, 8), sharex=True, sharey=True)
# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0, hspace=0)

ax[0,0].set_xlim(8.5, 12.5)
ax[0,0].set_ylim(-5.4, -0.6)

xlabel = r"$\log_{10} (M_* \,[M_{\odot}])$"
ylabel = r"$\log_{10} (dn/d\log_{10}M_* \,[{\rm cMpc}^{-3} {\rm dex}^{-1}])$"
ax[0,0].set_ylabel(ylabel)
ax[1,0].set_ylabel(ylabel)
ax[1,0].set_xlabel(xlabel)
ax[1,1].set_xlabel(xlabel)


# Panel 1: z = 6
d = obs.load_target_obsdata("SMF", "song2016_z6")
ax[0,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Song+ 16 (z=6)")

d = obs.load_target_obsdata("SMF", "stefanon2017_z6")
ax[0,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Stefanon+ 17 (z=6)")

d = obs.load_target_obsdata("SMF", "stefanon2021_z6")
ax[0,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Stefanon+ 21 (z=6)")

ax[0,0].set_prop_cycle(None)

d = np.loadtxt("stellar_mass_function/SMF_z6_Fiducial.dat")
ax[0,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z6_SNonly.dat")
ax[0,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z6_NoSNGalWind.dat")
ax[0,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z6_AGNonly.dat")
ax[0,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z6_NoZdepSN.dat")
ax[0,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z6_NoFB.dat")
ax[0,0].plot(d[:,0], d[:,1], ms=0)

ax[0,0].text(0.8, 0.7, "z=6", transform=ax[0,0].transAxes, fontsize=15)

ax[0,0].legend(loc="upper right", fontsize=10)

# Panel 2: z = 2.2

d = obs.load_target_obsdata("SMF", "davidzon2017_z2.25")
ax[0,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Davidzon+ 17 (z=2.25)")

d = obs.load_target_obsdata("SMF", "mcleod2021_z2")
ax[0,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="McLeod+ 21 (z=2)")

ax[0,1].set_prop_cycle(None)

d = np.loadtxt("stellar_mass_function/SMF_z2_Fiducial.dat")
ax[0,1].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z2_SNonly.dat")
ax[0,1].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z2_NoSNGalWind.dat")
ax[0,1].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z2_AGNonly.dat")
ax[0,1].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z2_NoZdepSN.dat")
ax[0,1].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z2_NoFB.dat")
ax[0,1].plot(d[:,0], d[:,1], ms=0)

ax[0,1].text(0.8, 0.7, "z=2.2", transform=ax[0,1].transAxes, fontsize=15)

ax[0,1].legend(loc="upper right", fontsize=10)

# Panel 3: z=1

d = obs.load_target_obsdata("SMF", "davidzon2017_z1.05")
ax[1,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Davidzon+ 17 (z=1.05)")

d = obs.load_target_obsdata("SMF", "mcleod2021_z1")
ax[1,0].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="McLeod+ 21 (z=1)")

ax[1,0].set_prop_cycle(None)

d = np.loadtxt("stellar_mass_function/SMF_z1_Fiducial.dat")
ax[1,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z1_SNonly.dat")
ax[1,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z1_NoSNGalWind.dat")
ax[1,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z1_AGNonly.dat")
ax[1,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z1_NoZdepSN.dat")
ax[1,0].plot(d[:,0], d[:,1], ms=0)

d = np.loadtxt("stellar_mass_function/SMF_z1_NoFB.dat")
ax[1,0].plot(d[:,0], d[:,1], ms=0)

ax[1,0].text(0.8, 0.7, "z=1", transform=ax[1,0].transAxes, fontsize=15)

ax[1,0].legend(loc="upper right", fontsize=10)

# Panel 4: z=0

d = obs.load_target_obsdata("SMF", "baldry2012_z0")
ax[1,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Baldry+ 12 (z=0)")

d = obs.load_target_obsdata("SMF", "driver2022_z0")
ax[1,1].fill_between(d["x"], d["y1"], d["y2"], lw=0, alpha=0.2, label="Driver+ 22 (z=0)")

d = np.loadtxt("stellar_mass_function/SMF_EAGLE_z0.txt")
ax[1,1].plot(d[:,0], d[:,1], ms=0, label="EAGLE (Schaye +15)", c="k", ls="--")

ax[1,1].set_prop_cycle(None)

d = np.loadtxt("stellar_mass_function/SMF_z0_Fiducial.dat")
ax[1,1].plot(d[:,0], d[:,1], ms=0, label="Fiducial")

d = np.loadtxt("stellar_mass_function/SMF_z0_SNonly.dat")
ax[1,1].plot(d[:,0], d[:,1], ms=0, label="SNonly")

d = np.loadtxt("stellar_mass_function/SMF_z0_NoSNGalWind.dat")
ax[1,1].plot(d[:,0], d[:,1], ms=0, label="NoSNGalWind")

d = np.loadtxt("stellar_mass_function/SMF_z0_AGNonly.dat")
ax[1,1].plot(d[:,0], d[:,1], ms=0, label="AGNonly")

d = np.loadtxt("stellar_mass_function/SMF_z0_NoZdepSN.dat")
ax[1,1].plot(d[:,0], d[:,1], ms=0, label="NoZdepSN")

d = np.loadtxt("stellar_mass_function/SMF_z0_NoFB.dat")
ax[1,1].plot(d[:,0], d[:,1], ms=0, label="NoFB")

ax[1,1].text(0.8, 0.7, "z=0.1", transform=ax[1,1].transAxes, fontsize=15)

ax[1,1].legend(loc="lower left", fontsize=10)

plt.savefig("fig3_smf.pdf", bbox_inches="tight", dpi=300)