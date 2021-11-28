import pygame
import random
import button
pygame.init()

clock = pygame.time.Clock()
fps = 8

# set screen
screen_width = 800
screen_height = 487


# Global variables
player_name = "ryu"
enemy_name = "ken"
player_state = None
enemy_state = None
wait_time = None
enemy_ai_count = 0
game_start = False
disp_button = False
selection_confirm = False
player_select = ""
enemy_select = ""
arena_select = ""
player_hit = False
# bg_arena = ".\\background\\Chinatown.gif"
bg_arena = "white_bg.png"

# Define game window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Street Fighter")

# Load background image
bg_img = pygame.image.load(bg_arena)
# pygame.transform.scale(bg_img,(bg_img.get_width()*0.5,bg_img.get_height()*0.5))

butn_img = pygame.image.load("start_game.png")
dragon_img = pygame.image.load(".\\background\\dragon.png")
# right_sel = pygame.image.load(".\\select_player\\right_sel.png")
# left_sel = pygame.image.load(".\\select_player\\left_sel.png")





# Define font
font = pygame.font.SysFont("Times New Roman", 26)
font2 = pygame.font.SysFont("Impact", 30)
font3 = pygame.font.SysFont("Segoe UI", 35)
font4 = pygame.font.SysFont("Magneto", 32)
font5 = pygame.font.SysFont("Goudy Stout", 40)

# Define colours
red = (255,0,0)
green = (203,254,228)
black = (0,0,0)
violet = (84,14,122)

# function to draw text
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img, (x,y))

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
        self.action = 0 #0 idle 1 walk 2 punch 3 kick 4 block 5 hit 6 die
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

        #load images for hit state
        temp_list = self.load_img("hit",enemy_flg)            
        self.animation_list.append(temp_list)

        #load images for hit state
        temp_list = self.load_img("die",enemy_flg)            
        self.animation_list.append(temp_list)                        


        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    
    def load_img(self,action,enemy_flg):
        temp_list = []
        for i in range(4):
            img = pygame.image.load(f".\\{self.name}_img\\{action}\\{self.name}_{action}_new{i}.png")
            if self.name == "ken":
                img = pygame.transform.scale(img,(img.get_width()*0.9,img.get_height()*0.9))
            if action in ("hk","die") and self.name == "ryu":
                img = pygame.transform.scale(img,(img.get_width()*0.75,img.get_height()*0.75))
            elif action in ("punch","block"):        
                img = pygame.transform.scale(img,(img.get_width()*1.05,img.get_height()*1.05))
            elif action in ("hit"):        
                img = pygame.transform.scale(img,(img.get_width()*0.90,img.get_height()*0.90))
                # self.rect.y += 10                                           
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
        global player_state
        global enemy_state
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
                        en_action = random.choice(["idle","idle","idle","idle","idle","hk","punch","idle","block"])
                        # en_action = "idle"
                        # Cycle for vulnerability
                    else: 
                        en_action = random.choice(["idle","walk","walk","idle","block"])
                    print("idle")
                    temp_list = self.load_img(en_action,1)            
                    self.animation_list.append(temp_list)
                    if en_action == "hk":
                        self.rect.y -= 50
                        self.action = 3
                        # pl.rect.x -=100
                        if self.rect.centerx - pl.rect.centerx < 120:
                            if pl.action in (0,1):
                                print("player is hit")
                                player_state = "Hit!!"
                                enemy_state = "Kick!!"
                                pl.health -= 10
                                pl.rect.x -=20
                                self.rect.x += 10
                                pl.action = 5
                            elif pl.action == 4:
                                print("player blocked")
                                player_state = "Block!!"
                                enemy_state = "Kick!!"
                                pl.rect.x -=20
                                self.rect.x += 10
                                pl.action = 5                                
                        self.rect.y += 50
                    elif en_action == "punch":
                        self.rect.y -= 60
                        self.action = 2
                        if self.rect.centerx - pl.rect.centerx < 120:
                            if pl.action in (0,1):
                                print("player is hit")
                                player_state = "Hit!!"
                                enemy_state = "Kick!!"
                                pl.health -= 10
                                pl.rect.x -=20
                                self.rect.x += 10
                                pl.action = 5
                            elif pl.action == 4:
                                print("player blocked")
                                player_state = "Block!!"
                                enemy_state = "Kick!!"
                                pl.rect.x -=20
                                self.rect.x += 10
                                pl.action = 5                        
                        self.rect.y += 60
                    elif en_action == "block":
                        self.rect.y += 65
                        self.action = 4
                        if self.rect.centerx - pl.rect.centerx < 110:
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

    def draw(self,health,en_flg):
        self.health = health
        ratio = self.health/self.maxhealth
        if en_flg == 1:
            pygame.draw.rect(screen,"red",(self.x,self.y,250,10))
            pygame.draw.rect(screen,"green",(self.x,self.y,250*ratio,10))
        else:
            pygame.draw.rect(screen,"red",(self.x,self.y,250,10))
            pygame.draw.rect(screen,"green",(self.x + (250-(250*ratio)),self.y,250*ratio,10))


pl = Player(100, 340, player_name, 100,0)
en = Player(500, 340, enemy_name, 100,1)

pl_health = Healthbar(70, 50, pl.health, pl.maxhealth)
en_health = Healthbar(500, 50, en.health, en.maxhealth)

player_list = [".\\select_player\\ryu1.png",".\\select_player\\ken1.png"]
# pl_right_butn =  button.Button(250,100, right_sel)
# pl_left_butn =  button.Button(100,100, left_sel)

# en_right_butn =  button.Button(600,100, right_sel)
# en_left_butn =  button.Button(450,100, left_sel)

fight_butn = button.Button(340,430, butn_img)

landing_screen_btn = True
strt_bt_img = pygame.image.load(".\\buttons\\start_game.png")
start_butn = button.Button(320,270, strt_bt_img)
opt_bt_img = pygame.image.load(".\\buttons\\option.png")
opt_butn = button.Button(320,350, opt_bt_img)
# sel_ryu = ".\\select_player\\ryu1.png"

# player_list = [".\\select_player\\ryu1.png",".\\select_player\\ken1.png"]




def select_options():
    global player_name
    global enemy_name
    global arena_select
    global bg_arena
    disp_button = True

    if disp_button == True:
        # pl_btn
        pl_butn_list = []
        en_butn_list = []
        arena_butn_list = []
        player_list = [".\\select_options\\player\\ryu1.png",".\\select_options\\player\\ken1.png"]
        arena_list = [".\\select_options\\arena\\Graveyard.jpg",".\\select_options\\arena\\Chinatown.gif",".\\select_options\\arena\\Future.jpg"]
        # Select Player
        x_pos = 0
        for i in player_list:
            x_pos += 100
            btn = button.Button(x_pos,50,pygame.image.load(i))
            # btn.draw(screen)
            pl_butn_list.append(btn)
        for i in range(len(pl_butn_list)):
            if pl_butn_list[i].draw(screen):
                temp = player_list[i].replace(".\\select_options\\player\\","")
                print(temp,"selected")
                player_name = temp.replace("1.png","")
                
        # select enemy
        x_pos = 400
        for i in player_list:
            x_pos += 100
            btn = button.Button(x_pos,50,pygame.image.load(i))
            # btn.draw(screen)
            en_butn_list.append(btn)
        for i in range(len(en_butn_list)):
            if en_butn_list[i].draw(screen):
                temp = player_list[i].replace(".\\select_options\\player\\","")
                print(temp,"selected")
                enemy_name = temp.replace("1.png","")

        # select arena
        x_pos = 70
        for i in arena_list:
            btn = button.Button(x_pos,230,pygame.image.load(i))
            x_pos += 220
            # btn.draw(screen)
            arena_butn_list.append(btn)
        for i in range(len(arena_butn_list)):
            if arena_butn_list[i].draw(screen):
                temp = arena_list[i].replace(".\\select_options\\arena\\","")
                # print(temp,"selected")
                print(temp.replace(temp[-4:],""))
                arena_select = temp.replace(temp[-4:],"")
                bg_arena = ".\\background\\" + temp
            
        


run = True
while run:
    clock.tick(fps)
    # Load background
    # screen.fill((153,217,234))
    screen.blit(dragon_img,(0,0))
    # draw_text("Player", font2, green, 150, 10)
    # draw_text("Opponent", font2, green, 530, 10)
    # draw_text("Vs", font2, red, 360, 100)
    # draw_text(player_name, font2, red, 170, 180)
    # draw_text(enemy_name, font2, red, 560, 180)
    # draw_text(arena_select, font2, red, 320, 350)

    # pl.name = player_name
    # en.name = enemy_name


    # pl.update_anim()
    # en.update_anim() 
    
    # temporary code
    if landing_screen_btn == True:
        if start_butn.draw(screen):
            landing_screen_btn = False
            disp_button = True
            
        if opt_butn.draw(screen):
            print("Clicked")            
        
        draw_text("Street Fighter", font5, green, 100, 100)

    # Load player

    # disp_button = False

    if disp_button == True: # check display button flag

        select_options()
        # create instances based on player selection
        pl = Player(100, 340, player_name, 100,0)
        en = Player(500, 340, enemy_name, 100,1)

        pl_health = Healthbar(70, 50, pl.health, pl.maxhealth)
        en_health = Healthbar(500, 50, en.health, en.maxhealth)

        if fight_butn.draw(screen):
            bg_img = pygame.image.load(bg_arena)
            game_start = True
            disp_button = False # stop displaying start button

    pl.update_anim()
    en.update_anim()        

    # if game_start == True:
    if game_start:
        load_bg()
        draw_text("Player", font2, violet, 100, 10)
        draw_text("Opponent", font2, violet, 590, 10)
        draw_text("Fight", font4, red, 360, 35)
        draw_text(player_state, font, red, 100, 55)
        draw_text(enemy_state, font, red, 650, 55)               
        pl.draw()
        en.draw()
        pl_health.draw(pl.health,0)
        en_health.draw(en.health,1)
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
                pl.action = 3
                pl.rect.y += 20
        
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
                pl.action = 0
                pl.rect.y -= 40
            if event.key == pygame.K_s:                
                # pl.idle_state()
                pl.action = 0
                pl.rect.y -= 20

    # if en.rect.centerx - pl.rect.centerx < 110 and pl.action in (2,3) and en.action in (0,1,2,3):
    #     print("enemy hit")
    #     en.rect.x += 100
    #     pl.rect.x -= 50
    # if en.rect.centerx - pl.rect.centerx < 110 and pl.action in (2,3) and en.action == 4:
    #     print("enemy blocked")
    #     en.rect.x += 100
    #     pl.rect.x -= 50                        
    if en.rect.centerx - pl.rect.centerx < 110 and pl.action in (2,3):
        if en.action in (0,1,2,3,5):
                print("enemy collision")
                if pl.action == 2:
                    player_state = "Punch"
                else:
                    player_state = "Kick"
                enemy_state = "Hit"
                en.health -= 10
                en.rect.x += 50
                pl.rect.x -= 50
                curr_time = pygame.time.get_ticks()
                wait_time = curr_time + 1000
                if curr_time < wait_time:
                    en.action = 5
        elif en.action == 4:
                print("enemy block")
                if pl.action == 2:
                    player_state = "Punch"
                else:
                    player_state = "Kick"
                enemy_state = "Block"
                en.rect.x += 50
                pl.rect.x -= 50            

    #     pl.rect.y += 10
    #     pl.action = 5
    #     curr_time = pygame.time.get_ticks()
    #     wait_time = curr_time + 1000
    #     print("curr_time",curr_time)
    #     print("wait_time",wait_time)
    #     if curr_time < wait_time:
    #         pl.action = 0
    #         pl.rect.y -= 10
    #         player_hit = False
    #                 # img = pygame.image.load("enemy_hit.png")
    #                 # en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
                    # en.health -= 10
    #                 # 
    # if en.rect.centerx - pl.rect.centerx < 150 and en.action == "hk":
    #     print("player is hit")
    #     break
    #     curr_time = pygame.time.get_ticks()
    #     wait_time = curr_time + 1000        
    #     # pl.rect.y += 10
    #     # en.rect.x += 30
    #     # pl.rect.x -= 30
    #     # pl.action = 5

    #     print("curr_time",curr_time)
    #     print("wait_time",wait_time)
    #     if curr_time < wait_time:
    #         print("within current time less than wait time loop")
    #         print("curr_time",curr_time)
    #         print("wait_time",wait_time)
    #         curr_time = pygame.time.get_ticks()
    #     else:
    #         print("curr_time",curr_time)
    #         print("wait_time",wait_time)
    #         break           
    #         # break
    #         # pl.action = 0
    #         # pl.rect.y -= 10
    #     print("outside current time less than wait time loop")
    #     print("curr_time",curr_time)
    #     print("wait_time",wait_time)
    #     # break        
    #         # player_hit = False           

    if en.health == 0:
        # img = pygame.image.load("enemy_die.png")
        # en.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
        en.action = 6
        en.rect.y = 360
        en.alive = False
         

    if pl.health == 0:
        # img = pygame.image.load("player_die.png")
        # pl.image = pygame.transform.scale(img,(img.get_width()*2.5,img.get_height()*2.5))
        pl.rect.y = 360
        pl.action = 6
        pl.alive = False
        en.alive = False # stop enemy movement
                                                                                               
    pygame.display.update()
pygame.quit()
