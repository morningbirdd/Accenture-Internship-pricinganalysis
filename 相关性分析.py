import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 加载数据集
df = pd.read_csv(r'D:\Desktop\个人\实习\埃森哲\定价分析\定价分析数据预处理.csv')

#定义数值型变量的列表
numeric_vars = ['wheelbase', 'carlength', 'carwidth', 'carheight', 
                'curbweight', 'enginesize', 'boreratio', 'stroke', 
                'compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg']

# 为每个数值型变量绘制一个散点图
for var in numeric_vars:
    plt.figure(figsize=(6, 4))  # 创建新的图形
    plt.scatter(df[var], df['price'])  # 绘制散点图
    
# 计算回归线的参数
    slope, intercept = np.polyfit(df[var], df['price'], 1)
    
# 绘制回归线
    plt.plot(df[var], slope*df[var] + intercept, color='r')
    
# 将斜率和截距添加到图像中
    plt.text(0.08, 0.95, f'y = {slope:.3f}x + {intercept:.3f}', transform=plt.gca().transAxes)
    
    #定义标签，绘制图像
    plt.title(f'{var.upper()} and PRICE') 
    plt.xlabel(var.upper()) 
    plt.ylabel('PRICE')  
    
sns.pairplot(df, x_vars=numeric_vars, y_vars='price', height=7, aspect=0.8, kind='reg')
plt.show() 
 
# 计算相关系数矩阵
corr_matrix = df[numeric_vars].corr()

# 打印相关系数矩阵
print(corr_matrix)