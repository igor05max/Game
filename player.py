from math import sin, cos, pi, tan
import pygame


DIST = 120 / (2 * tan((pi / 3) / 2))


class Player:
    def __init__(self, screen, x=350, y=350):
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
                if self.x > 1230:
                    self.x = 1230
                if self.x < 10:
                    self.x = 10
                self.y = y
                if self.y > 1230:
                    self.y = 1230
                if self.y < 10:
                    self.y = 10

        if pygame.key.get_pressed()[pygame.K_RIGHT]:  # вправо от луча
            x = self.x + 6 * cos(self.angle + pi / 2)
            y = self.y + 6 * sin(self.angle + pi / 2)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                if self.x > 1230:
                    self.x = 1230
                if self.x < 10:
                    self.x = 10
                self.y = y
                if self.y > 1230:
                    self.y = 1230
                if self.y < 10:
                    self.y = 10

        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
            x = self.x + 6 * cos(self.angle)
            y = self.y + 6 * sin(self.angle)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                if self.x > 1230:
                    self.x = 1230
                if self.x < 10:
                    self.x = 10
                self.y = y
                if self.y > 1230:
                    self.y = 1230
                if self.y < 10:
                    self.y = 10

        if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
            x = self.x + 8 * cos(self.angle)
            y = self.y + 8 * sin(self.angle)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                if self.x > 1230:
                    self.x = 1230
                if self.x < 10:
                    self.x = 10
                self.y = y
                if self.y > 1230:
                    self.y = 1230
                if self.y < 10:
                    self.y = 10

        if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:  # назад от луча
            x = self.x + 6 * cos(self.angle + pi)
            y = self.y + 6 * sin(self.angle + pi)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                if self.x > 1230:
                    self.x = 1230
                if self.x < 10:
                    self.x = 10
                self.y = y
                if self.y > 1230:
                    self.y = 1230
                if self.y < 10:
                    self.y = 10

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
    pygame.draw.rect(screen, (173, 214, 255), (0, 0, 1150, 575))
    pygame.draw.rect(screen, (128, 161, 95), (0, 350, 1150, 575))
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
