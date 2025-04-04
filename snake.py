import pygame
from constants import GRID_SIZE, GREEN, DARK_GREEN

class Snake:
    def __init__(self, start_pos):
        self.body = [start_pos]
        self.direction = [GRID_SIZE, 0]
        self.grow_pending = False
        self.powerup_stacks = 0

    def move(self):
        new_head = [self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]]
        if new_head in self.body:
            return False  # Collision with self
        self.body.insert(0, new_head)
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False
        return True

    def change_direction(self, new_direction):
        if (new_direction[0], new_direction[1]) != (-self.direction[0], -self.direction[1]):
            self.direction = new_direction

    def grow(self):
        self.grow_pending = True

    def draw(self, surface):
        color = DARK_GREEN if self.powerup_stacks > 0 else GREEN
        for segment in self.body:
            pygame.draw.rect(surface, color, (*segment, GRID_SIZE, GRID_SIZE))

    def head_rect(self):
        return pygame.Rect(*self.body[0], GRID_SIZE, GRID_SIZE)

    def wrap_around(self, width, height):
        head = self.body[0]
        head[0] %= width
        head[1] %= height

