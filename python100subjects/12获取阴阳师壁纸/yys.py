import requests
from lxml import etree
import os

list_url = 'https://yys.163.com/media/picture.html'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
list_resp = requests.get(url=list_url,headers=heads)

e = etree.HTML(list_resp.text)

imgs1 = [url[:url.rindex('/')]+'/2732x2048.jpg' for url in e.xpath('//div[@class="tab-cont"][1]/div/div/img/@data-src')]
imgs2 = [url[:url.rindex('/')]+'/1080x1920.jpg' for url in e.xpath('//div[@class="tab-cont"][2]/div/div/img/@data-src')]
#print(imgs1)

if not os.path.exists('./12获取阴阳师壁纸/heng'):
    os.makedirs('./12获取阴阳师壁纸/heng')
if not os.path.exists('./12获取阴阳师壁纸/shu'):
    os.makedirs('./12获取阴阳师壁纸/shu')

for url in imgs1:
    resp = requests.get(url,headers=heads)
    #print(url)
    #print(url.rindex('20'))
# >>> 'https://yys.res.netease.com/pc/zt/20170731172708/data/picture/20221020/1/2732x2048.jpg'[78:] 
# '2048.jpg'
# >>> 'https://yys.res.netease.com/pc/zt/20170731172708/data/picture/20221020/1/2732x2048.jpg'.rindex('picture')
# 54
# >>> 'https://yys.res.netease.com/pc/zt/20170731172708/data/picture/20221020/1/2732x2048.jpg'[54:] 
# 'picture/20221020/1/2732x2048.jpg'
    file_name = url[url.rindex('picture'):url.rindex('/')].replace('/','_')+'.jpg'
    #print(url[url.rindex('picture'):url.rindex('/')])
    #print(file_name)
    #break
    print('正在保存：'+file_name+'壁纸')
    with open(f'12获取阴阳师壁纸/heng/{file_name}','wb') as f:
        f.write(resp.content)

for url in imgs2:
    resp = requests.get(url,headers=heads)
    print(url)
    print(url.rindex('20'))
# >>> 'https://yys.res.netease.com/pc/zt/20170731172708/data/picture/20221020/1/2732x2048.jpg'[78:] 
# '2048.jpg'
# >>> 'https://yys.res.netease.com/pc/zt/20170731172708/data/picture/20221020/1/2732x2048.jpg'.rindex('picture')
# 54
# >>> 'https://yys.res.netease.com/pc/zt/20170731172708/data/picture/20221020/1/2732x2048.jpg'[54:] 
# 'picture/20221020/1/2732x2048.jpg'
    file_name = url[url.rindex('picture'):url.rindex('/')].replace('/','_')+'.jpg'
    print(url[url.rindex('picture'):url.rindex('/')])
    print(file_name)
    #break
    print('正在保存：'+file_name+'壁纸')
    with open(f'12获取阴阳师壁纸/shu/{file_name}','wb') as f:
        f.write(resp.content)