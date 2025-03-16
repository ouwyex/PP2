import pygame
import math
import datetime

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mickey Clock")

mickey = pygame.image.load("mickeyclock.jpeg")
mickey = pygame.transform.scale(mickey, (400, 400))

def rotate_image(image, angle):
    return pygame.transform.rotate(image, angle)

def draw_clock():
    screen.fill((255, 255, 255))
    screen.blit(mickey, (0, 0))

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -6 * minutes
    second_angle = -6 * seconds

    minute_hand = pygame.Surface((20, 200), pygame.SRCALPHA)
    pygame.draw.line(minute_hand, (0, 0, 0), (10, 10), (10, 200), 5)
    minute_hand = rotate_image(minute_hand, minute_angle)
    screen.blit(minute_hand, (200 - minute_hand.get_width() // 2, 200 - minute_hand.get_height() // 2))

    second_hand = pygame.Surface((10, 200), pygame.SRCALPHA)
    pygame.draw.line(second_hand, (255, 0, 0), (5, 5), (5, 200), 3)
    second_hand = rotate_image(second_hand, second_angle)
    screen.blit(second_hand, (200 - second_hand.get_width() // 2, 200 - second_hand.get_height() // 2))

    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_clock()
    pygame.time.delay(1000)

pygame.quit()

#task2

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

pygame.mixer.init()
pygame.mixer.music.load("sample.mp3")  # Replace with your music file

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    # Implement logic to load and play the next track
    pass

def previous_track():
    # Implement logic to load and play the previous track
    pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
            elif event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()

    pygame.display.flip()

pygame.quit()

#task3

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Move the Ball")

ball_radius = 25
ball_x = 200
ball_y = 150

def draw_ball():
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ball_y - 20 >= ball_radius:
                    ball_y -= 20
            elif event.key == pygame.K_DOWN:
                if ball_y + 20 <= 300 - ball_radius:
                    ball_y += 20
            elif event.key == pygame.K_LEFT:
                if ball_x - 20 >= ball_radius:
                    ball_x -= 20
            elif event.key == pygame.K_RIGHT:
                if ball_x + 20 <= 400 - ball_radius:
                    ball_x += 20

    draw_ball()

pygame.quit()