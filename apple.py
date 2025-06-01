from constants import *
import pygame
import random

class Apple():

    def __init__(self, snake):
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE

        self.x, self.y = self.new_loc(snake)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.dir = 0 #0 up, 1 right, 2 down, 3 left

        self.frame_count = 0
        self.movement_speed = 15


    def new_loc(self, snake):
        while True:
            x = random.randint(0, COLS - 1) * BLOCK_SIZE
            y = random.randint(0, ROWS - 1) * BLOCK_SIZE
            new_position = (x, y)
            if new_position != snake.rect.topleft and all(seg.rect.topleft != new_position for seg in snake.segments):
                return new_position


    def update(self, snake):
        collide = self.rect.colliderect(snake.rect)
        if collide:
            self.rect.x, self.rect.y = self.new_loc(snake)
            snake.add_segment()



    def draw(self, surface):
        # pygame.draw.rect(surface, RED, self.rect)
        pygame.draw.ellipse(surface, RED, self.rect)
        pygame.draw.ellipse(surface, WHITE, (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 4, self.rect.width // 4, self.height // 4))
