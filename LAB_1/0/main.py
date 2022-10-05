import numpy as np                  # импорт бибилиотеки numpy
import matplotlib.pyplot as plt     # импорт модуля matplotlib.pyplot

def my_fun(x):
    size = np.shape(x)[0]

    y = np.empty(size, dtype=float)

    for i in range(0, size):
        if x[i] == 0:
            y[i] = 1
        else:
            y[i] = np.sin(2 * np.pi * 0.07 * x[i])/x[i]

    return y

print("Создание массивов")

array = np.array([1, 3, 5, 7, 9])
arange = np.arange(1, 10, 2, dtype=int)
linspace = np.linspace(1, 9, num=5, dtype=int)

print(array)
print(arange)
print(linspace)

print("Построение синуса")
k = np.arange(0, 101, 1, dtype=int)

x = np.empty(101, dtype=float)
for i in range(0, 101):
    x[i] = np.sin(2 * np.pi * 0.07 * k[i])

for i in range(0, 101):
    print("sin(", k[i], ") = ", x[i])

y = my_fun(k)

z = np.empty(101, dtype=complex)
for i in range(0, 101):
    z[i] = np.exp(-2j * np.pi * 0.07 * k[i])

plt.figure(figsize=[12, 5])
plt.plot(k, x, color = 'r', linestyle='dashed')
plt.stem(k, x)
plt.xlabel('Аргумент')
plt.ylabel('sin')
plt.title('Построение синуса')

plt.figure(figsize=[12, 5])
plt.xlabel('Аргумент')
plt.ylabel('sinc')
plt.title('Построение sinc')
plt.plot(k, y, color = 'b', linestyle='dashed')

plt.figure(figsize=[12, 5])
plt.xlabel('Аргумент')
plt.ylabel('Функция')
plt.title('Построение z')
plt.plot(k, z.real)
plt.plot(k, z.imag)

plt.show()