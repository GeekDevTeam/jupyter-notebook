#!/usr/bin/env python
# coding: utf-8

# In[7]:


# y = x**2 - 6*abs(x) + 8
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0


# In[11]:


from sympy import Symbol, oo, diff, Interval, is_increasing, is_decreasing, pprint
from sympy.solvers import solve, solveset
from sympy.plotting import plot
import sympy
import math
from sympy import *

init_printing()


# In[12]:


x = Symbol('x', real = True)
y = x**2 - 6*abs(x) + 8
y


# In[14]:


# 1. Определить корни
roots = solve(y, x)
roots


# In[29]:


# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
for i in range(len(roots)):
    if i == 0:
        if is_increasing(y, Interval(-oo, roots[i] - 1)):
            print(f'Функция возврастает в промедутке {Interval(-oo, roots[i])}')
        else:
            print(f'Функция убывает в промедутке {Interval(-oo, roots[i])}')
    elif i == len(roots) - 1:
        if is_increasing(y, Interval(roots[i] + 1, +oo)):
            print(f'Функция возврастает в промедутке {Interval(roots[i], +oo)}')
        else:
            print(f'Функция убывает в промедутке {Interval(roots[i], +oo)}')
    else:
        if is_increasing(y, Interval(roots[i-1] + 1, roots[i] - 1)):
            print(f'Функция возврастает в промедутке {Interval(roots[i-1], roots[i])}')
        else:
            print(f'Функция убывает в промедутке {Interval(roots[i-1], roots[i])}')
            


# In[24]:


# 4. Построить график
p1 = plot(y)
p1


# In[35]:


# 5. Вычислить вершину
derivate = diff(y, x)
roots_diff = solve(derivate, x)
if len(roots_diff) == 1:
    root_plus = roots_diff[0]
    root_minus = -roots_diff[0]

top_y1 = y.subs(x, root_plus)
top_y2 = y.subs(x, root_minus)

print(f'(x={root_plus}, y={top_y1}) (x={root_minus}, y={top_y2})')


# In[39]:


# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0

for i in range(len(roots)):
    is_positive = y.subs(x, roots[i] - 0.000001) > 0
    if i == 0:
        if is_positive:
            print(f'Функция f > 0 в промежутке {Interval(-oo, roots[i])}')
        else:
            print(f'Функция f < 0 в промежутке {Interval(-oo, roots[i])}')
    elif i == len(roots) - 1:
        if is_positive:
            print(f'Функция f > 0 в промежутке {Interval(roots[i], +oo)}')
        else:
            print(f'Функция f < 0 в промежутке {Interval(roots[i], +oo)}')
    else:
        if is_positive:
            print(f'Функция f > 0 в промедутке {Interval(roots[i-1], roots[i])}')
        else:
            print(f'Функция f < 0 в промедутке {Interval(roots[i-1], roots[i])}')

