# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:29:48 2019

@author: ZhaoYongqiang
"""

class Settings():
    """储存《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)
        
        #飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 0
        
        #子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3
        
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1