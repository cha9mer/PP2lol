import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()  # all modules
pygame.mixer.init()  # music module

FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # enemy speed
SCORE = 0  # track of players score
COINS_COLLECTED = 0  # track coins collected

font = pygame.font.SysFont("Arial", 60)  # gameover text
font_small = pygame.font.SysFont("Arial", 20)  # score
game_over = font.render("Game Over", True, BLACK)  # rendered using 'font'

background = pygame.image.load("images/AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))  # window creating
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")  # window title
pygame.mixer.music.load("sounds/background.wav")
pygame.mixer.music.set_volume(0.5)  # volume 50%
pygame.mixer.music.play(-1)  # playing forever

class Enemy(pygame.sprite.Sprite):  # initializing image, hitbox and position
    def __init__(self):
        super().__init__()  # parent sprite class to init
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()  # hitbox
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # enemy spawn position

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # moves 5 fps vertically down
        if self.rect.top > 600:  # if enemy moves past the bottom
            SCORE += 1  # it means player successfully avoided it
            self.rect.top = 0  # resetting enemy
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # resetting enemy

class Coin(pygame.sprite.Sprite):  # coin class to represent coins
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Coin.png")  # Replace with actual coin image path
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT // 2))  # Random position

        # Random coin weight
        self.weight = random.randint(1, 3)  # Random weight between 1 and 3

    def move(self):
        self.rect.move_ip(0, SPEED)  # coins move down with same speed as enemies
        if self.rect.top > SCREEN_HEIGHT:  # If coin goes off the screen
            self.rect.top = 0  # reset coin position
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # reset coin

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()  # hitbox
        self.rect.center = (160, 520)  # starting position

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:  # checks if the player is not already at the far left edge of the screen
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:  # checks if the player is not already at the far right edge of the screen
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Add coin generation to the game
coins = pygame.sprite.Group()
coin = Coin()  # Only one coin initially
coins.add(coin)
all_sprites.add(coin)

# Event to increase speed after collecting coins
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            if COINS_COLLECTED % 5 == 0:  # Increase speed after every 5 coins collected
                SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))

    # Display score
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Display coins collected
    coins_collected_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coins_collected_text, (10, 40))

    # Move and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check for collision between player and enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('sounds/crash.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check for coin collection
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)  # Get coins collected by the player
    if collected_coins:
        COINS_COLLECTED += sum(coin.weight for coin in collected_coins)  # Increase score by coin weight
        
        # Spawn new coin for each enemy
        coin = Coin()  # Only one coin for each enemy
        coins.add(coin)
        all_sprites.add(coin)

    pygame.display.update()
    FramePerSec.tick(FPS)