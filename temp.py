# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

order1 = pd.read_excel('AirQualityUCI.xlsx')

print('读取到的数据为：')
print(order1)
#j=0
#k=0
#for i in order1['CO(GT)']:
#    if(i==-200):
#        order1['CO(GT)'][j]=0
#    j = j+1;
#
#for i in order1['T']:
#    if(i==-200):
#        order1['T'][k]=0
#    k = k+1;
order1=order1.replace(-200,np.nan)
order1=order1.fillna(method='ffill')
print('再次处理缺失值后：')
print(order1)
    
def outRange(Ser1):
    QL = Ser1.quantile(0.25)
    QU = Ser1.quantile(0.75)
    IQR = QU-QL
    Ser1.loc[Ser1>(QU+1.5*IQR)] = QU
    Ser1.loc[Ser1<(QL-1.5*IQR)] = QL
    return Ser1
print('数据处理前温度最小值：')
print(order1['T'].min())
print('数据处理前二氧化碳浓度最小值：')
print(order1['CO(GT)'].min())
order1['T'] = outRange(order1['T'])
order1['CO(GT)'] = outRange(order1['CO(GT)'])
print('数据处理后温度最小值：')
print(order1['T'].min())
print('数据处理后二氧化碳浓度最小值：')
print(order1['CO(GT)'].min())




#p = plt.boxplot(order1['CO(GT)'].values,notch=True)
#outCO = p['fliers'][0].get_ydata()
group1 = order1[['Date','CO(GT)','T']].groupby(by = 'Date')
agroup1 = group1.mean()
print('分组聚合切进行均值处理后：')
print(agroup1)

co = agroup1['CO(GT)']
tem = agroup1['T']
FoMarchc = co[:22]
FoMarcht = tem[:22]
date = co.keys()

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus']=False

plt.figure(figsize=(12,6),)
plt.title('04年3月份一氧化碳浓度折线图')
plt.xlabel('日期/年月日')
plt.ylabel('一氧化碳浓度(mg /立方公尺)')
plt.plot(date[:22],co[:22])
plt.show()
plt.figure(figsize=(12,6))
plt.title('04年3月份温度折线图')
plt.xlabel('日期/年月日')
plt.ylabel('温度(°C)')
plt.plot(date[:22],tem[:22]) 
plt.show()
plt.figure(figsize=(12,6))
plt.title('04年3月份温度与一氧化碳对比折线图')
plt.xlabel('日期/年月日')
plt.ylabel('趋势')
plt.plot(date[:22],tem[:22]) 
plt.plot(date[:22],co[:22]*5) 
plt.legend(['温度','一氧化碳'])
plt.show()

FoApd = date[22:52]
FoApt = tem[22:52]
FoApc = co[22:52]
plt.figure(figsize=(12,6))
plt.title('04年4月份一氧化碳浓度折线图')
plt.xlabel('日期/年月日')
plt.ylabel('一氧化碳浓度(mg /立方公尺)')
plt.plot(FoApd,FoApc)
plt.show()
plt.figure(figsize=(12,6))
plt.title('04年4月份温度折线图')
plt.xlabel('日期/年月日')
plt.ylabel('温度(°C)')
plt.plot(FoApd,FoApt)
plt.show()
plt.figure(figsize=(12,6))
plt.title('04年4月份温度与一氧化碳对比折线图')
plt.xlabel('日期/年月日')
plt.ylabel('趋势')
plt.plot(FoApd,FoApt) 
plt.plot(FoApd,FoApc*5) 
plt.legend(['温度','一氧化碳'])
plt.show()

plt.figure(figsize=(12,6))
plt.title('03年3月份到04年4月份温度与一氧化碳浓度散点图')
plt.xlabel('一氧化碳浓度(mg /立方公尺)')
plt.ylabel('温度(°C)')
plt.scatter(co,tem)
plt.show()


target = order1[['CO(GT)']]
data = order1['Date']
from sklearn.linear_model import LinearRegression

mode1 = LinearRegression()

mode1.fit(order1[['CO(GT)']][:100],order1[['Date']][:100])
prediction = mode1.predict(order1[['CO(GT)']])

print(prediction[:5])
print(target[:5])

plt.figure(figsize=(18,6))
plt.title('线性回归预测趋势图')
plt.plot(prediction[:200])
plt.show()
plt.figure(figsize=(18,6))
plt.title('原数据趋势图')
plt.plot(range(200),order1['CO(GT)'][:200])



#data = order1[['CO(GT)']]
#target = order1['Date']
#from sklearn.model_selection import train_test_split
#data_train,data_test,\
#target_train,target_test=\
#train_test_split(data,target,\
#                 test_size=0.2,random_state=42)

#from sklearn.preprocessing import MinMaxScaler
#Scaler = MinMaxScaler().fit(data_train)
#co_trainScaler = Scaler.transform(data_train)
#co_testScaler = Scaler.transform(data_test)

#from sklearn.cluster import KMeans
#kmeans = KMeans(n_clusters = 3,
#               random_state = 123).fit(data_train)
#print(kmeans)

#result = kmeans.predict(data_test)
#print('结果：',result[0])
