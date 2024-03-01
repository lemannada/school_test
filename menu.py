import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400


class Menu(object):
    state = -1

    def __init__(self, items, font_color=(0, 0, 0), select_color=(167, 33, 43), ttf_font='Space-Matic.ttf', font_size=30):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font, font_size)
        self.rect_list = self.get_rect_list(items)

    def get_rect_list(self, items):
        rect_list = []
        for index, item in enumerate(items):
            size = self.font.size(item)
            width = size[0]
            height = size[1]
            # Расположение примера
            posX = (SCREEN_WIDTH / 2) - (width / 2)
            t_h = len(items) * height
            posY = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)
            rect = pygame.Rect(posX, posY, width, height)
            rect_list.append(rect)

        return rect_list

    def collide_points(self):
        index = -1
        mouse_pos = pygame.mouse.get_pos()
        for i, rect in enumerate(self.rect_list):
            if rect.collidepoint(mouse_pos):
                index = i

        return index

    def update(self):
        self.state = self.collide_points()

    def display_frame(self, screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item, True, self.select_color)
            else:
                label = self.font.render(item, True, self.font_color)

            width = label.get_width()
            height = label.get_height()

            posX = (SCREEN_WIDTH / 2) - (width / 2)
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)

            screen.blit(label, (posX, posY))