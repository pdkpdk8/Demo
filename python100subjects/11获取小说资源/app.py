#%%
import requests
from lxml import etree


url = 'https://www.qb5.tw/top/monthvisit/'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
resp = requests.get(url=url,headers=heads)
#print(resp.text)

e = etree.HTML(resp.text)
type = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[1]/text()')
names = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[2]/a/text()')
authors = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[3]/text()')
counts = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[5]/text()')
nums = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[6]/text()')

datas = []
for t,name,author,count,num in zip(type,names,authors,counts,nums):
    datas.append([t,name,author,count[:-1],num])
    #print(datas)
#%%
import pandas as pd
#分析
df = pd.DataFrame(datas,columns=['类型','书名','作者','字数','推荐'])

# data.to_excel(writer,)
# data.to_excel(writer,sheet_name='原始数据')
df
# %%
df.describe()
#%%
df.groupby('类型').count()
#%%
df.类型.hist()
#%%
import matplotlib
sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
#%%
df[df.类型=='玄幻魔法'].sort_values(by='推荐')
#%%
df['推荐']=df['推荐'].astype('int')
#%%









3