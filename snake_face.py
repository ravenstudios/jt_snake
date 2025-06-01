import pygame
from constants import *

def draw_face(surface, snake):
    w = snake.rect.width
    h = snake.rect.height
    x = snake.rect.x
    y = snake.rect.y

    if snake.dir == 0:  # Up
        left_eye = pygame.Rect(x + w // 5, y + h // 5, w // 8, h // 4)
        right_eye = pygame.Rect(x + 3 * w // 5, y + h // 5, w // 8, h // 4)
        tongue = pygame.Rect(x + w // 2 - w // 16, y - h // 2 + 4, w // 8, h // 2)

    elif snake.dir == 1:  # Right
        left_eye = pygame.Rect(x + 3 * w // 5, y + h // 5, w // 4, h // 8)
        right_eye = pygame.Rect(x + 3 * w // 5, y + 3 * h // 5, w // 4, h // 8)
        tongue = pygame.Rect(x + w, y + h // 2 - h // 16, w // 2, h // 8)

    elif snake.dir == 2:  # Down
        left_eye = pygame.Rect(x + w // 5, y + 3 * h // 5, w // 8, h // 4)
        right_eye = pygame.Rect(x + 3 * w // 5, y + 3 * h // 5, w // 8, h // 4)
        tongue = pygame.Rect(x + w // 2 - w // 16, y + h, w // 8, h // 2)

    elif snake.dir == 3:  # Left
        left_eye = pygame.Rect(x + w // 10, y + h // 5, w // 4, h // 8)
        right_eye = pygame.Rect(x + w // 10, y + 3 * h // 5, w // 4, h // 8)
        tongue = pygame.Rect(x - w // 2, y + h // 2 - h // 16, w // 2, h // 8)

    # Draw eyes and tongue
    pygame.draw.ellipse(surface, BLACK, left_eye)
    pygame.draw.ellipse(surface, BLACK, right_eye)
    pygame.draw.rect(surface, RED, tongue)
