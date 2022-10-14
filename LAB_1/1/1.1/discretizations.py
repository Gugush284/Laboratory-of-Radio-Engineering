import matplotlib.pyplot as plt  # импорт модуля matplotlib.pyplot
import numpy as np  # импорт бибилиотеки numpy
import quantize

# Описание констант
N = 25                                    # Число отсчетов по времени
f0 = 200.0                                # Частота синусоиды в Гц
fs = 2000.0                               # Частота дискретизации в Гц
num_levels = 50                           # число уровней квантования

k = np.arange(N)                          # Mассив времен k от 0 до N-1 с шагом 1
x = np.sin(2*np.pi*(f0/fs)*k)             # Последовательность x[k]

# Построение графиков аналогового и дискретизованного сигнала
plt.figure(figsize=[12, 4])                         # создание полотна размером шириной 8 X 4 дюйма
t = np.linspace(0, N/fs, num=1024)                  # создание массива времен t (1024 значения от 0 до N*fs)

plt.plot(t, np.sin(2*np.pi*f0*t), 'g', label='аналоговый сигнал $x(t)$')  
                                                    # построение графика x(t) (точки соединяются линиями)
                                                    # 'g' означает, что используется зеленая линия (green)

plt.stem(k/fs, x, 'b', 'bo', label='дискретизованный сигнал $x[k]$')            
                                                    # построение графика функции дискретного времени x[k]
                                                    # 'b', 'bo' означает, что отсчеты оборажаются синим цветом (blue)

plt.grid()                                          # сетка
plt.xlabel("$t$, c")                                # подпись оси X
plt.ylabel("$x(t), x[k]$")                          # подпись оси Y
plt.title("Аналоговый и дискретизованный сигналы")  # заголовок графика
plt.legend(loc='best', bbox_to_anchor=(1, 1))
plt.tight_layout()                                  # автоматическая корректировка расположения осей графика

# моделирование квантования дискретного сигнала
y = quantize.quantize_uniform(x, quant_min=-1, quant_max=1, quant_level=num_levels)
bins = np.linspace(-1, 1, num_levels)

# Вывод графика аналогового и цифрового сигнала
plt.figure(figsize=[12, 4])                         # создание полотна размером шириной 8 X 4 дюйма
t = np.linspace(0, N/fs, num=1024)                    # создание массива времен t (1024 значения от 0 до N*fs)
plt.plot(t, np.sin(2*np.pi*f0*t), 'g', label='аналоговый сигнал $x(t)$')        
                                                    # построение графика x(t) (точки соединяются линиями)

plt.stem(k/fs, y, 'b', 'bo', label='цифровой сигнал $y[k]$')                
                                                    # построение графика функции дискретного времени y[k]
                                                    # k/fs - м
    
if num_levels < 21:                                 # если число уровней не велико, то производится
    plt.yticks(bins)                                # установка делений шкалы оси Y, совпадающих с уровнями квантования

plt.grid()                                                         # сетка
plt.xlabel("$t$, c")                                               # подпись оси X
plt.ylabel("$x(t), y[k]$")                                         # подпись оси Y
plt.title("Аналоговый и цифровой сигналы  (квантование)")          # заголовок графика
plt.legend(loc='best', bbox_to_anchor=(1, 1))
plt.tight_layout()                                  # автоматическая корректировка расположения осей графика

xy = abs(x-y)
print(xy)
#np.savetxt("x-y.txt", xy)

# Ошибки квантования
plt.figure(figsize=[12, 4])
plt.title("Ошибка квантования") 
plt.plot(t, np.sin(2*np.pi*f0*t), 'g', label='аналоговый сигнал $x(t)$')
plt.stem(k/fs, xy, 'm', 'mo', label="абсолютная ошибка \nквантования \n$\\epsilon[k]=|x[k]-y[k]|$")       
                                      #вывод абсолютных значений ошибки квантования для дискретного сигнала
plt.yticks(bins)
plt.grid()
plt.xlabel("$t$, c")                                          # подпись оси X
plt.ylabel("$x(t), \\varepsilon[k]=|x[k]-y[k]|$")             # подпись оси Y
plt.legend(loc='best', bbox_to_anchor=(1, 1))
plt.tight_layout()

plt.show()