import pygame
from game import Game

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 400

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Завтра тест")
    done = False
    clock = pygame.time.Clock()
    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        # FPS
        clock.tick(24)

    pygame.quit()

if __name__ == '__main__':
    main()