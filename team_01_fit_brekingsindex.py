# Alle libraries en packages inladen
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd

# DATA INLEZEN
df = pd.read_csv('team_01_breakingsindex_bepalen/data-22-09.csv')
i_data = df['hoek_graden']
i_rad = i_data*np.pi/180
N_data = df['aantal_franjes']
s_N = df['onzekerheid_N']

# FORMULE DEFINIEREN
def f(i, n):
    d = 2.9e-3 # d = 2.9 mm
    l = 530e-9 # lambda = 530 nm
    return 2*d/l*(np.sqrt(n**2-np.sin(i)**2)-np.cos(i)+(1-n))

# CURVE FIT
# popt, pcov = curve_fit(f, i_rad, N_data, sigma=s_N)
popt, pcov = curve_fit(f, i_rad, N_data)

# Variabelen definieren voor plot
x = np.linspace(0,.4, 100)

# Plot
plt.scatter(0,0, c='green',marker='*',label=r'$\lambda=530\cdot 10^{-9}$ m')
plt.scatter(0,0,c='black',marker='s',label=r'$d=2.9\cdot 10^{-3}$ m')
plt.scatter(0,0,marker=r'$n$',label=f'= {popt[0]:.3f}')

plt.plot(x, f(x, *popt), label='curve fit')
plt.errorbar(i_rad, N_data, s_N, fmt='o', label='data met error')

# plt.text(.3,20,s=f'$n$={popt[0]:.3f}')

plt.title(r'Curve fit over datapunten om $n$ te berekenen')
plt.xlabel(r'Hoek $\theta$ (rad)')
plt.ylabel('Franjes $\\#$ (-)')

plt.legend()

# print(popt)

plt.show()
# plt.savefig('plot-22-09-v2.png', dpi=350)