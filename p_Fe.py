#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:40:59 2020

@author: cindy

- Gráficas de X_max, \sigma X_max y distribuciones lateral.
- Chubascos producidos por protones y por hierro
- Energías: 10^{17} - 10^{20} eV
"""
import numpy as np
#import scikit-learn
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

folder = Path("/home/cindy/TEST")

obsxmax_file = str(folder/Path("datos/Xmax_Auger2019"))
obsxmax_table = pd.DataFrame(np.genfromtxt(obsxmax_file, comments='#'),
                columns=['meanLgE', 'nEvts', 'Xmax', 'meanErr', 'meanSystUp',
                'meanSystLow', 'Std dv', 'sigmaErr', 'sigmaSystUp', 'sigmaSystLow'])

############ Protones ############

## SIB ##
sibp_xmax_file = str(folder/Path("sim_sibyll/p/Xmax_SIB_p.dat"))
sibp_edistlat_file = str(folder/Path("sim_sibyll/p/p_SIB.t2205"))
sibp_mudistlat_file = str(folder/Path("sim_sibyll/p/p_SIB.t2207"))
sibp_chdistlat_file = str(folder/Path("sim_sibyll/p/p_SIB.t2291"))

sibp_xmax_table = pd.DataFrame(np.genfromtxt(sibp_xmax_file, comments='#'),
                                            columns=['Bin','logEmin','logEmax','Mean','RMS Error','Std dev',
                                                         'Min','Max'])
sibp_xmax_table.set_index('Bin')
sibp_edistlat_table = pd.DataFrame(np.genfromtxt(sibp_edistlat_file, comments='#'),
                                                columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
sibp_edistlat_table.set_index('Bin')
sibp_mudistlat_table = pd.DataFrame(np.genfromtxt(sibp_mudistlat_file, comments='#'),
                                                 columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
sibp_mudistlat_table.set_index('Bin')
sibp_chdistlat_table = pd.DataFrame(np.genfromtxt(sibp_chdistlat_file, comments='#'),
                                                 columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
sibp_chdistlat_table.set_index('Bin')

## EPO ##
epop_xmax_file = str(folder/Path("sim_epos/p/Xmax_EPO_p.dat"))
epop_edistlat_file = str(folder/Path("sim_epos/p/p_EPOS.t2205"))
epop_mudistlat_file = str(folder/Path("sim_epos/p/p_EPOS.t2207"))
epop_chdistlat_file = str(folder/Path("sim_epos/p/p_EPOS.t2291"))

epop_xmax_table = pd.DataFrame(np.genfromtxt(epop_xmax_file, comments='#'),
                                            columns=['Bin','logEmin','logEmax','Mean','RMS Error','Std dev',
                                                         'Min','Max'])
epop_xmax_table.set_index('Bin')
epop_edistlat_table = pd.DataFrame(np.genfromtxt(epop_edistlat_file, comments='#'),
                                                columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
epop_edistlat_table.set_index('Bin')
epop_mudistlat_table = pd.DataFrame(np.genfromtxt(epop_mudistlat_file, comments='#'),
                                                 columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
epop_mudistlat_table.set_index('Bin')
epop_chdistlat_table = pd.DataFrame(np.genfromtxt(epop_chdistlat_file, comments='#'),
                                                 columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
epop_chdistlat_table.set_index('Bin')


############ Hierro ############

## SIB ##
sibFe_xmax_file = str(folder/Path("sim_sibyll/Fe/Xmax_SIB_Fe.dat"))
sibFe_edistlat_file = str(folder/Path("sim_sibyll/Fe/Fe_SIB.t2205"))
sibFe_mudistlat_file = str(folder/Path("sim_sibyll/Fe/Fe_SIB.t2207"))
sibFe_chdistlat_file = str(folder/Path("sim_sibyll/Fe/Fe_SIB.t2291"))

sibFe_xmax_table = pd.DataFrame(np.genfromtxt(sibFe_xmax_file, comments='#'),
                                            columns=['Bin','logEmin','logEmax','Mean','RMS Error','Std dev',
                                                         'Min','Max'])
sibFe_edistlat_table = pd.DataFrame(np.genfromtxt(sibFe_edistlat_file, comments='#'),
                                                columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
sibFe_mudistlat_table = pd.DataFrame(np.genfromtxt(sibFe_mudistlat_file, comments='#'),
                                                 columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
sibFe_chdistlat_table = pd.DataFrame(np.genfromtxt(sibFe_chdistlat_file, comments='#'),
                                                 columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])

## EPO ##
#epoFe_xmax_file = str(folder/Path("sim_epos/p/Xmax_EPO_Fe.dat"))
epoFe_edistlat_file = str(folder/Path("sim_epos/Fe/Fe_EPOS.t2205"))
epoFe_mudistlat_file = str(folder/Path("sim_epos/Fe/Fe_EPOS.t2207"))
epoFe_chdistlat_file = str(folder/Path("sim_epos/Fe/Fe_EPOS.t2291"))

#epoFe_xmax_table = pd.DataFrame(np.genfromtxt(epoFe_xmax_file, comments='#'),
#                                            columns=['Bin','logEmin','logEmax','Mean','RMS Error','Std dev',
#                                                         'Min','Max'])
#epoFe_xmax_table.set_index('Bin')
epoFe_edistlat_table = pd.DataFrame(np.genfromtxt(epoFe_edistlat_file, comments='#'),
                                                columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
epoFe_edistlat_table.set_index('Bin')
epoFe_mudistlat_table = pd.DataFrame(np.genfromtxt(epoFe_mudistlat_file, comments='#'),
                                                 columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
epoFe_mudistlat_table.set_index('Bin')
epoFe_chdistlat_table = pd.DataFrame(np.genfromtxt(epoFe_chdistlat_file, comments='#'),
                                                 columns=['Bin','R','Mean',
                                                         'RMS Error','Std dev',
                                                         'Min','Max'])
epoFe_chdistlat_table.set_index('Bin')



#### PLOTTING #####
### SIB ###
sib_xmax_fig, sib_xmax_ax = plt.subplots()
sibp_xmax_table.plot(kind='line', x='logEmin', y='Mean', ax=sib_xmax_ax, color='green',label='p')
sibFe_xmax_table.plot(kind='line', x='logEmin', y='Mean', ax=sib_xmax_ax, color='orange',label='Fe')
obsxmax_table.plot(kind='scatter',x='meanLgE',y='Xmax', ax=sib_xmax_ax, color='black',label='Auger')
#plt.savefig(str(folder/Path('sim_sibyll/Xmax.png')), transparent=True)
plt.savefig(str(folder/Path('sim_sibyll/Xmax_SIB.png')), transparent=False)
#plt.show()

sib_xmaxdev_fig, sib_xmaxdev_ax = plt.subplots()
sibp_xmax_table.plot(kind='line', x='logEmin', y='Std dev', ax=sib_xmaxdev_ax, color='green',label='p')
sibFe_xmax_table.plot(kind='line', x='logEmin', y='Std dev', ax=sib_xmaxdev_ax, color='orange',label='Fe')
obsxmax_table.plot(kind='scatter',x='meanLgE',y='Std dv', ax=sib_xmaxdev_ax, color='black',label='Auger')
#plt.savefig(str(folder/Path('sim_sibyll/devXmax.png')), transparent=True)
plt.savefig(str(folder/Path('sim_sibyll/devXmax_SIB.png')), transparent=False)
#plt.show()

sib_mudistlat_fig, sib_mudistlat_ax = plt.subplots()

sibp_mudistlat_table.plot(kind='scatter',x='R',y='Mean',ax=sib_mudistlat_ax,color='green',label='p')
sibFe_mudistlat_table.plot(kind='scatter',x='R',y='Mean',ax=sib_mudistlat_ax,color='orange',label='Fe')
#plt.savefig(str(folder/Path('sim_sibyll/mudistlat.png')), transparent=True)
plt.savefig(str(folder/Path('sim_sibyll/mudistlat_SIB.png')), transparent=False)
#plt.show()

sib_edistlat_fig, sib_edistlat_ax = plt.subplots()

sibp_edistlat_table.plot(kind='scatter',x='R',y='Mean',ax=sib_edistlat_ax,color='green',label='p')
sibFe_edistlat_table.plot(kind='scatter',x='R',y='Mean',ax=sib_edistlat_ax,color='orange',label='Fe')
#plt.savefig(str(folder/Path('sim_sibyll/edistlat.png')), transparent=True)
plt.savefig(str(folder/Path('sim_sibyll/edistlat_SIB.png')), transparent=False)
#plt.show()

### EPOS ###
epo_xmax_fig, epo_xmax_ax = plt.subplots()
epop_xmax_table.plot(kind='line', x='logEmin', y='Mean', ax=epo_xmax_ax, color='green',label='p')
#epoFe_xmax_table.plot(kind='line', x='logEmin', y='Mean', ax=epo_xmax_ax, color='orange',label='Fe')
obsxmax_table.plot(kind='scatter',x='meanLgE',y='Xmax', ax=epo_xmax_ax, color='black',label='Auger')
#plt.savefig(str(folder/Path('sim_epoyll/Xmax.png')), transparent=True)
plt.savefig(str(folder/Path('sim_epos/Xmax_EPO.png')), transparent=False)
#plt.show()

epo_xmaxdev_fig, epo_xmaxdev_ax = plt.subplots()
epop_xmax_table.plot(kind='line', x='logEmin', y='Std dev', ax=epo_xmaxdev_ax, color='green',label='p')
#epoFe_xmax_table.plot(kind='line', x='logEmin', y='Std dev', ax=epo_xmaxdev_ax, color='orange',label='Fe')
obsxmax_table.plot(kind='scatter',x='meanLgE',y='Std dv', ax=epo_xmaxdev_ax, color='black',label='Auger')
#plt.savefig(str(folder/Path('sim_epoyll/devXmax.png')), transparent=True)
plt.savefig(str(folder/Path('sim_epos/devXmax_EPO.png')), transparent=False)
#plt.show()

epo_mudistlat_fig, epo_mudistlat_ax = plt.subplots()

epop_mudistlat_table.plot(kind='scatter',x='R',y='Mean',ax=epo_mudistlat_ax,color='green',label='p')
epoFe_mudistlat_table.plot(kind='scatter',x='R',y='Mean',ax=epo_mudistlat_ax,color='orange',label='Fe')
#plt.savefig(str(folder/Path('sim_epoyll/mudistlat.png')), transparent=True)
plt.savefig(str(folder/Path('sim_epos/mudistlat_EPO.png')), transparent=False)
#plt.show()

epo_edistlat_fig, epo_edistlat_ax = plt.subplots()

epop_edistlat_table.plot(kind='scatter',x='R',y='Mean',ax=epo_edistlat_ax,color='green',label='p')
epoFe_edistlat_table.plot(kind='scatter',x='R',y='Mean',ax=epo_edistlat_ax,color='orange',label='Fe')
#plt.savefig(str(folder/Path('sim_epoyll/edistlat.png')), transparent=True)
plt.savefig(str(folder/Path('sim_epos/edistlat_EPO.png')), transparent=False)
#plt.show()

### ALL MODELS ###
# xmax_fig, xmax_ax = plt.subplots()
# sibp_xmax_table.plot(kind='line', x='logEmin', y='Mean', ax=xmax_ax, color='green', linestyle='-',label='SIBp')
# epop_xmax_table.plot(kind='line', x='logEmin', y='Mean', ax=xmax_ax, color='green', linestyle='-.',label='EPOp')
# sibFe_xmax_table.plot(kind='line', x='logEmin', y='Mean', ax=xmax_ax, color='orange', linestyle='-',label='SIBFe')
# epoFe_xmax_table.plot(kind='line', x='logEmin', y='Mean', ax=xmax_ax, color='orange', linestyle='-.',label='EPOFe')
# #mix_obsxmax_table.plot(kind='scatter',x='meanLgE',y='Xmax', ax=xmax_ax, color='black',label='Auger')
# #plt.savefig(str(folder/Path('sim_sibyll/Xmax.png')), transparent=True)
# plt.savefig(str(folder/Path('sim_sibyll/Xmax.png')), transparent=False)
# #plt.show()
#
# xmaxdev_fig, xmaxdev_ax = plt.subplots()
# sibp_xmax_table.plot(kind='line', x='logEmin', y='Std dev', ax=xmaxdev_ax, color='green',label='SIBp')
# epop_xmax_table.plot(kind='line', x='logEmin', y='Std dev', ax=xmaxdev_ax, color='green',label='EPOp')
# sibFe_xmax_table.plot(kind='line', x='logEmin', y='Std dev', ax=xmaxdev_ax, color='orange',label='EPOFe')
# epoFe_xmax_table.plot(kind='line', x='logEmin', y='Std dev', ax=xmaxdev_ax, color='orange',label='EPOFe')
#mix_obsxmax_table.plot(kind='scatter',x='meanLgE',y='Std dv', ax=xmaxdev_ax, color='black',label='Auger')
#plt.savefig(str(folder/Path('sim_sibyll/devXmax.png')), transparent=True)
#plt.savefig(str(folder/Path('sim_sibyll/devXmax.png')), transparent=False)
# plt.show()

mudistlat_fig, mudistlat_ax = plt.subplots()
sibp_mudistlat_table.plot(kind='line',x='R',y='Mean',ax=mudistlat_ax,color='green',linestyle='-',label='SIBp')
epop_mudistlat_table.plot(kind='line',x='R',y='Mean',ax=mudistlat_ax,color='green',linestyle='-.',label='EPOp')
sibFe_mudistlat_table.plot(kind='line',x='R',y='Mean',ax=mudistlat_ax,color='orange',linestyle='-',label='SIBFe')
epoFe_mudistlat_table.plot(kind='line',x='R',y='Mean',ax=mudistlat_ax,color='orange',linestyle='-.',label='EPOFe')
#plt.savefig(str(folder/Path('sim_sibyll/mudistlat.png')), transparent=True)
plt.savefig(str(folder/Path('mudistlat.png')), transparent=False)
#plt.show()

edistlat_fig, edistlat_ax = plt.subplots()
sibp_edistlat_table.plot(kind='scatter',x='R',y='Mean',ax=edistlat_ax,color='green',label='SIBp')
epop_edistlat_table.plot(kind='scatter',x='R',y='Mean',ax=edistlat_ax,color='green',label='EPOp')
sibFe_edistlat_table.plot(kind='scatter',x='R',y='Mean',ax=edistlat_ax,color='orange',label='SIBFe')
epoFe_edistlat_table.plot(kind='scatter',x='R',y='Mean',ax=edistlat_ax,color='orange',label='EPOFe')
#plt.savefig(str(folder/Path('sim_sibyll/edistlat.png')), transparent=True)
plt.savefig(str(folder/Path('edistlat.png')), transparent=False)
#plt.show()
