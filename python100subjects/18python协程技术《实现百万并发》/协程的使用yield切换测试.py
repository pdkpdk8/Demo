from time import sleep,time

def fun1():
    num = 0
    for i in range(10001):
        num += i 
        # yield  #生成器

def fun2():
    # g = fun1()
    # next(g)
    num = 0
    for i in range(10000):
        num += i 
        # next(g)
        # sleep(1)

if __name__ == "__main__":
    start = time()
    fun1()
    fun2()
    end = time()
    print(end-start)