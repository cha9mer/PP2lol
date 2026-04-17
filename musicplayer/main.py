import pygame
import sys #for quitting
from player import MusicPlayer #importing class from player

pygame.init() #initializing

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player") #window title
font = pygame.font.SysFont(None, 25) #all text size
clock = pygame.time.Clock() #fps

player = MusicPlayer("music") #papka music - where it gets music files

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get(): #all user actions 
        if event.type == pygame.QUIT: #if action quit then quitting
            running = False 

        if event.type == pygame.KEYDOWN: #if any key pressed then
            if event.key == pygame.K_p: #if pressed P
                player.play()
            elif event.key == pygame.K_s: #if pressed S
                player.stop()
            elif event.key == pygame.K_n: #if pressed N
                player.next_track()
            elif event.key == pygame.K_b: #if pressed B
                player.prev_track()
            elif event.key == pygame.K_q: #if pressed Q we quit
                running = False

    track_text = font.render(f"Track: {player.get_current_track_name()}", True, (173, 216, 230))
    screen.blit(track_text, (20, 40)) #for displaying

    status_text = font.render(f"Status: {player.status}", True, (173, 216, 230))
    screen.blit(status_text, (20, 80)) 

    progress = player.get_progress() #getting progress bar (minutes)
    pygame.draw.rect(screen, (173, 216, 230), (20, 140, 560, 20)) #poloska progressa cvet
    pygame.draw.rect(screen, (0, 200, 0), (20, 140, int(560 * progress), 20)) #poloska progressa valitii cvet 

    instructions = [
        "P=Play <3  S=Stop <3  N=Next <3  B=Back <3  Q=Quit <3"
    ]

    for i, line in enumerate(instructions):
        txt = font.render(line, True, (180, 180, 180))
        screen.blit(txt, (20, 200 + i * 25)) #instructions displaying

    pygame.display.flip() #updating
    clock.tick(30)

pygame.quit()
sys.exit()