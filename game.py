# 導入所需模組
import pygame
import time
import random

# 初始化pygame
pygame.init()

# 定義顏色
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 定義遊戲視窗大小
window_width = 800
window_height = 600

# 創建遊戲視窗
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('貪食蛇遊戲')

# 定義時鐘
clock = pygame.time.Clock()

# 定義蛇的大小和速度
snake_block = 20
snake_speed = 15

# 定義字體樣式
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# 顯示分數的函數
def display_score(score):
    score_text = score_font.render("Score: " + str(score), True, white)
    game_window.blit(score_text, [0, 0])

# 繪製蛇的函數
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, green, [block[0], block[1], snake_block, snake_block])

# 顯示訊息的函數
def display_message(msg, color):
    msg_text = font_style.render(msg, True, color)
    game_window.blit(msg_text, [window_width / 6, window_height / 3])

# 主遊戲循環
def game_loop():
    game_over = False
    game_close = False

    # 蛇的初始位置
    snake_head = [window_width / 2, window_height / 2]
    snake_body = [[window_width / 2, window_height / 2]]
    snake_length = 1

    # 食物的初始位置
    food_position = [random.randrange(1, (window_width // snake_block)) * snake_block,
                     random.randrange(1, (window_height // snake_block)) * snake_block]
    food_spawn = True

    # 初始移動方向
    direction = 'RIGHT'
    change_direction = direction

    while not game_over:

        while game_close:
            game_window.fill(black)
            display_message("Game Over! Press Q to Quit or C to Play Again", red)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_direction = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_direction = 'RIGHT'
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_direction = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_direction = 'DOWN'

        # 更新蛇頭位置
        direction = change_direction
        if direction == 'LEFT':
            snake_head[0] -= snake_block
        if direction == 'RIGHT':
            snake_head[0] += snake_block
        if direction == 'UP':
            snake_head[1] -= snake_block
        if direction == 'DOWN':
            snake_head[1] += snake_block

        # 檢查是否撞牆或撞到自己
        if (snake_head[0] < 0 or snake_head[0] >= window_width or
            snake_head[1] < 0 or snake_head[1] >= window_height or
            snake_head in snake_body[:-1]):
            game_close = True

        # 檢查是否吃到食物
        snake_body.insert(0, list(snake_head))
        if snake_head[0] == food_position[0] and snake_head[1] == food_position[1]:
            food_spawn = False
            snake_length += 1
        else:
            snake_body.pop()

        if not food_spawn:
            food_position = [random.randrange(1, (window_width // snake_block)) * snake_block,
                             random.randrange(1, (window_height // snake_block)) * snake_block]
            food_spawn = True

        # 更新遊戲視窗
        game_window.fill(black)
        draw_snake(snake_block, snake_body)
        pygame.draw.rect(game_window, red, [food_position[0], food_position[1], snake_block, snake_block])
        display_score(snake_length - 1)
        pygame.display.update()

        # 控制遊戲速度
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# 啟動遊戲
game_loop()