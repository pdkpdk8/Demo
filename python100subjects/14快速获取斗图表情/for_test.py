import requests
from lxml import etree
from urllib.request import urlretrieve

list_url = 'https://www.fabiaoqing.com/biaoqing/lists/page/2.html'

#同时获取200页的表情包，可以使用for循环拼写道url上，，可以将下面的封装成一个方法

heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
resp = requests.get(url=list_url,headers=heads)
#print(resp.text)
e = etree.HTML(resp.text)

items = e.xpath('//div[@class="tagbqppdiv"]/a/img/@data-original')
#print(items)
names = e.xpath('//div[@class="tagbqppdiv"]/a/img/@title')

for item,name in zip(items,names):
    #print(f'图片名{item} 地址：{name} \n')
    end = item.split('.')[-1]
    new_name = f'14快速获取斗图表情/斗图/{name}.{end}'.replace('?','')
    urlretrieve(item,new_name)