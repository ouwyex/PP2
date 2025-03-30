import pygame
import random

GRID_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
INITIAL_SPEED = 10

class Food:
    def __init__(self, snake_body, walls):
        while True:
            x = random.randint(1, GRID_WIDTH-2)
            y = random.randint(1, GRID_HEIGHT-2)
            self.position = (x * GRID_SIZE, y * GRID_SIZE)
            self.weight = random.choice([1, 2, 3])
            self.max_timer = 300 // self.weight
            self.timer = self.max_timer
            self.color = (0, 255, 0) if self.weight == 1 else (0, 200, 0) if self.weight == 2 else (0, 150, 0)
            if self.position not in snake_body and self.position not in walls:
                break

class SnakeGame:
    def __init__(self):
        self.snake_body = [(GRID_WIDTH//2 * GRID_SIZE, GRID_HEIGHT//2 * GRID_SIZE)]
        self.walls = self._generate_walls()
        self.foods = []
        self.score = 0
        self.level = 1
        self.speed = INITIAL_SPEED
        self.direction = (1, 0)
        self.last_update = 0

    def _generate_walls(self):
        walls = []
        for x in range(GRID_WIDTH):
            walls.append((x * GRID_SIZE, 0))
            walls.append((x * GRID_SIZE, (GRID_HEIGHT-1) * GRID_SIZE))
        for y in range(GRID_HEIGHT):
            walls.append((0, y * GRID_SIZE))
            walls.append(((GRID_WIDTH-1) * GRID_SIZE, y * GRID_SIZE))
        return walls

    def update(self, current_time):
        if current_time - self.last_update < 1000 // self.speed:
            return False

        self.last_update = current_time
        
        for food in self.foods[:]:
            food.timer -= 1
            if food.timer <= 0:
                self.foods.remove(food)
        
        if random.randint(1, 50) == 1 and len(self.foods) < 3:
            self.foods.append(Food(self.snake_body, self.walls))
        
        head_x, head_y = self.snake_body[0]
        dir_x, dir_y = self.direction
        new_head = (
            (head_x + dir_x * GRID_SIZE) % (GRID_WIDTH * GRID_SIZE),
            (head_y + dir_y * GRID_SIZE) % (GRID_HEIGHT * GRID_SIZE)
        )
        
        if new_head in self.snake_body or new_head in self.walls:
            return True
        
        self.snake_body.insert(0, new_head)
        
        for food in self.foods[:]:
            if new_head == food.position:
                self.foods.remove(food)
                for _ in range(food.weight):
                    self.snake_body.append(self.snake_body[-1])
                self.score += food.weight * self.level
                if len(self.snake_body) % (3 + self.level) == 0:
                    self.level += 1
                    self.speed = min(INITIAL_SPEED + self.level * 1, 20)
                break
        else:
            self.snake_body.pop()
        
        return False