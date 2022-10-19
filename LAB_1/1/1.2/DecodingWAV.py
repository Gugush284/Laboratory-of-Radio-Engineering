import matplotlib.pyplot as plt  # импорт модуля matplotlib.pyplot
import numpy as np  # импорт бибилиотеки numpy
import scipy.io.wavfile  # импорт модуля scipy.io.wavfile
from IPython.display import Audio

Audio('glockenspiel.wav')

fs, x = scipy.io.wavfile.read('glockenspiel.wav') # чтение аудиофайла

print(fs)
print(x)
print(x.dtype)
print(x.size)

x1=x[8000:10000]                   # выбор наблюдаемого диапазона
k=np.arange(x1.size)               # отсчеты по времени
print(x1)
print(k)

# Построение графиков 
plt.figure(figsize=[16, 4])        # создание полотна размером шириной 8 X 4 дюйма
plt.plot(k/fs, x1, 'b.')           # построение графика цифрового сигнала точками точками
plt.grid()                             
plt.xlabel("$t$, c")                      
plt.ylabel("$x[k]$")             
plt.tight_layout()

plt.show()