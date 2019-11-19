# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:58:30 2019

@author: ASUS I5
"""

"""
ALGORITMOS PARA SUAVIZADO DE LA SEÑAL DATA SMOOTHING """
#LIBRERIAS
import senal1 as sig
import numpy as np
import pylab as plt
from scipy import signal
from scipy.ndimage import gaussian_filter
###### Presión #####
#Visualizar la señal 
sig_input_sensor =sig.sensor
### numero de muestras##
n_1=len(sig_input_sensor)
plt.plot(sig_input_sensor, color='blue',label="Señal original")

### Mean Average para la señal de corazon
#definir ventana
k=14
m=0
mean_smooth=np.zeros(n_1)#Llenar un vector de tamano n con zeros
for i in range(k+1,n_1-k-1):
    m+=1 
    mean_smooth[i]=np.mean(sig_input_sensor[i-k:m+k])
plt.plot(mean_smooth,color='blue', label ='data smoothing')
plt.plot(sig_input_sensor,color='red',label='original samples')
plt.show()

#### Variacion Mean average



####### Presión ######
#### visualizar la señal del corazon ####
sig_input_sensor=sig.sensor
#Para saber el numero de muestras
n_1=len(sig_input_sensor)
plt.plot(sig_input_sensor)
n
plt.plot(sig_input)
############## MEAN AVERAGE ################
##Definir ventana
k=11
m=0
#linea para encerar0
mean_smooth=np.zeros(n) # llenar un vector de tamaño n con zeros
for i in range (k+1,n_1-k-1):
    m+=1    #m++
    mean_smooth[i]= np.mean(sig_input[i-k:m+k])
    
#plt.plot(mean_smooth,color='blue', label='data smoothinng')
#plt.plot(sig_input,colo='red',label='original sample')

plt.plot(mean_smooth,color='blue', label='data smoothinng')
plt.plot(sig_input_sensor,color='red',label='original sample')    
plt.show()
############## MEAN AVERAGE ################


k=9
mean_smooth1=np.zeros(n)
for i in range (int(np.floor(k/2)),int(n-np.floor(k/2)-1)):
    mean_smooth1[i]=0
    for j in range (int(-np.floor(k/2)),int (np.floor(k/2))):
        mean_smooth1[i]=mean_smooth1[i]+sig_input[i+j]
        mean_smooth1[i]=mean_smooth1[i]/k
plt.plot(mean_smooth1,color='blue', label='data smoothing')
plt.show()

############## MEAN AVERAGE ################
k=11
m=0
median_smooth=np.zeros(n)
for i in range (k+1,n-k-1):
    n+=1
    median_smooth[i]=np.median(sig_input[i-k:m+k])
plt.plot(median_smooth,color='blue', label='daa smoothing')
plt.plot(sig_input,color='red',label='original sample')   
plt.show()   
 ############## MEAN AVERAGE ################
savis_smooth= signal.savgol_filter   (sig_input,11,3)
