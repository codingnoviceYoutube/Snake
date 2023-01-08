import sys
import random
import pygame

# Initialize pygame
pygame.init()

# Set screen width and height
screen_width, screen_height = 640, 480

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title and icon
pygame.display.set_caption("Snake")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Set clock
clock = pygame.time.Clock()

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set snake starting position and size
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set food starting position and size
food_pos = [300, 300]
food_spawn = True

# Set snake movement direction
direction = 'RIGHT'
change_to = direction

# Set score
score = 0

# Set font
font = pygame.font.SysFont("times new roman", 25)

# Game over function
def game_over():
    my_font = pygame.font.SysFont("times new roman", 35)
    game_over_surface = my_font.render("Your Score: " + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width/2, screen_height/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    show_score(0, red, "times", 20)
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Show score function
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (screen_width/10, 15)
    else:
        score_rect.midtop = (screen_width/2, screen_height/1.25)
    screen.blit(score_surface, score_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validate direction change
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if food_spawn == False:
        food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn = True

    screen.fill(black)

    # Snake body
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Food
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Boundary conditions
    if snake_pos[0] < 0 or snake_pos[0] > screen_width-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > screen_height-10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # Refresh game screen
    pygame.display.update()

    # Frame per second
    clock.tick(20)
