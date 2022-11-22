from time import sleep

def fun1():
    for i in range(6):
        print('111111111111')
        yield  #生成器

def fun2():
    g = fun1()
    next(g)
    for i in range(5):
        print('222222222222')
        next(g)
        sleep(1)

if __name__ == "__main__":
    fun2()