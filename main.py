import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snake Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create an empty array
snake_segments = []

# Set the speed
x_change = 0
y_change = 0

# Set the starting position of the snake
x_start = 300
y_start = 250

# Set the size of the snake
snake_block = 10

# Set the score to 0
score = 0

# Set the font
font = pygame.font.SysFont('Calibri', 25, True, False)

# Create the snake
snake_segments.append([x_start, y_start])

# Create the food
foodx = round(random.randrange(0, size[0] - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, size[1] - snake_block) / 10.0) * 10.0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_block

    # --- Game logic should go here

    # Move the snake
    x_start += x_change
    y_start += y_change

    # Boundaries
    if x_start >= size[0] or x_start < 0 or y_start >= size[1] or y_start < 0:
        done = True

    # Add the new position to the snake
    snake_segments.insert(0, [x_start, y_start])

    # Check if the snake has eaten the food
    if x_start == foodx and y_start == foody:
        foodx = round(random.randrange(0, size[0] - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, size[1] - snake_block) / 10.0) * 10.0
        score += 1
    else:
        snake_segments.pop()

    # --- Drawing code should go here

    # Clear the screen
    screen.fill(BLACK)

    # Draw the snake
    for segment in snake_segments:
        pygame.draw.rect(screen, WHITE, [segment[0], segment[1], snake_block, snake_block])

    # Draw the food
    pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])

    # Draw the score
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [0, 0])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(30)

# Close the window and quit.
pygame.quit()
