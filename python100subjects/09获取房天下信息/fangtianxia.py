import requests
from lxml import etree

url = 'https://hz.newhouse.fang.com/house/s/binjiang/'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
resp = requests.get(url=url,headers=heads)
resp.encoding = 'utf-8'
#print(resp.text)
e= etree.HTML(resp.text)

names =[n.strip() for n in e.xpath('//div[@class="nlcd_name"]/a/text()')]
#print(names)
addres = e.xpath('//div[@class="address"]/a/@title')
prices = [d.xpath('string(.)').strip() for d in e.xpath('//div[@class="nhouse_price"]')]

# with open('./09获取房天下信息/fangtianxia.xlsx','w',encoding='utf-8') as f:
#     for n,a,p in zip(names,addres,prices):
#         f.write(f'小区名：{n} 地址：{a} 价格：{p}\n')
for n,a,p in zip(names,addres,prices):
    print(f'小区名：{n} 地址：{a} 价格：{p}\n')