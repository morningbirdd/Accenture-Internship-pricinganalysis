import pandas as pd
import matplotlib.pyplot as plt

# 使用黑体
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False  

# 加载数据集
df = pd.read_csv(r'D:\Desktop\个人\实习\埃森哲\定价分析\定价参考.csv')

# 查看数据信息
print('原始数据信息：')
print(df.info())

# 查看含有缺失值的行
print('含有缺失值的行：')
print(df[df.isnull().any(axis=1)])

# 处理缺失值
df = df.dropna()

# 处理重复值
df = df.drop_duplicates()

# 查看处理后的数据信息
print('处理后的数据信息：')
print(df.info())

# 提取厂商名称
df['厂商名称'] = df['name'].apply(lambda x: x.split(' ')[0])

# 统计每个厂商的数量
manufacturer_counts = df['厂商名称'].value_counts()

# 打印统计结果
print(manufacturer_counts)

# 绘制条形图
manufacturer_counts.plot(kind='bar')
plt.xticks(fontsize=6)
plt.title('汽车厂商数量统计')
plt.xlabel('厂商名称')
plt.ylabel('数量')
plt.show()


#对厂商的分布绘制饼图
plt.figure(figsize=(20, 15))
manufacturer_counts.plot(kind='pie', autopct='%.2f%%')
plt.title('汽车厂商数量统计')
plt.show()

# 将处理后的数据保存
df.to_csv(r'D:\Desktop\个人\实习\埃森哲\定价分析\定价分析数据预处理.csv', index=False)
