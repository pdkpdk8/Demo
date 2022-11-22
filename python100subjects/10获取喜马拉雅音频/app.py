import requests
#获取集数音频ID的连接
url_list = 'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=31527949&pageNum=1'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
url_list_resp = requests.get(url_list,headers=heads)
print([tracks.get('trackId') for tracks in url_list_resp.json().get('data').get('tracks')])
track_list = [(tracks.get('trackId'),tracks.get('title')) for tracks in url_list_resp.json().get('data').get('tracks')]
#获取音频地址的连接
for id,name in track_list:
    audio_src = f'https://www.ximalaya.com/revision/play/v1/audio?id={id}&ptype=1' 
    src = requests.get(audio_src,headers=heads)
    #print(src.json().get('data').get('src'))
    audio_url = src.json().get('data').get('src')


# url = 'https://aod.cos.tx.xmcdn.com/group76/M04/3A/23/wKgO1F5rs6WwmcK4AMd2hEEzuYU640.m4a'

    resp = requests.get(url=audio_url,headers=heads)
    print(f'正在保存{name}音频')
# #保存文件w写文件b字节流
    with open(f'./10获取喜马拉雅音频/{name}.mp3','wb') as f:
        #resp.text 文本  resp.content 内容  resp.json() json格式的字符串
        f.write(resp.content)