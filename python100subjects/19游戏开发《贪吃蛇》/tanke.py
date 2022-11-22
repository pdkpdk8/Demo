import pygame


def show_text(surface_handle, pos, text, color, font_size = 20, font_bold = False, font_italic = False):
    cur_font = pygame.font.SysFont("华文宋体", font_size)
    cur_font.set_bold(font_bold)
    cur_font.set_italic(font_italic)
    text_message = cur_font.render(text, 1, color)
    surface_handle.blit(text_message, pos)


def tank_play():
    pygame.init()
    tank_image = pygame.image.load(r"./images/tank.png")
    tank_rect = tank_image.get_rect()
    back_image = pygame.image.load(r"./images/background2.jpg")
    back_rect = back_image.get_rect()
    screen = pygame.display.set_mode(back_rect.size)
    pygame.display.set_caption("用户方向键控制坦克移动")

    tank_rect.center = back_rect.center
    offset = 2                            
    fps_clock = pygame.time.Clock()
    while True:
        fps_clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            tank_rect.x += offset
        if keys_pressed[pygame.K_LEFT]:
            tank_rect.x -= offset
        if keys_pressed[pygame.K_UP]:
            tank_rect.y -= offset
        if keys_pressed[pygame.K_DOWN]:
            tank_rect.y += offset
        tank_rect.clamp_ip(back_rect)
        screen.blit(back_image, back_rect)
        screen.blit(tank_image, tank_rect)

        text = "坦克大战"
        show_text(screen, (20, 220), text, (255, 0, 0))
        text = f"坦克位置：（{tank_rect.x}，{tank_rect.y}）"
        show_text(screen, (20, 250), text, (0, 255, 255))
        pygame.display.update()


if __name__ == '__main__':
    tank_play()
    
