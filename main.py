"""
 Численное дифференцирование.

Первая часть - разностный аналог первой производной. Заключается в поиске производной с помощью разности между
 значениями функции в разных точках. Используется конечные разности, а не бесконечно малые величины.

 Используют три разностных аналога, по правой стороне - (f(x0 + h) - f(x0)) / h
 по левой стороне - (f(x0) - f(x0 - h)) / h
 по центру - (f(x0+ h) - f(x0 - h)) / 2h

центральная разность имеет наименьшее отклонение от производной функции

"""
from left_right_diff import left, right, central, second
import matplotlib.pyplot as plt
from math import *


def f1(x):
    return x / sin(x)


def df1(x):
    return (sin(x) - x * cos(x)) / sin(x) ** 2


def ddf1(x):
    return (x*sin(x)**2 - 2*sin(x)*cos(x)+2*x*cos(x)**2) / (sin(x)**3)


h = 0.1
x0 = pi / 2
# x1 = x0 - 1 a
# x2 = x0 + 1 b

print(df1(x0))
print()

plotx = []
plotl = []
plotr = []
plotc = []
plotscnd = []

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

while h >= 1e-15:  # пока шаг не станет с точностью не меньше 15 знаково после запятой
    plotx.append(h)
    plotl.append(abs(left(f1, x0, h) - df1(x0)))
    plotr.append(abs(right(f1, x0, h) - df1(x0)))
    plotc.append(abs(central(f1, x0, h) - df1(x0)))

    plotscnd.append(abs(second(f1, x0, h) - ddf1(x0)))
    h = h / 10
    print()

ax1.plot(plotx, plotl, color='red', ls='--', marker='*', label='left')
ax1.plot(plotx, plotr, color='blue', ls='-', marker='^', label='right')
ax1.plot(plotx, plotc, color='green', ls='dotted', marker='8', label='central')
ax1.plot(plotx, plotscnd, color='orange', ls='-', marker='o', label='second derivative')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_title('Left, right and central methode')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True)



ax2.plot(plotx, plotscnd, color='orange', ls='-', marker='o', label='second derivative')
ax2.set_title('Second derivative')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.legend()
ax2.grid(True)

plt.tight_layout()

plt.show()
