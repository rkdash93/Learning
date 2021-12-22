import pygame

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.65)


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Super Mario")

# set framerate
clock = pygame.time.Clock()
fps = 60

#color
white = (255,255,255)
black = (0,0,0)

tile_size = 100

def load_bg():
    screen.fill(white)
    for line in range(0,8):
        pygame.draw.line(screen, black, (0,line*tile_size), (SCREEN_WIDTH,line*tile_size))
        pygame.draw.line(screen, black, (line*tile_size,0), (line*tile_size,SCREEN_HEIGHT))        
    # temp



run = True
while run:
    clock.tick(fps)
    load_bg()                   

                   

    for event in pygame.event.get():                                                 
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()    