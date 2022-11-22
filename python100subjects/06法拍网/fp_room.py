#发送求情
from distutils.log import info
from email import header
import requests
import pandas as pd
#使用xpath工具模块
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'Referer': 'https://www1.rmfysszc.gov.cn/projects.shtml?dh=3&gpstate=1&wsbm_slt=1'
    }
from_data= {
'type': '1',
'name': ' ',
'area': '北京市',
'city': '北京市',
'city1': '==请选择==',
'city2': '==请选择==',
'xmxz': '0',
'state': '0',
'money': '',
'money1': '',
'number': '0',
'fid1': '',
'fid2':'' ,
'fid3': '',
'order': '0',
'page': '1',
'include': '0'
}
resp = requests.post('https://www1.rmfysszc.gov.cn/ProjectHandle.shtml',data=from_data,headers=headers)

#查看结果
#print(resp)

e = etree.HTML(resp.text)
#提取数据
#标题
titles = e.xpath('//div[@class="product"]/div[@class="p_img"]/a/@title')
#数据类型
infos = e.xpath('//div[@class="prod-guj"]/p[1]/text()')
#评估价
price1 = e.xpath('//div[@class="prod-guj"]/p[1]/span/text()')
price2 = e.xpath('//div[@class="prod-guj"]/p[2]/span/text()')
#处理数据
# print(titles)
# print(infos)
# print(price1)
# print(price2)

for t,i,p1,p2 in zip(titles,infos,price1,price2):
    if i == '起拍价':
        tp = p2
    else:
        tp = p1
    print(f'名称：{t} -----评估价：{tp}')