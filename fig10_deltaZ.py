# plot delta_dm vs metallcity

import numpy as np
import matplotlib.pyplot as plt


# 2x2 grid of plots
fig, ax = plt.subplots(2, 2, figsize=(8, 8), sharex=True, sharey=True)
# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0, hspace=0)

ax[0,0].set_xlim(-0.8, 3.8)
ax[0,0].set_ylim(-6.8, -1.5)
ylabel = r"$\log_{10} \,Z$"
xlabel1 = r"$\log_{10}\,(1 + \delta_{\rm DM})$"
xlabel2 = r"$\log_{10}\,(1 + \delta_{\rm gas})$"

ax[0,0].set_ylabel(ylabel)
ax[1,0].set_ylabel(ylabel)
ax[1,0].set_xlabel(xlabel1)
ax[1,1].set_xlabel(xlabel2)

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z2_Fiducial.txt").T
ax[0,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,0].plot(Xpoints, Ym, ms=0)#, label="Fiducial")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z2_SNonly.txt").T
ax[0,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,0].plot(Xpoints, Ym, ms=0)#, label="SNonly")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z2_NoSNGalWind.txt").T
ax[0,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,0].plot(Xpoints, Ym, ms=0)#, label="NoSNGalWind")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z2_AGNonly.txt").T
ax[0,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,0].plot(Xpoints, Ym, ms=0)#, label="AGNonly")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z2_NoZdepSN.txt").T
ax[0,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,0].plot(Xpoints, Ym, ms=0)#, label="NoZdepSN")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z2_NoFB.txt").T
ax[0,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,0].plot(Xpoints, Ym, ms=0)#, label="NoFB")

ax[0,0].text(-0.5, -2, "z = 2.2", fontsize=15)



Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z2_Fiducial.txt").T
ax[0,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,1].plot(Xpoints, Ym, ms=0)#, label="Fiducial")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z2_SNonly.txt").T
ax[0,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,1].plot(Xpoints, Ym, ms=0)#, label="SNonly")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z2_NoSNGalWind.txt").T
ax[0,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,1].plot(Xpoints, Ym, ms=0)#, label="NoSNGalWind")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z2_AGNonly.txt").T
ax[0,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,1].plot(Xpoints, Ym, ms=0)#, label="AGNonly")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z2_NoZdepSN.txt").T
ax[0,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,1].plot(Xpoints, Ym, ms=0)#, label="NoZdepSN")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z2_NoFB.txt").T
ax[0,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[0,1].plot(Xpoints, Ym, ms=0)#, label="NoFB")

ax[0,1].text(-0.5, -2, "z = 2.2", fontsize=15)

# best fit line from Schaye et al. (2003). carbon metallicity [C/H]
def DeltaZSchaye(z, logdelta):
    return -3.47 + 0.08 * (z-3) + 0.65 * (logdelta - 0.5)

logd = np.linspace(-0.5, 2, 100)
logd1 = np.log10(1 + 10**logd)
logZ = DeltaZSchaye(2.2, logd) + np.log10(0.0134)
ax[0,1].plot(logd1, logZ, label="Schaye+03", linestyle="--", color="black", ms=0)

ax[0,1].legend(loc="lower right", fontsize=10)


Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z0_Fiducial.txt").T
ax[1,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,0].plot(Xpoints, Ym, ms=0)#, label="Fiducial")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z0_SNonly.txt").T
ax[1,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,0].plot(Xpoints, Ym, ms=0)#, label="SNonly")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z0_NoSNGalWind.txt").T
ax[1,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,0].plot(Xpoints, Ym, ms=0)#, label="NoSNGalWind")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z0_AGNonly.txt").T
ax[1,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,0].plot(Xpoints, Ym, ms=0)#, label="AGNonly")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z0_NoZdepSN.txt").T
ax[1,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,0].plot(Xpoints, Ym, ms=0)#, label="NoZdepSN")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaDMZ_z0_NoFB.txt").T
ax[1,0].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,0].plot(Xpoints, Ym, ms=0)#, label="NoFB")

ax[1,0].text(-0.5, -2, "z = 0", fontsize=15)


Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z0_Fiducial.txt").T
ax[1,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,1].plot(Xpoints, Ym, ms=0, label="Fiducial")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z0_SNonly.txt").T
ax[1,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,1].plot(Xpoints, Ym, ms=0, label="SNonly")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z0_NoSNGalWind.txt").T
ax[1,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,1].plot(Xpoints, Ym, ms=0, label="NoSNGalWind")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z0_AGNonly.txt").T
ax[1,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,1].plot(Xpoints, Ym, ms=0, label="AGNonly")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z0_NoZdepSN.txt").T
ax[1,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,1].plot(Xpoints, Ym, ms=0, label="NoZdepSN")

Xpoints, Ym, Y16, Y84 = np.loadtxt("overdensity_metallicity/DeltaGasZ_z0_NoFB.txt").T
ax[1,1].fill_between(Xpoints, Y16, Y84, alpha=0.15)
ax[1,1].plot(Xpoints, Ym, ms=0, label="NoFB")

ax[1,1].text(-0.5, -2, "z = 0", fontsize=15)
ax[1,1].legend(loc="lower right", fontsize=10)


# plt.legend(bbox_to_anchor=(0.95, 0.05), loc='lower right')
plt.savefig("fig10_deltaZ.pdf", bbox_inches="tight", dpi=300)
plt.close()
