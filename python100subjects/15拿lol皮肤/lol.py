import requests
import re #re是正则表达式
from time import sleep
import os #os是文件处理

heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}

all_heros_url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2780598'

all_heros_resp = requests.get(url=all_heros_url,headers=heads)
all_heros_names = re.findall(r'"alias":"(.+?)"',all_heros_resp.text)
#print(all_heros_names)

for n in range(len(all_heros_names)):

    sleep(1)
    n = f'https://game.gtimg.cn/images/lol/act/img/js/hero/{n}.js?ts=2780591'

    hero_info_js_resp = requests.get(url=n,headers=heads)
    hero_info_js = hero_info_js_resp.text

    #print(hero_info_js)
    hero_ids = re.findall(r'"skinId":"(\d+?)"',hero_info_js)
    #print(hero_ids)
    mainImg_ids = re.findall(r'"mainImg":"(.+?)"',hero_info_js)
    print(mainImg_ids)
    names = re.findall(r'"name":"(.+?)".+?"chrom',hero_info_js)
    print(names)

    for id,name,i in zip(hero_ids,names,all_heros_names):
            #print("http:"+p.replace('\\',''))
            img_url = f'https://game.gtimg.cn/images/lol/act/img/skin/big{id}.jpg'
            img_resp = requests.get(img_url,headers=heads)
            name = name.encode().decode('unicode_escape')
            if not os.path.exists(f'./15拿lol皮肤/img/{i}'):
                os.makedirs(f'./15拿lol皮肤/img/{i}')
            with open(f'./15拿lol皮肤/img/{i}/{name}.jpg','wb') as f:
                f.write(img_resp.content)
            sleep(2)