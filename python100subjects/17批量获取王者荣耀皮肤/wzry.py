import requests
from lxml import etree
import re
import os

heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}

all_heros_url = 'https://pvp.qq.com/web201605/js/herolist.json'
all_heros_resp = requests.get(url=all_heros_url,headers=heads)
print(all_heros_resp.json)
for h in all_heros_resp.json():
    ename = h.get('ename')
    cname = h.get('cname')

    if not os.path.exists(cname):
        os.makedirs(cname)

# all_heros_names = re.findall(r'"ename":(.+?),',all_heros_resp.text)
# print(all_heros_names)

    #for h in all_heros_names:
    hero_info_url = f'https://pvp.qq.com/web201605/herodetail/{ename}.shtml'
    hero_info_resp = requests.get(url=hero_info_url,headers=heads)
    hero_info_resp.encoding='gbk'
    e = etree.HTML(hero_info_resp.text)
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
    print([name[0:name.index('&')] for name in names.split('|')])
    names = [name[0:name.index('&')] for name in names.split('|')]#检测字符串中是否包含子字符串

    #for i in range(len(names)):
    for i,n in enumerate(names):#将names里面的值依次赋给n，i表示第几次
        hero_url = f'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i+1}.jpg'
        resp = requests.get(url=hero_url,headers=heads)

        with open(f'{cname}/{n}.jpg','wb') as f:
            f.write(resp.content)

