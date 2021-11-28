import pygame
import button

# set screen
screen_width = 800
screen_height = 487

# Define game window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Street Fighter")

butn_img = pygame.image.load("start_game.png")

def draw():
    screen.blit(butn_img, (0,0))


run = True
while run:
    screen.fill((153,217,234))
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()                