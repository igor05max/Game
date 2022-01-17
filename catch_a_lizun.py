from field import dist
from sprite_movements import sprite_movements
import pygame

pygame.init()

number_of_caught = 0
lizun_ = 0
set_caught = set()

music = pygame.mixer.Sound('Music/зел1.ogg')
music.stop()

music_minus = pygame.mixer.Sound('Music/кр1.ogg')
music_minus.stop()


def catch_a_lizun(x_player, y_player, sprite):
    global number_of_caught
    t = -1
    for lizun in sprite.sprite_types_pos:
        t += 1
        x_lizun, y_lizun = sprite.sprite_types_pos[lizun]
        if 's' in lizun:
            view = 's'
        else:
            view = 'rot'
        if dist(x_player, y_player, x_lizun * 100 + 50, y_lizun * 100 + 50) <= 132 \
                and lizun not in set_caught and view == 'rot':
            sprite_movements(1, 1, sprite, sprite_type=(lizun, t), cleaning=True, view=view)
            set_caught.add(lizun)
        elif dist(x_player, y_player, x_lizun * 100 + 50, y_lizun * 100 + 50) <= 80 \
                and lizun not in set_caught and view == 's':
            sprite_movements(1, 1, sprite, sprite_type=(lizun, t), cleaning=True, view=view)
            set_caught.add(lizun)
        else:
            continue
        if view == 'rot':
            number_of_caught -= 1
            music_minus.play()
        else:
            number_of_caught += 1
            music.play()


def ball(screen, hall):
    x = 7
    x2 = 4
    if hall == 1:
        x = x2 = 1
    if hall == 2:
        x2 = x = 4
    if hall == 4:
        x2 = 1
    font = pygame.font.Font(None, 100)
    text = font.render(f"/{x}", True, (50, 185, 50))
    text_number_of_caught = font.render(f"{number_of_caught}", True, (250, 100, 50))
    if number_of_caught >= x2:
        text_number_of_caught = font.render(f"{number_of_caught}", True, (50, 185, 50))
    text_x = 960
    text_y = 700
    screen.blit(text, (text_x, text_y))
    screen.blit(text_number_of_caught, (920, text_y))


def lizun(screen, true):
    global lizun_
    if number_of_caught and true:
        lizun_ += 1
        if lizun_ > 7:
            lizun_ = 1
        sky = pygame.image.load(f'Ball/{lizun_}.png').convert()
        screen.blit(sky, (900, 630))
    elif not number_of_caught:
        sky = pygame.image.load(f'Ball/8.png').convert()
        screen.blit(sky, (900, 630))
    else:
        sky = pygame.image.load(f'Ball/{lizun_}.png').convert()
        screen.blit(sky, (900, 630))


def number():
    return number_of_caught


def set_caught_():
    global set_caught
    set_caught = set()


def number_of_caught_new():
    global number_of_caught, lizun_
    number_of_caught = 0
    lizun_ = 0
    set_caught_()


def time_to_destroy_the_lizun_():
    global number_of_caught
    number_of_caught = max(number_of_caught - 1, 0)
