import pygame
from time import sleep
import random
WIDTH = 600
HEIGHT = 600

class Snake:
    def __init__(self,screen): #蛇显示在screen，所以需要传参
        self.screen = screen
        #长度
        self.body = [] #方块组成的列表
        #方向,初始化向右走
        self.fx = pygame.K_RIGHT
        self.init_body()
    def init_body(self,length=5): #初始化身体，有长度=5
        left,top = (0,0)
        for i in range(5):
            if self.body:
                left,top = self.body[0].left,self.body[0].top
                node = pygame.Rect(left+20,top,20,20)
            else:
                node = pygame.Rect(0,0,20,20) #设置要绘画的正方形
            self.body.insert(0,node)
    def draw_snake(self):
        for  n in self.body:
            pygame.draw.rect(self.screen,(62,122,178),n,0)
    
    def del_node(self):
        self.body.pop()
    def add_node(self):
        if self.body:
            left,top = self.body[0].left,self.body[0].top
            if self.fx == pygame.K_RIGHT:
                left += 20
            elif self.fx == pygame.K_LEFT:
                left -= 20
            elif self.fx == pygame.K_UP:
                top -= 20
            else:
                top += 20
            node = pygame.Rect(left,top,20,20)
            self.body.insert(0,node)

    def move(self):
        self.del_node()
        self.add_node()
    def change(self,fx):
        LR = [pygame.K_LEFT,pygame.K_RIGHT]
        UD = [pygame.K_UP,pygame.K_DOWN]
        if fx in LR+UD:
            if fx in LR and self.fx in LR:
                return
            if fx in UD and self.fx in UD:
                return
            self.fx = fx
    def is_dead(self):
        if self.body[0].left not in range(WIDTH):
            return True
        if self.body[0].top not in range(HEIGHT):
            return True
        if self.body[0] in self.body[1:]:
            return True

class Food:
    def __init__(self):
        self.node = pygame.Rect(60,80,20,20)
        self.flag = False

    def set(self):
        all_x_point = range(20,WIDTH-20,20)
        all_y_point = range(20,HEIGHT-20,20)
        left = random.choice(all_x_point)
        top = random.choice(all_y_point)
        self.node = pygame.Rect(left,top,20,20)
        self.flag = False
    def reset(self):
        self.flag = True

def show_text(screen, pos, text, color, font_bold = False, font_size = 60, font_italic = False):
    # cur_font = pygame.font.SysFont('宋体', font_size)		# 获取系统字体
    cur_font = pygame.font.SysFont('幼圆', font_size)			 # 获取字体，并设置大小
    cur_font.set_bold(font_bold)							 # 设置是否加粗
    cur_font.set_italic(font_italic)						 # 设置是否斜体
    text_fmt = cur_font.render(text, 1, color)				 # 设置文本内容
    screen.blit(text_fmt, pos)	


def main():
    pygame.init() #初始化
    screen = pygame.display.set_mode([WIDTH,HEIGHT]) #创建窗口，输入长和宽
    clock = pygame.time.Clock()

    sk = Snake(screen)
    fd = Food()
    dead = False
    while True:
        for e in pygame.event.get(): #获取pygame里面的事件
            if e.type == pygame.QUIT:  #如果事件等于退出
                pygame.quit()  #关闭游戏，也可以用 sys.exit()
            if e.type == pygame.KEYDOWN:
                sk.change(e.key)
                if e.key == pygame.K_SPACE:
                    sk = Snake(screen)
                    fd = Food()
                    dead = False

        screen.fill((255,255,255)) #填充背景颜色

        #画蛇
        sk.draw_snake()
        if not dead:
            sk.move()
        
        #每移动一下就要判断是否死亡
        if sk.is_dead():
            #pygame.quit()
            show_text(screen,(140,160),'扑街了！',(202,92,85),True,100)
            show_text(screen,(180,320),'按 空格 重新开始！',(116,181,103),False,font_size=30)
            dead = True
        
        if fd.flag:
            fd.set()
        # #放食物
        # fd.set()
        pygame.draw.rect(screen,(231,175,95),fd.node,0)
        #吃食物
        if sk.body[0] == fd.node:
            sk.add_node()
            fd.reset()

        pygame.display.update() #更新显示
        #sleep(0.1)
        clock.tick(10)
if __name__ == "__main__":
    main()