"""
 Численное дифференцирование.

Первая часть - разностный аналог первой производной. Заключается в поиске производной с помощью разности между
 значениями функции в разных точках. Используется конечные разности, а не бесконечно малые величины.

 Используют три разностных аналога, по правой стороне - (f(x0 + h) - f(x0)) / h
 по левой стороне - (f(x0) - f(x0 - h)) / h
 по центру - (f(x0+ h) - f(x0 - h)) / 2h

центральная разность имеет наименьшее отклонение от производной функции
Бояршинов МГ, 2006 -- Численные методы.ч4
"""
from left_right_diff import left, right, central, second
import matplotlib.pyplot as plt
from math import *


def f1(x):
    return sin(x)


def df1(x):
    return cos(x)

#ff
def ddf1(x):
    return -sin(x)


x0 = 0
h = 1e-7
x1 = 2 * pi
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

while x0 <= x1:  # пока шаг не станет с точностью не меньше 15 знаково после запятой
    plotx.append(x0)
    plotl.append(df1(x0) - left(f1, x0, h))
    plotr.append(df1(x0) - right(f1, x0, h))
    plotc.append(df1(x0) - central(f1, x0, h))

    plotscnd.append(ddf1(x0) - second(f1, x0, h))
    x0 += 1e5 * h

ax1.plot(plotx, plotl, color='red', ls='--', marker='*', label='left')
ax1.plot(plotx, plotr, color='blue', ls='-', marker='^', label='right')
ax1.plot(plotx, plotc, color='green', ls='dotted', marker='8', label='central')
#ax1.set_xscale('log')
#ax1.set_yscale('log')
ax1.set_title('Left, right and central methode')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True)

ax2.plot(plotx, plotscnd, color='orange', ls='-', marker='o', label='second derivative')
ax2.set_title('Second derivative')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
#ax2.set_xscale('log')
#ax2.set_yscale('log')
ax2.legend()
ax2.grid(True)

plt.tight_layout()

plt.show()
