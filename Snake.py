import pygame
import time
import random
from pygame import Rect

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((400, 400))

# Title
pygame.display.set_caption("Snake")

snake_x = [200, 200, 200]
snake_y = [200, 190, 180]
next_x = 200
next_y = 200
is_game_over = False
block_size = 10
move_direction = "up"
is_snack_present = False
game_over_font = pygame.font.Font('freesansbold.ttf', 32)
snack_x = random.randint(0, 40) * 10
snack_y = random.randint(0, 40) * 10
grow = False


def game_over():
    game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over_text, (100, 150))


def snake():
    global is_snack_present

    if next_x == snack_x and next_y == snack_y:
        is_snack_present = False

    for i in range(len(snake_x)):
        pygame.draw.rect(screen, (0, 255, 0), Rect(snake_x[i], snake_y[i], block_size, block_size))


def move_snake():
    global snake_x, snake_y, is_game_over, grow

    # Move snake or crash
    if 0 <= next_x < 400:
        if grow:
            snake_x.append(0)

        # Shift array right to move snake
        snake_x = [snake_x[-1]] + snake_x[:-1]
        snake_x[0] = next_x
    else:
        is_game_over = True

    if 0 <= next_y < 400:
        if grow:
            snake_y.append(0)
            grow = False

        # Shift array right to move snake
        snake_y = [snake_y[-1]] + snake_y[:-1]
        snake_y[0] = next_y
    else:
        is_game_over = True


def prepare_next_move():
    global next_x, next_y, grow

    # Next move
    if move_direction == "left":
        next_x -= block_size
    elif move_direction == "right":
        next_x += block_size
    elif move_direction == "up":
        next_y -= block_size
    elif move_direction == "down":
        next_y += block_size

    if next_x == snack_x and next_y == snack_y:
        grow = True


def snack():
    global is_snack_present, snack_x, snack_y

    if not is_snack_present:
        snack_x = random.randint(0, 39) * 10
        snack_y = random.randint(0, 39) * 10
        is_snack_present = True

    pygame.draw.rect(screen, (255, 0, 0), Rect(snack_x, snack_y, block_size, block_size))


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

    if not is_game_over:
        prepare_next_move()
        move_snake()
    else:
        game_over()

    # Snake
    snake()

    # Snack
    snack()

    pygame.display.update()
