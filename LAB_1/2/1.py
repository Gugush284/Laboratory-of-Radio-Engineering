import helpers as h
import matplotlib.pyplot as plt  # импорт модуля matplotlib.pyplot
import numpy as np  # импорт бибилиотеки numpy


def boxcar(t, tau):
    if mod == 1:
        if abs(t)<tau/2:
            return 1.0                 
        else:
            return 0.0
    elif mod == 2:
        if abs(t)<tau/2:
            return (1 - abs(t)/(tau/2))                 
        else:
            return 0.0
    elif mod == 3:
        if abs(t)<tau/2:
            return (0.5 * (1 + np.cos(2 * np.pi * t/tau)))                 
        else:
            return 0.0
    else:
        return 0.0

       

"""
mod = 1 прямоугольное окно
mod = 2 треугольное окно
mod = 3 окно Ханна
"""
mod = 3 
tau=1000e-6 #100 мкс
print(tau)

f_band=np.linspace(-8/tau, 8/tau, 500) # 500 - число точек в диапазоне, в которых вычисляется X(f)            
    
t_band=np.linspace(-2*tau, 2*tau, 1024)
plt.figure(figsize=[6, 4])
plt.plot(t_band*1e6, [boxcar(t, tau) for t in t_band])
plt.xlabel("Время t, мкс")
plt.ylabel("$x(t)$, В")
plt.title("Сигнал")
plt.tight_layout() 
plt.grid()

plt.figure(figsize=[6, 4])
plt.plot(f_band/1e3, h.fourier_transform(signal=boxcar, f_band=f_band, tau=tau, t1=-tau/2, t2=tau/2, res_type="abs")*1e6)
plt.xlabel("Частота f, кГц")
plt.ylabel("$|X(f)|$,  мкВ / Гц")
plt.title("Спектр")
plt.tight_layout() 
plt.grid()

plt.show()