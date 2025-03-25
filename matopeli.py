import pygame
import time
import random

# Pygame alustaminen
pygame.init()

# Värit
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Näytön koko
width = 600
height = 400

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matopeli")

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y])

def gameLoop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(black)
            message("Hävisit! Paina C jatkaaksesi tai Q poistuaksesi", red, width / 6, height / 3)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        display.fill(blue)
        pygame.draw.rect(display, green, [food_x, food_y, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake_list:
            pygame.draw.rect(display, white, [segment[0], segment[1], snake_block, snake_block])
        
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()