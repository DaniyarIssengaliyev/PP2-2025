import pygame
import time
import random
import psycopg2
from psycopg2 import sql

def create_database():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='*Danik3009!@*',
            host='localhost',
            port='5432'
        )
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("CREATE DATABASE snake_game")
        print("Database created successfully")
        cur.close()
    except psycopg2.Error as e:
        print(f"Database already exists or error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

def get_db_connection():
    return psycopg2.connect(
        dbname='snake_game',
        user='postgres',
        password='*Danik3009!@*',
        host='localhost',
        port='5432'
    )

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        current_level INTEGER DEFAULT 1
    )""")
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS levels (
        level_id SERIAL PRIMARY KEY,
        level_name VARCHAR(50) NOT NULL,
        speed INTEGER NOT NULL,
        walls TEXT,
        required_score INTEGER NOT NULL
    )""")
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        score_id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(user_id),
        score INTEGER NOT NULL,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    
    cur.execute("SELECT COUNT(*) FROM levels")
    if cur.fetchone()[0] == 0:
        cur.execute("""
        INSERT INTO levels (level_name, speed, walls, required_score) VALUES
            ('Beginner', 15, '[]', 0),
            ('Intermediate', 20, '[[100,100,200,20],[400,300,200,20]]', 50),
            ('Advanced', 25, '[[50,50,20,300],[300,150,300,20],[200,350,200,20]]', 100)
        """)
    
    conn.commit()
    cur.close()
    conn.close()

def get_or_create_user(username):
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT user_id, current_level FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    
    if user:
        user_id, level = user
        print(f"Welcome back, {username}! Level: {level}")
    else:
        cur.execute(
            "INSERT INTO users (username) VALUES (%s) RETURNING user_id, current_level",
            (username,)
        )
        user_id, level = cur.fetchone()
        print(f"New user created! Starting at level {level}")
    
    conn.commit()
    cur.close()
    conn.close()
    return user_id, level

def get_level_info(level_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT level_name, speed, walls, required_score 
    FROM levels WHERE level_id = %s
    """, (level_id,))
    level = cur.fetchone()
    cur.close()
    conn.close()
    if level:
        return {
            'name': level[0],
            'speed': level[1],
            'walls': eval(level[2]),
            'required_score': level[3]
        }
    return None

def save_score(user_id, score):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO scores (user_id, score) VALUES (%s, %s)", (user_id, score))
    conn.commit()
    cur.close()
    conn.close()

create_database()
init_db()
username = input("Enter your username: ")
user_id, current_level = get_or_create_user(username)
level_info = get_level_info(current_level)

pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
window_x, window_y = 720, 480
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption(f'Snake Game - {level_info["name"]}')

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


snake_speed = level_info['speed']
walls = level_info['walls']
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
direction = 'RIGHT'
change_to = direction
score = 0

wall_surface = pygame.Surface((10, 10), pygame.SRCALPHA)
wall_surface.fill((100, 100, 100, 255))
food_surfaces = {
    10: pygame.Surface((10, 10)),
    20: pygame.Surface((10, 10)),
    30: pygame.Surface((10, 10))
}
food_surfaces[10].fill(red)
food_surfaces[20].fill(blue)
food_surfaces[30].fill(green)

food_position = None
current_food = None

def spawn_food():
    global food_position, current_food
    while True:
        food_position = [random.randrange(1, (window_x//10)) * 10, 
                        random.randrange(1, (window_y//10)) * 10]
        
        valid = True
        for wall in walls:
            wall_rect = pygame.Rect(wall[0], wall[1], wall[2], wall[3])
            if wall_rect.collidepoint(food_position):
                valid = False
                break
        if valid: 
            break
    
    current_food = random.choice([(red, 10), (blue, 20), (green, 30)])

spawn_food()

def show_score():
    font = pygame.font.SysFont('arial', 20)
    score_text = f'Score: {score} | Level: {level_info["name"]}'
    score_surface = font.render(score_text, True, white)
    game_window.blit(score_surface, (10, 10))

def game_over():
    save_score(user_id, score)
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render(f'Game Over! Score: {score}', True, red)
    game_over_rect = game_over_surface.get_rect(center=(window_x/2, window_y/4))
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

clock = pygame.time.Clock()
running = True
last_update = 0
update_interval = 100 

while running:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_p:
                save_score(user_id, score)
                print("Game saved!")
    
    if current_time - last_update > update_interval:
        last_update = current_time
        
        
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_position[1] -= 10
        elif direction == 'DOWN':
            snake_position[1] += 10
        elif direction == 'LEFT':
            snake_position[0] -= 10
        elif direction == 'RIGHT':
            snake_position[0] += 10

        snake_body.insert(0, list(snake_position))
        if snake_position == food_position:
            score += current_food[1]
            spawn_food()
        else:
            snake_body.pop()

        
        if (snake_position[0] < 0 or snake_position[0] > window_x-10 or
            snake_position[1] < 0 or snake_position[1] > window_y-10):
            game_over()
        
        for block in snake_body[1:]:
            if snake_position == block:
                game_over()
        
        for wall in walls:
            wall_rect = pygame.Rect(wall[0], wall[1], wall[2], wall[3])
            if wall_rect.collidepoint(snake_position):
                game_over()
        
        
        next_level_info = get_level_info(current_level + 1) if current_level < 3 else None
        if next_level_info and score >= next_level_info['required_score']:
            current_level += 1
            level_info = get_level_info(current_level)
            snake_speed = level_info['speed']
            walls = level_info['walls']
            pygame.display.set_caption(f'Snake Game - {level_info["name"]}')
            print(f"Level up! Now playing: {level_info['name']}")
    
    game_window.fill(black)
    
    for wall in walls:
        for x in range(wall[0], wall[0] + wall[2], 10):
            for y in range(wall[1], wall[1] + wall[3], 10):
                game_window.blit(wall_surface, (x, y))
    
    for pos in snake_body:
        pygame.draw.rect(game_window, green, (*pos, 10, 10))
    
    game_window.blit(food_surfaces[current_food[1]], food_position)
    
    show_score()
    pygame.display.update()
    clock.tick(120)

pygame.quit()