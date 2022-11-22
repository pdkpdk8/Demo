from gevent import monkey
monkey.patch_all()
from time import sleep,time
import gevent #引入协程的模块

def fun1(name):
    print(f'{name}:我要买包！！')
   # gevent.sleep(2) #模拟IO
    sleep(2) #加上最上面写的两句话-补丁，就可以识别gevent
    print(f'{name}:我要学编程！！')

def fun2(name):
    print(f'{name}:买买买！！！')
    #gevent.sleep(2) #模拟IO
    sleep(2)
    print(f'{name}:一定去学习！！')



if __name__ == "__main__":
    start = time()
    # fun1('吕布')
    # fun2('貂蝉')
    g1 = gevent.spawn(fun1,"貂蝉") #调用 启动协程任务
    g2 = gevent.spawn(fun2,"吕布")
    gevent.joinall([g1,g2]) #等待所有任务完成
    end = time()
    print(end-start)