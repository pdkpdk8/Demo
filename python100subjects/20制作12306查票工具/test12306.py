'''
3车次
4车起始
6查询起始点
5车终点
7查询车终点
8出发时间
9到达时间
10历时
32商务特等
31一等座
30二等座二等包厢
21高级软座
23软卧一等卧动卧
28硬卧二等卧
27软座？
29硬座
26无座
'''
import requests
import sys

print('请输入出发地、目的地、时间格式为xxxx-xx-xx\，以空格隔开')
start_time = sys.argv[3]
begin_addr = sys.argv[1]
end_addr = sys.argv[2]

# start_time = '2022-11-20'
# begin_addr = '北京'
# end_addr = '深圳'

#获取城市信息
station_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9242'
station_heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
}

city_resp = requests.get(url=station_url,headers=station_heads)
s_data = city_resp.text[city_resp.text.find('='):-1]
s_data = s_data.split('|')
num = len(s_data)//5
station_name={}
station_name2={}
for i in range(num):
    station_name[(s_data[1+i*5])]=(s_data[2+i*5])
    station_name2[(s_data[2+i*5])]=(s_data[1+i*5])
#获取票信息
ba = station_name.get(begin_addr)
ea = station_name.get(end_addr)
# start_time = ''
url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={start_time}&leftTicketDTO.from_station={ba}&leftTicketDTO.to_station={ea}&purpose_codes=ADULT'
print(url)
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'Cookie': '_uab_collina=166878578321378299425324; JSESSIONID=B7F6471286158759B6694703CDE95BDC; BIGipServerotn=1944584458.24610.0000; BIGipServerpassport=786956554.50215.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1669080853902; RAIL_DEVICEID=D0AgrlXWfCCvaJ4Gqm0kMvJ5uYnICvXt9QVYvSOvMWWOIbU04DpyEMQuOTnktLwbM-VlgY6SIbU9SnVJQnCzW7beOKg2U8kzgQLsH75xtug1prsQuTciToNmFrjxii5yx-VQ9uvLQ3SECU1P3ZIzaI8lHkJkSl_t; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toDate=2022-11-18; _jc_save_wfdc_flag=dc; fo=qspft4etpccmk2vtYxINdYozsRmI-ptfnZ1jmOQdBE794Al-ScKJUqqQKWs8XACiW4p5No4wttfvjRwKL0Rs-3j1S2bNesuZnychNvsL_LUUvY4lBZpAkWzcjO3WqYbW6B_BEED7HdIr4hDuDR16ot9w1WdwbDp6QMC4UZBxo-5Y2fxv2kZ7jh8Aluo; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2022-11-30'
}
resp = requests.get(url=url,headers=heads)
#print(resp.text)
resp_data = resp.json().get('data').get('result')
for r in resp_data:
    data = [a for a in r.split('|')]
    if data[1]!='列车停运':
        print(f'{data[13]}--{data[8]}---{station_name2.get(data[6])}----{station_name2.get(data[7])}---{data[32]}----{data[31]}')