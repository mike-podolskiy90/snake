import pygame
import time
from pygame import Rect

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((400, 400))

block_size = 10
snake_head_x = 200
snake_head_y = 200
move_direction = "up"

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Catch button pressed and store snake's movement direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_direction = "left"
            elif event.key == pygame.K_RIGHT:
                move_direction = "right"
            elif event.key == pygame.K_UP:
                move_direction = "up"
            elif event.key == pygame.K_DOWN:
                move_direction = "down"

    # Sleep to slower snake's speed
    time.sleep(.100)

    # Move snake
    if move_direction == "left":
        snake_head_x -= block_size
    elif move_direction == "right":
        snake_head_x += block_size
    elif move_direction == "up":
        snake_head_y -= block_size
    elif move_direction == "down":
        snake_head_y += block_size

    # Snake
    pygame.draw.rect(screen, (0, 255, 0), Rect(snake_head_x, snake_head_y, block_size, block_size))

    pygame.display.update()
