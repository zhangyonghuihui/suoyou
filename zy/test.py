# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:56:02 2021

@author: 123
"""
import  matplotlib.pyplot  as  plt
import pandas as pd
plt.rcParams['font.sans-serif'] = 'SimHei'  
plt.rcParams['axes.unicode_minus'] = False 
df = pd.read_excel('zcxx.xlsx') 
df2 = df.copy()
df2.index = pd.to_datetime(df2.时间)
df3=df[['代理买卖证券业务净收入','证券承销与保荐业务净收入','财务顾问业务净收入','投资咨询业务净收入','资产管理业务净收入','证券投资收益','融资融券业务利息收入']]
#--------------------------------------------------
df4=df3.iloc[0]
rate=df4.values
labels =df4.index
plt.figure(figsize=(6,9))    		# 设置图形大小
patches, ltext, ptext = plt.pie(rate, labels=labels,
                            autopct='%.1f%%', shadow=False,
                            startangle=90)
#-------------------------------------------------
df4=df3.iloc[1]
rate=df4.values
labels =df4.index
plt.figure(figsize=(6,9))    		# 设置图形大小
patches, ltext, ptext = plt.pie(rate, labels=labels,
                            autopct='%.1f%%', shadow=False,
                            startangle=90)
#----------------------------------------------------------
df4=df3.iloc[2]
rate=df4.values
labels =df4.index
plt.figure(figsize=(6,9))    		# 设置图形大小
patches, ltext, ptext = plt.pie(rate, labels=labels,
                            autopct='%.1f%%', shadow=False,
                            startangle=90)
#------------------------------------------------
df4=df3.iloc[3]
rate=df4.values
labels =df4.index
plt.figure(figsize=(6,9))    		# 设置图形大小
patches, ltext, ptext = plt.pie(rate, labels=labels,
                            autopct='%.1f%%', shadow=False,
                            startangle=90)
#----------------------------------------------------
df4=df3.iloc[4]
rate=df4.values
labels =df4.index
plt.figure(figsize=(6,9))    		# 设置图形大小
patches, ltext, ptext = plt.pie(rate, labels=labels,
                            autopct='%.1f%%', shadow=False,
                            startangle=90)
#----------------------------------------------------------
df4=df3.iloc[5]
rate=df4.values
labels =df4.index
plt.figure(figsize=(6,9))    		# 设置图形大小
patches, ltext, ptext = plt.pie(rate, labels=labels,
                            autopct='%.1f%%', shadow=False,
                            startangle=90)
#------------------------------------------

