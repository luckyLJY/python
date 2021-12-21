'''
Version:1.2
存储该游戏的所有设置
1.游戏初始化设置
    屏幕宽度、屏幕高度、背景颜色
'''
class Settings():

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)