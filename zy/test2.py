
import pandas as pd
dff = pd.read_excel('cr.xlsx') 
dff1=dff.iloc[:5]
dff2=dff1.sum(axis=0)
dff2=dff2[1:]
print("前五企业行业集中度为：")
print(dff2)
dff3=dff.iloc[:10]
dff4=dff3.sum(axis=0)
dff4=dff4[1:]
print("前十企业行业集中度为：")
print(dff4)
import  matplotlib.pyplot as plt 
plt.rcParams['font.sans-serif'] = 'SimHei'  
plt.rcParams['axes.unicode_minus'] = False 
dff5=dff2.index.values
x=dff5
dff2=dff2.values
dff4=dff4.values           		
y1 = dff2   
y2 = dff4
plt.plot(x,y1,'rs-',x,y2, 'go--')
plt.plot(x, y1, label='cr5年变化')        	
plt.plot(x, y2, label='cr10年变化')  
plt.xlabel('年度', fontsize=14)        		
plt.ylabel('营业收入', fontsize=14)        		
plt.title('产业集中度每年变化折线图', fontsize=18)  		
plt.legend()                       			
plt.show()   