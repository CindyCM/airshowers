"""
Created on Tue Dic 02 13:49:59 2020

@author: cindy

- Funciones para graficar cositas
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

folder = Path("/home/cindy/TEST")
obsxmax_file = str(folder/Path("datos/Xmax_Auger2019"))
obsxmax_df = pd.DataFrame(np.genfromtxt(obsxmax_file, comments='#'),
                columns=['meanLgE', 'nEvts', 'Xmax', 'meanErr', 'meanSystUp',
                'meanSystLow', 'Std dv', 'sigmaErr', 'sigmaSystUp', 'sigmaSystLow'])

def powerlawfit(x,a,b):
    Es = 1e18
    return a*((10**x)/Es)**b

def nkgaugerfit(r,a,b):
    rs = 1e3
    return a*(r/rs)**(-b)*(1+r/rs)**(-b)

def plotXmax(dfp,dfFe,model,fig,ax,plotkind,linestyle,png):
    dfp.plot(kind=plotkind,style=linestyle, x='logEbin', y='Mean', ax=ax, color='green',label='p-'+model)
    dfFe.plot(kind=plotkind,style=linestyle, x='logEbin', y='Mean', ax=ax, color='orange',label='Fe-'+model)
    obsxmax_df.plot(kind='scatter',x='meanLgE',y='Xmax', ax=ax, color='black',label='Auger')
    plt.savefig(str(folder/Path('graficas/Xmax_'+png+'.png')), transparent=False)
    plt.close(fig)

    # tablep.plot(kind=plotkind, x='logEmin', y='Std dev', ax=ax_devXmax, color='green',label='p')
    # tableFe.plot(kind=plotkind, x='logEmin', y='Std dev', ax=ax_devXmax, color='orange',label='Fe')
    # obsxmax_table.plot(kind='scatter',x='meanLgE',y='Std dv', ax=ax_devXmax, color='black',label='Auger')
    # plt.savefig(str(folder/Path('graficas/devXmax_'+model+'.png')), transparent=False)

#graficar Xmu

def plotdistlat(dfp,dfFe,optp,optFe,particle,model,fig,ax,pngname): #grafica distribución lateral y su respectiva función nkg
    dfp.plot(kind='scatter',marker= '.',x='R',y='Mean',ax=ax,color='green',label='p '+model)
    dfFe.plot(kind='scatter',marker= '.',x='R',y='Mean',ax=ax,color='orange',label='Fe '+model)
    plt.plot(dfp['R'],nkgaugerfit(dfp['R'],*optp),color='green',linestyle='--',label='p-fit')
    plt.plot(dfFe['R'],nkgaugerfit(dfFe['R'],*optFe),color='orange',linestyle='--',label='Fe-fit')
    plt.legend()
    plt.savefig(str(folder/Path('graficas/'+particle+'distlat_'+pngname+'.png')), transparent=False)
    plt.close(fig)

def plotdensity(dfp,dfFe,optp,optFe,particle,model,fig,ax,pngname): #grafica la densidad de partículas a r=1000m vs. E0 y su ajuste a una ley de potencias
    dfp.plot(kind='scatter',marker= '.',x='logEbin',y='Mean',ax=ax,color='green',label='p-'+model)
    dfFe.plot(kind='scatter',marker= '.',x='logEbin',y='Mean',ax=ax,color='orange',label='Fe-'+model)
    plt.plot(dfp['logEbin'],powerlawfit(dfp['logEbin'],*optp),color='green',linestyle='--',label='p-fit')
    plt.plot(dfFe['logEbin'],powerlawfit(dfFe['logEbin'],*optFe),color='orange',linestyle='--',label='Fe-fit')
    plt.legend()
    plt.savefig(str(folder/Path('graficas/'+particle+'density1000_'+pngname+'.png')), transparent=False)
    plt.close(fig)
