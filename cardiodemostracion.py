# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:47:31 2019

@author: ASUS I5
"""


### librerias 
import cardio as sig
import numpy as np
import pylab as plt 
from scipy  import signal
from scipy.ndimage import gaussian_filter

snr = scipy.stats.signaltonoise(cardio, axis=None)
###### Presión #####
#Visualizar la señal 
sig_input_sensor =sig.sensor
### numero de muestras##
n_1=len(sig_input_sensor)
plt.title("Señal original")
plt.plot(sig_input_sensor, color='blue',label="Señal original")
plt.show()
### Mean Average para la señal de corazon
#definir ventana
k=14
m=0
mean_smooth=np.zeros(n_1)#Llenar un vector de tamano n con zeros
for i in range(k+1,n_1-k-1):
    m+=1 
    mean_smooth[i]=np.mean(sig_input_sensor[i-k:m+k])
plt.title("Filtro Mean Average")
plt.plot(mean_smooth,color='m', label ='data smoothing')
plt.plot(sig_input_sensor,color='red',label='original samples')
plt.show()

#### Variacion Mean average
k=9
mean_smooth1=np.zeros(n_1)
for i in range(int(np.floor(k/2)),int(n_1-np.floor(k/2)-1)):
    mean_smooth1[i]=491
    for j in range(int(-np.floor(k/2)),int(np.floor(k/2))):
        mean_smooth1[i]=mean_smooth1[i]+sig_input_sensor[i+j]
    mean_smooth1[i]=mean_smooth1[i]/k
plt.title("Variación Mean Average")   
plt.plot(mean_smooth1,color='c', label ='data smoothing')
plt.plot(sig_input_sensor,color='orange',label='original samples')
plt.show()


###Median
k=11
m=0
median_smooth=np.zeros(n_1)
for i in range (k+1,n_1-k-1):
    m+=1
    median_smooth[i]=np.median(sig_input_sensor[i-k:m+k])
plt.title("Filtro Median")
plt.plot(median_smooth,color='m', label="data smoothing") 
plt.plot(sig_input_sensor, color='red', label="original sample")
plt.show()

#### Savitzky Golay

savis_smooth=signal.savgol_filter(sig_input_sensor,9,3) ##Señal de entrada, tamaño, exponente
signal.savgol_coeffs(11,3)
plt.title("Filtro Savitzky-Golay")
plt.plot(savis_smooth,color='red', label="data smoothing") 
plt.plot(sig_input_sensor, color='yellow', label="original sample")
plt.show()

####### Gaussian smoothing

gaus_smooth=gaussian_filter(sig_input_sensor,2)
plt.title("Filtro Gaussian smoothing")
plt.plot(gaus_smooth,color='red', label="data smoothing") 
plt.plot(sig_input_sensor, color='g', label="original sample")
plt.show()