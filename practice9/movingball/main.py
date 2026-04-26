import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock() #fps

ball = Ball(WIDTH // 2, HEIGHT // 2, screen_width=WIDTH, screen_height=HEIGHT) #(centre and borders)

running = True
while running:
    clock.tick(20) #fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #quitting

    keys = pygame.key.get_pressed() #gettin all pressed keys

    if keys[pygame.K_LEFT]: #if left strelka - move it left
        ball.move(-1, 0)
    if keys[pygame.K_RIGHT]: #if right strelka - move it right
        ball.move(1, 0)
    if keys[pygame.K_UP]: #if up strelka - move it up
        ball.move(0, -1)
    if keys[pygame.K_DOWN]: #if down strelka - move it down
        ball.move(0, 1)

    screen.fill((255, 255, 255)) #background
    ball.draw(screen) 

    pygame.display.flip() #updatin

pygame.quit()

