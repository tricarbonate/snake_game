import pygame
import time
import random
from constants import *
from snake import Snake
from apple import Apple

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.snake = Snake([WIDTH // 2, HEIGHT // 2])
        self.apples = []
        self.score = 0
        self.apples_eaten = 0
        self.powerup_end_time = 0
        self.font = pygame.font.SysFont(None, 50)
        self.timer_duration = 5
        self.timer_start = time.time()
        self.spawn_initial_apples()
        self.frame_count = 0
        self.base_update_rate = 10
        self.snake_update_interval = 60 // self.base_update_rate


    def spawn_initial_apples(self):
        for i in range(3):
            is_powerup = (i == 0 and random.random() < 0.2)
            self.apples.append(Apple(WIDTH, HEIGHT, is_powerup))

    def update(self):
        self.frame_count += 1
        self.snake_update_interval = max(1, 60 // int(self.base_update_rate * (1.5 ** self.snake.powerup_stacks)))

        if self.frame_count % self.snake_update_interval == 0:
            # Move snake
            if not self.snake.move():
                return False  # Game over
            self.snake.wrap_around(WIDTH, HEIGHT)


            # Check for collisions
            for i, apple in enumerate(self.apples):
                if self.snake.head_rect().colliderect(apple.rect()):
                    self.snake.grow()
                    self.score += 2 if apple.is_powerup else 1
                    self.apples_eaten += 1
                    if apple.is_powerup:
                        self.snake.powerup_stacks += 1
                        self.powerup_end_time = max(self.powerup_end_time, time.time()) + 5
                    self.timer_start = time.time()
                    self.apples[i] = Apple(WIDTH, HEIGHT, random.random() < 0.9)

        # Move apples
        for apple in self.apples:
            apple.move(WIDTH, HEIGHT)

        # Powerup expiration
        if self.snake.powerup_stacks > 0 and time.time() > self.powerup_end_time:
            self.snake.powerup_stacks -= 1
            if self.snake.powerup_stacks > 0:
                self.powerup_end_time = time.time() + 5

        return True

    def draw(self):
        self.surface.fill(BLACK)
        self.snake.draw(self.surface)
        for apple in self.apples:
            apple.draw(self.surface)
        self.draw_ui()

    def draw_ui(self):
        time_left = max(0, self.timer_duration - (time.time() - self.timer_start))
        texts = [
            f'Time: {time_left:.1f}',
            f'Score: {self.score}',
            f'Apples Eaten: {self.apples_eaten}',
            f'Powerups: {self.snake.powerup_stacks}'
        ]
        colors = [WHITE, WHITE, WHITE, GOLD if self.snake.powerup_stacks > 0 else WHITE]
        for i, (text, color) in enumerate(zip(texts, colors)):
            rendered = self.font.render(text, True, color)
            self.surface.blit(rendered, (10, 10 + i * 40))

