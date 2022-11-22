from nturl2path import url2pathname
from re import T
from sys import flags
from flask import Flask,render_template,request

#pip install requests 发送请求模块
#pip install lxml 解析数据模块
import requests
from lxml import etree

app = Flask(__name__) #创建一个可以支持web应用的对象



def get_mobile(phone):
    #发送请求的地址,到对方的服务器，服务器返回响应
    url = f'https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile'
    #伪装自己
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'}

    resp = requests.get(url,headers=header)
    resp.encoding = 'utf-8'


    e = etree.HTML(resp.text)
    datas = e.xpath('//tr/td[2]/span/text()')
    #解析响应
    print(datas)
    return datas

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_phone') #建立路由
def search_phone():
    phone = request.args.get('phone')
    data = get_mobile(phone)#返回的是列表
    return '<br/>'.join(data)

#get_mobile(17788889999)
app.run(debug=True)