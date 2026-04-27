import pygame
import random
import time  # For tracking time for food disappearance

pygame.init()

# Размер окна
width = 600
height = 400
cell = 20

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Цвета
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

# Змея
snake = [(100, 100)]
dx = cell
dy = 0

# Счет и уровень
score = 0
level = 1
speed = 8

font = pygame.font.SysFont(None, 25)

# Структура для еды с весом и временем исчезновения
class Food:
    def __init__(self):
        self.x = random.randint(0, (width - cell) // cell) * cell
        self.y = random.randint(0, (height - cell) // cell) * cell
        self.weight = random.randint(1, 3)  # Random weight of food (1, 2, or 3 points)
        self.time_created = time.time()  # Time when the food was created

    def is_expired(self):
        """Returns True if the food should disappear (after 5 seconds)."""
        return time.time() - self.time_created > 5  # Food disappears after 5 seconds

# Генерация еды
def new_food():
    return Food()

food = new_food()

run = True
while run:
    clock.tick(speed)

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx = 0
                dy = -cell
            elif event.key == pygame.K_DOWN and dy == 0:
                dx = 0
                dy = cell
            elif event.key == pygame.K_LEFT and dx == 0:
                dx = -cell
                dy = 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx = cell
                dy = 0

    # Новая голова
    head = snake[0]
    new_head = (head[0] + dx, head[1] + dy)

    # Проверка стены
    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
        print("Game Over (wall)")
        run = False

    # Проверка самоудара
    if new_head in snake:
        print("Game Over (self)")
        run = False

    # Если съели еду
    if new_head == (food.x, food.y):
        snake.insert(0, new_head)
        score += food.weight  # Add score based on food weight
        food = new_food()

        # Новый уровень каждые 3 очка
        if score % 3 == 0:
            level += 1
            speed += 1

    else:
        snake.insert(0, new_head)
        snake.pop()

    # Удаляем еду, если она истекла по времени
    if food.is_expired():
        food = new_food()

    # Рисуем
    screen.fill(black)

    # Змея
    for s in snake:
        pygame.draw.rect(screen, green, (s[0], s[1], cell, cell))

    # Еда
    pygame.draw.rect(screen, red, (food.x, food.y, cell, cell))

    # Текст
    text1 = font.render("Score: " + str(score), True, white)
    text2 = font.render("Level: " + str(level), True, white)

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 30))

    pygame.display.update()

pygame.quit()