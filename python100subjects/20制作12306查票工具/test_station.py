import requests

station_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9242'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
}

resp = requests.get(url=station_url,headers=heads)
s_data = resp.text[resp.text.find('='):-1]
s_data = s_data.split('|')
num = len(s_data)//5
station_name={}
for i in range(num):
    station_name[(s_data[1+i*5])]=(s_data[2+i*5])
print(station_name)
#print(resp.text)
