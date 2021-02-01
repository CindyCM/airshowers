"""
Created on Thu Jan 21 17:26 2021

@author: cindy

Modulo que lee todos los archivos de texto con los datos y crea los respectivos DataFrames.

"""
import numpy as np
import pandas as pd
from pathlib import Path

folder = Path("/home/cindy/TEST")

def tablas(file,observable): # function to create dataframe from file
    if observable == "Xmax":
        table = pd.DataFrame(np.genfromtxt(file, comments='#'), columns=['Bin','logEmin','logEmax','Mean','RMS Error','Std dev','Min','Max'])
        table.set_index('Bin')
        table['logEbin'] = (table['logEmax'] + table['logEmin'])/2
    elif observable == "density":
        table = pd.DataFrame(np.genfromtxt(file, comments='#'), columns=['Bin','logEmin','logEmax','R','Mean','RMS Error','Std dev','Min','Max'])
        table.set_index('Bin')
        table['logEbin'] = (table['logEmax'] + table['logEmin'])/2
    else:
        table = pd.DataFrame(np.genfromtxt(file, comments='#'),columns=['Bin','R','Mean','RMS Error','Std dev','Min','Max'])
        table.set_index('Bin')
    return table

#########################
####### Xmax data #######
#########################
# Sibyll p/Fe
sibp_xmax_file = str(folder/Path("sim_sibyll/p/Xmax_SIB_p.dat"))
sibFe_xmax_file = str(folder/Path("sim_sibyll/Fe/Xmax_SIB_Fe.dat"))
sibp_xmax_df = tablas(sibp_xmax_file,"Xmax")
sibFe_xmax_df = tablas(sibFe_xmax_file,"Xmax")
# EPOS p/Fe
epop_xmax_file = str(folder/Path("sim_epos/p/Xmax_EPO_p.dat"))
epoFe_xmax_file = str(folder/Path("sim_epos/Fe/Xmax_EPO_Fe.dat"))
epop_xmax_df = tablas(epop_xmax_file,"Xmax")
epoFe_xmax_df = tablas(epoFe_xmax_file,"Xmax")
# QGSJETII p/Fe
qgsp_xmax_file = str(folder/Path("sim_qgsjet/p/Xmax_QGS_p.dat"))
qgsFe_xmax_file = str(folder/Path("sim_qgsjet/Fe/Xmax_QGS_Fe.dat"))
qgsp_xmax_df = tablas(qgsp_xmax_file,"Xmax")
qgsFe_xmax_df = tablas(qgsFe_xmax_file,"Xmax")

######################################################################
####### Lateral distributions data for the entire energy range #######
######################################################################
# Sibyll p/Fe e/mu/ch
sibp_edistlat_file = str(folder/Path("sim_sibyll/p/p_SIB.t2205"))
sibp_mudistlat_file = str(folder/Path("sim_sibyll/p/p_SIB.t2207"))
sibp_chdistlat_file = str(folder/Path("sim_sibyll/p/p_SIB.t2291"))
sibFe_edistlat_file = str(folder/Path("sim_sibyll/Fe/Fe_SIB.t2205"))
sibFe_mudistlat_file = str(folder/Path("sim_sibyll/Fe/Fe_SIB.t2207"))
sibFe_chdistlat_file = str(folder/Path("sim_sibyll/Fe/Fe_SIB.t2291"))
sibp_edistlat_df = tablas(sibp_edistlat_file,"edistlat")
sibFe_edistlat_df = tablas(sibFe_edistlat_file,"edistlat")
sibp_mudistlat_df = tablas(sibp_mudistlat_file,"mudistlat")
sibFe_mudistlat_df = tablas(sibFe_mudistlat_file,"mudistlat")
# EPOS p/Fe e/mu/ch
epop_edistlat_file = str(folder/Path("sim_epos/p/p_EPOS.t2205"))
epop_mudistlat_file = str(folder/Path("sim_epos/p/p_EPOS.t2207"))
epop_chdistlat_file = str(folder/Path("sim_epos/p/p_EPOS.t2291"))
epoFe_edistlat_file = str(folder/Path("sim_epos/Fe/Fe_EPOS.t2205"))
epoFe_mudistlat_file = str(folder/Path("sim_epos/Fe/Fe_EPOS.t2207"))
epoFe_chdistlat_file = str(folder/Path("sim_epos/Fe/Fe_EPOS.t2291"))
epop_edistlat_df = tablas(epop_edistlat_file,"edistlat")
epoFe_edistlat_df = tablas(epoFe_edistlat_file,"edistlat")
epop_mudistlat_df = tablas(epop_mudistlat_file,"mudistlat")
epoFe_mudistlat_df = tablas(epoFe_mudistlat_file,"mudistlat")
# QGSJETII p/Fe e/mu/ch
qgsp_edistlat_file = str(folder/Path("sim_qgsjet/p/p_QGS.t2205"))
qgsp_mudistlat_file = str(folder/Path("sim_qgsjet/p/p_QGS.t2207"))
qgsp_chdistlat_file = str(folder/Path("sim_qgsjet/p/p_QGS.t2291"))
qgsFe_edistlat_file = str(folder/Path("sim_qgsjet/Fe/Fe_QGS.t2205"))
qgsFe_mudistlat_file = str(folder/Path("sim_qgsjet/Fe/Fe_QGS.t2207"))
qgsFe_chdistlat_file = str(folder/Path("sim_qgsjet/Fe/Fe_QGS.t2291"))
qgsp_edistlat_df = tablas(qgsp_edistlat_file,"edistlat")
qgsFe_edistlat_df = tablas(qgsFe_edistlat_file,"edistlat")
qgsp_mudistlat_df = tablas(qgsp_mudistlat_file,"mudistlat")
qgsFe_mudistlat_df = tablas(qgsFe_mudistlat_file,"mudistlat")


##################################################################
####### Lateral distributions data for certain energy bins #######
##################################################################
## BIN 02 ##
# Sibyll p/Fe/mix e/mu
sibp02_edistlat_file = str(folder/Path("sim_sibyll/p/ebin/p_SIB_bin02.t2205"))
sibp02_mudistlat_file = str(folder/Path("sim_sibyll/p/ebin/p_SIB_bin02.t2207"))
sibFe02_edistlat_file = str(folder/Path("sim_sibyll/Fe/ebin/Fe_SIB_bin02.t2205"))
sibFe02_mudistlat_file = str(folder/Path("sim_sibyll/Fe/ebin/Fe_SIB_bin02.t2207"))
sibmix02_edistlat_file = str(folder/Path("sim_sibyll/E2/SimE2.t2205"))
sibmix02_mudistlat_file = str(folder/Path("sim_sibyll/E2/SimE2.t2207"))
sibp02_edistlat_df = tablas(sibp02_edistlat_file,"edistlat")
sibp02_mudistlat_df = tablas(sibp02_mudistlat_file,"mudistlat")
sibFe02_edistlat_df = tablas(sibFe02_edistlat_file,"edistlat")
sibFe02_mudistlat_df = tablas(sibFe02_mudistlat_file,"mudistlat")
sibmix02_edistlat_df = tablas(sibmix02_edistlat_file,"edistlat")
sibmix02_mudistlat_df = tablas(sibmix02_mudistlat_file,"mudistlat")
# EPOS p/Fe/mix e/mu
epop02_edistlat_file = str(folder/Path("sim_epos/p/ebin/p_EPO_bin02.t2205"))
epop02_mudistlat_file = str(folder/Path("sim_epos/p/ebin/p_EPO_bin02.t2207"))
epoFe02_edistlat_file = str(folder/Path("sim_epos/Fe/ebin/Fe_EPO_bin02.t2205"))
epoFe02_mudistlat_file = str(folder/Path("sim_epos/Fe/ebin/Fe_EPO_bin02.t2207"))
epomix02_edistlat_file = str(folder/Path("sim_epos/E2/SimE2EPOS.t2205"))
epomix02_mudistlat_file = str(folder/Path("sim_epos/E2/SimE2EPOS.t2207"))
epop02_edistlat_df = tablas(epop02_edistlat_file,"edistlat")
epop02_mudistlat_df = tablas(epop02_mudistlat_file,"mudistlat")
epoFe02_edistlat_df = tablas(epoFe02_edistlat_file,"edistlat")
epoFe02_mudistlat_df = tablas(epoFe02_mudistlat_file,"mudistlat")
epomix02_edistlat_df = tablas(epomix02_edistlat_file,"edistlat")
epomix02_mudistlat_df = tablas(epomix02_mudistlat_file,"mudistlat")
# QGSJETII p/Fe/mix e/mu
qgsp02_edistlat_file = str(folder/Path("sim_qgsjet/p/ebin/p_QGS_bin02.t2205"))
qgsp02_mudistlat_file = str(folder/Path("sim_qgsjet/p/ebin/p_QGS_bin02.t2207"))
qgsFe02_edistlat_file = str(folder/Path("sim_qgsjet/Fe/ebin/Fe_QGS_bin02.t2205"))
qgsFe02_mudistlat_file = str(folder/Path("sim_qgsjet/Fe/ebin/Fe_QGS_bin02.t2207"))
qgsmix02_edistlat_file = str(folder/Path("sim_qgsjet/E2/SimE2QGS.t2205"))
qgsmix02_mudistlat_file = str(folder/Path("sim_qgsjet/E2/SimE2QGS.t2207"))
qgsp02_edistlat_df = tablas(qgsp02_edistlat_file,"edistlat")
qgsp02_mudistlat_df = tablas(qgsp02_mudistlat_file,"mudistlat")
qgsFe02_edistlat_df = tablas(qgsFe02_edistlat_file,"edistlat")
qgsFe02_mudistlat_df = tablas(qgsFe02_mudistlat_file,"mudistlat")
qgsmix02_edistlat_df = tablas(qgsmix02_edistlat_file,"edistlat")
qgsmix02_mudistlat_df = tablas(qgsmix02_mudistlat_file,"mudistlat")

## BIN 13 ##
# Sibyll p/Fe/mix e/mu
sibp13_edistlat_file = str(folder/Path("sim_sibyll/p/ebin/p_SIB_bin13.t2205"))
sibp13_mudistlat_file = str(folder/Path("sim_sibyll/p/ebin/p_SIB_bin13.t2207"))
sibFe13_edistlat_file = str(folder/Path("sim_sibyll/Fe/ebin/Fe_SIB_bin13.t2205"))
sibFe13_mudistlat_file = str(folder/Path("sim_sibyll/Fe/ebin/Fe_SIB_bin13.t2207"))
sibmix13_edistlat_file = str(folder/Path("sim_sibyll/E2/SimE2.t2205"))
sibmix13_mudistlat_file = str(folder/Path("sim_sibyll/E2/SimE2.t2207"))
sibp13_edistlat_df = tablas(sibp13_edistlat_file,"edistlat")
sibp13_mudistlat_df = tablas(sibp13_mudistlat_file,"mudistlat")
sibFe13_edistlat_df = tablas(sibFe13_edistlat_file,"edistlat")
sibFe13_mudistlat_df = tablas(sibFe13_mudistlat_file,"mudistlat")
sibmix13_edistlat_df = tablas(sibmix13_edistlat_file,"edistlat")
sibmix13_mudistlat_df = tablas(sibmix13_mudistlat_file,"mudistlat")
# EPOS p/Fe/mix e/mu
epop13_edistlat_file = str(folder/Path("sim_epos/p/ebin/p_EPO_bin13.t2205"))
epop13_mudistlat_file = str(folder/Path("sim_epos/p/ebin/p_EPO_bin13.t2207"))
epoFe13_edistlat_file = str(folder/Path("sim_epos/Fe/ebin/Fe_EPO_bin13.t2205"))
epoFe13_mudistlat_file = str(folder/Path("sim_epos/Fe/ebin/Fe_EPO_bin13.t2207"))
epomix13_edistlat_file = str(folder/Path("sim_epos/E2/SimE2EPOS.t2205"))
epomix13_mudistlat_file = str(folder/Path("sim_epos/E2/SimE2EPOS.t2207"))
epop13_edistlat_df = tablas(epop13_edistlat_file,"edistlat")
epop13_mudistlat_df = tablas(epop13_mudistlat_file,"mudistlat")
epoFe13_edistlat_df = tablas(epoFe13_edistlat_file,"edistlat")
epoFe13_mudistlat_df = tablas(epoFe13_mudistlat_file,"mudistlat")
epomix13_edistlat_df = tablas(epomix13_edistlat_file,"edistlat")
epomix13_mudistlat_df = tablas(epomix13_mudistlat_file,"mudistlat")
# QGSJETII p/Fe/mix e/mu
qgsp13_edistlat_file = str(folder/Path("sim_qgsjet/p/ebin/p_QGS_bin13.t2205"))
qgsp13_mudistlat_file = str(folder/Path("sim_qgsjet/p/ebin/p_QGS_bin13.t2207"))
qgsFe13_edistlat_file = str(folder/Path("sim_qgsjet/Fe/ebin/Fe_QGS_bin13.t2205"))
qgsFe13_mudistlat_file = str(folder/Path("sim_qgsjet/Fe/ebin/Fe_QGS_bin13.t2207"))
qgsmix13_edistlat_file = str(folder/Path("sim_qgsjet/E2/SimE2QGS.t2205"))
qgsmix13_mudistlat_file = str(folder/Path("sim_qgsjet/E2/SimE2QGS.t2207"))
qgsp13_edistlat_df = tablas(qgsp13_edistlat_file,"edistlat")
qgsp13_mudistlat_df = tablas(qgsp13_mudistlat_file,"mudistlat")
qgsFe13_edistlat_df = tablas(qgsFe13_edistlat_file,"edistlat")
qgsFe13_mudistlat_df = tablas(qgsFe13_mudistlat_file,"mudistlat")
qgsmix13_edistlat_df = tablas(qgsmix13_edistlat_file,"edistlat")
qgsmix13_mudistlat_df = tablas(qgsmix13_mudistlat_file,"mudistlat")

## BIN 24 ##
# Sibyll p/Fe/mix e/mu
sibp24_edistlat_file = str(folder/Path("sim_sibyll/p/ebin/p_SIB_bin24.t2205"))
sibp24_mudistlat_file = str(folder/Path("sim_sibyll/p/ebin/p_SIB_bin24.t2207"))
sibFe24_edistlat_file = str(folder/Path("sim_sibyll/Fe/ebin/Fe_SIB_bin24.t2205"))
sibFe24_mudistlat_file = str(folder/Path("sim_sibyll/Fe/ebin/Fe_SIB_bin24.t2207"))
sibmix24_edistlat_file = str(folder/Path("sim_sibyll/E2/SimE2.t2205"))
sibmix24_mudistlat_file = str(folder/Path("sim_sibyll/E2/SimE2.t2207"))
sibp24_edistlat_df = tablas(sibp24_edistlat_file,"edistlat")
sibp24_mudistlat_df = tablas(sibp24_mudistlat_file,"mudistlat")
sibFe24_edistlat_df = tablas(sibFe24_edistlat_file,"edistlat")
sibFe24_mudistlat_df = tablas(sibFe24_mudistlat_file,"mudistlat")
sibmix24_edistlat_df = tablas(sibmix24_edistlat_file,"edistlat")
sibmix24_mudistlat_df = tablas(sibmix24_mudistlat_file,"mudistlat")
# EPOS p/Fe/mix e/mu
epop24_edistlat_file = str(folder/Path("sim_epos/p/ebin/p_EPO_bin24.t2205"))
epop24_mudistlat_file = str(folder/Path("sim_epos/p/ebin/p_EPO_bin24.t2207"))
epoFe24_edistlat_file = str(folder/Path("sim_epos/Fe/ebin/Fe_EPO_bin24.t2205"))
epoFe24_mudistlat_file = str(folder/Path("sim_epos/Fe/ebin/Fe_EPO_bin24.t2207"))
epomix24_edistlat_file = str(folder/Path("sim_epos/E2/SimE2EPOS.t2205"))
epomix24_mudistlat_file = str(folder/Path("sim_epos/E2/SimE2EPOS.t2207"))
epop24_edistlat_df = tablas(epop24_edistlat_file,"edistlat")
epop24_mudistlat_df = tablas(epop24_mudistlat_file,"mudistlat")
epoFe24_edistlat_df = tablas(epoFe24_edistlat_file,"edistlat")
epoFe24_mudistlat_df = tablas(epoFe24_mudistlat_file,"mudistlat")
epomix24_edistlat_df = tablas(epomix24_edistlat_file,"edistlat")
epomix24_mudistlat_df = tablas(epomix24_mudistlat_file,"mudistlat")
# QGSJETII p/Fe/mix e/mu
qgsp24_edistlat_file = str(folder/Path("sim_qgsjet/p/ebin/p_QGS_bin24.t2205"))
qgsp24_mudistlat_file = str(folder/Path("sim_qgsjet/p/ebin/p_QGS_bin24.t2207"))
qgsFe24_edistlat_file = str(folder/Path("sim_qgsjet/Fe/ebin/Fe_QGS_bin24.t2205"))
qgsFe24_mudistlat_file = str(folder/Path("sim_qgsjet/Fe/ebin/Fe_QGS_bin24.t2207"))
qgsmix24_edistlat_file = str(folder/Path("sim_qgsjet/E2/SimE2QGS.t2205"))
qgsmix24_mudistlat_file = str(folder/Path("sim_qgsjet/E2/SimE2QGS.t2207"))
qgsp24_edistlat_df = tablas(qgsp24_edistlat_file,"edistlat")
qgsp24_mudistlat_df = tablas(qgsp24_mudistlat_file,"mudistlat")
qgsFe24_edistlat_df = tablas(qgsFe24_edistlat_file,"edistlat")
qgsFe24_mudistlat_df = tablas(qgsFe24_mudistlat_file,"mudistlat")
qgsmix24_edistlat_df = tablas(qgsmix24_edistlat_file,"edistlat")
qgsmix24_mudistlat_df = tablas(qgsmix24_mudistlat_file,"mudistlat")

###########################################################################
####### Particle density at 1000 m data for the entire energy range #######
###########################################################################
# Sibyll p/Fe/mix e/mu
sibp_edensity_file = str(folder/Path("sim_sibyll/p/edensity.dat"))
sibp_mudensity_file = str(folder/Path("sim_sibyll/p/mudensity.dat"))
sibFe_edensity_file = str(folder/Path("sim_sibyll/Fe/edensity.dat"))
sibFe_mudensity_file = str(folder/Path("sim_sibyll/Fe/mudensity.dat"))
sibmix_edensity_file = str(folder/Path("sim_sibyll/edensity_mix.dat"))
sibmix_mudensity_file = str(folder/Path("sim_sibyll/mudensity_mix.dat"))
sibp_edensity_df = tablas(sibp_edensity_file,"density")
sibp_mudensity_df = tablas(sibp_mudensity_file,"density")
sibFe_edensity_df = tablas(sibFe_edensity_file,"density")
sibFe_mudensity_df = tablas(sibFe_mudensity_file,"density")
sibmix_edensity_df = tablas(sibmix_edensity_file,"density")
sibmix_mudensity_df = tablas(sibmix_mudensity_file,"density")
# EPOS p/Fe/mix e/mu
epop_edensity_file = str(folder/Path("sim_epos/p/edensity.dat"))
epop_mudensity_file = str(folder/Path("sim_epos/p/mudensity.dat"))
epoFe_edensity_file = str(folder/Path("sim_epos/Fe/edensity.dat"))
epoFe_mudensity_file = str(folder/Path("sim_epos/Fe/mudensity.dat"))
epomix_edensity_file = str(folder/Path("sim_epos/edensity_mix.dat"))
epomix_mudensity_file = str(folder/Path("sim_epos/mudensity_mix.dat"))
epop_edensity_df = tablas(epop_edensity_file,"density")
epop_mudensity_df = tablas(epop_mudensity_file,"density")
epoFe_edensity_df = tablas(epoFe_edensity_file,"density")
epoFe_mudensity_df = tablas(epoFe_mudensity_file,"density")
epomix_edensity_df = tablas(epomix_edensity_file,"density")
epomix_mudensity_df = tablas(epomix_mudensity_file,"density")
# QGSJETII p/Fe/mix e/mu
qgsp_edensity_file = str(folder/Path("sim_qgsjet/p/edensity.dat"))
qgsp_mudensity_file = str(folder/Path("sim_qgsjet/p/mudensity.dat"))
qgsFe_edensity_file = str(folder/Path("sim_qgsjet/Fe/edensity.dat"))
qgsFe_mudensity_file = str(folder/Path("sim_qgsjet/Fe/mudensity.dat"))
qgsmix_edensity_file = str(folder/Path("sim_qgsjet/edensity_mix.dat"))
qgsmix_mudensity_file = str(folder/Path("sim_qgsjet/mudensity_mix.dat"))
qgsp_edensity_df = tablas(qgsp_edensity_file,"density")
qgsp_mudensity_df = tablas(qgsp_mudensity_file,"density")
qgsFe_edensity_df = tablas(qgsFe_edensity_file,"density")
qgsFe_mudensity_df = tablas(qgsFe_mudensity_file,"density")
qgsmix_edensity_df = tablas(qgsmix_edensity_file,"density")
qgsmix_mudensity_df = tablas(qgsmix_mudensity_file,"density")
