"""
Created on Tue Dic 02 16:44:40 2020

@author: cindy

- Grafica resultados individuales de cada modelo para todo el rango de energías.
(Xmax, edistlat y mudistlat)

- Grafica densidad de partículas a r=1000 m para cada modelo.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import plot
from files import *

folder = Path("/home/cindy/TEST")
## Sibyll2.3c ##
fig_sib_xmax, ax_sib_xmax = plt.subplots()
plot.plotXmax(sibp_xmax_file,sibFe_xmax_file,'sib',fig_sib_xmax,ax_sib_xmax,'line','-','SIB')
fig_sib_mudistlat, ax_sib_mudistlat = plt.subplots()
plot.plotmudistlat(sibp_mudistlat_file,sibFe_mudistlat_file,'sib',fig_sib_mudistlat,ax_sib_mudistlat,'scatter','SIB')
fig_sib_edistlat, ax_sib_edistlat = plt.subplots()
plot.plotedistlat(sibp_edistlat_file,sibFe_edistlat_file,'sib',fig_sib_edistlat,ax_sib_edistlat,'scatter','SIB')
fig_sib_mudensity, ax_sib_mudensity = plt.subplots()
plot.plotmudensity(sibp_mudensity_file,sibFe_mudensity_file,'sib',fig_sib_mudensity,ax_sib_mudensity,'scatter','SIB')
fig_sib_edensity, ax_sib_edensity = plt.subplots()
plot.plotedensity(sibp_edensity_file,sibFe_edensity_file,'sib',fig_sib_edensity,ax_sib_edensity,'scatter','SIB')

## EPOS-LHC ##
fig_epo_xmax, ax_epo_xmax = plt.subplots()
plot.plotXmax(epop_xmax_file,epoFe_xmax_file,'epo',fig_epo_xmax,ax_epo_xmax,'line','-','EPO')
fig_epo_mudistlat, ax_epo_mudistlat = plt.subplots()
plot.plotmudistlat(epop_mudistlat_file,epoFe_mudistlat_file,'epo',fig_epo_mudistlat,ax_epo_mudistlat,'scatter','EPO')
fig_epo_edistlat, ax_epo_edistlat = plt.subplots()
plot.plotedistlat(epop_edistlat_file,epoFe_edistlat_file,'epo',fig_epo_edistlat,ax_epo_edistlat,'scatter','EPO')
fig_epo_mudensity, ax_epo_mudensity = plt.subplots()
plot.plotmudensity(epop_mudensity_file,epoFe_mudensity_file,'epo',fig_epo_mudensity,ax_epo_mudensity,'scatter','EPO')
fig_epo_edensity, ax_epo_edensity = plt.subplots()
plot.plotedensity(epop_edensity_file,epoFe_edensity_file,'epo',fig_epo_edensity,ax_epo_edensity,'scatter','EPO')

## QGSJETII-04 ##
fig_qgs_xmax, ax_qgs_xmax = plt.subplots()
plot.plotXmax(qgsp_xmax_file,qgsFe_xmax_file,'qgs',fig_qgs_xmax,ax_qgs_xmax,'line','-','QGS')
fig_qgs_mudistlat, ax_qgs_mudistlat = plt.subplots()
plot.plotmudistlat(qgsp_mudistlat_file,qgsFe_mudistlat_file,'qgs',fig_qgs_mudistlat,ax_qgs_mudistlat,'scatter','QGS')
fig_qgs_edistlat, ax_qgs_edistlat = plt.subplots()
plot.plotedistlat(qgsp_edistlat_file,qgsFe_edistlat_file,'qgs',fig_qgs_edistlat,ax_qgs_edistlat,'scatter','QGS')
fig_qgs_mudensity, ax_qgs_mudensity = plt.subplots()
plot.plotmudensity(qgsp_mudensity_file,qgsFe_mudensity_file,'qgs',fig_qgs_mudensity,ax_qgs_mudensity,'scatter','QGS')
fig_qgs_edensity, ax_qgs_edensity = plt.subplots()
plot.plotedensity(qgsp_edensity_file,qgsFe_edensity_file,'qgs',fig_qgs_edensity,ax_qgs_edensity,'scatter','QGS')
