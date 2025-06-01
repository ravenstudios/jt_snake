from constants import *
import pygame
import state_manager



clock = pygame.time.Clock()
screen_height = GAME_HEIGHT + BLOCK_SIZE
surface = pygame.display.set_mode((GAME_WIDTH, screen_height))

pygame.init()
state_manager = state_manager.StateManager()

font_size = 36
game_over_font_size = font_size * 0.8
org_font_size = font_size
def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_RETURN:
                    if state_manager.current_state == state_manager.game:
                        if state_manager.current_state.snake.is_game_over:
                            state_manager.current_state.snake.__init__()

                if event.key == pygame.K_p:
                    if state_manager.current_state == state_manager.game:
                        state_manager.current_state = state_manager.pause
                    else:
                        state_manager.current_state = state_manager.game

        update()
        draw()

    pygame.quit()

def update():
    state_manager.update()

def draw():
    surface.fill((0, 0, 0))#background
    draw_grid()
    state_manager.draw(surface)
    draw_score()
    pygame.display.flip()



def draw_score():
    pygame.draw.rect(surface, WHITE, (0, screen_height - BLOCK_SIZE, GAME_WIDTH, GAME_HEIGHT))
    if state_manager.current_state == state_manager.game:
        if state_manager.current_state.snake.is_game_over:
            font_size = game_over_font_size
            str = f"GAME OVER Your score is {len(state_manager.current_state.snake.segments)}, press enter to start new game."
        else:
            font_size = org_font_size
            str = f"Score: {len(state_manager.current_state.snake.segments)}"
        font = pygame.font.Font(None, int(font_size))
        text_surface = font.render(str, True, BLACK)  # white text
        surface.blit(text_surface, (GAME_WIDTH // 2 - text_surface.get_rect().width // 2, screen_height - BLOCK_SIZE + font_size // 8))





def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            if (r + c) % 2 == 0:
                color = (173, 255, 47)
            else:
                color = (0, 200, 0)
            pygame.draw.rect(surface, color, (BLOCK_SIZE * c, BLOCK_SIZE * r, BLOCK_SIZE, BLOCK_SIZE))
if __name__ == "__main__":
    main()
