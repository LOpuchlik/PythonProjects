import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
tio_volume = [2.2, 2.0, 1.8, 1.6, 1.4, 1.2] # os x
data1 = [750, 780, 820, 870, 950, 1100] # lewa os y
data2 = [37, 39, 41, 52, 60, 90] # prawa oś y

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Volume of $\mathregular{Na_2S_2O_3}$ (mL)')
ax1.set_ylabel('Wavelength or NIR peak (nm)', color=color)
ax1.set_ylim(600, 1150)
ax1.set_yticks(np.arange(600, 1151, step=50))
ax1.set_xlim(1.1, 2.3, 0.1)
ax1.scatter(tio_volume, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = '#1111DB' #blue color
ax2.set_ylabel('Triangle edge length (nm)', color=color)
ax2.set_ylim(30, 110)
ax2.set_yticks(np.arange(30, 111, step=10))
ax2.scatter(tio_volume, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig('/Users/jagoodka/Desktop/figureGobin_volumetio.pdf')
plt.show()
