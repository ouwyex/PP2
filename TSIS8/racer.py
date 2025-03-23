import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

player_car = pygame.image.load("car.png")
player_x = WIDTH // 2 - CAR_WIDTH // 2
player_y = HEIGHT - CAR_HEIGHT - 20
player_speed = 5

enemy_car = pygame.image.load("enemy_car.png")
enemy_x = random.randint(0, WIDTH - CAR_WIDTH)
enemy_y = -CAR_HEIGHT
enemy_speed = 5

score = 0
running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - CAR_WIDTH:
        player_x += player_speed
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -CAR_HEIGHT
        enemy_x = random.randint(0, WIDTH - CAR_WIDTH)
        score += 1
        enemy_speed += 0.5
    player_rect = pygame.Rect(player_x, player_y, CAR_WIDTH, CAR_HEIGHT)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, CAR_WIDTH, CAR_HEIGHT)
    if player_rect.colliderect(enemy_rect):
        print(f"Game Over! Score: {score}")
        running = False
    screen.blit(player_car, (player_x, player_y))
    screen.blit(enemy_car, (enemy_x, enemy_y))
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
