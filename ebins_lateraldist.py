"""
Created on Thu Jan 21 17:26 2021

@author: cindy

- Realiza ajuste de los datos a función de ley de potencias o NKG.
- Grafica las distribuciones laterales de electrones y muones para algunos energy bins.
  (bins 02, 13 y 24)
- Grafica la densidad para una distancia fija (r = 1000 m) en todo el rango de energías.

"""
import numpy as np
#import scikit-learn
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import plot
from files import *
from scipy.optimize import curve_fit

################################################
##### Curve fitting for electron densities #####
################################################

def powerlawfit(x,a,b):
    Es = 1e18
    return a*((10**x)/Es)**b

def nkgaugerfit(r,a,b):
    rs = 1e3
    return a*(r/rs)**(-b)*(1+r/rs)**(-b)

def densityfit(df,observable):
    # df = df.drop(np.arange(0,15),axis=0)
    ydata = df['Mean']
    if observable == "density":
        xdata = df['logEbin']
        opt,cov = curve_fit(powerlawfit,xdata,ydata)
    else:
        xdata = df['R']
        opt,cov = curve_fit(nkgaugerfit,xdata,ydata)
    return opt, cov

# Fitting lateral distributions (all energy range) (sib/epo/qgs, p/Fe, e/mu)
sibp_edistlat_opt, sibp_edistlat_cov = densityfit(sibp_edistlat_df,"edistlat")
sibFe_edistlat_opt, sibFe_edistlat_cov = densityfit(sibFe_edistlat_df,"edistlat")
epop_edistlat_opt, epop_edistlat_cov = densityfit(epop_edistlat_df,"edistlat")
epoFe_edistlat_opt, epoFe_edistlat_cov = densityfit(epoFe_edistlat_df,"edistlat")
qgsp_edistlat_opt, qgsp_edistlat_cov = densityfit(qgsp_edistlat_df,"edistlat")
qgsFe_edistlat_opt, qgsFe_edistlat_cov = densityfit(qgsFe_edistlat_df,"edistlat")

sibp_mudistlat_opt, sibp_mudistlat_cov = densityfit(sibp_mudistlat_df,"mudistlat")
sibFe_mudistlat_opt, sibFe_mudistlat_cov = densityfit(sibFe_mudistlat_df,"mudistlat")
epop_mudistlat_opt, epop_mudistlat_cov = densityfit(epop_mudistlat_df,"mudistlat")
epoFe_mudistlat_opt, epoFe_mudistlat_cov = densityfit(epoFe_mudistlat_df,"mudistlat")
qgsp_mudistlat_opt, qgsp_mudistlat_cov = densityfit(qgsp_mudistlat_df,"mudistlat")
qgsFe_mudistlat_opt, qgsFe_mudistlat_cov = densityfit(qgsFe_mudistlat_df,"mudistlat")

# Fitting lateral distributions for bin02 (sib/epo/qgs, p/Fe/mix, e/mu)
sibp02_edistlat_opt, sibp02_edistlat_cov = densityfit(sibp02_edistlat_df,"edistlat")
sibFe02_edistlat_opt, sibFe02_edistlat_cov = densityfit(sibFe02_edistlat_df,"edistlat")
sibmix02_edistlat_opt, sibmix02_edistlat_cov = densityfit(sibmix02_edistlat_df,"edistlat")
epop02_edistlat_opt, epop02_edistlat_cov = densityfit(epop02_edistlat_df,"edistlat")
epoFe02_edistlat_opt, epoFe02_edistlat_cov = densityfit(epoFe02_edistlat_df,"edistlat")
epomix02_edistlat_opt, epomix02_edistlat_cov = densityfit(epomix02_edistlat_df,"edistlat")
qgsp02_edistlat_opt, qgsp02_edistlat_cov = densityfit(qgsp02_edistlat_df,"edistlat")
qgsFe02_edistlat_opt, qgsFe02_edistlat_cov = densityfit(qgsFe02_edistlat_df,"edistlat")
qgsmix02_edistlat_opt, qgsmix02_edistlat_cov = densityfit(qgsmix02_edistlat_df,"edistlat")

sibp02_mudistlat_opt, sibp02_mudistlat_cov = densityfit(sibp02_mudistlat_df,"mudistlat")
sibFe02_mudistlat_opt, sibFe02_mudistlat_cov = densityfit(sibFe02_mudistlat_df,"mudistlat")
sibmix02_mudistlat_opt, sibmix02_mudistlat_cov = densityfit(sibmix02_mudistlat_df,"mudistlat")
epop02_mudistlat_opt, epop02_mudistlat_cov = densityfit(epop02_mudistlat_df,"mudistlat")
epoFe02_mudistlat_opt, epoFe02_mudistlat_cov = densityfit(epoFe02_mudistlat_df,"mudistlat")
epomix02_mudistlat_opt, epomix02_mudistlat_cov = densityfit(epomix02_mudistlat_df,"mudistlat")
qgsp02_mudistlat_opt, qgsp02_mudistlat_cov = densityfit(qgsp02_mudistlat_df,"mudistlat")
qgsFe02_mudistlat_opt, qgsFe02_mudistlat_cov = densityfit(qgsFe02_mudistlat_df,"mudistlat")
qgsmix02_mudistlat_opt, qgsmix02_mudistlat_cov = densityfit(qgsmix02_mudistlat_df,"mudistlat")

# Fitting lateral distributions for bin13 (sib/epo/qgs, p/Fe/mix, e/mu)
sibp13_edistlat_opt, sibp13_edistlat_cov = densityfit(sibp13_edistlat_df,"edistlat")
sibFe13_edistlat_opt, sibFe13_edistlat_cov = densityfit(sibFe13_edistlat_df,"edistlat")
sibmix13_edistlat_opt, sibmix13_edistlat_cov = densityfit(sibmix13_edistlat_df,"edistlat")
epop13_edistlat_opt, epop13_edistlat_cov = densityfit(epop13_edistlat_df,"edistlat")
epoFe13_edistlat_opt, epoFe13_edistlat_cov = densityfit(epoFe13_edistlat_df,"edistlat")
epomix13_edistlat_opt, epomix13_edistlat_cov = densityfit(epomix13_edistlat_df,"edistlat")
qgsp13_edistlat_opt, qgsp13_edistlat_cov = densityfit(qgsp13_edistlat_df,"edistlat")
qgsFe13_edistlat_opt, qgsFe13_edistlat_cov = densityfit(qgsFe13_edistlat_df,"edistlat")
qgsmix13_edistlat_opt, qgsmix13_edistlat_cov = densityfit(qgsmix13_edistlat_df,"edistlat")

sibp13_mudistlat_opt, sibp13_mudistlat_cov = densityfit(sibp13_mudistlat_df,"mudistlat")
sibFe13_mudistlat_opt, sibFe13_mudistlat_cov = densityfit(sibFe13_mudistlat_df,"mudistlat")
sibmix13_mudistlat_opt, sibmix13_mudistlat_cov = densityfit(sibmix13_mudistlat_df,"mudistlat")
epop13_mudistlat_opt, epop13_mudistlat_cov = densityfit(epop13_mudistlat_df,"mudistlat")
epoFe13_mudistlat_opt, epoFe13_mudistlat_cov = densityfit(epoFe13_mudistlat_df,"mudistlat")
epomix13_mudistlat_opt, epomix13_mudistlat_cov = densityfit(epomix13_mudistlat_df,"mudistlat")
qgsp13_mudistlat_opt, qgsp13_mudistlat_cov = densityfit(qgsp13_mudistlat_df,"mudistlat")
qgsFe13_mudistlat_opt, qgsFe13_mudistlat_cov = densityfit(qgsFe13_mudistlat_df,"mudistlat")
qgsmix13_mudistlat_opt, qgsmix13_mudistlat_cov = densityfit(qgsmix13_mudistlat_df,"mudistlat")

# Fitting lateral distributions for bin24 (sib/epo/qgs, p/Fe/mix, e/mu)
sibp24_edistlat_opt, sibp24_edistlat_cov = densityfit(sibp24_edistlat_df,"edistlat")
sibFe24_edistlat_opt, sibFe24_edistlat_cov = densityfit(sibFe24_edistlat_df,"edistlat")
sibmix24_edistlat_opt, sibmix24_edistlat_cov = densityfit(sibmix24_edistlat_df,"edistlat")
epop24_edistlat_opt, epop24_edistlat_cov = densityfit(epop24_edistlat_df,"edistlat")
epoFe24_edistlat_opt, epoFe24_edistlat_cov = densityfit(epoFe24_edistlat_df,"edistlat")
epomix24_edistlat_opt, epomix24_edistlat_cov = densityfit(epomix24_edistlat_df,"edistlat")
qgsp24_edistlat_opt, qgsp24_edistlat_cov = densityfit(qgsp24_edistlat_df,"edistlat")
qgsFe24_edistlat_opt, qgsFe24_edistlat_cov = densityfit(qgsFe24_edistlat_df,"edistlat")
qgsmix24_edistlat_opt, qgsmix24_edistlat_cov = densityfit(qgsmix24_edistlat_df,"edistlat")

sibp24_mudistlat_opt, sibp24_mudistlat_cov = densityfit(sibp24_mudistlat_df,"mudistlat")
sibFe24_mudistlat_opt, sibFe24_mudistlat_cov = densityfit(sibFe24_mudistlat_df,"mudistlat")
sibmix24_mudistlat_opt, sibmix24_mudistlat_cov = densityfit(sibmix24_mudistlat_df,"mudistlat")
epop24_mudistlat_opt, epop24_mudistlat_cov = densityfit(epop24_mudistlat_df,"mudistlat")
epoFe24_mudistlat_opt, epoFe24_mudistlat_cov = densityfit(epoFe24_mudistlat_df,"mudistlat")
epomix24_mudistlat_opt, epomix24_mudistlat_cov = densityfit(epomix24_mudistlat_df,"mudistlat")
qgsp24_mudistlat_opt, qgsp24_mudistlat_cov = densityfit(qgsp24_mudistlat_df,"mudistlat")
qgsFe24_mudistlat_opt, qgsFe24_mudistlat_cov = densityfit(qgsFe24_mudistlat_df,"mudistlat")
qgsmix24_mudistlat_opt, qgsmix24_mudistlat_cov = densityfit(qgsmix24_mudistlat_df,"mudistlat")

# Fitting particle densities at r=1000m (all energy range) (sib/epo/qgs, p/Fe/mix, e/mu)
sibp_edensity_opt, sibp_edensity_cov = densityfit(sibp_edensity_df,"density")
sibFe_edensity_opt, sibFe_edensity_cov = densityfit(sibFe_edensity_df,"density")
sibmix_edensity_opt, sibmix_edensity_cov = densityfit(sibmix_edensity_df,"density")
epop_edensity_opt, epop_edensity_cov = densityfit(epop_edensity_df,"density")
epoFe_edensity_opt, epoFe_edensity_cov = densityfit(epoFe_edensity_df,"density")
epomix_edensity_opt, epomix_edensity_cov = densityfit(epomix_edensity_df,"density")
qgsp_edensity_opt, qgsp_edensity_cov = densityfit(qgsp_edensity_df,"density")
qgsFe_edensity_opt, qgsFe_edensity_cov = densityfit(qgsFe_edensity_df,"density")
qgsmix_edensity_opt, qgsmix_edensity_cov = densityfit(qgsmix_edensity_df,"density")

sibp_mudensity_opt, sibp_mudensity_cov = densityfit(sibp_mudensity_df,"density")
sibFe_mudensity_opt, sibFe_mudensity_cov = densityfit(sibFe_mudensity_df,"density")
sibmix_mudensity_opt, sibmix_mudensity_cov = densityfit(sibmix_mudensity_df,"density")
epop_mudensity_opt, epop_mudensity_cov = densityfit(epop_mudensity_df,"density")
epoFe_mudensity_opt, epoFe_mudensity_cov = densityfit(epoFe_mudensity_df,"density")
epomix_mudensity_opt, epomix_mudensity_cov = densityfit(epomix_mudensity_df,"density")
qgsp_mudensity_opt, qgsp_mudensity_cov = densityfit(qgsp_mudensity_df,"density")
qgsFe_mudensity_opt, qgsFe_mudensity_cov = densityfit(qgsFe_mudensity_df,"density")
qgsmix_mudensity_opt, qgsmix_mudensity_cov = densityfit(qgsmix_mudensity_df,"density")

######################################################
##### Plotting simulation data and fitting curves #####
######################################################

# Electron lateral distributions for bin02 (sib/epo/qgs)
fig_sib02_edistlat, ax_sib02_edistlat = plt.subplots()
plot.plotdistlat(sibp02_edistlat_df,sibFe02_edistlat_df,sibp02_edistlat_opt,sibFe02_edistlat_opt,'e','sib',fig_sib02_edistlat,ax_sib02_edistlat,'sib_bin02')

fig_epo02_edistlat, ax_epo02_edistlat = plt.subplots()
plot.plotdistlat(epop02_edistlat_df,epoFe02_edistlat_df,epop02_edistlat_opt,epoFe02_edistlat_opt,'e','epo',fig_sib02_edistlat,ax_epo02_edistlat,'epo_bin02')

fig_qgs02_edistlat, ax_qgs02_edistlat = plt.subplots()
plot.plotdistlat(qgsp02_edistlat_df,qgsFe02_edistlat_df,qgsp02_edistlat_opt,qgsFe02_edistlat_opt,'e','qgs',fig_qgs02_edistlat,ax_qgs02_edistlat,'qgs_bin02')

# Electron lateral distributions for bin13 (sib/epo/qgs)
fig_sib13_edistlat, ax_sib13_edistlat = plt.subplots()
plot.plotdistlat(sibp13_edistlat_df,sibFe13_edistlat_df,sibp13_edistlat_opt,sibFe13_edistlat_opt,'e','sib',fig_sib13_edistlat,ax_sib13_edistlat,'sib_bin13')

fig_epo13_edistlat, ax_epo13_edistlat = plt.subplots()
plot.plotdistlat(epop13_edistlat_df,epoFe13_edistlat_df,epop13_edistlat_opt,epoFe13_edistlat_opt,'e','epo',fig_epo13_edistlat,ax_epo13_edistlat,'epo_bin13')

fig_qgs13_edistlat, ax_qgs13_edistlat = plt.subplots()
plot.plotdistlat(qgsp13_edistlat_df,qgsFe13_edistlat_df,qgsp13_edistlat_opt,qgsFe13_edistlat_opt,'e','qgs',fig_qgs13_edistlat,ax_qgs13_edistlat,'qgs_bin13')

# Electron lateral distributions for bin24 (sib/epo/qgs)
fig_sib24_edistlat, ax_sib24_edistlat = plt.subplots()
plot.plotdistlat(sibp24_edistlat_df,sibFe24_edistlat_df,sibp24_edistlat_opt,sibFe24_edistlat_opt,'e','sib',fig_sib24_edistlat,ax_sib24_edistlat,'sib_bin24')

fig_epo24_edistlat, ax_epo24_edistlat = plt.subplots()
plot.plotdistlat(epop24_edistlat_df,epoFe24_edistlat_df,epop24_edistlat_opt,epoFe24_edistlat_opt,'e','epo',fig_epo24_edistlat,ax_epo24_edistlat,'epo_bin24')

fig_qgs24_edistlat, ax_qgs24_edistlat = plt.subplots()
plot.plotdistlat(qgsp24_edistlat_df,qgsFe24_edistlat_df,qgsp24_edistlat_opt,qgsFe24_edistlat_opt,'e','qgs',fig_qgs24_edistlat,ax_qgs24_edistlat,'qgs_bin24')

# Muon lateral distributions for bin02 (sib/epo/qgs)
fig_sib02_mudistlat, ax_sib02_mudistlat = plt.subplots()
plot.plotdistlat(sibp02_mudistlat_df,sibFe02_mudistlat_df,sibp02_mudistlat_opt,sibFe02_mudistlat_opt,'mu','sib',fig_sib02_mudistlat,ax_sib02_mudistlat,'sib_bin02')

fig_epo02_mudistlat, ax_epo02_mudistlat = plt.subplots()
plot.plotdistlat(epop02_mudistlat_df,epoFe02_mudistlat_df,epop02_mudistlat_opt,epoFe02_mudistlat_opt,'mu','epo',fig_epo02_mudistlat,ax_epo02_mudistlat,'epo_bin02')

fig_qgs02_mudistlat, ax_qgs02_mudistlat = plt.subplots()
plot.plotdistlat(qgsp02_mudistlat_df,qgsFe02_mudistlat_df,qgsp02_mudistlat_opt,qgsFe02_mudistlat_opt,'mu','qgs',fig_qgs02_mudistlat,ax_qgs02_mudistlat,'qgs_bin02')

# Muon lateral distributions for bin13 (sib/epo/qgs)
fig_sib13_mudistlat, ax_sib13_mudistlat = plt.subplots()
plot.plotdistlat(sibp13_mudistlat_df,sibFe13_mudistlat_df,sibp13_mudistlat_opt,sibFe13_mudistlat_opt,'mu','sib',fig_sib13_mudistlat,ax_sib13_mudistlat,'sib_bin13')

fig_epo13_mudistlat, ax_epo13_mudistlat = plt.subplots()
plot.plotdistlat(epop13_mudistlat_df,epoFe13_mudistlat_df,epop13_mudistlat_opt,epoFe13_mudistlat_opt,'mu','epo',fig_epo13_mudistlat,ax_epo13_mudistlat,'epo_bin13')

fig_qgs13_mudistlat, ax_qgs13_mudistlat = plt.subplots()
plot.plotdistlat(qgsp13_mudistlat_df,qgsFe13_mudistlat_df,qgsp13_mudistlat_opt,qgsFe13_mudistlat_opt,'mu','qgs',fig_qgs13_mudistlat,ax_qgs13_mudistlat,'qgs_bin13')

# Muon lateral distributions for bin24 (sib/epo/qgs)
fig_sib24_mudistlat, ax_sib24_mudistlat = plt.subplots()
plot.plotdistlat(sibp24_mudistlat_df,sibFe24_mudistlat_df,sibp24_mudistlat_opt,sibFe24_mudistlat_opt,'mu','sib',fig_sib24_mudistlat,ax_sib24_mudistlat,'sib_bin24')

fig_epo24_mudistlat, ax_epo24_mudistlat = plt.subplots()
plot.plotdistlat(epop24_mudistlat_df,epoFe24_mudistlat_df,epop24_mudistlat_opt,epoFe24_mudistlat_opt,'mu','epo',fig_epo24_mudistlat,ax_epo24_mudistlat,'epo_bin24')

fig_qgs24_mudistlat, ax_qgs24_mudistlat = plt.subplots()
plot.plotdistlat(qgsp24_mudistlat_df,qgsFe24_mudistlat_df,qgsp24_mudistlat_opt,qgsFe24_mudistlat_opt,'mu','qgs',fig_qgs24_mudistlat,ax_qgs24_mudistlat,'qgs_bin24')

# Electron density ar r=1000m vs. primary energy (sib/epo/qgs)
fig_sib_edensity, ax_sib_edensity = plt.subplots()
plot.plotdensity(sibp_edensity_df,sibFe_edensity_df,sibp_edensity_opt,sibFe_edensity_opt,'e','sib',fig_sib_edensity,ax_sib_edensity,'sib')

fig_epo_edensity, ax_epo_edensity = plt.subplots()
plot.plotdensity(epop_edensity_df,epoFe_edensity_df,epop_edensity_opt,epoFe_edensity_opt,'e','epo',fig_epo_edensity,ax_epo_edensity,'epo')

fig_qgs_edensity, ax_qgs_edensity = plt.subplots()
plot.plotdensity(qgsp_edensity_df,qgsFe_edensity_df,qgsp_edensity_opt,qgsFe_edensity_opt,'e','qgs',fig_qgs_edensity,ax_qgs_edensity,'qgs')

# Muon density ar r=1000m vs. primary energy (sib/epo/qgs)
fig_sib_mudensity, ax_sib_mudensity = plt.subplots()
plot.plotdensity(sibp_mudensity_df,sibFe_mudensity_df,sibp_mudensity_opt,sibFe_mudensity_opt,'mu','sib',fig_sib_mudensity,ax_sib_mudensity,'sib')

fig_epo_mudensity, ax_epo_mudensity = plt.subplots()
plot.plotdensity(epop_mudensity_df,epoFe_mudensity_df,epop_mudensity_opt,epoFe_mudensity_opt,'mu','epo',fig_epo_mudensity,ax_epo_mudensity,'epo')

fig_qgs_mudensity, ax_qgs_mudensity = plt.subplots()
plot.plotdensity(qgsp_mudensity_df,qgsFe_mudensity_df,qgsp_mudensity_opt,qgsFe_mudensity_opt,'mu','qgs',fig_qgs_mudensity,ax_qgs_mudensity,'qgs')
