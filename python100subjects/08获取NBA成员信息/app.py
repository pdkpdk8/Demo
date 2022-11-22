from lxml import etree
import requests

url = 'https://nba.hupu.com/stats/players'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}

resp = requests.get(url=url,headers=heads)
#print(resp.text)
#帮助我们处理XPATH
e = etree.HTML(resp.text)
numbers = e.xpath('//table[@class="players_table"]//tr//td[1]/text()')
del(numbers[0])
names = e.xpath('//table[@class="players_table"]//tr//td[2]/a/text()')
teams = e.xpath('//table[@class="players_table"]//tr//td[3]/a/text()')
scores = e.xpath('//table[@class="players_table"]//tr//td[4]/text()')
del(scores[0])

for u,n,t,s in zip(numbers,names,teams,scores):
    print(f'排名：{u} 球员：{n} 球队：{t} 分数：{s}')

with open('./08获取NBA成员信息/nba.text','w',encoding='utf-8') as f:
    for u,n,t,s in zip(numbers,names,teams,scores):
        f.write(f'排名：{u} 球员：{n} 球队：{t} 分数：{s}\n')