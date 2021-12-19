import pygame


class Field:
    def __init__(self):
        pass

    def field_generation(self):
        self.field = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                      [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
                      [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                      [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1],
                      [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

        self.mass = []

        for i, elem in enumerate(self.field):
            for j, el in enumerate(elem):
                if el == 1:
                    self.mass.append((i, j))

    def visualization(self, screen):
        for i in self.mass:
            pygame.draw.rect(screen, (123, 125, 200), (i[1] * 100, i[0] * 100, 100, 100), 2)
