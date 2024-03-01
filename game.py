import pygame
import random
from menu import Menu

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (20, 80, 50)
RED = (167, 33, 43)


class Game(object):
    def __init__(self):
        # Дизайн
        self.font = pygame.font.Font(None, 65)
        self.score_font = pygame.font.Font("Space-Matic.ttf", 30)
        self.problem = {"num1": 0, "num2": 0, "result": 0}
        self.operation = ""
        self.symbols = self.get_symbols()
        self.button_list = self.get_button_list()
        self.reset_problem = False

        items = ("Addition", "Subtraction", "Multiplication", "Division")
        self.menu = Menu(items, ttf_font="Space-Matic.ttf", font_size=50)

        self.show_menu = True

        self.score = 0
        self.count = 0

        new_icon = pygame.image.load('backgrounds/icon.png')
        pygame.display.set_icon(new_icon)

        self.bg_list = ['backgrounds/classroom.png']
        self.bg = pygame.image.load(random.choice(self.bg_list))
        self.bg = pygame.transform.scale(self.bg, (640, 400))

        self.music_list = ['music/home.mp3', 'music/near_school.mp3', 'music/classroom.mp3']
        pygame.mixer.music.load(random.choice(self.music_list))
        pygame.mixer.music.play(-1)

    def get_button_list(self):
        button_list = []
        choice = random.randint(1, 4)
        width = 100
        height = 100
        t_w = width * 2 + 50
        posX = (SCREEN_WIDTH / 2) - (t_w / 2)
        posY = 100
        if choice == 1:
            btn = Button(posX, posY, width, height, self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX, posY, width, height, random.randint(0, 100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w / 2) + 150

        if choice == 2:
            btn = Button(posX, posY, width, height, self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX, posY, width, height, random.randint(0, 100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w / 2)
        posY = 250

        if choice == 3:
            btn = Button(posX, posY, width, height, self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX, posY, width, height, random.randint(0, 100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w / 2) + 150

        if choice == 4:
            btn = Button(posX, posY, width, height, self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX, posY, width, height, random.randint(0, 100))
            button_list.append(btn)

        return button_list

    def get_symbols(self):
        """ Return a dictionary with all the operation symbols """
        symbols = {}
        sprite_sheet = pygame.image.load("sprites/symbols.png").convert()
        image = self.get_image(sprite_sheet, 0, 0, 64, 64)
        symbols["addition"] = image
        image.set_colorkey((255, 255, 255))
        image = self.get_image(sprite_sheet, 64, 0, 64, 64)
        symbols["subtraction"] = image
        image.set_colorkey((255, 255, 255))
        image = self.get_image(sprite_sheet, 128, 0, 64, 64)
        symbols["multiplication"] = image
        image.set_colorkey((255, 255, 255))
        image = self.get_image(sprite_sheet, 192, 0, 64, 64)
        symbols["division"] = image
        image.set_colorkey((255, 255, 255))

        return symbols

    def get_image(self, sprite_sheet, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(sprite_sheet, (0, 0), (x, y, width, height))
        return image

    # Сложение
    def addition(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a + b
        self.operation = "addition"

    # Вычитание
    def subtraction(self):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        if a > b:
            self.problem["num1"] = a
            self.problem["num2"] = b
            self.problem["result"] = a - b
        else:
            self.problem["num1"] = b
            self.problem["num2"] = a
            self.problem["result"] = b - a
        self.operation = "subtraction"

    # Умножение
    def multiplication(self):
        a = random.randint(0, 12)
        b = random.randint(0, 12)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a * b
        self.operation = "multiplication"

    # Деление
    def division(self):
        divisor = random.randint(1, 12)
        dividend = divisor * random.randint(1, 12)
        quotient = int(dividend / divisor)
        self.problem["num1"] = dividend
        self.problem["num2"] = divisor
        self.problem["result"] = quotient
        self.operation = "division"

    # Проверка
    def check_result(self):
        for button in self.button_list:
            if button.isPressed():
                if button.get_number() == self.problem["result"]:
                    button.set_color(GREEN)
                    # Увеличение счета
                    self.score += 1
                else:
                    button.set_color(RED)
                    # Уменьшение счета
                    self.score -= 1
                self.reset_problem = True

    def set_problem(self):
        if self.operation == "addition":
            self.addition()
        elif self.operation == "subtraction":
            self.subtraction()
        elif self.operation == "multiplication":
            self.multiplication()
        elif self.operation == "division":
            self.division()
        self.button_list = self.get_button_list()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_menu:
                    if self.menu.state == 0:
                        self.operation = "addition"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 1:
                        self.operation = "subtraction"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 2:
                        self.operation = "multiplication"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 3:
                        self.operation = "division"
                        self.set_problem()
                        self.show_menu = False

                else:
                    self.check_result()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_menu = True
                    self.score = 0
                    self.count = 0

        return False

    def run_logic(self):
        self.menu.update()

    def display_message(self, screen, items):
        for index, message in enumerate(items):
            label = self.font.render(message, True, BLACK)
            width = label.get_width()
            height = label.get_height()

            posX = (SCREEN_WIDTH / 2) - (width / 2)
            t_h = len(items) * height
            posY = (SCREEN_HEIGHT / 2) - (t_h / 2) + (index * height)

            screen.blit(label, (posX, posY))

    def display_frame(self, screen):
        # Отображаем программу
        screen.blit(self.bg, (0, 0))
        time_wait = False
        if self.show_menu:
            self.menu.display_frame(screen)
        elif self.count == 20:
            msg_1 = "You answered " + str(self.score / 5) + " correctly"
            msg_2 = "Your score was " + str(self.score)
            self.display_message(screen, (msg_1, msg_2))
            self.show_menu = True
            # Обнуляем счетчик
            self.score = 0
            self.count = 0
            time_wait = True
        else:
            label_1 = self.font.render(str(self.problem["num1"]), True, BLACK)
            label_2 = self.font.render(str(self.problem["num2"]) + " = ?", True, BLACK)
            t_w = label_1.get_width() + label_2.get_width() + 65
            posX = (SCREEN_WIDTH / 2) - (t_w / 2)
            screen.blit(label_1, (posX, 50))
            screen.blit(self.symbols[self.operation], (posX + label_1.get_width(), 40))

            screen.blit(label_2, (posX + label_1.get_width() + 65, 50))
            for btn in self.button_list:
                btn.draw(screen)
            score_label = self.score_font.render("Score: " + str(self.score), True, BLACK)
            screen.blit(score_label, (10, 10))

        # Изменения на экране
        pygame.display.flip()
        if self.reset_problem:
            pygame.time.wait(1000)
            self.set_problem()
            self.count += 1
            self.reset_problem = False
        # Ожидание в 3 секунды
        elif time_wait:
            pygame.time.wait(3000)


class Button(object):
    def __init__(self, x, y, width, height, number):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render(str(number), True, BLACK)
        self.number = number
        self.background_color = WHITE

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 3)
        width = self.text.get_width()
        height = self.text.get_height()
        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)
        screen.blit(self.text, (posX, posY))

    def isPressed(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    # Вспомогательные функции
    def set_color(self, color):
        self.background_color = color

    def get_number(self):
        return self.number