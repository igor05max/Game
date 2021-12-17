from player import Player
from field import Field
import pygame

clock = pygame.time.Clock()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)

player = Player()
field = Field()
field.field_generation()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.motion(field.mass)

    screen.fill((0, 0, 0))
    field.visualization(screen)
    player.display(screen)
    pygame.display.flip()
    clock.tick(25)
