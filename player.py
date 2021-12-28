from math import sin, cos, pi, tan
from field import *
from sys import exit
from pprint import pprint
import pygame


DIST = 300 / (2 * tan((pi / 3) / 2))


class Player:
    def __init__(self, screen, x=150, y=150, mouse=False, sens=0.005, mouse_vision=True):
        pygame.mouse.set_visible(mouse_vision)

        self.x, self.y = x, y
        self.angle = 0
        self.screen = screen
        self.mouse = mouse
        self.sens = sens

    def display(self, screen):  # отображение игрока
        pygame.draw.circle(screen, ((145, 230, 145)), (self.x, self.y), 8)
        pygame.draw.line(screen, ((120, 150, 200)), (self.x, self.y), (self.x + 1250 * cos(self.angle),
                                                                        self.y + 900 * sin(self.angle)))

    def motion(self):  # движение игрока
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            exit()
        if self.mouse:
            pygame.mouse.get_pos()
            difference = pygame.mouse.get_pos()[0] - 600
            pygame.mouse.set_pos((600, 400))
            self.angle += difference * self.sens

        if pygame.key.get_pressed()[pygame.K_LEFT]:  # влево от луча
            x = self.x + 4 * cos(self.angle - pi / 2)
            y = self.y + 4 * sin(self.angle - pi / 2)
            if (x // 100 * 100, y // 100 * 100) not in mass and \
                    ((x + 40 * cos(self.angle - pi / 2)) // 100 * 100,
                     (y + 40 * sin(self.angle - pi / 2)) // 100 * 100) not in mass:
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_RIGHT]:  # вправо от луча
            x = self.x + 4 * cos(self.angle + pi / 2)
            y = self.y + 4 * sin(self.angle + pi / 2)
            if (x // 100 * 100, y // 100 * 100) not in mass and \
                    ((x + 40 * cos(self.angle + pi / 2)) // 100 * 100,
                     (y + 40 * sin(self.angle + pi / 2)) // 100 * 100) not in mass:
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
            x = self.x + 4 * cos(self.angle)
            y = self.y + 4 * sin(self.angle)
            if (x // 100 * 100, y // 100 * 100) not in mass and \
                    ((x + 40 * cos(self.angle)) // 100 * 100, (y + 40 * sin(self.angle)) // 100 * 100) not in mass:
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
            x = self.x + 5 * cos(self.angle)
            y = self.y + 5 * sin(self.angle)
            if (x // 100 * 100, y // 100 * 100) not in mass and \
                    ((x + 50 * cos(self.angle)) // 100 * 100, (y + 50 * sin(self.angle)) // 100 * 100) not in mass:
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:  # назад от луча
            x = self.x + 4 * cos(self.angle + pi)
            y = self.y + 4 * sin(self.angle + pi)
            if (x // 100 * 100, y // 100 * 100) not in mass and \
                    ((x + 40 * cos(self.angle + pi)) // 100 * 100,
                     (y + 40 * sin(self.angle + pi)) // 100 * 100) not in mass:
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_a]:
            self.angle -= 0.05
        if pygame.key.get_pressed()[pygame.K_d]:
            self.angle += 0.05

    def checking_the_progress(self, x, y):
        pass

    def verification_of_correctness(self, walls, x, y):
        for i in walls:
            if i[1] * 100 - 8 <= x <= i[1] * 100 + 108 and i[0] * 100 - 8 <= y <= i[0] * 100 + 108:
                return False
        return True


def mapping(a, b):
    return (a // 100) * 100, (b // 100) * 100


wall_column = 0


def vision(sc, x_pl, y_pl, player_angle, textures):
    global wall_column
    fov = pi / 3
    ox, oy = x_pl, y_pl
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - fov / 2
    texture_v, texture_h = 1, 1
    for ray in range(300):
        sin_a = sin(cur_angle)
        cos_a = cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        x, dx = (xm + 100, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, 2500, 100):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in field_:
                texture_v = field_[tile_v]
                break
            x += dx * 100

        y, dy = (ym + 100, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, 1500, 100):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in field_:
                texture_h = field_[tile_h]
                break
            y += dy * 100

        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % 100
        depth *= cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int((3 * DIST * 100) / depth), 5 * 800)

        try:
            wall_column = textures[texture].subsurface(offset * (1200 // 100), 0, 1200 // 100, 1200)
            wall_column = pygame.transform.scale(wall_column, (1200 // 300, proj_height))
            sc.blit(wall_column, (ray * (1200 // 300), 400 - proj_height // 2))
        except Exception:
            pass

        cur_angle += fov / 300
