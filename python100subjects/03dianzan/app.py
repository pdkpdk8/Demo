#建立一个服务
from flask import Flask , render_template, request
#创建对象，面向对象
app = Flask(__name__)

data = [
    {'id':0,'name':'中秋','num':0},
    {'id':1,'name':'国庆','num':0},
    {'id':2,'name':'建军节','num':0}
]

@app.route('/index')
def index():
    return render_template('index.html',data = data)

@app.route('/dianzan')
def dianzan():
    id = request.args.get('id')
    print(f'想要给{id}点赞！')

    data[int(id)]['num']+=1
    return render_template('index.html',data = data)
    return '点赞成功'
    
app.run(debug=True)
