import pygame
import time
import random

snake_speed = 15

# Window size
window_x = 720
window_y = 480

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize game
pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Snake initial position and body
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

direction = 'RIGHT'
change_to = direction

score = 0

# Food variables
food_types = [(red, 10), (blue, 20), (green, 30)]  # Different colors and scores
food_position = None
food_spawn_time = None
food_duration = 5  # Food disappears after 5 seconds

def spawn_food():
    global food_position, food_spawn_time, current_food
    food_position = [random.randrange(1, (window_x // 10)) * 10,
                     random.randrange(1, (window_y // 10)) * 10]
    current_food = random.choice(food_types)  # Random food type
    food_spawn_time = time.time()  # Set the spawn time

spawn_food()

def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score : {score}', True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Your Score is : {score}', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                change_to = 'UP'
            if event.key in (pygame.K_DOWN, pygame.K_s):
                change_to = 'DOWN'
            if event.key in (pygame.K_LEFT, pygame.K_a):
                change_to = 'LEFT'
            if event.key in (pygame.K_RIGHT, pygame.K_d):
                change_to = 'RIGHT'

    # Prevent snake from moving in the opposite direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake growth and food collision
    snake_body.insert(0, list(snake_position))
    if snake_position == food_position:
        score += current_food[1]  # Add corresponding score
        spawn_food()
    else:
        snake_body.pop()

    # Food timeout
    if time.time() - food_spawn_time > food_duration:
        spawn_food()

    # Refresh game screen
    game_window.fill('black')
    for pos in snake_body:  
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, current_food[0], pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Collision detection
    if snake_position[0] < 0 or snake_position[0] > window_x - 10 or \
       snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    show_score(white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)
