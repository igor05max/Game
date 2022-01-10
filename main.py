from player import Player, vision_new, world
from sprite import Sprites, SpriteObject
from sprite_movements import movements, sprite_movements
from menu import Menu
# from land import land
from field import hall_4_, mass, field_
from transition import transition
from catch_a_lizun import catch_a_lizun, ball, lizun, number, set_caught_
from random import choice
import pygame
import sys


pygame.init()
clock = pygame.time.Clock()
size = width, height = 1200, 800
screen = pygame.display.set_mode(size)
TIMER = 30

running = True

screensaver = pygame.image.load(f'Menu/105.png').convert()
batten = pygame.image.load(f'Menu/106.png').convert()
t = False

music_menu = pygame.mixer.Sound('Music/music.ogg')
music_menu.play(-1)

clock_ = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:

            if 485 <= event.pos[0] <= 690 and 500 <= event.pos[1] <= 630:
                batten = pygame.image.load(f'Menu/107.png').convert()
                t = True

            else:
                batten = pygame.image.load(f'Menu/106.png').convert()
                t = False
        if event.type == pygame.MOUSEBUTTONDOWN and t:
            running = False

    screen.fill((100, 100, 100))

    screen.blit(screensaver, (0, 0))
    screen.blit(batten, (485, 500))

    pygame.display.flip()
    clock.tick(60)

# print(music_menu.get_volume())
menu = Menu(screen, music_menu)

player = Player(screen, mass=mass, mouse=True)
sprite = Sprites()
running = True
textures = {
    '1': pygame.image.load('Texture/5.png').convert(),
    '2': pygame.image.load('Texture/15.png').convert(),
    '3': pygame.image.load('Texture/030.png').convert(),
    '4': pygame.image.load('Texture/wall.jpg').convert()
}
textures_ = {
    '1': ['Texture/5.png', 'Texture/15.png'],
    '2': ['Texture/4.png', 'Texture/14.png'],
    '3': ['Texture/6.png', 'Texture/16.png'],
    '4': ['Texture/5.png', 'Texture/15.png']
}

# COLOR_ = land(textures_["1"][0])
COLOR_ = (69, 71, 48)
MYEVENTTYPE = pygame.USEREVENT + 1
sprite_movements(8, 12, sprite)
sky_ = choice([i for i in range(1, 9)])
pygame.time.set_timer(MYEVENTTYPE, 1500)
true = False
number_sprite = 1
hall = 1
sprite_true = True
sprite_true_2 = True
sprite_true_3 = True
hall_4 = False
clearing_hall_4 = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == MYEVENTTYPE:
            true = True

        menu.actions(event)
    if menu.active:
        screen.fill((0, 0, 0))
        menu.visualization()
        player.sens = menu.settings_sens
        player.mouse = menu.mouse
        player.mouse_vision = menu.mouse_vision
        player.keyboard = menu.keyboard
        pygame.display.flip()
        clock.tick(60)
        continue

    else:
        music_menu.stop()

    player.motion()
    screen.fill((0, 0, 0))
    sky = pygame.image.load(f'Sky/{sky_}.png').convert()
    screen.blit(sky, (0, 0))
    # pygame.draw.rect(screen, (34, 139, 34), (0, 350, 1200, 600))
    pygame.draw.rect(screen, COLOR_, (0, 350, 1200, 600))
    walls = vision_new(player.x, player.y, player.angle, textures, field_)
    world(screen, walls + [obj.object_locate(player, walls) for obj in sprite.list_of_objects])
    catch_a_lizun(player.x, player.y, sprite)
    lizun(screen, true)
    ball(screen, hall)
    true = False
    if transition(player.x, player.y, field_) and number() >= number_sprite and not hall_4:
        player.new_hall(150, 150)
        hall += 1
        textures["1"] = pygame.image.load(textures_[str(hall)][0]).convert()
        textures["2"] = pygame.image.load(textures_[str(hall)][1]).convert()
        sky_ = choice([i for i in range(1, 9)])
        sky = pygame.image.load(f'Sky/{sky_}.png').convert()
        screen.blit(sky, (0, 0))
        if hall == 2 and sprite_true:
            number_sprite = 4
            sprite_true = False
            set_caught_()
            sprite.list_of_objects = [
                SpriteObject(sprite.sprite_types['s'], True, (8.5, 12.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['s'], True, (5.5, 20.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['s'], True, (13.5, 2.5), 0.8, 0.8)
            ]
            sprite.sprite_types_pos = {
                's2': (8, 12),
                's3': (5, 20),
                's4': (13, 2)
            }
        if hall == 3 and sprite_true_2:
            sprite_true_2 = False
            number_sprite = 4
            set_caught_()
            sprite.list_of_objects = [
                SpriteObject(sprite.sprite_types['s'], True, (8.5, 12.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['s'], True, (5.5, 20.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['s'], True, (13.5, 2.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (2.5, 20.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (4.5, 11.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (2.5, 8.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (12.5, 16.5), 0.8, 0.8),
                SpriteObject(sprite.sprite_types['rot'], True, (5.5, 3.5), 0.8, 0.8)
            ]
            sprite.sprite_types_pos = {
                's5': (8, 12),
                's6': (5, 20),
                's7': (13, 2),
                'rot': (2, 20),
                'rot2': (4, 11),
                'rot3': (3, 8),
                'rot4': (12, 16),
                'rot5': (5, 3)
            }
        if hall == 4:
            sprite_true_3 = False
            hall_4 = True
    if hall_4:
        if clearing_hall_4:
            clearing_hall_4 = False
            set_caught_()
            sprite.list_of_objects = [
                SpriteObject(sprite.sprite_types['s'], True, (30.5, 30.5), 0.0, 0.0)
            ]
            sprite.sprite_types_pos = {
                's': (30, 30)
            }
            field_, mass = hall_4_()
            player.mass = mass

    pygame.display.flip()
    clock.tick(60)
