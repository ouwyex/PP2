import pygame
import time
import random

pygame.init()

WINDOW_X = 600
WINDOW_Y = 400
CELL_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

direction = 'RIGHT'
change_to = direction

score = 0
level = 1
speed = 10

def generate_food():
    while True:
        x = random.randint(0, (WINDOW_X // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (WINDOW_Y // CELL_SIZE) - 1) * CELL_SIZE
        if [x, y] not in snake_body:
            return [x, y]

food_pos = generate_food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= CELL_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += CELL_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= CELL_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += CELL_SIZE

    if snake_pos[0] < 0 or snake_pos[0] >= WINDOW_X or snake_pos[1] < 0 or snake_pos[1] >= WINDOW_Y:
        running = False

    if snake_pos in snake_body[1:]:
        running = False

    snake_body.insert(0, list(snake_pos))
    
    if snake_pos == food_pos:
        score += 1
        food_pos = generate_food()
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake_body.pop()

    game_window.fill(BLACK)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))
    
    pygame.draw.rect(game_window, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))
    
    font = pygame.font.SysFont('Arial', 20)
    score_text = font.render(f'Score: {score}  Level: {level}', True, WHITE)
    game_window.blit(score_text, [10, 10])
    
    pygame.display.flip()
    
    clock.tick(speed)

pygame.quit()
