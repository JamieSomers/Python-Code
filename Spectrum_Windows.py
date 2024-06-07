# %%
import pandas as pd; # type: ignore
import numpy as np; # type: ignore
import matplotlib.pyplot as plt; # type: ignore
import matplotlib.ticker as ticker; # type: ignore
from scipy.signal import savgol_filter as savitzky_golay; # type: ignore

import numpy as np; # type: ignore
import jaraco.collections; # type: ignore
import pylab; # type: ignore

new_list = [] #Creates an empty list

# the folder the data is located in
directory = 'C:/Users/JamieSomers/Desktop/Incident Spectra 04-06-2024'

with open(f'{directory}/bg-0deg.txt','r') as f:
    bgx,bgy = [], []
    for line in f:
        line = line.strip()
        row = [float(f) for f in line.split(';')]
        bgx.append(row[0])
        bgy.append(row[1])
f.close()

with open(f'{directory}/wl-0deg.txt','r') as f:
    wlx,wly = [], []
    for line in f:
        line = line.strip()
        row = [float(f) for f in line.split(';')]
        wlx.append(row[0])
        wly.append(row[1])
f.close()

with open(f'{directory}//pink-10deg.txt','r') as f:
    tx,ty = [], []
    for line in f:
        line = line.strip()
        row = [float(f) for f in line.split(';')]
        tx.append(row[0])
        ty.append(row[1])
f.close()

ty = np.array(ty)
bgy = np.array(bgy) 
wly = np.array(wly)

transmittance = (ty - bgy) / (wly - bgy)
yhat = savitzky_golay(transmittance, 51, 5) # window size 51, polynomial order 3
# plots the data
plt.figure(figsize=(4,2.25))
plt.plot(tx, yhat)
plt.title(f'Complex Grating 10°')
plt.ylim(0, 1.1)
plt.ylabel('Transmittance')
plt.xlabel('Wavelength (nm)')
plt.xlim([400, 800])
# ax.xaxis.set_major_locator(ticker.FixedLocator([300,400, 500, 600,700,800]))
# ax.xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(200, 900, 100)))

    # saves the graphs, adjust dimensions to get clearer images/xticks are overlapping
    #plt.savefig(f'{directory}Sample {i} p0 t div ref')
plt.savefig(f'{directory}/pink-10deg.png', dpi=300)
plt.show()
# %%
