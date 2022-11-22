#pip install pandas  
from csv import writer
from dataclasses import dataclass
import pandas as pd

#读入文件
data = pd.read_excel('./autoexcel/film.xlsx')
# print(data)
# print(data['type'])

#lambda 匿名函数，请求的时候会赋值给x；按/号分割；strip去空格
data['year']=data['type'].apply(lambda x:x.split('/')[0].strip())
data['city']=data['type'].apply(lambda x:x.split('/')[1].strip())
data['t']=data['type'].apply(lambda x:x.split('/')[2].strip())
#print(data['year'])

#创建新文件temp.xlsx
writer = pd.ExcelWriter('./autoexcel/temp.xlsx')

#将数据写入新文件，命名为xxx
# data.to_excel(writer,sheet_name='原始数据')
#关闭服务/文档
# writer.close()

#打印city列里面全是美国的数据
# print(data[data['city'] == '美国'])

#打印共有哪些国家
# print(data['city'].unique())

#遍历所有年份，分别将数据按照每个sheet年份写入新文件，根据年限分割
# for i in data['year'].unique():
#     data[data['year'] == i].to_excel(writer,sheet_name=i)

#抓取所有的类型，set是去重
type_list = set(z for i in data['t'] for z in i.split(' '))
print(type_list)
#上面两行相当于下面4行代码
# type_list = []
# for i in data['type']:
#     for z in i.split(' '):
#         type_list.append()

#根据类型分割,删选type里面包含科幻的内容
for ty in type_list:
    data[data['type'].str.contains(ty)].to_excel(writer,sheet_name=ty)



writer.close()