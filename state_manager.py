import snake
import apple
import pygame
from constants import *

class StateManager():


    def __init__(self):
        self.game = Game()
        self.pause = Pause()
        self.current_state = self.game

    def update(self):
        self.current_state.update()

    def draw(self, surface):
        self.current_state.draw(surface)


class State():
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self, surface):
        pass


class Game(State):
    def __init__(self):
        self.snake = snake.Snake()
        self.apple = apple.Apple(self.snake)

    def update(self):
        self.snake.update()
        self.apple.update(self.snake)

    def draw(self, surface):
        self.apple.draw(surface)
        self.snake.draw(surface)

class Pause(State):
    def __init__(self):
        pass

    def draw(self, surface):
        screen_height = GAME_HEIGHT + BLOCK_SIZE
        font_size = 36
        str = f"PAUSED"
        font = pygame.font.Font(None, 75)
        text_surface = font.render(str, True, BLACK)  # white text
        surface.blit(text_surface, (GAME_WIDTH // 2 - text_surface.get_rect().width // 2, GAME_HEIGHT // 2 - text_surface.get_rect().height // 2))
