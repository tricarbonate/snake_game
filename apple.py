import pygame
import random
import time
from constants import GRID_SIZE, RED, GOLD

class Apple:
    def __init__(self, width, height, is_powerup=False):
        self.x = random.randrange(0, width - GRID_SIZE, GRID_SIZE)
        self.y = random.randrange(0, height - GRID_SIZE, GRID_SIZE)
        self.is_powerup = is_powerup
        speed = 1.5 if self.is_powerup else 0.8
        self.direction = [random.choice([-1, 1]) * speed, random.choice([-1, 1]) * speed]

    def move(self, width, height):
        self.x += self.direction[0]
        self.y += self.direction[1]

        if self.x < 0 or self.x >= width - GRID_SIZE:
            self.direction[0] *= -1
            self.x = max(0, min(self.x, width - GRID_SIZE))
        if self.y < 0 or self.y >= height - GRID_SIZE:
            self.direction[1] *= -1
            self.y = max(0, min(self.y, height - GRID_SIZE))

    def rect(self):
        return pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

    def draw(self, surface):
        if self.is_powerup:
            size = GRID_SIZE + (5 if time.time() % 0.5 < 0.25 else 0)
            pygame.draw.rect(surface, GOLD, (self.x, self.y, size, size))
        else:
            pygame.draw.rect(surface, RED, (self.x, self.y, GRID_SIZE, GRID_SIZE))

