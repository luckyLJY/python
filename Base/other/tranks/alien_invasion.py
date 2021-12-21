'''
Version:1.0
    1.导入sys、pygame
    2.使用pygame.init初始haul屏幕
    3.使用pygame.display.set_mode()设置屏幕大小，并获得屏幕对象
    4.使用pygame.display.set_caption()设置屏幕主题
    5.游戏循环
        5.1 监控键盘和鼠标事件：pygame.event.get()
        5.2 获取时间类型为event.type==pygame.QUIT时退出sys.exit()
        5.3 让屏幕可见:pygame.display.flip()
Version:1.1
    1.设置背景色：bg_color=(230,230,230)
    2. 每次循环时重绘屏幕：屏幕对象.fill(bg_color)
Version:1.2
    使用Settings类替换屏幕的宽度、高度、背景色的设置
'''
import sys
import pygame
from settings import Settings

def run_game():
    #初始化游戏并创建屏幕对象
    pygame.init()

    #screen = pygame.display.set_mode((1200,800))
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
   # bg_color = (230, 230, 230)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环重回屏幕
        screen.fill(ai_settings.bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()