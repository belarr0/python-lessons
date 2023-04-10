import pygame
from pygame.constants import QUIT

pygame.init()
screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE = 0, 0, 255
GREEN = 0, 255, 0
RED = 255, 0, 0

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True
while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)

    if ball_rect.bottom >= height:
        ball_speed[1] = -ball_speed[1] #1=y
        ball.fill(RED)

    if ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]  #1=y
        ball.fill(BLUE)

    if ball_rect.right >= width:
        ball_speed[0] = -ball_speed[0] #0=x
        ball.fill(GREEN)

    if ball_rect.left <= 0:
        ball_speed[0] = -ball_speed[0]  #0=x
        ball.fill(WHITE)

    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)


    #main_surface.fill((155, 155, 155))
    pygame.display.flip()
