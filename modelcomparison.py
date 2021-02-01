"""
Created on Tue Dic 08 17:10:59 2020

@author: cindy

- Comparación entre los tres modelos de interacción hadrónica:
Sibyll 2.3c, EPOS-LHC  y QGSJETII-04
- Grafica los resultados superpuestos de los tres modelos.
(- Calcula y grafica las razones entre pares de modelos.)

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import plot
from files import *

folder = Path("/home/cindy/TEST")

###### Graficas de X_max ######
fig_sibepo_Xmax, ax_sibepo_Xmax = plt.subplots() #comparar Xmax de sibyll y epos
plot.plotXmax(sibp_xmax_file, sibFe_xmax_file, 'sib', fig_sibepo_Xmax, ax_sibepo_Xmax, 'line','-')
plot.plotXmax(epop_xmax_file,epoFe_xmax_file, 'epo',fig_sibepo_Xmax, ax_sibepo_Xmax, 'line',':')
plt.savefig(str(folder/Path('data_plots/Xmax_sibepo.png')), transparent=False)

fig_sibqgs_Xmax, ax_sibqgs_Xmax = plt.subplots()
plot.plotXmax(sibp_xmax_file, sibFe_xmax_file, 'sib', fig_sibqgs_Xmax, ax_sibqgs_Xmax, 'line','-')
plot.plotXmax(qgsp_xmax_file,qgsFe_xmax_file, 'qgs',fig_sibqgs_Xmax, ax_sibqgs_Xmax, 'line','--')
plt.savefig(str(folder/Path('data_plots/Xmax_sibqgs.png')), transparent=False)

fig_qgsepo_Xmax, ax_qgsepo_Xmax = plt.subplots()
plot.plotXmax(qgsp_xmax_file, qgsFe_xmax_file, 'qgs', fig_qgsepo_Xmax, ax_qgsepo_Xmax, 'line','--')
plot.plotXmax(epop_xmax_file,epoFe_xmax_file, 'epo',fig_qgsepo_Xmax, ax_qgsepo_Xmax, 'line',':')
plt.savefig(str(folder/Path('data_plots/Xmax_qgsepo.png')), transparent=False)

fig_sibepoqgs_Xmax, ax_sibepoqgs_Xmax = plt.subplots()
plot.plotXmax(sibp_xmax_file, sibFe_xmax_file, 'sib', fig_sibepoqgs_Xmax, ax_sibepoqgs_Xmax, 'line','-')
plot.plotXmax(epop_xmax_file, epoFe_xmax_file, 'epo',fig_sibepoqgs_Xmax, ax_sibepoqgs_Xmax, 'line',':')
plot.plotXmax(qgsp_xmax_file, qgsFe_xmax_file, 'qgs', fig_sibepoqgs_Xmax,ax_sibepoqgs_Xmax,'line','--')
plt.savefig(str(folder/Path('data_plots/Xmax_sibepoqgs.png')), transparent=False)


###### Graficas de mudistlat ######
fig_sibepo_mudistlat, ax_sibepo_mudistlat = plt.subplots() #comparar mudistlat de sibyll y epos
plot.plotmudistlat(sibp_mudistlat_file, sibFe_mudistlat_file, 'sib', fig_sibepo_mudistlat, ax_sibepo_mudistlat, 'line','-')
plot.plotmudistlat(epop_mudistlat_file,epoFe_mudistlat_file, 'epo',fig_sibepo_mudistlat, ax_sibepo_mudistlat, 'line',':')
plt.savefig(str(folder/Path('data_plots/mudistlat_sibepo.png')), transparent=False)

fig_sibqgs_mudistlat, ax_sibqgs_mudistlat = plt.subplots()
plot.plotmudistlat(sibp_mudistlat_file, sibFe_mudistlat_file, 'sib', fig_sibqgs_mudistlat, ax_sibqgs_mudistlat, 'line','-')
plot.plotmudistlat(qgsp_mudistlat_file,qgsFe_mudistlat_file, 'qgs',fig_sibqgs_mudistlat, ax_sibqgs_mudistlat, 'line','--')
plt.savefig(str(folder/Path('data_plots/mudistlat_sibqgs.png')), transparent=False)

fig_qgsepo_mudistlat, ax_qgsepo_mudistlat = plt.subplots()
plot.plotmudistlat(qgsp_mudistlat_file, qgsFe_mudistlat_file, 'qgs', fig_qgsepo_mudistlat, ax_qgsepo_mudistlat, 'line','--')
plot.plotmudistlat(epop_mudistlat_file,epoFe_mudistlat_file, 'epo',fig_qgsepo_mudistlat, ax_qgsepo_mudistlat, 'line',':')
plt.savefig(str(folder/Path('data_plots/mudistlat_qgsepo.png')), transparent=False)

fig_sibepoqgs_mudistlat, ax_sibepoqgs_mudistlat = plt.subplots()
plot.plotmudistlat(sibp_mudistlat_file, sibFe_mudistlat_file, 'sib', fig_sibepoqgs_mudistlat, ax_sibepoqgs_mudistlat, 'line','-')
plot.plotmudistlat(epop_mudistlat_file, epoFe_mudistlat_file, 'epo',fig_sibepoqgs_mudistlat, ax_sibepoqgs_mudistlat, 'line',':')
plot.plotmudistlat(qgsp_mudistlat_file, qgsFe_mudistlat_file, 'qgs', fig_sibepoqgs_mudistlat,ax_sibepoqgs_mudistlat,'line','--')
plt.savefig(str(folder/Path('data_plots/mudistlat_sibepoqgs.png')), transparent=False)

###### Graficas de edistlat ######
fig_sibepo_edistlat, ax_sibepo_edistlat = plt.subplots() #comparar edistlat de sibyll y epos
plot.plotedistlat(sibp_edistlat_file, sibFe_edistlat_file, 'sib', fig_sibepo_edistlat, ax_sibepo_edistlat, 'line','-')
plot.plotedistlat(epop_edistlat_file,epoFe_edistlat_file, 'epo',fig_sibepo_edistlat, ax_sibepo_edistlat, 'line',':')
plt.savefig(str(folder/Path('data_plots/edistlat_sibepo.png')), transparent=False)

fig_sibqgs_edistlat, ax_sibqgs_edistlat = plt.subplots()
plot.plotedistlat(sibp_edistlat_file, sibFe_edistlat_file, 'sib', fig_sibqgs_edistlat, ax_sibqgs_edistlat, 'line','-')
plot.plotedistlat(qgsp_edistlat_file,qgsFe_edistlat_file, 'qgs',fig_sibqgs_edistlat, ax_sibqgs_edistlat, 'line','--')
plt.savefig(str(folder/Path('data_plots/edistlat_sibqgs.png')), transparent=False)

fig_qgsepo_edistlat, ax_qgsepo_edistlat = plt.subplots()
plot.plotedistlat(qgsp_edistlat_file, qgsFe_edistlat_file, 'qgs', fig_qgsepo_edistlat, ax_qgsepo_edistlat, 'line','--')
plot.plotedistlat(epop_edistlat_file,epoFe_edistlat_file, 'epo',fig_qgsepo_edistlat, ax_qgsepo_edistlat, 'line',':')
plt.savefig(str(folder/Path('data_plots/edistlat_qgsepo.png')), transparent=False)

fig_sibepoqgs_edistlat, ax_sibepoqgs_edistlat = plt.subplots()
plot.plotedistlat(sibp_edistlat_file, sibFe_edistlat_file, 'sib', fig_sibepoqgs_edistlat, ax_sibepoqgs_edistlat, 'line','-')
plot.plotedistlat(epop_edistlat_file, epoFe_edistlat_file, 'epo',fig_sibepoqgs_edistlat, ax_sibepoqgs_edistlat, 'line',':')
plot.plotedistlat(qgsp_edistlat_file, qgsFe_edistlat_file, 'qgs', fig_sibepoqgs_edistlat,ax_sibepoqgs_edistlat,'line','--')
plt.savefig(str(folder/Path('data_plots/edistlat_sibepoqgs.png')), transparent=False)
