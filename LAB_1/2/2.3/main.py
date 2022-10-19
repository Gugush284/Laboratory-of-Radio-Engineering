import helpers as h
import matplotlib.pyplot as plt  # импорт модуля matplotlib.pyplot
import numpy as np  # импорт бибилиотеки numpy

f0=10*1e3       # 10 кГц
tau=500*1e-6    # 500 мкс

def sin_with_boxcar(t, tau):                            
    if 0<=t<=tau:
        if mode == 0:
        # случай прямоугольного окна
            return np.sin(2*np.pi*f0*t)
        elif mode == 1: 
            # случай окна Ханна
            return np.sin(2*np.pi*f0*t) * (0.5+0.5*np.cos(np.pi*(t-tau/2)/(tau/2)))
        else:
            return 0.0
    else:
        return 0.0
    
f_band=np.linspace(-2*f0, 2*f0, 2000)
t_band=np.linspace(-0.5*tau, 1.5*tau, 1024)
mode = 1

plt.figure(figsize=[8, 4])
plt.plot(t_band*1e6, [sin_with_boxcar(t, tau) for t in t_band])
plt.title("Сигнал окна Ханна")
plt.xlabel("Время t, мкс")
plt.ylabel("$x(t)$, В")
plt.tight_layout() 
plt.grid()

plt.figure(figsize=[8, 4])
plt.plot(f_band/1e3, h.fourier_transform(signal=sin_with_boxcar, f_band=f_band, tau=tau, t1=-2*tau, t2=2*tau, res_type="abs")*1e6)
plt.title("Спектр окна Ханна")
plt.xlabel("Частота f, кГц")
plt.ylabel("$|X(f)|$,  мкВ / Гц")
plt.tight_layout() 
plt.grid()

mode = 0

plt.figure(figsize=[8, 4])
plt.plot(t_band*1e6, [sin_with_boxcar(t, tau) for t in t_band])
plt.title("Сигнал синусоиды")
plt.xlabel("Время t, мкс")
plt.ylabel("$x(t)$, В")
plt.tight_layout() 
plt.grid()

plt.figure(figsize=[8, 4])
plt.plot(f_band/1e3, h.fourier_transform(signal=sin_with_boxcar, f_band=f_band, tau=tau, t1=-2*tau, t2=2*tau, res_type="abs")*1e6)
plt.title("Спектр синусоиды")
plt.xlabel("Частота f, кГц")
plt.ylabel("$|X(f)|$,  мкВ / Гц")
plt.tight_layout() 
plt.grid()

plt.show()