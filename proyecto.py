
import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_speed = 15

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, CELL_SIZE, CELL_SIZE])

def message(msg, color):
    font = pygame.font.SysFont(None, 50)
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - CELL_SIZE) / 20.0) * 20.0
    foody = round(random.randrange(0, HEIGHT - CELL_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            screen.fill(BLACK)
            message("¡Perdiste! Presiona C para continuar o Q para salir", RED)
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
                    x1_change = -CELL_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = CELL_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -CELL_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = CELL_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, CELL_SIZE, CELL_SIZE])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - CELL_SIZE) / 20.0) * 20.0
            foody = round(random.randrange(0, HEIGHT - CELL_SIZE) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

if __name__ == "__main__":
    gameLoop()