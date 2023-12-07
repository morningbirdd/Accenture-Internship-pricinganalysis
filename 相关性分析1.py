import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 加载数据集
df = pd.read_csv(r'D:\Desktop\个人\实习\埃森哲\定价分析\定价分析数据预处理.csv')

#定义数值型变量的列表
numeric_vars = [ 'wheelbase', 'carlength', 'carwidth', 'carheight', 
                'curbweight', 'enginesize','boreratio', 'stroke', 
                'compressionratio',  'horsepower', 'peakrpm', 'citympg', 'highwaympg']

# 为每个数值型变量绘制一个散点图
for var in numeric_vars:
    plt.figure(figsize=(6, 4)) 
    plt.scatter(df[var], df['price'])  
    plt.title(f'{var} vs price') 
    plt.xlabel(var)  
    plt.ylabel('price') 
#在绘制散点图的同时绘制每个变量的回归线和置信区间以及斜率的表示
sns.pairplot(df, x_vars=numeric_vars, y_vars='price', height=7, aspect=0.8, kind='reg')
plt.show()