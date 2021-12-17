from math import sin, cos, pi
import pygame


class Player:
    def __init__(self, x=350, y=350):
        self.x, self.y = x, y
        self.angle = 0

    def display(self, screen):  # отображение игрока
        pygame.draw.circle(screen, ((145, 230, 145)), (self.x, self.y), 8)
        pygame.draw.line(screen, ((120, 150, 200)), (self.x, self.y), (self.x + 700 * cos(self.angle),
                                                                        self.y + 700 * sin(self.angle)))

    def motion(self, walls):  # движение игрока
        if pygame.key.get_pressed()[pygame.K_LEFT]:  # влево от луча
            x = self.x + 4 * cos(self.angle - pi / 2)
            y = self.y + 4 * sin(self.angle - pi / 2)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                if self.x > 680:
                    self.x = 680
                if self.x < 10:
                    self.x = 10
                self.y = y
                if self.y > 680:
                    self.y = 680
                if self.y < 10:
                    self.y = 10

        if pygame.key.get_pressed()[pygame.K_RIGHT]:  # вправо от луча
            x = self.x + 4 * cos(self.angle + pi / 2)
            y = self.y + 4 * sin(self.angle + pi / 2)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                if self.x > 680:
                    self.x = 680
                if self.x < 10:
                    self.x = 10
                self.y = y
                if self.y > 680:
                    self.y = 680
                if self.y < 10:
                    self.y = 10

        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:  # вперёд от луча
            x = self.x + 4 * cos(self.angle)
            y = self.y + 4 * sin(self.angle)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                if self.x > 680:
                    self.x = 680
                if self.x < 10:
                    self.x = 10
                self.y = y
                if self.y > 680:
                    self.y = 680
                if self.y < 10:
                    self.y = 10

        if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:  # назад от луча
            x = self.x + 4 * cos(self.angle + pi)
            y = self.y + 4 * sin(self.angle + pi)
            if self.verification_of_correctness(walls, x, y):
                self.x = x
                if self.x > 680:
                    self.x = 680
                if self.x < 10:
                    self.x = 10
                self.y = y
                if self.y > 680:
                    self.y = 680
                if self.y < 10:
                    self.y = 10

        if pygame.key.get_pressed()[pygame.K_a]:
            self.angle -= 0.05
        if pygame.key.get_pressed()[pygame.K_d]:
            self.angle += 0.05

    def verification_of_correctness(self, walls, x, y):
        for i in walls:
            if i[1] * 70 - 8 <= x <= i[1] * 70 + 78 and i[0] * 70 - 8 <= y <= i[0] * 70 + 78:
                return False
        return True
