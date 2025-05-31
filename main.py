import time
import pygame
import random

from define import *

pygame.init()
pygame.mixer.init()


dis = pygame.display.set_mode((dis_width, dis_height))

#Đặt tên tiêu đề cho màn hình hiển thị trò chơi là "Snake game"
pygame.display.set_caption('Snake game')
pygame.display.set_icon(pygame.image.load(PATH_IMAGES + '/icon_game.png'))

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def draw_score(score):
    value = score_font.render(f"Score: {score}", True, yellow)
    dis.blit(value, [10, 10])

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block], border_radius=4)


def show_message_center(msg, color, size=30):
    font = pygame.font.SysFont("bahnschrift", size)
    mesg = font.render(msg, True, color)
    rect = mesg.get_rect(center=(dis_width / 2, dis_height / 2))
    dis.blit(mesg, rect)

def gameLooping_func():
    game_end = False
    game_Close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    #Tạo một tập hợp kiểu List chứa các thành phần của con rắn
    snake_list = []

    #Độ dài ban đầu của con rắn là 1
    length_of_snake = 1

    #Vị trí tọa độ (x, y) của đồ ăn trong trò chơi
    foodx = round(random.randrange(0, dis_width - snake_block) /10.0) *10.0
    foody = round(random.randrange(0, dis_height - snake_block) /10.0) *10.0

    dis_color = blue

    while not game_end:
        while game_Close:
            dis.fill(white)
            show_message_center("Game Over! Press C to Play Again or Q to Quit", red, size=24)
            draw_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_end = True
                        game_Close = False
                    elif event.key == pygame.K_c:
                        gameLooping_func()
                    if event.key == pygame.K_x:
                        pygame.quit()
                        quit()

    #Lấy ra các sự kiện xảy ra
        for event in pygame.event.get():
        #Nếu kiểu sự kiện là QUIT, thực hiện kết thúc trò chơi
            if event.type == pygame.QUIT:
                game_end = True
        #Nếu kiểu sự kiện là KEYDOWN (nhấn phím mũi tên xuống)
            if event.type == pygame.KEYDOWN:
            #Nếu phím nhấn xuống là phím mũi tên bên trái, thực hiện cập nhật đầu con rắn sang trái
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
            #Nếu phím nhấn xuống là phím mũi tên bên phải, thực hiện cập nhật đầu con rắn sang phải
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
            #Nếu phím nhấn xuống là phím mũi tên lên trên, thực hiện cập nhật đầu con rắn tiến lên trên
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
            #Nếu phím nhấn xuống là phím mũi tên xuống dưới, thực hiện cập nhật đầu con rắn tiến đi xuống
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

    #Kiểm tra xem vị trí (x, y) của đầu con rắn đã chạm vào ranh giới hiển thị màn hình trò chơi hay chưa
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_Close = True

    #Thực hiện cập nhật tọa độ cho đầu con rắn
        x1 += x1_change
        y1 += y1_change

    #Tô lại toàn bộ màn hình là màu xanh
        dis.fill(dis_color)

    #Thực hiện vẽ đồ ăn màu xanh lá lên trên màn hình với kích thước bằng kích thước của một ô vuông
    #biểu diễn cho 1 phần thân của con rắn.
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
    
    #Thực hiện thêm phần thân của con rắn vào danh sách
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)

    #Thực hiện cập nhật danh sách chứa các thành phần của con rắn để cập nhật vị trí của từng thành
    #phần (ô vuông) của con rắn. Nếu số ô vuông (biểu diễn cho con rắn), lớn hơn kích thước hiện tại
    #của con rắn (độ dài của con rắn), Length_of_snake, thực hiện xóa vị trí cũ của phần đầu con rắn.
        if len(snake_list) > length_of_snake:
            del snake_list[0] 

    #Kiểm tra từng bộ phận của con rắn có chạm vào phần đầu của con rắn hay không, nếu có, tức là
        #người chơi thua, thực hiện kết thúc trò chơi bằng cách đặt biến game_close = True.
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_Close = True   

        draw_snake(snake_list)
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
 
        clock.tick(snake_speed)

#Thoát trò chơi
    pygame.quit()
    quit()

gameLooping_func()