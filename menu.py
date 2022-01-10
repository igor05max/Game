import pygame
import sys

pygame.init()


class Menu:
    def __init__(self, screen, music):
        self.screen = screen
        self.active = True

        self.music = music

        self.color_batten_exit = (200, 0, 0)
        self.color_text_exit = (80, 180, 80)
        self.batten_exit = False

        self.color_batten_play = (200, 0, 0)
        self.color_text_play = (80, 180, 80)
        self.batten_play = False

        self.color_batten_rules = (80, 180, 80)
        self.color_text_rules = (40, 40, 40)
        self.batten_rules = False
        self.visualization_rules = False

        self.color_batten_settings = (80, 180, 80)
        self.color_text_settings = (40, 40, 40)
        self.batten_settings = False
        self.visualization_settings = False

        self.settings_sens_bool = False
        self.settings_sens = 0.005
        self.mass_setting_sens = ["Низкая", "Средняя", "Высокая"]
        self.mass_setting_sens_index = "Средняя"

        self.color_back_settings = (200, 10, 10)
        self.settings_back = False

        self.settings_sound_bool = False
        self.settings_sound = 1.0
        self.mass_setting_sound = ["Нет", "Низкая", "Средняя", "Высокая"]
        self.mass_setting_sound_index = "Высокая"

        self.mouse = False
        self.mouse_vision = True
        self.keyboard = True

        self.color_batten_achievement = (200, 0, 0)

    def actions(self, event):
        if self.active:
            if not self.visualization_rules and not self.visualization_settings:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # self.active = False
                        pass
                if event.type == pygame.MOUSEMOTION:
                    if 1000 <= event.pos[0] <= 1170 and 680 <= event.pos[1] <= 760:
                        self.color_batten_exit = (80, 180, 80)
                        self.color_text_exit = (200, 0, 0)
                        self.batten_exit = True
                    else:
                        self.color_batten_exit = (200, 0, 0)
                        self.color_text_exit = (80, 180, 80)
                        self.batten_exit = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.batten_exit:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    if 390 <= event.pos[0] <= 670 and 500 <= event.pos[1] <= 580:
                        self.color_batten_play = (80, 180, 80)
                        self.color_text_play = (200, 0, 0)
                        self.batten_play = True
                    else:
                        self.color_batten_play = (200, 0, 0)
                        self.color_text_play = (80, 180, 80)
                        self.batten_play = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.batten_play:
                    self.active = False

                if event.type == pygame.MOUSEMOTION:
                    if 35 <= event.pos[0] <= 235 and 50 <= event.pos[1] <= 129:
                        self.color_batten_rules = (80, 180, 80)
                        self.color_text_rules = (80, 80, 80)
                        self.batten_rules = True
                    else:
                        self.color_batten_rules = (100, 200, 100)
                        self.color_text_rules = (40, 40, 40)
                        self.batten_rules = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.batten_rules:
                    self.visualization_rules = True

                if event.type == pygame.MOUSEMOTION:
                    if 35 <= event.pos[0] <= 295 and 250 <= event.pos[1] <= 330:
                        self.color_batten_settings = (80, 180, 80)
                        self.color_text_settings = (80, 80, 80)
                        self.batten_settings = True
                    else:
                        self.color_batten_settings = (100, 200, 100)
                        self.color_text_settings = (40, 40, 40)
                        self.batten_settings = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.batten_settings:
                    self.visualization_settings = True

            elif self.visualization_rules:
                pass

            else:
                if event.type == pygame.MOUSEMOTION:
                    if 710 <= event.pos[0] <= 940 and 330 <= event.pos[1] <= 360:
                        self.settings_sens_bool = True
                    else:
                        self.settings_sens_bool = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.settings_sens_bool:
                    self.mass_setting_sens_index =\
                        self.mass_setting_sens[(self.mass_setting_sens.index(self.mass_setting_sens_index)
                                                + 1) % 3]
                    if self.mass_setting_sens_index == "Низкая":
                        self.settings_sens = 0.001
                    elif self.mass_setting_sens_index == "Высокая":
                        self.settings_sens = 0.008
                    else:
                        self.settings_sens = 0.005

                if event.type == pygame.MOUSEMOTION:
                    if 180 <= event.pos[0] <= 330 and 620 <= event.pos[1] <= 680:
                        self.color_back_settings = (255, 255, 255)
                        self.settings_back = True
                    else:
                        self.settings_back = False
                        self.color_back_settings = (200, 10, 10)
                if event.type == pygame.MOUSEBUTTONDOWN and self.settings_back:
                    self.visualization_settings = False

                if event.type == pygame.MOUSEMOTION:
                    if 730 <= event.pos[0] <= 950 and 530 <= event.pos[1] <= 585:
                        self.settings_sound_bool = True
                    else:
                        self.settings_sound_bool = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.settings_sound_bool:
                    self.mass_setting_sound_index = \
                        self.mass_setting_sound[(self.mass_setting_sound.index(self.mass_setting_sound_index)
                                                + 1) % 4]
                    if self.mass_setting_sound_index == "Нет":
                        self.settings_sound = 0
                    elif self.mass_setting_sound_index == "Низкая":
                        self.settings_sound = 0.1
                    elif self.mass_setting_sound_index == "Средняя":
                        self.settings_sound = 0.5
                    else:
                        self.settings_sound = 1
                    self.music.set_volume(self.settings_sound)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 730 <= event.pos[0] <= 950 and 195 <= event.pos[1] <= 240:
                        self.mouse = not self.mouse

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 725 <= event.pos[0] <= 940 and 265 <= event.pos[1] <= 310:
                        self.mouse_vision = not self.mouse_vision

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 700 <= event.pos[0] <= 955 and 455 <= event.pos[1] <= 500:
                        self.keyboard = not self.keyboard

    def visualization(self):
        if not self.visualization_rules and not self.visualization_settings:
            self.screen.fill((100, 100, 150))
            screensaver = pygame.image.load(f'Menu/menu.png').convert()
            self.screen.blit(screensaver, (0, 0))
            pygame.draw.rect(self.screen, self.color_batten_exit,
                             (1000, 680, 170, 80), 0)

            font = pygame.font.Font(None, 60)
            text = font.render(f"Выход", True, self.color_text_exit)
            self.screen.blit(text, (1016, 700))

            pygame.draw.rect(self.screen, self.color_batten_play,
                             (390, 500, 280, 80), 0)

            font = pygame.font.Font(None, 60)
            text = font.render(f"Начать игру", True, self.color_text_play)
            self.screen.blit(text, (406, 518))

            pygame.draw.rect(self.screen, self.color_batten_rules,
                             (35, 50, 200, 80), 0)
            font = pygame.font.Font(None, 60)
            text = font.render(f"Правила", True, self.color_text_rules)
            self.screen.blit(text, (50, 70))

            pygame.draw.rect(self.screen, self.color_batten_settings,
                             (35, 250, 260, 80), 0)
            font = pygame.font.Font(None, 60)
            text = font.render(f"Настройки", True, self.color_text_settings)
            self.screen.blit(text, (50, 270))

            # pygame.draw.rect(self.screen, self.color_batten_achievement,
            #                  (30, 500, 280, 80), 0)

        elif self.visualization_rules:
            self.screen.fill((100, 100, 150))
            screensaver = pygame.image.load(f'Menu/110.png').convert()
            self.screen.blit(screensaver, (0, 0))

        else:
            self.screen.fill((100, 100, 150))
            screensaver = pygame.image.load(f'Menu/98.png').convert()
            self.screen.blit(screensaver, (0, 0))

            font = pygame.font.Font(None, 45)
            text = font.render(self.mass_setting_sens_index, True, (10, 10, 10))
            self.screen.blit(text, (770, 340))

            font = pygame.font.Font(None, 50)
            text = font.render("Назад", True, self.color_back_settings)
            self.screen.blit(text, (200, 630))

            font = pygame.font.Font(None, 50)
            text = font.render(self.mass_setting_sound_index, True, (10, 10, 10))
            self.screen.blit(text, (770, 535))

            font = pygame.font.Font(None, 50)
            text = font.render("Да" if self.mouse else "Нет", True, (10, 10, 10))
            self.screen.blit(text, (780, 202))

            font = pygame.font.Font(None, 50)
            text = font.render("Да" if self.mouse_vision else "Нет", True, (10, 10, 10))
            self.screen.blit(text, (780, 270))

            font = pygame.font.Font(None, 40)
            text = font.render("Левая      Правая" if self.keyboard else "Правая     Левая",
                               True, (10, 10, 10))
            self.screen.blit(text, (707, 460))
