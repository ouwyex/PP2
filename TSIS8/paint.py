import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint Application")
clock = pygame.time.Clock()

current_color = (255, 0, 0)
brush_size = 5
drawing = False
shape = 'brush'
start_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                end_pos = event.pos
                if shape == 'rectangle':
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, current_color, rect, brush_size)
                elif shape == 'circle':
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, current_color, start_pos, radius, brush_size)
            start_pos = None
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = (255, 0, 0)
            elif event.key == pygame.K_g:
                current_color = (0, 255, 0)
            elif event.key == pygame.K_b:
                current_color = (0, 0, 255)
            elif event.key == pygame.K_e:
                shape = 'eraser'
            elif event.key == pygame.K_p:
                shape = 'brush'
            elif event.key == pygame.K_c:
                shape = 'circle'
            elif event.key == pygame.K_t:
                shape = 'rectangle'
            elif event.key == pygame.K_UP:
                brush_size += 1
            elif event.key == pygame.K_DOWN:
                brush_size = max(1, brush_size - 1)
    if drawing and shape in ['brush', 'eraser']:
        mouse_pos = pygame.mouse.get_pos()
        if shape == 'eraser':
            pygame.draw.circle(screen, (255, 255, 255), mouse_pos, brush_size)
        else:
            pygame.draw.circle(screen, current_color, mouse_pos, brush_size)
    pygame.display.flip()
    clock.tick(60)
