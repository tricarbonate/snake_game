import pygame
from constants import *
from game import Game

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game with Classes")
    clock = pygame.time.Clock()
    game = Game(window)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.snake.change_direction([-GRID_SIZE, 0])
                elif event.key == pygame.K_RIGHT:
                    game.snake.change_direction([GRID_SIZE, 0])
                elif event.key == pygame.K_UP:
                    game.snake.change_direction([0, -GRID_SIZE])
                elif event.key == pygame.K_DOWN:
                    game.snake.change_direction([0, GRID_SIZE])

        if not game.update():
            running = False

        game.draw()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

