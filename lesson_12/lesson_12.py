#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Прочитайте все данные о продажах продукта и покажите их с помощью многострочного графика
# 2. Прочитайте данные о продажах мыла для купания за все месяцы и покажите их с помощью столбчатой диаграммы.
# 3. Рассчитайте общие данные о продажах за год для каждого продукта и покажите их с помощью круговой диаграммы


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


pd_df = pd.read_csv('company_sales_data.csv')
pd_df.head(12)


# In[4]:


# 1. Прочитайте все данные о продажах продукта и покажите их с помощью многострочного графика
month_list = pd_df['month_number']
total_units = pd_df['total_units']

facecream = pd_df['facecream'].tolist()
facewash = pd_df['facewash'].tolist()
toothpaste = pd_df['toothpaste'].tolist()
bathingsoap = pd_df['bathingsoap'].tolist()
shampoo = pd_df['shampoo'].tolist()
moisturizer = pd_df['moisturizer'].tolist()

plt.plot(month_list, facecream, label = 'Крем для лица', color = 'red', marker = 'o')
plt.plot(month_list, facewash, label = 'Средство для мытья лица', color = 'orange', marker = 'o')
plt.plot(month_list, toothpaste, label = 'Зубная паста', color = 'yellow', marker = 'o')
plt.plot(month_list, bathingsoap, label = 'Мыло для купания', color = 'green', marker = 'o')
plt.plot(month_list, shampoo, label = 'Шампунь', color = 'purple', marker = 'o')
plt.plot(month_list, moisturizer, label = 'Увлажнитель', color = 'blue', marker = 'o')

plt.xticks(month_list)
plt.title('Информация о продажа')
plt.ylabel('Количество проданных единиц')
plt.xlabel('Номер месяца')
plt.legend(loc = 'lower right')
plt.show()


# In[5]:


# 2. Прочитайте данные о продажах мыла для купания за все месяцы и покажите их с помощью столбчатой диаграммы.
plt.bar(month_list - 0.3, bathingsoap, color = 'r', width = 0.7, align='edge')
plt.xticks(month_list)
plt.title('Информация по продажам мыла для купания')
plt.ylabel('Количество проданных единиц')
plt.xlabel('Номер месяца')
plt.show()


# In[6]:


# 3. Рассчитайте общие данные о продажах за год для каждого продукта и покажите их с помощью круговой диаграммы
facecream_sum = sum(facecream) 
facewash = sum(facewash)
toothpaste = sum(toothpaste)
bathingsoap = sum(bathingsoap)
shampoo = sum(shampoo)
moisturizer = sum(moisturizer)

my_labels = [
    'Крем для лица',
    'Средство для мытья лица',
    'Зубная паста',
    'Мыло для купания',
    'Шампунь',
    'Увлажнитель'
]

y = np.array([
    facecream_sum,
    facewash,
    toothpaste,
    bathingsoap,
    shampoo,
    moisturizer
])

plt.pie(y, labels = my_labels)
#plt.legend(loc = 'center left') #не красиво отображется где бы не размещал
plt.show() 


# In[ ]:




