import os
import numpy as np
import matplotlib.pyplot as plt

def f(x,A):
    return 100*(np.sqrt(np.abs(A-0.01*x**2))+0.01*np.abs(x+10))

#параметры
A=1
x_values = np.linspace(-15, 5, 800)

#расчёт координат
y_values = f(x_values, A)
data = [{"x": x, "y": y} for x, y in zip(x_values, y_values)]

#cоздание директории
if not os.path.exists('results'):
    os.makedirs('results')

# Сохранение в XML
with open('results/function_values.xml', 'w') as file:
    file.write('<?xml version="1.1" encoding="UTF-8" ?>\n')
    file.write('<data>\n')
    file.write('    <xdata>\n')
    for x in x_values:
        file.write('        <x>{}</x>\n'.format(x))
    file.write('    </xdata>\n')
    file.write('    <ydata>\n')
    for y in y_values:
        file.write('        <y>{}</y>\n'.format(y))
    file.write('    </ydata>\n')
    file.write('</data>')

#построение графика функции
plt.figure(figsize=(16, 9))
plt.plot(x_values, y_values, label='f(x)', color='blue')
plt.title('График функции f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()