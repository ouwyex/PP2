import pygame
import random

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.weight = random.choice([1, 2, 3])
        self.color = (255, 215, 0) if self.weight == 1 else (255, 165, 0) if self.weight == 2 else (255, 69, 0)
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

enemy_speed = 5
score = 0

def game_loop():
    global enemy_speed, score
    coins = []
    
    while True:
        if random.randint(1, 100) < 3:
            coin_x = random.randint(50, SCREEN_WIDTH-50)
            coins.append(Coin(coin_x, 0))
        
        for coin in coins[:]:
            coin.y += 3
            coin.rect.y = coin.y
            if coin.y > SCREEN_HEIGHT:
                coins.remove(coin)
            if player_rect.colliderect(coin.rect):
                coins.remove(coin)
                score += coin.weight
                if score % 10 == 0:
                    enemy_speed += 0.5
        
        pygame.display.update()