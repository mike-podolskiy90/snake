import pygame
import time
from pygame import Rect

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((400, 400))

# Title
pygame.display.set_caption("Snake")

snake_x = [200]
snake_y = [200]
next_x = 200
next_y = 200
snake_length = 1
is_game_over = False
block_size = 10
move_direction = "up"
game_over_font = pygame.font.Font('freesansbold.ttf', 32)


def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (100, 150))


def snake():
    for i in range(snake_length):
        pygame.draw.rect(screen, (0, 255, 0), Rect(snake_x[i], snake_y[i], block_size, block_size))


def move_snake():
    global is_game_over

    # Move snake or crash
    if 0 <= next_x < 400:
        snake_x[0] = next_x
    else:
        is_game_over = True

    if 0 <= next_y < 400:
        snake_y[0] = next_y
    else:
        is_game_over = True


def prepare_next_move():
    global next_x, next_y

    # Next move
    if move_direction == "left":
        next_x -= block_size
    elif move_direction == "right":
        next_x += block_size
    elif move_direction == "up":
        next_y -= block_size
    elif move_direction == "down":
        next_y += block_size


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Sleep to slower snake's speed
    time.sleep(.100)

    if not is_game_over:
        for event in pygame.event.get():
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

        prepare_next_move()

        move_snake()
    else:
        game_over()

    # Snake
    snake()

    pygame.display.update()
