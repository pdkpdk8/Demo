#flask是为我们提供web服务的一个框架
from flask import Flask,render_template, request
from ctypes import HRESULT
import imp

app = Flask(__name__)

#告诉浏览器应该显示什么
@app.route('/login')
def login():
    return render_template('login.html')  #去浏览器中登录网址“http://127.0.0.1:5000/login”
@app.route('/index_login')
def index_login():
    uname = request.args.get('uname')
    #判断用户名是否正确
    #连接数据库判断
    return f"主页！！！欢迎登录{uname}"#return r,返回的是f函数的结果，return f 是返回函数名

app.run(debug=True)

