import requests
from lxml import etree
from urllib.request import urlretrieve #下载图片
import re

list_url = 'https://search.baihe.com/search/getUserList?userIDs=155478110,231723074,161492995,151221664&jsonCallBack=jQuery18303814868185572171_1668312580348'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
    'Cookie': 'cookie_pcc=701%7C%7Cwww.baidu.com%7C%7C%7C%7Chttps%3A//www.baidu.com/link/url%3DI4Cg6KULgzGAN8QM-9gWD2B-51w5UO5ZU0wA3ruiWPG%26wd%3D%26eqid%3Dcbf78d8c0009794e00000004636fbbe2; function(val) {; accessID=20221113010607673959; Hm_lvt_5caa30e0c191a1c525d4a6487bf45a9d=1668267229; orderSource=10130301; lastLoginDate=Sun%20Nov%2013%202022%2012%3A02%3A20%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29; accessToken=BH1668312140323360202; AuthCookie=4BFFD62B611D896EB900274397DEE48894648D4CA037462DE24ADB5B22B21F38B60EBCEA45A0B128E9BB77602E041C1BF4D5EBCA9753DFFE9BF608CB30C4F468740A0A3FA06C20991BCFFDC7804A582899F4E1A464E2A5F3; AuthMsgCookie=597D34DDE14A948A12880B305A4D710303C5F100A85C6856ADF9160B339BC57450AD149EB3FE314A3AC81E1DA469354AC9C7888C3CEBE3A85F7D3E1CDA2F7241A4F529E4CC5AB59C30EEDFB09D5320181C0B2DB32FC82174; GCUserID=325453547; OnceLoginWEB=325453547; userID=325453547; spmUserID=325453547; tempID=1979933450; setIp=1; hasphoto=1; _fmdata=Ie%2BkzxEQKFcHRg30HXJcJlBTu3lBdXya%2BQO4otj9MhanAd06OWKGhHxY%2F99kYPeELxpmJeUOcWRGckhihJP5dNlUbBlH90wgoKvZT4RIWIw%3D; tgw_l7_route=7b6e8d312b52a5ee4107a1e3ee77ad54; AuthCheckStatusCookie=7FFC149B2C37B70EC7579A6B88506ECF14D1D3015978705726A127B203C4931405E9D878DCC812E7; Hm_lpvt_5caa30e0c191a1c525d4a6487bf45a9d=1668312581'
}
resp = requests.post(url=list_url,headers=heads)
#print(resp.text)

#正则表达式提取数据
nickname_list = re.findall(r'"nickname":"(.+?)"', resp.text)
age_list = re.findall(r'"age":(.+?),', resp.text)
Photo_list = re.findall(r'"headPhotoUrl":"(.+?)"', resp.text)
userid_list =  re.findall(r'"userID":(.+?),', resp.text)
#print(nickname_list)


#print(Photo_list)
with open('./16爬取百合网/user.txt','a',encoding='utf-8') as f:
    for p,u in zip(Photo_list,userid_list):
        #print("http:"+p.replace('\\',''))
        img_url = "http:"+p.replace('\\','')
        urlretrieve(img_url,'./16爬取百合网/img/{}.jpg'.format(u))
        f.write(f'userID:{u}\n')
