from player import Player, vision_3d
from field import Field
import pygame

clock = pygame.time.Clock()
size = width, height = 1150, 700
screen = pygame.display.set_mode(size)

player = Player(screen, x=220, y=200)
field = Field()
field.field_generation()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.motion(field.mass)

    screen.fill((0, 0, 0))
    vision_3d(screen, player.angle, player.x, player.y, field.mass)
    pygame.display.flip()
    clock.tick(60)
