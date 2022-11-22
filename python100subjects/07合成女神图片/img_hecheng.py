#爬虫 - 获取女生图片
from cgitb import text
import requests
from lxml import etree

#地址
url = 'http://www.netbian.com/mei/index_66.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}

#发送请求
resp = requests.get(url=url,headers=headers)
resp.encoding = 'gbk'
#print(resp.text)

xp = etree.HTML(resp.text)
img_urls = xp.xpath('//div[@class="list"]/ul/li/a/img/@src')
img_namnes= xp.xpath('//div[@class="list"]/ul/li/a/img/@alt')

#保存数据
for u,n in zip(img_urls,img_namnes):
    print(f'正在下载 图片名：{n} 地址：{u}')
    #图片结果
    img_resp = requests.get(u,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'})
    with open(f'./07合成女神图片/img_file/{n}.jpg','wb') as f:
        f.write(img_resp.content)