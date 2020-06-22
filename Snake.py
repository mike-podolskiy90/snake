import pygame
from pygame import Rect

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((400, 400))

snake_head_x = 200
snake_head_y = 200

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Snake
    pygame.draw.rect(screen, (0, 255, 0), Rect(snake_head_x, snake_head_y, 10, 10))

    pygame.display.update()
