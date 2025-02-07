
import pygame
import sys


pygame.init()


screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dota 3 ")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


hero1_width, hero1_height = 50, 50
hero1_x, hero1_y = 200, 200
hero1_speed = 10
hero1_color = RED


hero2_width, hero2_height = 50, 50
hero2_x, hero2_y = 500, 250
hero2_speed = 10
hero2_color = GREEN


running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hero1_x > 0:
        hero1_x -= hero1_speed
    if keys[pygame.K_RIGHT] and hero1_x < screen_width - hero1_width:
        hero1_x += hero1_speed
    if keys[pygame.K_UP] and hero1_y > 0:
        hero1_y -= hero1_speed
    if keys[pygame.K_DOWN] and hero1_y < screen_height - hero1_height:
        hero1_y += hero1_speed


    if keys[pygame.K_a] and hero2_x > 0:
        hero2_x -= hero2_speed
    if keys[pygame.K_d] and hero2_x < screen_width - hero2_width:
        hero2_x += hero2_speed
    if keys[pygame.K_w] and hero2_y > 0:
        hero2_y -= hero2_speed
    if keys[pygame.K_s] and hero2_y < screen_height - hero2_height:
        hero2_y += hero2_speed


    screen.fill(BLACK)


    pygame.draw.rect(screen, hero1_color, (hero1_x, hero1_y, hero1_width, hero1_height))
    pygame.draw.rect(screen, hero2_color, (hero2_x, hero2_y, hero2_width, hero2_height))


    pygame.display.flip()


pygame.quit()


