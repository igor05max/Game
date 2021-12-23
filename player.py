from math import sin, cos, pi, tan
from field import *

import pygame


DIST = 300 / (2 * tan((pi / 3) / 2))


class Player:
    def __init__(self, screen, x=200, y=650):
        self.x, self.y = x, y
        self.angle = 0
        self.screen = screen

    def display(self, screen):  # отображение игрока
        pygame.draw.circle(screen, ((145, 230, 145)), (self.x, self.y), 8)
        pygame.draw.line(screen, ((120, 150, 200)), (self.x, self.y), (self.x + 1250 * cos(self.angle),
                                                                        self.y + 900 * sin(self.angle)))

    def motion(self, walls):  # движение игрока
        if pygame.key.get_pressed()[pygame.K_LEFT]:  # влево от луча
            x = self.x + 6 * cos(self.angle - pi / 2)
            y = self.y + 6 * sin(self.angle - pi / 2)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_RIGHT]:  # вправо от луча
            x = self.x + 6 * cos(self.angle + pi / 2)
            y = self.y + 6 * sin(self.angle + pi / 2)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
            x = self.x + 6 * cos(self.angle)
            y = self.y + 6 * sin(self.angle)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
            x = self.x + 8 * cos(self.angle)
            y = self.y + 8 * sin(self.angle)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:  # назад от луча
            x = self.x + 6 * cos(self.angle + pi)
            y = self.y + 6 * sin(self.angle + pi)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                self.y = y

        if pygame.key.get_pressed()[pygame.K_a]:
            self.angle -= 0.05
        if pygame.key.get_pressed()[pygame.K_d]:
            self.angle += 0.05

    def verification_of_correctness(self, walls, x, y):
        for i in walls:
            if i[1] * 100 - 8 <= x <= i[1] * 100 + 108 and i[0] * 100 - 8 <= y <= i[0] * 100 + 108:
                return False
        return True


def verification_of_correctness(walls, x, y):
    for i in walls:
        if i[1] * 100 <= x <= i[1] * 100 + 100 and i[0] * 100 <= y <= i[0] * 100 + 100:
            return False
    return True


def vision_2d(screen, angle, x_pl, y_pl, mass):
    fov = pi / 3
    angle_2 = angle - fov / 2
    for _ in range(70):
        cos_ = cos(angle_2)
        sin_ = sin(angle_2)
        for j in range(750):
            x = x_pl + j * cos_
            y = y_pl + j * sin_
            pygame.draw.line(screen, (200, 200, 200), (x_pl, y_pl), (x, y), 1)
            if not verification_of_correctness(mass, x, y):
                break
        angle_2 += fov / 80


def vision_3d(screen, angle, x_pl, y_pl, mass):
    pygame.draw.rect(screen, (127, 199, 255), (0, 0, 1200, 600))
    pygame.draw.rect(screen, (34, 139, 34), (0, 350, 1200, 600))
    fov = pi / 3
    angle_2 = angle - fov / 2
    for i in range(115):
        cos_ = cos(angle_2)
        sin_ = sin(angle_2)
        for j in range(740):
            x = x_pl + j * cos_
            y = y_pl + j * sin_
            if not verification_of_correctness(mass, x, y):
                j *= cos(angle - angle_2)
                pygame.draw.rect(screen, (255 / (1 + j / 100), 255 / (1 + j / 100), 255 / (1 + j / 100) // 3),
                                 (i * 10, 350 - min(3 * DIST * 100 / (j + 0.0001), 700) // 2,
                                  10, min(3 * DIST * 100 / (j + 0.0001), 700)))
                break
        angle_2 += fov / 115


def mapping(a, b):
    return (a // 100) * 100, (b // 100) * 100


def vision(sc, x_pl, y_pl, player_angle, textures):
    fov = pi / 3
    ox, oy = x_pl, y_pl
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - fov / 2
    for ray in range(300):
        sin_a = sin(cur_angle)
        cos_a = cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        x, dx = (xm + 100, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, 1200, 100):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in field_:
                texture_v = field_[tile_v]
                break
            x += dx * 100

        y, dy = (ym + 100, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, 800, 100):
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
        proj_height = min(int((3 * DIST * 100) / depth), 2 * 800)

        wall_column = textures[texture].subsurface(offset * (1200 // 100), 0, 1200 // 100, 1200)
        wall_column = pygame.transform.scale(wall_column, (1200 // 300, proj_height))
        sc.blit(wall_column, (ray * (1200 // 300), 400 - proj_height // 2))

        cur_angle += fov / 300

