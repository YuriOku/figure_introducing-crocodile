
import numpy as np
import matplotlib.pyplot as plt


# 1x2 grid of plots
fig, ax = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)
# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0, hspace=0)

BoxSize = 50
Nmesh = 1536
ax[0].set_xlim(2*np.pi/BoxSize, np.pi/BoxSize*Nmesh/4)
ax[0].set_ylim(5e-1, 7e3)
xlabel = r"$k\,[h\,{\rm cMpc}^{-1}]$"
ylabel = r"$P(k)\,[h^{-3}\,{\rm cMpc}^3]$"

ax[0].set_ylabel(ylabel)
ax[0].set_xlabel(xlabel)
ax[1].set_xlabel(xlabel)

# Panel 1: z = 2.2
d = np.loadtxt("power_spectra/Pk_nbodykit_Fiducial_z2.txt")
ax[0].plot(d[:,0], d[:,1], label="Fiducial", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoAGN_z2.txt")
ax[0].plot(d[:,0], d[:,1], label="SNonly", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoSNWind_z2.txt")
ax[0].plot(d[:,0], d[:,1], label="NoSNGalWind", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoStellar_z2.txt")
ax[0].plot(d[:,0], d[:,1], label="AGNonly", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoZdepSN_z2.txt")
ax[0].plot(d[:,0], d[:,1], label="NoZdepSN", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoFB_z2.txt")
ax[0].plot(d[:,0], d[:,1], label="NoFB", ms=0)

ax[0].text(0.7, 0.8, "z=2.2", transform=ax[0].transAxes, fontsize=15)
ax[0].set_xscale("log")
ax[0].set_yscale("log")

ax[0].legend(loc="lower left", fontsize=10)


# Panel 2: z = 0
d = np.loadtxt("power_spectra/Pk_nbodykit_Fiducial_z0.txt")
ax[1].plot(d[:,0], d[:,1], label="Fiducial", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoAGN_z0.txt")
ax[1].plot(d[:,0], d[:,1], label="SNonly", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoSNWind_z0.txt")
ax[1].plot(d[:,0], d[:,1], label="NoSNGalWind", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoStellar_z0.txt")
ax[1].plot(d[:,0], d[:,1], label="AGNonly", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoZdepSN_z0.txt")
ax[1].plot(d[:,0], d[:,1], label="NoZdepSN", ms=0)

d = np.loadtxt("power_spectra/Pk_nbodykit_NoFB_z0.txt")
ax[1].plot(d[:,0], d[:,1], label="NoFB", ms=0)

ax[1].text(0.7, 0.8, "z=0", transform=ax[1].transAxes, fontsize=15)
ax[1].set_xscale("log")
ax[1].set_yscale("log")

# ax[1].legend(loc="lower right", fontsize=10)

plt.savefig("fig11_metalPk.pdf", bbox_inches="tight", dpi=300)
plt.close()
