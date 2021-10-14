import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
from scipy import constants

def wrap2pmpi(phasedata):
    """It wraps phase from -pi, pi"""
    return (phasedata + np.pi) % (2*np.pi) -np.pi

path = r'E:\Attolab\Raw data VMI DyR in SE1\20200213_matrices\Scans c--\Tests with lock 2w\\'

VMI_spontaneous_lock = np.loadtxt(path + '20200213_He_RABBIT_c00_P0_std_lock239')
VMI_imposed_lock = np.loadtxt(path + '20200213_He_RABBIT_c00_P0_std_lock243')
TOF = np.loadtxt(path + '20200213_He_RABBIT_TOF_c00_P0_std_lock243')
energy_VMI = [(VMI_spontaneous_lock[k,0]+VMI_spontaneous_lock[k,1])/2 for k in range(0,4)]
energy_TOF = [(TOF[k,0]+TOF[k,1])/2 for k in range(0,4)]

plt.figure()
plt.errorbar(energy_VMI,VMI_spontaneous_lock[:,3] - VMI_spontaneous_lock[0,3], yerr = VMI_spontaneous_lock[:,4], label='VMI self locked at 239' )
plt.errorbar(energy_VMI,VMI_imposed_lock[:,3] - VMI_imposed_lock[0,3] , yerr = VMI_imposed_lock[:,4], label='VMI with TOF lock at 243' )
plt.errorbar(energy_TOF,TOF[:,3] - TOF[0,3] , yerr = TOF[:,4], label='TOF lock at 243' )
plt.xlabel('Energy [eV]')
plt.ylabel('Phase [rad]')
plt.title('comparison of extracted phases 13-02-20 scan c00')
plt.legend()

VMI_spontaneous_lock_Rainbow = np.loadtxt(path + '20200213_He_RABBIT_c00_P0_Rainbow_lock239')
VMI_imposed_lock_Rainbow = np.loadtxt(path + '20200213_He_RABBIT_c00_P0_Rainbow_lock243')
TOF_Rainbow = np.loadtxt(path + '20200213_He_RABBIT_TOF_c00_P0_Rainbow_lock243')

energy_VMI_Rainbow = VMI_spontaneous_lock_Rainbow[:,0]
energy_TOF_Rainbow = TOF_Rainbow[:,0]


fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,4))
ax1.set_ylabel("2w Amplitude [arb. u.]")
ax1.set_xlabel("Photon Energy [eV]")
ax2.set_ylabel("2w Phase [rad]")
ax2.set_xlabel("Photon Energy [eV]")
ax1.plot(energy_VMI_Rainbow,VMI_spontaneous_lock_Rainbow[:,1],label='2w amplitude self lock 239' )
ax2.plot(energy_VMI_Rainbow,wrap2pmpi(VMI_spontaneous_lock_Rainbow[:,2]))

ax1.plot(energy_VMI_Rainbow,VMI_imposed_lock_Rainbow[:,1],label='2w amplitude lock imposed 243' )
ax2.plot(energy_VMI_Rainbow,wrap2pmpi(VMI_imposed_lock_Rainbow[:,2]))

ax1.plot(energy_TOF_Rainbow,TOF_Rainbow[:,1]*10e16,label='2w amplitude TOF lock at 243' )
ax2.plot(energy_TOF_Rainbow,wrap2pmpi(TOF_Rainbow[:,2]))

ax1.legend()
plt.title("2w amplitude and phases of scan 20200213 c00")
fig.tight_layout()




