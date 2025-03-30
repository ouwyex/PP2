import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

current_color = (0, 0, 0)
brush_size = 5
drawing = False
last_pos = None
current_shape = "free"
shapes = []

def draw_square(start, end):
    size = max(abs(end[0]-start[0]), abs(end[1]-start[1]))
    return pygame.Rect(start[0], start[1], size, size)

def draw_right_triangle(start, end):
    return [start, (start[0], end[1]), end]

def draw_equilateral_triangle(start, end):
    height = int(abs(end[1] - start[1]) * 0.866)
    return [start, (end[0], start[1]), ((start[0]+end[0])//2, start[1]-height)]

def draw_rhombus(start, end):
    center_x = (start[0] + end[0]) // 2
    center_y = (start[1] + end[1]) // 2
    width = abs(end[0] - start[0]) // 2
    height = abs(end[1] - start[1]) // 2
    return [
        (center_x, center_y - height),
        (center_x + width, center_y),
        (center_x, center_y + height),
        (center_x - width, center_y)
    ]

def main():
    global current_color, brush_size, drawing, last_pos, current_shape
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_shape = "free"
                elif event.key == pygame.K_2:
                    current_shape = "square"
                elif event.key == pygame.K_3:
                    current_shape = "right_triangle"
                elif event.key == pygame.K_4:
                    current_shape = "equilateral_triangle"
                elif event.key == pygame.K_5:
                    current_shape = "rhombus"
                elif event.key == pygame.K_c:
                    current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                elif event.key == pygame.K_PLUS:
                    brush_size += 1
                elif event.key == pygame.K_MINUS:
                    brush_size = max(1, brush_size - 1)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                last_pos = event.pos
                if current_shape != "free":
                    shapes.append((current_shape, last_pos, last_pos, current_color))
            
            if event.type == pygame.MOUSEMOTION and drawing:
                if current_shape == "free":
                    pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)
                    last_pos = event.pos
                else:
                    shapes[-1] = (shapes[-1][0], shapes[-1][1], event.pos, shapes[-1][3])
            
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
        
        screen.fill((255, 255, 255))
        
        for shape in shapes:
            if shape[0] == "square":
                pygame.draw.rect(screen, shape[3], draw_square(shape[1], shape[2]), brush_size)
            elif shape[0] == "right_triangle":
                pygame.draw.polygon(screen, shape[3], draw_right_triangle(shape[1], shape[2]), brush_size)
            elif shape[0] == "equilateral_triangle":
                pygame.draw.polygon(screen, shape[3], draw_equilateral_triangle(shape[1], shape[2]), brush_size)
            elif shape[0] == "rhombus":
                pygame.draw.polygon(screen, shape[3], draw_rhombus(shape[1], shape[2]), brush_size)
        
        pygame.display.update()

if __name__ == "__main__":
    main()