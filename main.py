from player import Player, vision
from random import choice
import pygame

pygame.init()
clock = pygame.time.Clock()
size = width, height = 1200, 800
screen = pygame.display.set_mode(size)

player = Player(screen)
running = True
textures = {
    '1': pygame.image.load('Texture/wall.jpg').convert(),
    '2': pygame.image.load('Texture/wall_.jpg').convert()
}

sky_ = choice([i for i in range(1, 9)])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.motion()

    screen.fill((0, 0, 0))
    sky = pygame.image.load(f'Sky/{sky_}.png').convert()
    screen.blit(sky, (0, 0))
    pygame.draw.rect(screen, (34, 139, 34), (0, 350, 1200, 600))
    vision(screen, player.x, player.y, player.angle, textures)
    pygame.display.flip()
    clock.tick(60)
