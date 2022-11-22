import requests
import os

list_url = 'https://v.6.cn/minivideo/getMiniVideoList.php?act=recommend&page=1&pagesize=25'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
list_resp = requests.get(url=list_url,headers=heads)

for user in list_resp.json().get('content').get('list'):
    #获取了视频地址和主播名字
    print(user.get('alias'),'-----',user.get('playurl'))
    m_url = user.get('playurl')
    uname = user.get('alias')
    #视频名字
    title = user.get('title')
    #发送请求获取视频
    m_resp = requests.get(url=m_url,headers=heads)
    with open(f'13获取主播小视频/movie/{title}.mp4','wb') as f:
        f.write(m_resp.content)


#print([list.get('playurl') for list in list_resp.json().get('content').get('list')])
video_list = [list.get('playurl') for list in list_resp.json().get('content').get('list')]
