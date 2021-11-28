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
bg_img = pygame.image.load("background.gif")
# pygame.transform.scale(bg_img,(bg_img.get_width()*0.5,bg_img.get_height()*0.5))

butn_img = pygame.image.load("start_game.png")



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

    
    def load_img(self,action,enemy_flg):
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f".\\ryu_img\\{action}\\ryu_{action}_new{i}.png")
            if action == "hk":
                img = pygame.transform.scale(img,(img.get_width()*0.75,img.get_height()*0.75))
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
           self.frame_index = 0     

    def move(self,dir):
        if dir == "left" and self.rect.x > 48:
            self.rect.x -= 10
            # self.image = pygame.image.load(".\\ryu_img\\walk\\ryu_wwalk_new1.png")
            # print(self.rect.x)
        if dir == "right":       
        # if dir == "right" and self.rect.x < 320:
            self.rect.x += 10
            # print(self.rect.x)

    def block(self):
        global player_state
        # self.rect.y -= 10
        player_state = "defensive"

    # def attack(self,attack_type):
    #     if attack_type == "punch":
    #         pl.image = pygame.image.load("ryu_punch1_new.png")
    #         pl.rect.y += 50
    #         pl.image = pygame.transform.scale(pl.image,(pl.image.get_width()*0.8,pl.image.get_height()*0.8))
    #     if attack_type == "push":
    #         pl.image = pygame.image.load("ryu_pl1_kick.png")
    #         # pl.image = pygame.transform.flip(pl.image,True,False)
    #         pl.image = pygame.transform.scale(pl.image,(pl.image.get_width()*0.75,pl.image.get_height()*0.75)) 
    #         pl.rect.y +=20     # temporary                   


    def draw(self):
        screen.blit(self.image,self.rect)

    

    # def idle_state(self):
    #     global player_state
    #     img = pygame.image.load("ryu_idle_new.png")
    #     pl.image = pygame.transform.scale(img,(img.get_width()*1.2,img.get_height()*1.2))
    #     player_state = "idle"

    # def en_idle_state(self):
    #     img = pygame.image.load("enemy_idle.png")
    #     en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))        

    # def enemy_hit(self):
    #     pass

    def enemy_ai(self):
        global enemy_ai_count
        if self.alive == True:
            enemy_ai_count += 1
            if self.rect.x > 320 or self.rect.x < 550:
                print(self.alive)
                print("within alive condition")
                move_list = [2,1,2,-5,5-2,-1,-3,-5]
                self.rect.x += int(random.choice(move_list))
                print(self.rect.x)
                if self.rect.x >= 580:
                    print(self.rect.x)
                    self.rect.x -= 5

                #load images for walk state
                en_action = random.choice(["walk","idle"])
                temp_list = self.load_img(en_action,1)            
                self.animation_list.append(temp_list)
                if en_action == "walk":
                    self.action = 1
                else:
                    self.action = 0

                
                if self.rect.centerx - pl.rect.centerx  < 150:
                    print("player and enemy distance: ",self.rect.centerx - pl.rect.centerx)
                    if enemy_ai_count % 4 == 0:
                        # Cycle for attack
                        en_action = random.choice(["idle","idle","hk","punch","idle","block"])
                        # Cycle for vulnerability
                    else: 
                        en_action = random.choice(["idle","walk","walk","idle","block"])
                    print(en_action)
                    temp_list = self.load_img(en_action,1)            
                    self.animation_list.append(temp_list)
                    if en_action == "hk":
                        self.rect.y -= 50
                        self.action = 3
                        if self.rect.centerx - pl.rect.centerx < 110 and pl.action in (0,1):
                            print("player is hit")
                            pl.rect.x -= 10
                            self.rect.x += 10
                        self.rect.y += 50
                    elif en_action == "punch":
                        self.rect.y -= 60
                        self.action = 2
                        if self.rect.centerx - pl.rect.centerx < 110 and pl.action in (0,1):
                            print("player is hit")
                            pl.rect.x -= 10
                            self.rect.x += 10                        
                        self.rect.y += 60
                    elif en_action == "block":
                        self.rect.y += 65
                        self.action = 4
                        if self.rect.centerx - pl.rect.centerx < 110 and pl.action in (0,1):
                            print("enemy blocked")
                            pl.rect.x -= 10
                            self.rect.x += 10                        
                        self.rect.y -= 65                                                 
                    else:
                        self.action = 0                    
                
        else:
            print("within dead condition")
            enemy_ai_count = 0

class Healthbar():
    def __init__(self,x,y,health,maxhealth):
        self.x = x
        self.y = y
        self.health = health
        self.maxhealth = maxhealth

    def draw(self,health):
        self.health = health
        ratio = self.health/self.maxhealth
        pygame.draw.rect(screen,"red",(self.x,self.y,250,20))
        pygame.draw.rect(screen,"green",(self.x,self.y,250*ratio,20))


pl = Player(100, 340, "player", 100,0)
en = Player(500, 340, "enemy", 100,1)

pl_health = Healthbar(70, 30, pl.health, pl.maxhealth)
en_health = Healthbar(500, 30, en.health, en.maxhealth)


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
    # Load background
    screen.fill((153,217,234))
    
    
    
    pl.update_anim()
    en.update_anim()
    # Load player

    if disp_button == True: # check display button flag
        select_player()
        if fight_butn.draw(screen):
            game_start = True
            disp_button = False # stop displaying start button

    if game_start == True:
        load_bg()
        pl.draw()
        en.draw()
        pl_health.draw(pl.health)
        en_health.draw(en.health)
        en.enemy_ai()
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
                # pl.image = pygame.image.load("ryu_block_new.png")
                # pl.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))                
                # pl.block()
                pl.rect.x += 15
                pl.rect.y += 18
                pl.action = 4

            # player punch
            if event.key == pygame.K_w:                 
                pl.action = 2
                pl.rect.y += 40

            # player high kick                  
            if event.key == pygame.K_s:
                pl.rect.y += 20
                pl.action = 3
        
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
                pl.rect.y -= 40
                pl.action = 0
            if event.key == pygame.K_s:                
                # pl.idle_state()
                pl.rect.y -= 20
                pl.action = 0
    if pygame.Rect.colliderect(en.rect, pl.rect) and player_state in ("punch","push"):
                print("enemy collision")
                en.rect.x += 100
                pl.rect.x -= 50
                curr_time = pygame.time.get_ticks()
                wait_time = curr_time + 1000
                if curr_time < wait_time:
                    img = pygame.image.load("enemy_hit.png")
                    en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                    en.health -= 10
    if en.health == 0:
        img = pygame.image.load("enemy_die.png")
        en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
        en.rect.y += 10
        en.alive = False
         

    if pl.health == 0:
        img = pygame.image.load("player_die.png")
        pl.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
        pl.rect.y = 355
        pl.alive = False
        en.alive = False # stop enemy movement                                                                                                
    pygame.display.update()
pygame.quit()
