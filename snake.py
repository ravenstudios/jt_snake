from constants import *
import pygame
import snake_face


class Snake():
    def __init__(self):
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.x = ROWS // 2 * BLOCK_SIZE
        self.y = COLS // 2 * BLOCK_SIZE

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.dir = 1 #0 up, 1 right, 2 down, 3 left
        self.can_check_head = False
        self.frame_count = 0
        self.movement_speed = 15
        self.segments = []
        self.speed_increase = 0.2
        self.is_game_over = False


    def update(self):
        if not self.is_game_over:
            self.key_handler()
            self.movment()
            self.check_collisions()


    def move_body(self):
        if self.segments:
            for i in range(len(self.segments) - 1, 0, -1):
                self.segments[i].rect.topleft = self.segments[i - 1].rect.topleft
            self.segments[0].rect.topleft = self.rect.topleft


    def key_handler(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.dir != 2:
                self.dir = 0
        elif keys[pygame.K_RIGHT] and self.dir != 3:
            self.dir = 1
        elif keys[pygame.K_DOWN] and self.dir != 0:
            self.dir = 2
        elif keys[pygame.K_LEFT] and self.dir != 1:
            self.dir = 3

        # if keys[pygame.K_SPACE]:
        #     self.add_segment()

    def check_collisions(self):
        if self.rect.left < 0 or self.rect.right > GAME_WIDTH or self.rect.top < 0 or self.rect.bottom > GAME_HEIGHT:
            self.game_over()

        if self.can_check_head:
            for seg in self.segments:
                if self.rect.colliderect(seg.rect):
                    self.game_over()

    def movment(self):
        self.frame_count += 1
        if self.frame_count % int(self.movement_speed) == 0:
            self.move_body()
            if self.dir == 0:
                self.rect.y -= self.rect.height
            elif self.dir == 1:
                self.rect.x += self.rect.width
            elif self.dir == 2:
                self.rect.y += self.rect.height
            elif self.dir == 3:
                self.rect.x -= self.rect.width
            self.can_check_head = True

    def game_over(self):
        self.is_game_over = True


    def add_segment(self):
        if self.segments:
            self.segments.append(Segment(self.segments[-1].rect.x, self.segments[-1].rect.y))

        else:
            self.segments.append(Segment(self.rect.x, self.rect.y))
            self.can_check_head = False

        self.movement_speed -= self.speed_increase



    def draw(self, surface):
        pygame.draw.ellipse(surface, (0, 150, 0), self.rect)
        for seg in self.segments:
            seg.draw(surface)
        snake_face.draw_face(surface, self)

class Segment():
    def __init__(self, x, y):
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        pass

    def draw(self, surface):
        pygame.draw.ellipse(surface, (0, 150, 0), self.rect)
