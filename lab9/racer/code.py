import pygame
import random, time

pygame.init()

# Window size
w, h, fps = 400, 600, 60
is_running, lose = True, False
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Racer')
clock = pygame.time.Clock()
y = 0
ry = 2  # Speed of Background
step, enemy_step, score, score_coin = 5, 5, 0, 0
speed_increase_threshold = 5  # Speed increase after N coins
speed_increment = 2  # How speed increases

# Image loading
game_over = pygame.image.load("A:\\PP2 2025\\lab9\\racer\\gameover.jpg")
bg = pygame.image.load("A:\\PP2 2025\\lab9\\racer\\track.png")
game_over = pygame.transform.scale(game_over, (w, h))

# Score
score_font = pygame.font.SysFont("Verdana", 20)
score_coins = pygame.font.SysFont("Verdana", 20)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("A:\\PP2 2025\\lab9\\racer\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)

    def update(self):
        global score
        self.rect.move_ip(0, enemy_step)
        if self.rect.bottom > h + 90:
            score += 1
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("A:\\PP2 2025\\lab9\\racer\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_a]:
            self.rect.move_ip(-step, 0)
        if self.rect.right < w and pressed_keys[pygame.K_d]:
            self.rect.move_ip(step, 0)
        if self.rect.top > 0 and pressed_keys[pygame.K_w]:
            self.rect.move_ip(0, -step)
        if self.rect.bottom < h and pressed_keys[pygame.K_s]:
            self.rect.move_ip(0, step)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("A:\\PP2 2025\\lab9\\racer\\coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, w - 30), random.randint(30, h - 130))
        self.value = random.choice([1, 2, 3])  

    def draw(self):
        screen.blit(self.image, self.rect)

# Create objects
p = Player()
e = Enemy()

#Create groups
enemies = pygame.sprite.Group()
enemies.add(e)

coins = pygame.sprite.Group()
coins.add(Coin())

#The game
while is_running:
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            is_running = False

    # Movement of background
    screen.blit(pygame.transform.scale(bg, (w, h)), (0, y % h))
    screen.blit(pygame.transform.scale(bg, (w, h)), (0, -h + (y % h)))
    y += ry

    p.update()
    e.update()

    #if enemy and player crash
    if pygame.sprite.spritecollideany(p, enemies):
        lose = True

    #Coin collecting
    for c in coins:
        c.draw()
        if pygame.sprite.collide_rect(p, c):
            score_coin += c.value  # Add weight of coin to the score
            c.kill()
            coins.add(Coin())  #Spawn new coin

            #Speed increase
            if score_coin % speed_increase_threshold == 0:
                enemy_step += speed_increment

    e.draw(screen)
    p.draw(screen)

    # Score
    counter = score_coins.render(f'Coins: {score_coin}', True, 'white')
    screen.blit(counter, (300, 10))

    #LOSER
    while lose:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(game_over, (0, 0))
        pygame.display.flip()

    pygame.display.flip()

pygame.quit()
