import pygame
import random
import sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

class PlayerCar:
    def __init__(self):
        self.image = pygame.Surface((50, 80))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT-100))
        self.speed = 5

class EnemyCar:
    def __init__(self):
        self.image = pygame.Surface((50, 80))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(random.randint(50, SCREEN_WIDTH-50), -100))
        self.speed = random.randint(3, 6)

class Coin:
    def __init__(self, x, y):
        self.weight = random.choice([1, 2, 3])
        self.color = (255, 215, 0) if self.weight == 1 else (255, 165, 0) if self.weight == 2 else (255, 69, 0)
        self.rect = pygame.Rect(x, y, 20, 20)

def main():
    player = PlayerCar()
    enemies = []
    coins = []
    score = 0
    enemy_speed = 5
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.rect.left > 0:
            player.rect.x -= player.speed
        if keys[pygame.K_RIGHT] and player.rect.right < SCREEN_WIDTH:
            player.rect.x += player.speed
        
        if random.randint(1, 100) < 3:
            coins.append(Coin(random.randint(50, SCREEN_WIDTH-50), -20))
        
        if random.randint(1, 100) < 2:
            enemies.append(EnemyCar())
        
        for coin in coins[:]:
            coin.rect.y += 3
            if coin.rect.colliderect(player.rect):
                coins.remove(coin)
                score += coin.weight
                if score % 10 == 0:
                    enemy_speed += 0.5
            elif coin.rect.top > SCREEN_HEIGHT:
                coins.remove(coin)
        
        for enemy in enemies[:]:
            enemy.rect.y += enemy_speed
            if enemy.rect.colliderect(player.rect):
                pygame.quit()
                sys.exit()
            elif enemy.rect.top > SCREEN_HEIGHT:
                enemies.remove(enemy)
        
        screen.fill((0, 0, 0))
        for coin in coins:
            pygame.draw.rect(screen, coin.color, coin.rect)
        for enemy in enemies:
            screen.blit(enemy.image, enemy.rect)
        screen.blit(player.image, player.rect)
        
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH-150, 20))
        
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()