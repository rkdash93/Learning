import pygame
import random
import button
pygame.init()

clock = pygame.time.Clock()
fps = 8

# set screen
screen_width = 800
screen_height = 487

# Define game window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Street Fighter")

# Load background image
bg_img = pygame.image.load("white_bg.png")
# pygame.transform.scale(bg_img,(bg_img.get_width()*0.5,bg_img.get_height()*0.5))

butn_img = pygame.image.load("start_game.png")


player_name = "ken"
enemy_name = None
player_state = "idle"
enemy_state = "idle"
wait_time = None
enemy_ai_count = 0
game_start = False
disp_button = True

# function to load background image
def load_bg():
    screen.blit(bg_img,(0,0))

# Player class

class Player():
    def __init__(self,x,y,name,maxhealth,enemy_flg):
        self.name = name
        self.maxhealth = maxhealth
        self.health = maxhealth
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 #0 idle 1 punch 2 kick 3 walk
        self.update_time = pygame.time.get_ticks()
        
        #load images for idle state
        temp_list = self.load_img("idle",enemy_flg)
        self.animation_list.append(temp_list)
        
        #load images for walk state
        temp_list = self.load_img("walk",enemy_flg)            
        self.animation_list.append(temp_list)

        #load images for punch state
        temp_list = self.load_img("punch",enemy_flg)                       
        self.animation_list.append(temp_list)
        
        #load images for kick state
        temp_list = self.load_img("hk",enemy_flg)            
        self.animation_list.append(temp_list)

        #load images for block state
        temp_list = self.load_img("block",enemy_flg)            
        self.animation_list.append(temp_list)                


        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self):
        screen.blit(self.image,self.rect)
    def load_img(self,action,enemy_flg):
        temp_list = []
        if action == "hk":
            num = 7
        else:
            num = 4
        for i in range(4):
            # if action == "hk":
            #     img = pygame.image.load(f".\\ryu_img\\{action}\\ryu_{action}{i}.png")
            # else:
            img = pygame.image.load(f".\\{self.name}_img\\{action}\\{self.name}_{action}_new{i}.png")
            if action == "hk":
                img = pygame.transform.scale(img,(img.get_width()*0.9,img.get_height()*0.9))
            elif action in ("punch","block"):        
                img = pygame.transform.scale(img,(img.get_width()*1.05,img.get_height()*1.05))                
            else:        
                img = pygame.transform.scale(img,(img.get_width()*1.2,img.get_height()*1.2))
            if enemy_flg == 1:
                img = pygame.transform.flip(img, True, False)
            temp_list.append(img)
        return  temp_list     


    def update_anim(self):
        animation_cooldown = 100
        # update image
        self.image = self.animation_list[self.action][self.frame_index] 
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # reset frame index to 0 after all the images are iterated
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 4:
                self.frame_index = 0
            else:    
                self.idle()

    def idle(self):
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()          

    def attack(self):
        self.rect.y += 20
        self.action = 3
        self.frame_index = 0
        self.rect.y -= 20
        self.update_time = pygame.time.get_ticks()     

    def move(self,dir):
        if dir == "left" and self.rect.x > 48:
            self.rect.x -= 10
            # self.image = pygame.image.load(".\\ryu_img\\walk\\ryu_wwalk_new1.png")
            # print(self.rect.x)
        if dir == "right":       
        # if dir == "right" and self.rect.x < 320:
            self.rect.x += 10
            # print(self.rect.x)



pl = Player(100, 300, player_name, 100,0)




fight_butn = button.Button(340,230, butn_img)
# sel_ryu = ".\\select_player\\ryu1.png"

def select_player():
    player_list = [".\\select_player\\ryu1.png",".\\select_player\\ken1.png"]
    x_pos = 0
    for i in player_list:
        x_pos += 100
        button.Button(x_pos,50,pygame.image.load(i)).draw(screen)

run = True
while run:
    clock.tick(fps)
    pl.update_anim()
    load_bg()
    pl.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False          
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pl.action = 1
                pl.move("left")
                # pl.action = 0
            if event.key == pygame.K_d:
                pl.action = 1
                pl.move("right")
            if event.key == pygame.K_SPACE:
                pl.rect.x += 15
                pl.rect.y += 18
                pl.action = 4

            # player punch
            if event.key == pygame.K_w:                 
                pl.action = 2
                # pl.rect.y += 40

            # player high kick                  
            if event.key == pygame.K_s:
                pl.rect.y += 20
                pl.attack()
                # pl.rect.y -= 20
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                pl.action = 0

            if event.key == pygame.K_d:
                pl.action = 0 

            if event.key == pygame.K_SPACE:
                pl.rect.x -= 15
                pl.rect.y -= 18                
                pl.action = 0

            if event.key == pygame.K_w:
                # pl.rect.y -= 40
                pl.action = 0
            if event.key == pygame.K_s:                
                # pl.idle_state()
                pl.rect.y -= 20
                pl.action = 0                                                                                            
    pygame.display.update()
pygame.quit()
