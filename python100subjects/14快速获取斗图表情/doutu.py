import requests
from lxml import etree
from urllib.request import urlretrieve
from threading import Thread  #创建线程
from queue import Queue


#同时获取200页的表情包，可以使用for循环拼写道url上，，可以将下面的封装成一个方法
def get_page():
    while not queue.empty():
        #print(url)
        heads = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
        }
        #获取一个url
        url = queue.get()

        resp = requests.get(url,headers=heads)
        #print(resp.text)
        e = etree.HTML(resp.text)

        items = e.xpath('//div[@class="tagbqppdiv"]/a/img/@data-original')
        #print(items)
        names = e.xpath('//div[@class="tagbqppdiv"]/a/img/@title')

        for item,name in zip(items,names):
            #print(f'图片名{item} 地址：{name} \n')
            end = item.split('.')[-1]
            new_name = f'14快速获取斗图表情/斗图/{name}.{end}'.replace('?','')
            print(f'正在下载{new_name}')
            urlretrieve(item,new_name)

if __name__ == "__main__":
    queue = Queue()

    for i in range(1,10):
        #print(f'正在获取第{i}页表情包')
        list_url = f'https://www.fabiaoqing.com/biaoqing/lists/page/{i}.html'
        #get_page(list_url)
        queue.put(list_url)
    
    for j in range(3):
        #创建线程
        t = Thread(target=get_page)
        #开启线程
        t.start()

    