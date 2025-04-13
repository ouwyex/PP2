import pygame
import sys
from db import get_user, get_last_score, save_score
from utils import serialize_game, deserialize_game, get_level_data

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

username = input("Enter your username: ")
user_id = get_user(username)

last = get_last_score(user_id)
level = last[0] if last else 1
score = last[1] if last else 0
state = deserialize_game(last[2]) if last and last[2] else None

level_data = get_level_data(level)
speed = level_data["speed"]
walls = level_data["walls"]

snake = state['snake'] if state else [(100, 100), (90, 100), (80, 100)]
direction = state['direction'] if state else (10, 0)
food = state['food'] if state else (300, 300)

paused = False
running = True

def draw_objects():
    screen.fill((0, 0, 0))
    for part in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*part, 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), (*food, 10, 10))
    for wall in walls:
        pygame.draw.rect(screen, (100, 100, 100), wall)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()

while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                state_data = {
                    'snake': snake,
                    'direction': direction,
                    'food': food
                }
                save_score(user_id, level, score, serialize_game(state_data))
                print("Game paused and saved.")
                paused = True
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_UP and direction != (0, 10):
                direction = (0, -10)
            elif event.key == pygame.K_DOWN and direction != (0, -10):
                direction = (0, 10)
            elif event.key == pygame.K_LEFT and direction != (10, 0):
                direction = (-10, 0)
            elif event.key == pygame.K_RIGHT and direction != (-10, 0):
                direction = (10, 0)

    if paused:
        continue

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if new_head in snake or new_head[0] < 0 or new_head[0] >= 600 or new_head[1] < 0 or new_head[1] >= 600:
        print("Game Over")
        running = False
        continue

    for wall in walls:
        wall_rect = pygame.Rect(*wall)
        if wall_rect.collidepoint(new_head):
            print("Hit the wall. Game Over.")
            running = False
            break

    snake.insert(0, new_head)
    if new_head == food:
        score += 10
        food = (10 * (score % 59), 10 * (score % 59))
        if score >= level * 30:
            level += 1
            level_data = get_level_data(level)
            speed = level_data["speed"]
            walls = level_data["walls"]
    else:
        snake.pop()

    draw_objects()

pygame.quit()
