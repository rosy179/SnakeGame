import os
import time
import pygame
import random

# ================================== CẤU HÌNH ==================================
pygame.init()

# Màu sắc
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Kích thước cửa sổ
dis_width = 600
dis_height = 400

# Đường dẫn icon
PATH_DIRECTORY = os.path.dirname(__file__)
PATH_IMAGES = os.path.join(PATH_DIRECTORY, 'images')

# Thông số rắn
snake_block = 10
snake_speed = 15

# Khởi tạo
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
pygame.display.set_icon(pygame.image.load(os.path.join(PATH_IMAGES, 'icon_game.png')))
clock = pygame.time.Clock()

