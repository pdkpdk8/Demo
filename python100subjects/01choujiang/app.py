##去浏览器中登录网址"http://127.0.0.1:5000/index"
from ctypes import HRESULT
from flask import Flask,render_template
from random import randint

app = Flask(__name__)

hero = [
'诡术妖姬','猩红收割','远古恐惧','正义天使','无极剑圣','牛头酋长','符文法师','亡灵战神',
'战争女神','众星之子','迅捷斥候','麦林炮手','祖安怒兽','雪原双子','赏金猎人','寒冰射手'
]

@app.route('/index')

def index():
    return render_template('index.html',hero1 = hero)

@app.route('/choujiang')
def choujiang():
    num = randint(0,len(hero)-1)
    return render_template('index.html',hero1 = hero,h = hero[num])

#不用频繁的重启应用
app.run(debug=True)