#Author Vodohleb04
import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
background_image = pygame.image.load('images/backgrounds/space.jpg')

while True:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)
